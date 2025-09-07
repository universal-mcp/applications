from typing import Any

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class DigitaloceanApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="digitalocean", integration=integration, **kwargs)
        self.base_url = "https://api.digitalocean.com"

    def one_clicks_list(self, type: str | None = None) -> Any:
        """
        List 1-Click Applications

        Args:
            type (string): Restrict results to a certain type of 1-Click. Example: 'kubernetes'.

        Returns:
            Any: A JSON object with a key of `1_clicks`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            1-Click Applications
        """
        url = f"{self.base_url}/v2/1-clicks"
        query_params = {k: v for k, v in [("type", type)] if v is not None}
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

    def one_clicks_install_kubernetes(
        self, addon_slugs: list[str], cluster_uuid: str
    ) -> dict[str, Any]:
        """
        Install Kubernetes 1-Click Applications

        Args:
            addon_slugs (array): An array of 1-Click Application slugs to be installed to the Kubernetes cluster. Example: "['kube-state-metrics', 'loki']".
            cluster_uuid (string): A unique ID for the Kubernetes cluster to which the 1-Click Applications will be installed. Example: '50a994b6-c303-438f-9495-7e896cfe6b08'.

        Returns:
            dict[str, Any]: The response will verify that a job has been successfully created to install a 1-Click. The
        post-installation lifecycle of a 1-Click application can not be managed via the DigitalOcean
        API. For additional details specific to the 1-Click, find and view its
        [DigitalOcean Marketplace](https://marketplace.digitalocean.com) page.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            1-Click Applications
        """
        request_body_data = None
        request_body_data = {
            "addon_slugs": addon_slugs,
            "cluster_uuid": cluster_uuid,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/1-clicks/kubernetes"
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

    def account_get(self) -> Any:
        """
        Get User Information

        Returns:
            Any: A JSON object keyed on account with an excerpt of the current user account data.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Account
        """
        url = f"{self.base_url}/v2/account"
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

    def ssh_keys_list(
        self, per_page: int | None = None, page: int | None = None
    ) -> Any:
        """
        List All SSH Keys

        Args:
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: A JSON object with the key set to `ssh_keys`. The value is an array of `ssh_key` objects, each of which contains the standard `ssh_key` attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            SSH Keys
        """
        url = f"{self.base_url}/v2/account/keys"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def ssh_keys_create(
        self,
        public_key: str,
        name: str,
        id: int | None = None,
        fingerprint: str | None = None,
    ) -> Any:
        """
        Create a New SSH Key

        Args:
            public_key (string): The entire public key string that was uploaded. Embedded into the root user's `authorized_keys` file if you include this key during Droplet creation. Example: 'ssh-rsa AEXAMPLEaC1yc2EAAAADAQABAAAAQQDDHr/jh2Jy4yALcK4JyWbVkPRaWmhck3IgCoeOO3z1e2dBowLh64QAM+Qb72pxekALga2oi4GvT+TlWNhzPH4V example'.
            name (string): A human-readable display name for this key, used to easily identify the SSH keys when they are displayed. Example: 'My SSH Public Key'.
            id (integer): A unique identification number for this key. Can be used to embed a  specific SSH key into a Droplet. Example: '512189'.
            fingerprint (string): A unique identifier that differentiates this key from other keys using  a format that SSH recognizes. The fingerprint is created when the key is added to your account. Example: '3b:16:bf:e4:8b:00:8b:b8:59:8c:a9:d3:f0:19:45:fa'.

        Returns:
            Any: The response body will be a JSON object with a key set to `ssh_key`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            SSH Keys
        """
        request_body_data = None
        request_body_data = {
            "id": id,
            "fingerprint": fingerprint,
            "public_key": public_key,
            "name": name,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/account/keys"
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

    def ssh_keys_get(self, ssh_key_identifier: str) -> Any:
        """
        Retrieve an Existing SSH Key

        Args:
            ssh_key_identifier (string): ssh_key_identifier

        Returns:
            Any: A JSON object with the key set to `ssh_key`. The value is an `ssh_key` object containing the standard `ssh_key` attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            SSH Keys
        """
        if ssh_key_identifier is None:
            raise ValueError("Missing required parameter 'ssh_key_identifier'.")
        url = f"{self.base_url}/v2/account/keys/{ssh_key_identifier}"
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

    def ssh_keys_update(self, ssh_key_identifier: str, name: str | None = None) -> Any:
        """
        Update an SSH Key's Name

        Args:
            ssh_key_identifier (string): ssh_key_identifier
            name (string): A human-readable display name for this key, used to easily identify the SSH keys when they are displayed. Example: 'My SSH Public Key'.

        Returns:
            Any: A JSON object with the key set to `ssh_key`. The value is an `ssh_key` object containing the standard `ssh_key` attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            SSH Keys
        """
        if ssh_key_identifier is None:
            raise ValueError("Missing required parameter 'ssh_key_identifier'.")
        request_body_data = None
        request_body_data = {
            "name": name,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/account/keys/{ssh_key_identifier}"
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

    def ssh_keys_delete(self, ssh_key_identifier: str) -> Any:
        """
        Delete an SSH Key

        Args:
            ssh_key_identifier (string): ssh_key_identifier

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            SSH Keys
        """
        if ssh_key_identifier is None:
            raise ValueError("Missing required parameter 'ssh_key_identifier'.")
        url = f"{self.base_url}/v2/account/keys/{ssh_key_identifier}"
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

    def actions_list(self, per_page: int | None = None, page: int | None = None) -> Any:
        """
        List All Actions

        Args:
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: The results will be returned as a JSON object with an actions key.  This will be set to an array filled with action objects containing the standard action attributes

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Actions
        """
        url = f"{self.base_url}/v2/actions"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def actions_get(self, action_id: str) -> Any:
        """
        Retrieve an Existing Action

        Args:
            action_id (string): action_id

        Returns:
            Any: The result will be a JSON object with an action key.  This will be set to an action object containing the standard action attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Actions
        """
        if action_id is None:
            raise ValueError("Missing required parameter 'action_id'.")
        url = f"{self.base_url}/v2/actions/{action_id}"
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

    def apps_list(
        self,
        page: int | None = None,
        per_page: int | None = None,
        with_projects: bool | None = None,
    ) -> Any:
        """
        List All Apps

        Args:
            page (integer): Which 'page' of paginated results to return. Example: '1'.
            per_page (integer): Number of items returned per page Example: '2'.
            with_projects (boolean): Whether the project_id of listed apps should be fetched and included. Example: 'True'.

        Returns:
            Any: A JSON object with a `apps` key. This is list of object `apps`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps, important
        """
        url = f"{self.base_url}/v2/apps"
        query_params = {
            k: v
            for k, v in [
                ("page", page),
                ("per_page", per_page),
                ("with_projects", with_projects),
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

    def apps_create(
        self, spec: dict[str, Any], project_id: str | None = None
    ) -> dict[str, Any]:
        """
        Create a New App

        Args:
            spec (object): The desired configuration of an application. Example: {'name': 'web-app', 'region': 'nyc', 'services': [{'name': 'api', 'github': {'branch': 'main', 'deploy_on_push': True, 'repo': 'digitalocean/sample-golang'}, 'run_command': 'bin/api', 'environment_slug': 'node-js', 'instance_count': 2, 'instance_size_slug': 'apps-s-1vcpu-0.5gb', 'routes': [{'path': '/api'}]}], 'egress': {'type': 'DEDICATED_IP'}}.
            project_id (string): The ID of the project the app should be assigned to. If omitted, it will be assigned to your default project.

        Returns:
            dict[str, Any]: A JSON or YAML of a `spec` object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps
        """
        request_body_data = None
        request_body_data = {
            "spec": spec,
            "project_id": project_id,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/apps"
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

    def apps_delete(self, id: str) -> dict[str, Any]:
        """
        Delete an App

        Args:
            id (string): id

        Returns:
            dict[str, Any]: the ID of the app deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/v2/apps/{id}"
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

    def apps_get(self, id: str, name: str | None = None) -> dict[str, Any]:
        """
        Retrieve an Existing App

        Args:
            id (string): id
            name (string): The name of the app to retrieve. Example: 'myApp'.

        Returns:
            dict[str, Any]: A JSON with key `app`

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/v2/apps/{id}"
        query_params = {k: v for k, v in [("name", name)] if v is not None}
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

    def apps_update(
        self,
        id: str,
        spec: dict[str, Any],
        update_all_source_versions: bool | None = None,
    ) -> dict[str, Any]:
        """
        Update an App

        Args:
            id (string): id
            spec (object): The desired configuration of an application.
            update_all_source_versions (boolean): Whether or not to update the source versions (for example fetching a new commit or image digest) of all components. By default (when this is false) only newly added sources will be updated to avoid changes like updating the scale of a component from also updating the respective code. Example: 'True'.

        Returns:
            dict[str, Any]: A JSON object of the updated `app`

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        request_body_data = {
            "spec": spec,
            "update_all_source_versions": update_all_source_versions,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/apps/{id}"
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

    def apps_restart(
        self, app_id: str, components: list[str] | None = None
    ) -> dict[str, Any]:
        """
        Restart an App

        Args:
            app_id (string): app_id
            components (array): components Example: "['component1', 'component2']".

        Returns:
            dict[str, Any]: A JSON object with a `deployment` key.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps
        """
        if app_id is None:
            raise ValueError("Missing required parameter 'app_id'.")
        request_body_data = None
        request_body_data = {
            "components": components,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/apps/{app_id}/restart"
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

    def get_app_component_logs(
        self,
        app_id: str,
        component_name: str,
        type: str,
        follow: bool | None = None,
        pod_connection_timeout: str | None = None,
    ) -> dict[str, Any]:
        """
        Retrieve Active Deployment Logs

        Args:
            app_id (string): app_id
            component_name (string): component_name
            type (string): The type of logs to retrieve
        - BUILD: Build-time logs
        - DEPLOY: Deploy-time logs
        - RUN: Live run-time logs
        - RUN_RESTARTED: Logs of crashed/restarted instances during runtime Example: 'BUILD'.
            follow (boolean): Whether the logs should follow live updates. Example: 'True'.
            pod_connection_timeout (string): An optional time duration to wait if the underlying component instance is not immediately available. Default: `3m`. Example: '3m'.

        Returns:
            dict[str, Any]: A JSON object with urls that point to archived logs

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps
        """
        if app_id is None:
            raise ValueError("Missing required parameter 'app_id'.")
        if component_name is None:
            raise ValueError("Missing required parameter 'component_name'.")
        url = f"{self.base_url}/v2/apps/{app_id}/components/{component_name}/logs"
        query_params = {
            k: v
            for k, v in [
                ("follow", follow),
                ("type", type),
                ("pod_connection_timeout", pod_connection_timeout),
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

    def get_component_execution_details(
        self, app_id: str, component_name: str
    ) -> dict[str, Any]:
        """
        Retrieve Exec URL

        Args:
            app_id (string): app_id
            component_name (string): component_name

        Returns:
            dict[str, Any]: A JSON object with a websocket URL that allows sending/receiving console input and output.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps
        """
        if app_id is None:
            raise ValueError("Missing required parameter 'app_id'.")
        if component_name is None:
            raise ValueError("Missing required parameter 'component_name'.")
        url = f"{self.base_url}/v2/apps/{app_id}/components/{component_name}/exec"
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

    def apps_get_instances(self, app_id: str) -> dict[str, Any]:
        """
        Retrieve App Instances

        Args:
            app_id (string): app_id

        Returns:
            dict[str, Any]: A JSON with key `instances`

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps
        """
        if app_id is None:
            raise ValueError("Missing required parameter 'app_id'.")
        url = f"{self.base_url}/v2/apps/{app_id}/instances"
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

    def apps_list_deployments(
        self, app_id: str, page: int | None = None, per_page: int | None = None
    ) -> Any:
        """
        List App Deployments

        Args:
            app_id (string): app_id
            page (integer): Which 'page' of paginated results to return. Example: '1'.
            per_page (integer): Number of items returned per page Example: '2'.

        Returns:
            Any: A JSON object with a `deployments` key. This will be a list of all app deployments

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps
        """
        if app_id is None:
            raise ValueError("Missing required parameter 'app_id'.")
        url = f"{self.base_url}/v2/apps/{app_id}/deployments"
        query_params = {
            k: v for k, v in [("page", page), ("per_page", per_page)] if v is not None
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

    def apps_create_deployment(
        self, app_id: str, force_build: bool | None = None
    ) -> dict[str, Any]:
        """
        Create an App Deployment

        Args:
            app_id (string): app_id
            force_build (boolean): force_build Example: 'True'.

        Returns:
            dict[str, Any]: A JSON object with a `deployment` key.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps
        """
        if app_id is None:
            raise ValueError("Missing required parameter 'app_id'.")
        request_body_data = None
        request_body_data = {
            "force_build": force_build,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/apps/{app_id}/deployments"
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

    def apps_get_deployment(self, app_id: str, deployment_id: str) -> dict[str, Any]:
        """
        Retrieve an App Deployment

        Args:
            app_id (string): app_id
            deployment_id (string): deployment_id

        Returns:
            dict[str, Any]: A JSON of the requested deployment

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps
        """
        if app_id is None:
            raise ValueError("Missing required parameter 'app_id'.")
        if deployment_id is None:
            raise ValueError("Missing required parameter 'deployment_id'.")
        url = f"{self.base_url}/v2/apps/{app_id}/deployments/{deployment_id}"
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

    def apps_cancel_deployment(self, app_id: str, deployment_id: str) -> dict[str, Any]:
        """
        Cancel a Deployment

        Args:
            app_id (string): app_id
            deployment_id (string): deployment_id

        Returns:
            dict[str, Any]: A JSON the `deployment` that was just cancelled.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps
        """
        if app_id is None:
            raise ValueError("Missing required parameter 'app_id'.")
        if deployment_id is None:
            raise ValueError("Missing required parameter 'deployment_id'.")
        request_body_data = None
        url = f"{self.base_url}/v2/apps/{app_id}/deployments/{deployment_id}/cancel"
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

    def apps_get_logs(
        self,
        app_id: str,
        deployment_id: str,
        component_name: str,
        type: str,
        follow: bool | None = None,
        pod_connection_timeout: str | None = None,
    ) -> dict[str, Any]:
        """
        Retrieve Deployment Logs

        Args:
            app_id (string): app_id
            deployment_id (string): deployment_id
            component_name (string): component_name
            type (string): The type of logs to retrieve
        - BUILD: Build-time logs
        - DEPLOY: Deploy-time logs
        - RUN: Live run-time logs
        - RUN_RESTARTED: Logs of crashed/restarted instances during runtime Example: 'BUILD'.
            follow (boolean): Whether the logs should follow live updates. Example: 'True'.
            pod_connection_timeout (string): An optional time duration to wait if the underlying component instance is not immediately available. Default: `3m`. Example: '3m'.

        Returns:
            dict[str, Any]: A JSON object with urls that point to archived logs

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps
        """
        if app_id is None:
            raise ValueError("Missing required parameter 'app_id'.")
        if deployment_id is None:
            raise ValueError("Missing required parameter 'deployment_id'.")
        if component_name is None:
            raise ValueError("Missing required parameter 'component_name'.")
        url = f"{self.base_url}/v2/apps/{app_id}/deployments/{deployment_id}/components/{component_name}/logs"
        query_params = {
            k: v
            for k, v in [
                ("follow", follow),
                ("type", type),
                ("pod_connection_timeout", pod_connection_timeout),
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

    def apps_get_logs_aggregate(
        self,
        app_id: str,
        deployment_id: str,
        type: str,
        follow: bool | None = None,
        pod_connection_timeout: str | None = None,
    ) -> dict[str, Any]:
        """
        Retrieve Aggregate Deployment Logs

        Args:
            app_id (string): app_id
            deployment_id (string): deployment_id
            type (string): The type of logs to retrieve
        - BUILD: Build-time logs
        - DEPLOY: Deploy-time logs
        - RUN: Live run-time logs
        - RUN_RESTARTED: Logs of crashed/restarted instances during runtime Example: 'BUILD'.
            follow (boolean): Whether the logs should follow live updates. Example: 'True'.
            pod_connection_timeout (string): An optional time duration to wait if the underlying component instance is not immediately available. Default: `3m`. Example: '3m'.

        Returns:
            dict[str, Any]: A JSON object with urls that point to archived logs

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps
        """
        if app_id is None:
            raise ValueError("Missing required parameter 'app_id'.")
        if deployment_id is None:
            raise ValueError("Missing required parameter 'deployment_id'.")
        url = f"{self.base_url}/v2/apps/{app_id}/deployments/{deployment_id}/logs"
        query_params = {
            k: v
            for k, v in [
                ("follow", follow),
                ("type", type),
                ("pod_connection_timeout", pod_connection_timeout),
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

    def apps_get_exec(
        self,
        app_id: str,
        deployment_id: str,
        component_name: str,
        instance_name: str | None = None,
    ) -> dict[str, Any]:
        """
        Retrieve Exec URL for Deployment

        Args:
            app_id (string): app_id
            deployment_id (string): deployment_id
            component_name (string): component_name
            instance_name (string): The name of the actively running ephemeral compute instance Example: 'go-app-d768568df-zz77d'.

        Returns:
            dict[str, Any]: A JSON object with a websocket URL that allows sending/receiving console input and output.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps
        """
        if app_id is None:
            raise ValueError("Missing required parameter 'app_id'.")
        if deployment_id is None:
            raise ValueError("Missing required parameter 'deployment_id'.")
        if component_name is None:
            raise ValueError("Missing required parameter 'component_name'.")
        url = f"{self.base_url}/v2/apps/{app_id}/deployments/{deployment_id}/components/{component_name}/exec"
        query_params = {
            k: v for k, v in [("instance_name", instance_name)] if v is not None
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

    def get_app_logs(
        self,
        app_id: str,
        type: str,
        follow: bool | None = None,
        pod_connection_timeout: str | None = None,
    ) -> dict[str, Any]:
        """
        Retrieve Active Deployment Aggregate Logs

        Args:
            app_id (string): app_id
            type (string): The type of logs to retrieve
        - BUILD: Build-time logs
        - DEPLOY: Deploy-time logs
        - RUN: Live run-time logs
        - RUN_RESTARTED: Logs of crashed/restarted instances during runtime Example: 'BUILD'.
            follow (boolean): Whether the logs should follow live updates. Example: 'True'.
            pod_connection_timeout (string): An optional time duration to wait if the underlying component instance is not immediately available. Default: `3m`. Example: '3m'.

        Returns:
            dict[str, Any]: A JSON object with urls that point to archived logs

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps
        """
        if app_id is None:
            raise ValueError("Missing required parameter 'app_id'.")
        url = f"{self.base_url}/v2/apps/{app_id}/logs"
        query_params = {
            k: v
            for k, v in [
                ("follow", follow),
                ("type", type),
                ("pod_connection_timeout", pod_connection_timeout),
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

    def apps_list_instance_sizes(self) -> dict[str, Any]:
        """
        List Instance Sizes

        Returns:
            dict[str, Any]: A JSON with key `instance_sizes`

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps
        """
        url = f"{self.base_url}/v2/apps/tiers/instance_sizes"
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

    def apps_get_instance_size(self, slug: str) -> dict[str, Any]:
        """
        Retrieve an Instance Size

        Args:
            slug (string): slug

        Returns:
            dict[str, Any]: A JSON with key `instance_size`

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps
        """
        if slug is None:
            raise ValueError("Missing required parameter 'slug'.")
        url = f"{self.base_url}/v2/apps/tiers/instance_sizes/{slug}"
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

    def apps_list_regions(self) -> dict[str, Any]:
        """
        List App Regions

        Returns:
            dict[str, Any]: A JSON object with key `regions`

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps
        """
        url = f"{self.base_url}/v2/apps/regions"
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

    def apps_validate_app_spec(
        self, spec: dict[str, Any], app_id: str | None = None
    ) -> dict[str, Any]:
        """
        Propose an App Spec

        Args:
            spec (object): The desired configuration of an application. Example: {'name': 'web-app', 'region': 'nyc', 'services': [{'name': 'api', 'github': {'branch': 'main', 'deploy_on_push': True, 'repo': 'digitalocean/sample-golang'}, 'run_command': 'bin/api', 'environment_slug': 'node-js', 'instance_count': 2, 'instance_size_slug': 'apps-s-1vcpu-0.5gb', 'routes': [{'path': '/api'}]}]}.
            app_id (string): An optional ID of an existing app. If set, the spec will be treated as a proposed update to the specified app. The existing app is not modified using this method. Example: 'b6bdf840-2854-4f87-a36c-5f231c617c84'.

        Returns:
            dict[str, Any]: A JSON object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps
        """
        request_body_data = None
        request_body_data = {
            "spec": spec,
            "app_id": app_id,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/apps/propose"
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

    def apps_list_alerts(self, app_id: str) -> dict[str, Any]:
        """
        List all app alerts

        Args:
            app_id (string): app_id

        Returns:
            dict[str, Any]: A JSON object with a `alerts` key. This is list of object `alerts`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps
        """
        if app_id is None:
            raise ValueError("Missing required parameter 'app_id'.")
        url = f"{self.base_url}/v2/apps/{app_id}/alerts"
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

    def apps_assign_alert_destinations(
        self,
        app_id: str,
        alert_id: str,
        emails: list[str] | None = None,
        slack_webhooks: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """
        Update destinations for alerts

        Args:
            app_id (string): app_id
            alert_id (string): alert_id
            emails (array): emails Example: "['sammy@digitalocean.com']".
            slack_webhooks (array): slack_webhooks

        Returns:
            dict[str, Any]: A JSON object with an `alert` key. This is an object of type `alert`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps
        """
        if app_id is None:
            raise ValueError("Missing required parameter 'app_id'.")
        if alert_id is None:
            raise ValueError("Missing required parameter 'alert_id'.")
        request_body_data = None
        request_body_data = {
            "emails": emails,
            "slack_webhooks": slack_webhooks,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/apps/{app_id}/alerts/{alert_id}/destinations"
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

    def apps_create_rollback(
        self,
        app_id: str,
        deployment_id: str | None = None,
        skip_pin: bool | None = None,
    ) -> dict[str, Any]:
        """
        Rollback App

        Args:
            app_id (string): app_id
            deployment_id (string): The ID of the deployment to rollback to. Example: '3aa4d20e-5527-4c00-b496-601fbd22520a'.
            skip_pin (boolean): Whether to skip pinning the rollback deployment. If false, the rollback deployment will be pinned and any new deployments including Auto Deploy on Push hooks will be disabled until the rollback is either manually committed or reverted via the CommitAppRollback or RevertAppRollback endpoints respectively. If true, the rollback will be immediately committed and the app will remain unpinned. Example: 'False'.

        Returns:
            dict[str, Any]: A JSON object with a `deployment` key.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps
        """
        if app_id is None:
            raise ValueError("Missing required parameter 'app_id'.")
        request_body_data = None
        request_body_data = {
            "deployment_id": deployment_id,
            "skip_pin": skip_pin,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/apps/{app_id}/rollback"
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

    def apps_validate_rollback(
        self,
        app_id: str,
        deployment_id: str | None = None,
        skip_pin: bool | None = None,
    ) -> dict[str, Any]:
        """
        Validate App Rollback

        Args:
            app_id (string): app_id
            deployment_id (string): The ID of the deployment to rollback to. Example: '3aa4d20e-5527-4c00-b496-601fbd22520a'.
            skip_pin (boolean): Whether to skip pinning the rollback deployment. If false, the rollback deployment will be pinned and any new deployments including Auto Deploy on Push hooks will be disabled until the rollback is either manually committed or reverted via the CommitAppRollback or RevertAppRollback endpoints respectively. If true, the rollback will be immediately committed and the app will remain unpinned. Example: 'False'.

        Returns:
            dict[str, Any]: A JSON object with the validation results.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps
        """
        if app_id is None:
            raise ValueError("Missing required parameter 'app_id'.")
        request_body_data = None
        request_body_data = {
            "deployment_id": deployment_id,
            "skip_pin": skip_pin,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/apps/{app_id}/rollback/validate"
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

    def apps_commit_rollback(self, app_id: str) -> Any:
        """
        Commit App Rollback

        Args:
            app_id (string): app_id

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps
        """
        if app_id is None:
            raise ValueError("Missing required parameter 'app_id'.")
        request_body_data = None
        url = f"{self.base_url}/v2/apps/{app_id}/rollback/commit"
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

    def apps_revert_rollback(self, app_id: str) -> dict[str, Any]:
        """
        Revert App Rollback

        Args:
            app_id (string): app_id

        Returns:
            dict[str, Any]: A JSON object with a `deployment` key.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps
        """
        if app_id is None:
            raise ValueError("Missing required parameter 'app_id'.")
        request_body_data = None
        url = f"{self.base_url}/v2/apps/{app_id}/rollback/revert"
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

    def get_app_bandwidth_daily(
        self, app_id: str, date: str | None = None
    ) -> dict[str, Any]:
        """
        Retrieve App Daily Bandwidth Metrics

        Args:
            app_id (string): app_id
            date (string): Optional day to query. Only the date component of the timestamp will be considered. Default: yesterday. Example: '2023-01-17T00:00:00Z'.

        Returns:
            dict[str, Any]: A JSON object with a `app_bandwidth_usage` key

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps
        """
        if app_id is None:
            raise ValueError("Missing required parameter 'app_id'.")
        url = f"{self.base_url}/v2/apps/{app_id}/metrics/bandwidth_daily"
        query_params = {k: v for k, v in [("date", date)] if v is not None}
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

    def create_daily_bandwidth_metrics(
        self, app_ids: list[str], date: str | None = None
    ) -> dict[str, Any]:
        """
        Retrieve Multiple Apps' Daily Bandwidth Metrics

        Args:
            app_ids (array): A list of app IDs to query bandwidth metrics for. Example: "['4f6c71e2-1e90-4762-9fee-6cc4a0a9f2cf', 'c2a93513-8d9b-4223-9d61-5e7272c81cf5']".
            date (string): Optional day to query. Only the date component of the timestamp will be considered. Default: yesterday. Example: '2023-01-17T00:00:00Z'.

        Returns:
            dict[str, Any]: A JSON object with a `app_bandwidth_usage` key

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps
        """
        request_body_data = None
        request_body_data = {
            "app_ids": app_ids,
            "date": date,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/apps/metrics/bandwidth_daily"
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

    def apps_get_health(self, app_id: str) -> dict[str, Any]:
        """
        Retrieve App Health

        Args:
            app_id (string): app_id

        Returns:
            dict[str, Any]: A JSON with key `app_health`

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Apps
        """
        if app_id is None:
            raise ValueError("Missing required parameter 'app_id'.")
        url = f"{self.base_url}/v2/apps/{app_id}/health"
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

    def cdn_list_endpoints(
        self, per_page: int | None = None, page: int | None = None
    ) -> Any:
        """
        List All CDN Endpoints

        Args:
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: The result will be a JSON object with an `endpoints` key. This will be set to an array of endpoint objects, each of which will contain the standard CDN endpoint attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            CDN Endpoints
        """
        url = f"{self.base_url}/v2/cdn/endpoints"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def cdn_create_endpoint(
        self,
        origin: str,
        id: str | None = None,
        endpoint: str | None = None,
        ttl: int | None = None,
        certificate_id: str | None = None,
        custom_domain: str | None = None,
        created_at: str | None = None,
    ) -> Any:
        """
        Create a New CDN Endpoint

        Args:
            origin (string): The fully qualified domain name (FQDN) for the origin server which provides the content for the CDN. This is currently restricted to a Space. Example: 'static-images.nyc3.digitaloceanspaces.com'.
            id (string): A unique ID that can be used to identify and reference a CDN endpoint. Example: '892071a0-bb95-49bc-8021-3afd67a210bf'.
            endpoint (string): The fully qualified domain name (FQDN) from which the CDN-backed content is served. Example: 'static-images.nyc3.cdn.digitaloceanspaces.com'.
            ttl (integer): The amount of time the content is cached by the CDN's edge servers in seconds. TTL must be one of 60, 600, 3600, 86400, or 604800. Defaults to 3600 (one hour) when excluded. Example: '3600'.
            certificate_id (string): The ID of a DigitalOcean managed TLS certificate used for SSL when a custom subdomain is provided. Example: '892071a0-bb95-49bc-8021-3afd67a210bf'.
            custom_domain (string): The fully qualified domain name (FQDN) of the custom subdomain used with the CDN endpoint. Example: 'static.example.com'.
            created_at (string): A time value given in ISO8601 combined date and time format that represents when the CDN endpoint was created. Example: '2018-03-21T16:02:37Z'.

        Returns:
            Any: The response will be a JSON object with an `endpoint` key. This will be set to an object containing the standard CDN endpoint attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            CDN Endpoints
        """
        request_body_data = None
        request_body_data = {
            "id": id,
            "origin": origin,
            "endpoint": endpoint,
            "ttl": ttl,
            "certificate_id": certificate_id,
            "custom_domain": custom_domain,
            "created_at": created_at,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/cdn/endpoints"
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

    def cdn_get_endpoint(self, cdn_id: str) -> Any:
        """
        Retrieve an Existing CDN Endpoint

        Args:
            cdn_id (string): cdn_id

        Returns:
            Any: The response will be a JSON object with an `endpoint` key. This will be set to an object containing the standard CDN endpoint attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            CDN Endpoints
        """
        if cdn_id is None:
            raise ValueError("Missing required parameter 'cdn_id'.")
        url = f"{self.base_url}/v2/cdn/endpoints/{cdn_id}"
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

    def cdn_update_endpoints(
        self,
        cdn_id: str,
        ttl: int | None = None,
        certificate_id: str | None = None,
        custom_domain: str | None = None,
    ) -> Any:
        """
        Update a CDN Endpoint

        Args:
            cdn_id (string): cdn_id
            ttl (integer): The amount of time the content is cached by the CDN's edge servers in seconds. TTL must be one of 60, 600, 3600, 86400, or 604800. Defaults to 3600 (one hour) when excluded. Example: '3600'.
            certificate_id (string): The ID of a DigitalOcean managed TLS certificate used for SSL when a custom subdomain is provided. Example: '892071a0-bb95-49bc-8021-3afd67a210bf'.
            custom_domain (string): The fully qualified domain name (FQDN) of the custom subdomain used with the CDN endpoint. Example: 'static.example.com'.

        Returns:
            Any: The response will be a JSON object with an `endpoint` key. This will be set to an object containing the standard CDN endpoint attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            CDN Endpoints
        """
        if cdn_id is None:
            raise ValueError("Missing required parameter 'cdn_id'.")
        request_body_data = None
        request_body_data = {
            "ttl": ttl,
            "certificate_id": certificate_id,
            "custom_domain": custom_domain,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/cdn/endpoints/{cdn_id}"
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

    def cdn_delete_endpoint(self, cdn_id: str) -> Any:
        """
        Delete a CDN Endpoint

        Args:
            cdn_id (string): cdn_id

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            CDN Endpoints
        """
        if cdn_id is None:
            raise ValueError("Missing required parameter 'cdn_id'.")
        url = f"{self.base_url}/v2/cdn/endpoints/{cdn_id}"
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

    def cdn_purge_cache(self, cdn_id: str, files: list[str]) -> Any:
        """
        Purge the Cache for an Existing CDN Endpoint

        Args:
            cdn_id (string): cdn_id
            files (array): An array of strings containing the path to the content to be purged from the CDN cache. Example: "['path/to/image.png', 'path/to/css/*']".

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            CDN Endpoints
        """
        if cdn_id is None:
            raise ValueError("Missing required parameter 'cdn_id'.")
        request_body_data = {
            "files": files,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/cdn/endpoints/{cdn_id}/cache"
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

    def certificates_list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        name: str | None = None,
    ) -> Any:
        """
        List All Certificates

        Args:
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.
            name (string): Name of expected certificate Example: 'certificate-name'.

        Returns:
            Any: The result will be a JSON object with a `certificates` key. This will be set to an array of certificate objects, each of which will contain the standard certificate attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Certificates
        """
        url = f"{self.base_url}/v2/certificates"
        query_params = {
            k: v
            for k, v in [("per_page", per_page), ("page", page), ("name", name)]
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

    def certificates_create(
        self,
        name: str | None = None,
        type: str | None = None,
        dns_names: list[str] | None = None,
        private_key: str | None = None,
        leaf_certificate: str | None = None,
        certificate_chain: str | None = None,
    ) -> dict[str, Any]:
        """
        Create a New Certificate

        Args:
            name (string): A unique human-readable name referring to a certificate. Example: 'web-cert-01'.
            type (string): A string representing the type of the certificate. The value will be `custom` for a user-uploaded certificate or `lets_encrypt` for one automatically generated with Let's Encrypt. Example: 'lets_encrypt'.
            dns_names (array): An array of fully qualified domain names (FQDNs) for which the certificate was issued. A certificate covering all subdomains can be issued using a wildcard (e.g. `*.example.com`). Example: "['www.example.com', 'example.com']".
            private_key (string): The contents of a PEM-formatted private-key corresponding to the SSL certificate. Example: '-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDBIZMz8pnK6V52\nSVf+CYssOfCQHAx5f0Ou5rYbq3xNh8VHAIYJCQ1QxQIxKSP6+uODSYrb2KWyurP1\nDwGb8OYm0J3syEDtCUQik1cpCzpeNlAZ2f8FzXyYQAqPopxdRpsFz8DtZnVvu86X\nwrE4oFPl9MReICmZfBNWylpV5qgFPoXyJ70ZAsTm3cEe3n+LBXEnY4YrVDRWxA3w\nZ2mzZ03HZ1hHrxK9CMnS829U+8sK+UneZpCO7yLRPuxwhmps0wpK/YuZZfRAKF1F\nZRnak/SIQ28rnWufmdg16YqqHgl5JOgnb3aslKRvL4dI2Gwnkd2IHtpZnTR0gxFX\nfqqbQwuRAgMBAAECggEBAILLmkW0JzOkmLTDNzR0giyRkLoIROqDpfLtjKdwm95l\n9NUBJcU4vCvXQITKt/NhtnNTexcowg8pInb0ksJpg3UGE+4oMNBXVi2UW5MQZ5cm\ncVkQqgXkBF2YAY8FMaB6EML+0En2+dGR/3gIAr221xsFiXe1kHbB8Nb2c/d5HpFt\neRpLVJnK+TxSr78PcZA8DDGlSgwvgimdAaFUNO2OqB9/0E9UPyKk2ycdff/Z6ldF\n0hkCLtdYTTl8Kf/OwjcuTgmA2O3Y8/CoQX/L+oP9Rvt9pWCEfuebiOmHJVPO6Y6x\ngtQVEXwmF1pDHH4Qtz/e6UZTdYeMl9G4aNO2CawwcaYECgYEA57imgSOG4XsJLRh\nGGncV9R/xhy4AbDWLtAMzQRX4ktvKCaHWyQV2XK2we/cu29NLv2Y89WmerTNPOU+\nP8+pB31uty2ELySVn15QhKpQClVEAlxCnnNjXYrii5LOM80+lVmxvQwxVd8Yz8nj\nIntyioXNBEnYS7V2RxxFGgFun1cCgYEA1V3W+Uyamhq8JS5EY0FhyGcXdHd70K49\nW1ou7McIpncf9tM9acLS1hkI98rd2T69Zo8mKoV1V2hjFaKUYfNys6tTkYWeZCcJ\n3rW44j9DTD+FmmjcX6b8DzfybGLehfNbCw6n67/r45DXIV/fk6XZfkx6IEGO4ODt\nNfnvx4TuI1cCgYBACDiKqwSUvmkUuweOo4IuCxyb5Ee8v98P5JIE/VRDxlCbKbpx\npxEam6aBBQVcDi+n8o0H3WjjlKc6UqbW/01YMoMrvzotxNBLz8Y0QtQHZvR6KoCG\nRKCKstxTcWflzKuknbqN4RapAhNbKBDJ8PMSWfyDWNyaXzSmBdvaidbF1QKBgDI0\no4oD0Xkjg1QIYAUu9FBQmb9JAjRnW36saNBEQS/SZg4RRKknM683MtoDvVIKJk0E\nsAlfX+4SXQZRPDMUMtA+Jyrd0xhj6zmhbwClvDMr20crF3fWdgcqtft1BEFmsuyW\nJUMe5OWmRkjPI2+9ncDPRAllA7a8lnSV/Crph5N/AoGBAIK249temKrGe9pmsmAo\nQbNuYSmwpnMoAqdHTrl70HEmK7ob6SIVmsR8QFAkH7xkYZc4Bxbx4h1bdpozGB+/\nAangbiaYJcAOD1QyfiFbflvI1RFeHgrk7VIafeSeQv6qu0LLMi2zUbpgVzxt78Wg\neTuK2xNR0PIM8OI7pRpgyj1I\n-----END PRIVATE KEY-----'.
            leaf_certificate (string): The contents of a PEM-formatted public SSL certificate. Example: '-----BEGIN CERTIFICATE-----\nMIIFFjCCA/6gAwIBAgISA0AznUJmXhu08/89ZuSPC/kRMA0GCSqGSIb3DQEBCwUA\nMEoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQD\nExpMZXQncyBFbmNyeXB0IEF1dGhvcml0eSBYMzAeFw0xNjExMjQwMDIzMDBaFw0x\nNzAyMjIwMDIzMDBaMCQxIjAgBgNVBAMTGWNsb3VkLmFuZHJld3NvbWV0aGluZy5j\nb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDBIZMz8pnK6V52SVf+\nCYssOfCQHAx5f0Ou5rYbq3xNh8VWHIYJCQ1QxQIxKSP6+uODSYrb2KWyurP1DwGb\n8OYm0J3syEDtCUQik1cpCzpeNlAZ2f8FzXyYQAqPopxdRpsFz8DtZnVvu86XwrE4\noFPl9MReICmZfBNWylpV5qgFPoXyJ70ZAsTm3cEe3n+LBXEnY4YrVDRWxA3wZ2mz\nZ03HZ1hHrxK9CMnS829U+8sK+UneZpCO7yLRPuxwhmps0wpK/YuZZfRAKF1FZRna\nk/SIQ28rnWufmdg16YqqHgl5JOgnb3aslKRvL4dI2Gwnkd2IHtpZnTR0gxFXfqqb\nQwuRAgMBAAGjggIaMIICFjAOBgNVHQ8BAf8EBAMCBaAwHQYDVR0lBBYwFAYIKwYB\nBQUHAwEGCCsGAQUFBwMCMAwGA1UdEwEB/wQCMAAwHQYDVR0OBBYEFLsAFcxAhFX1\nMbCnzr9hEO5rL4jqMB8GA1UdIwQYMBaAFKhKamMEfd265tE5t6ZFZe/zqOyhMHAG\nCCsGAQUFBwEBBGQwYjAvBggrBgEFBQcwAYYjaHR0cDovL29jc3AuaW50LXgzLmxl\ndHNlbmNyeXB0Lm9yZy8wLwYIKwYBBQUHMAKGI2h0dHA6Ly9jZXJ0LmludC14My5s\nZXRzZW5jcnlwdC5vcmcvMCQGA1UdEQQdMBuCGWNsb3VkLmFuZHJld3NvbWV0aGlu\nZy5jb20wgf4GA1UdIASB9jCB8zAIBgZngQwBAgWrgeYGCysGAQQBgt8TAQEBMIHW\nMCYGCCsGAQUFBwIBFhpodHRwOi8vY3BzLmxldHNlbmNyeXB0Lm9yZzCBqwYIKwYB\nBQUHAgIwgZ4MgZtUaGlzIENlcnRpZmljYXRlIG1heSBvbmx5IGJlIHJlbGllZCB1\ncG9uIGJ5IFJlbHlpbmcgUGFydGllcyBhbmQgb25seSQ2ziBhY2NvcmRhbmNlIHdp\ndGggdGhlIENlcnRpZmljYXRlIFBvbGljeSBmb3VuZCBhdCBodHRwczovL2xldHNl\nbmNyeXB0Lm9yZy9yZXBvc2l0b3J5LzANBgkqhkiG9w0BAQsFAAOCAQEAOZVQvrjM\nPKXLARTjB5XsgfyDN3/qwLl7SmwGkPe+B+9FJpfScYG1JzVuCj/SoaPaK34G4x/e\niXwlwOXtMOtqjQYzNu2Pr2C+I+rVmaxIrCUXFmC205IMuUBEeWXG9Y/HvXQLPabD\nD3Gdl5+Feink9SDRP7G0HaAwq13hI7ARxkL9p+UIY39X0dV3WOboW2Re8nrkFXJ7\nq9Z6shK5QgpBfsLjtjNsQzaGV3ve1gOg25aTJGearBWOvEjJNA1wGMoKVXOtYwm/\nWyWoVdCQ8HmconcbJB6xc0UZ1EjvzRr5ZIvSa5uHZD0L3m7/kpPWlAlFJ7hHASPu\nUlF1zblDmg2Iaw==\n-----END CERTIFICATE-----'.
            certificate_chain (string): The full PEM-formatted trust chain between the certificate authority's certificate and your domain's SSL certificate. Example: '-----BEGIN CERTIFICATE-----\nMIIFFjCCA/6gAwIBAgISA0AznUJmXhu08/89ZuSPC/kRMA0GCSqGSIb3DQEBCwUA\nMEoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQD\nExpMZXQncyBFbmNyeXB0IEF1dGhvcml0eSBYMzAeFw0xNjExMjQwMDIzMDBaFw0x\nNzAyMjIwMDIzMDBaMCQxIjAgBgNVBAMTGWNsb3VkLmFuZHJld3NvbWV0aGluZy5j\nb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDBIZMz7tnK6V52SVf+\nCYssOfCQHAx5f0Ou5rYbq3xNh8VHAIYJCQ1QxQIxKSP6+uODSYrb2KWyurP1DwGb\n8OYm0J3syEDtCUQik1cpCzpeNlAZ2f8FzXyYQAqPopxdRpsFz8DtZnVvu86XwrE4\noFPl9MReICmZfBNWylpV5qgFPoXyJ70ZAsTm3cEe3n+LBXEnY4YrVDRWxA3wZ2mz\nZ03HZ1hHrxK9CMnS829U+8sK+UneZpCO7yLRPuxwhmps0wpK/YuZZfRAKF1FZRna\nk/SIQ28rnWufmdg16YqqHgl5JOgnb3aslKRvL4dI2Gwnkd2IHtpZnTR0gxFXfqqb\nQwuRAgMBAAGjggIaMIICFjAOBgNVHQ8BAf8EBAMCBaAwHQYDVR0lBBYwFAYIKwYB\nBQUHAwEGCCsGAQUFBwMCMAwGA1UdEwEB/wQCMAAwHQYDVR0OBBYEFLsAFcxAhFX1\nMbCnzr9hEO5rL4jqMB8GA1UdIwQYMBaAFKhKamMEfd265tE5t6ZFZe/zqOyhMHAG\nCCsGAQUFBwEBBGQwYjAvBggrBgEFBQcwAYYjaHR0cDovL29jc3AuaW50LXgzLmxl\ndHNlbmNyeXB0Lm9yZy8wLwYIKwYBBQUHMAKGI2h0dHA6Ly9jZXJ0LmludC14My5s\nZXRzZW5jcnlwdC5vcmcvMCQGA1UdEQQdMBuCGWNsb3VkLmFuZHJld3NvbWV0aGlu\nZy5jb20wgf4GA1UdIASB9jCB8zAIBgZngQwBAgEwgeWECysGAQQBgt8TAQEBMIHW\nMCYGCCsGAQUFBwIBFhpodHRwOi8vY3BzLmxldHNlbmNyeXB0Lm9yZzCBqwYIKwYB\nBQUHAgIwgZ4MgZtUaGlzIENlcnRpZmljYXRlIG1heSBvbmx5IGJlIHJlbGllZCB1\ncG9uIGJ5IFJlbHlpbmcgUGFydGllcyBhbmQgb25seSQ2ziBhY2NvcmRhbmNlIHdp\ndGggdGhlIENlcnRpZmljYXRlIFBvbGljeSBmb3VuZCBhdCBsdHRwczovL2xldHNl\nbmNyeXB0Lm9yZy9yZXBvc2l0b3J5LzANBgkqhkiG9w0BAQsFAAOCAQEAOZVQvrjM\nPKXLARTjB5XsgfyDN3/qwLl7SmwGkPe+B+9FJpfScYG1JzVuCj/SoaPaK34G4x/e\niXwlwOXtMOtqjQYzNu2Pr2C+I+rVmaxIrCUXFmC205IMuUBEeWXG9Y/HvXQLPabD\nD3Gdl5+Feink9SDRP7G0HaAwq13hI7ARxkL3o+UIY39X0dV3WOboW2Re8nrkFXJ7\nq9Z6shK5QgpBfsLjtjNsQzaGV3ve1gOg25aTJGearBWOvEjJNA1wGMoKVXOtYwm/\nWyWoVdCQ8HmconcbJB6xc0UZ1EjvzRr5ZIvSa5uHZD0L3m7/kpPWlAlFJ7hHASPu\nUlF1zblDmg2Iaw==\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIEkjCCA3qgAwIBAgIQCgFBQgAAAVOFc2oLheynCDANBgkqhkiG9w0BAQsFADA/\nMSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT\nDkRTVCBSb290IENBIFgzMB4XDTE2MDMxNzE2NDA0NloXDTIxMDMxNzE2NDA0Nlow\nSjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxIzAhBgNVBAMT\nGkxldCdzIEVuY3J5cHQgQXV0aG9yaXR5IFgzMIIBIjANBgkqhkiG9w0BAQEFAAOC\nAQ8AMIIBCgKCAQEAnNMM8FrlLsd3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EF\nq6meNQhY7LEqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8\nSMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0\nZ8h/pZq4UmEUEz9l6YKHy9v6Dlb2honzhT+Xhq+w3Brvaw2VFn3EK6BlspkENnWA\na6xK8xuQSXgvopZPKiAlKQTGdMDQMc2PMTiVFrqoM7hD8bEfwzB/onkxEz0tNvjj\n/PIzark5McWvxI0NHWQWM6r6hCm21AvA2H3DkwIPOIUo4IBfTCCAXkwEgYDVR0T\nAQH/BAgwBgEB/wIBADAOBgNVHQ8BAf8EBAMCAYYwfwYIKwYBBQUHAQEEczBxMDIG\nCCsGAQUFBzABhiZodHRwOi8vaXNyZy50cnVzdGlkLm9jc3AuaWRlbnRydXN0LmNv\nbTA7BggrBgEFBQcwAoYvaHR0cDovL2FwcHMuaWRlbnRydXN0LmNvbS9yb290cy9k\nc3Ryb290Y2F4My5wN2MwHwYDVR0jBBgwFoAUxKexpHsscfrb4UuQdf/EFWCFiRAw\nVAYDVR0gBE0wSzAIBgZngQwBAgEwPwYLKwYBBAGC3xMBAQEwMDAuBggrBgEFBQcC\nARYiaHR0cDovL2Nwcy5yb290LXgxLmxldHNlbmNyeXB0Lm9yZzA8BgNVHR8ENTAz\nMDGgL6AthitodHRwOi8vY3JsLmlkZW50cnVzdC5jb20vRFNUUk9PVENBWDNDUkwu\nY3JsMB0GA1UdDgQWBBSoSmpjBH3duubRObemRWXv86jsoTANBgkqhkiG9w0BAQsF\nAAOCAQEA3TPXEfNjWDjdGBX7CVW+dla5cEilaUcne8IkCJLxWh9KEik3JHRRHGJo\nuM2VcGfl96S8TihRzZvoroed6ti6WqEBmtzw3Wodatg+VyOeph4EYpr/1wXKtx8/\nwApIvJSwtmVi4MFU5aMqrSDE6ea73Mj2tcMyo5jMd6jmeWUHK8so/joWUoHOUgwu\nX4Po1QYz+3dszkDqMp4fklxBwXRsW10KXzPMTZ+sOPAveyxindmjkW8lGy+QsRlG\nPfZ+G6Z6h7mjem0Y+iWlkYcV4PIWL1iwBi8saCbGS5jN2p8M+X+Q7UNKEkROb3N6\nKOqkqm57TH2H3eDJAkSnh6/DNFu0Qg==\n-----END CERTIFICATE-----'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `certificate`. The value of this will be an object that contains the standard attributes associated with a certificate.
        When using Let's Encrypt, the initial value of the certificate's `state` attribute will be `pending`. When the certificate has been successfully issued by Let's Encrypt, this will transition to `verified` and be ready for use.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Certificates
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "type": type,
            "dns_names": dns_names,
            "private_key": private_key,
            "leaf_certificate": leaf_certificate,
            "certificate_chain": certificate_chain,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/certificates"
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

    def certificates_get(self, certificate_id: str) -> dict[str, Any]:
        """
        Retrieve an Existing Certificate

        Args:
            certificate_id (string): certificate_id

        Returns:
            dict[str, Any]: The response will be a JSON object with a `certificate` key. This will be set to an object containing the standard certificate attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Certificates
        """
        if certificate_id is None:
            raise ValueError("Missing required parameter 'certificate_id'.")
        url = f"{self.base_url}/v2/certificates/{certificate_id}"
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

    def certificates_delete(self, certificate_id: str) -> Any:
        """
        Delete a Certificate

        Args:
            certificate_id (string): certificate_id

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Certificates
        """
        if certificate_id is None:
            raise ValueError("Missing required parameter 'certificate_id'.")
        url = f"{self.base_url}/v2/certificates/{certificate_id}"
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

    def balance_get(self) -> dict[str, Any]:
        """
        Get Customer Balance

        Returns:
            dict[str, Any]: The response will be a JSON object that contains the following attributes

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Billing
        """
        url = f"{self.base_url}/v2/customers/my/balance"
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

    def billing_history_list(self) -> Any:
        """
        List Billing History

        Returns:
            Any: The response will be a JSON object that contains the following attributes

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Billing
        """
        url = f"{self.base_url}/v2/customers/my/billing_history"
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

    def invoices_list(
        self, per_page: int | None = None, page: int | None = None
    ) -> Any:
        """
        List All Invoices

        Args:
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: The response will be a JSON object contains that contains a list of invoices under the `invoices` key, and the invoice preview under the `invoice_preview` key.
        Each element contains the invoice summary attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Billing
        """
        url = f"{self.base_url}/v2/customers/my/invoices"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def invoices_get_by_uuid(
        self,
        invoice_uuid: str,
        per_page: int | None = None,
        page: int | None = None,
    ) -> Any:
        """
        Retrieve an Invoice by UUID

        Args:
            invoice_uuid (string): invoice_uuid
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: The response will be a JSON object with a key called `invoice_items`. This will be set to an array of invoice item objects.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Billing
        """
        if invoice_uuid is None:
            raise ValueError("Missing required parameter 'invoice_uuid'.")
        url = f"{self.base_url}/v2/customers/my/invoices/{invoice_uuid}"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def invoices_get_csv_by_uuid(self, invoice_uuid: str) -> Any:
        """
        Retrieve an Invoice CSV by UUID

        Args:
            invoice_uuid (string): invoice_uuid

        Returns:
            Any: The response will be a CSV file.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Billing
        """
        if invoice_uuid is None:
            raise ValueError("Missing required parameter 'invoice_uuid'.")
        url = f"{self.base_url}/v2/customers/my/invoices/{invoice_uuid}/csv"
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

    def invoices_get_pdf_by_uuid(self, invoice_uuid: str) -> Any:
        """
        Retrieve an Invoice PDF by UUID

        Args:
            invoice_uuid (string): invoice_uuid

        Returns:
            Any: The response will be a PDF file.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Billing
        """
        if invoice_uuid is None:
            raise ValueError("Missing required parameter 'invoice_uuid'.")
        url = f"{self.base_url}/v2/customers/my/invoices/{invoice_uuid}/pdf"
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

    def invoices_get_summary_by_uuid(self, invoice_uuid: str) -> dict[str, Any]:
        """
        Retrieve an Invoice Summary by UUID

        Args:
            invoice_uuid (string): invoice_uuid

        Returns:
            dict[str, Any]: To retrieve a summary for an invoice, send a GET request to  `/v2/customers/my/invoices/$INVOICE_UUID/summary`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Billing
        """
        if invoice_uuid is None:
            raise ValueError("Missing required parameter 'invoice_uuid'.")
        url = f"{self.base_url}/v2/customers/my/invoices/{invoice_uuid}/summary"
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

    def databases_list_options(self) -> dict[str, Any]:
        """
        List Database Options

        Returns:
            dict[str, Any]: A JSON string with a key of `options`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases, important
        """
        url = f"{self.base_url}/v2/databases/options"
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

    def databases_list_clusters(self, tag_name: str | None = None) -> Any:
        """
        List All Database Clusters

        Args:
            tag_name (string): Limits the results to database clusters with a specific tag. Example: 'production'.

        Returns:
            Any: A JSON object with a key of `databases`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        url = f"{self.base_url}/v2/databases"
        query_params = {k: v for k, v in [("tag_name", tag_name)] if v is not None}
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

    def databases_create_cluster(
        self,
        name: str,
        engine: str,
        num_nodes: int,
        size: str,
        region: str,
        id: str | None = None,
        version: str | None = None,
        semantic_version: str | None = None,
        status: str | None = None,
        created_at: str | None = None,
        private_network_uuid: str | None = None,
        tags: list[str] | None = None,
        db_names: list[str] | None = None,
        ui_connection: Any | None = None,
        connection: Any | None = None,
        private_connection: Any | None = None,
        standby_connection: Any | None = None,
        standby_private_connection: Any | None = None,
        users: list[dict[str, Any]] | None = None,
        maintenance_window: Any | None = None,
        project_id: str | None = None,
        rules: list[dict[str, Any]] | None = None,
        version_end_of_life: str | None = None,
        version_end_of_availability: str | None = None,
        storage_size_mib: int | None = None,
        metrics_endpoints: list[dict[str, Any]] | None = None,
        backup_restore: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Create a New Database Cluster

        Args:
            name (string): A unique, human-readable name referring to a database cluster. Example: 'backend'.
            engine (string): A slug representing the database engine used for the cluster. The possible values are: "pg" for PostgreSQL, "mysql" for MySQL, "redis" for Redis, "mongodb" for MongoDB, "kafka" for Kafka, "opensearch" for OpenSearch, and "valkey" for Valkey. Example: 'mysql'.
            num_nodes (integer): The number of nodes in the database cluster. Example: '2'.
            size (string): The slug identifier representing the size of the nodes in the database cluster. Example: 'db-s-2vcpu-4gb'.
            region (string): The slug identifier for the region where the database cluster is located. Example: 'nyc3'.
            id (string): A unique ID that can be used to identify and reference a database cluster. Example: '9cc10173-e9ea-4176-9dbc-a4cee4c4ff30'.
            version (string): A string representing the version of the database engine in use for the cluster. Example: '8'.
            semantic_version (string): A string representing the semantic version of the database engine in use for the cluster. Example: '8.0.28'.
            status (string): A string representing the current status of the database cluster. Example: 'creating'.
            created_at (string): A time value given in ISO8601 combined date and time format that represents when the database cluster was created. Example: '2019-01-11T18:37:36Z'.
            private_network_uuid (string): A string specifying the UUID of the VPC to which the database cluster will be assigned. If excluded, the cluster when creating a new database cluster, it will be assigned to your account's default VPC for the region. Example: 'd455e75d-4858-4eec-8c95-da2f0a5f93a7'.
            tags (array): An array of tags that have been applied to the database cluster. Example: "['production']".
            db_names (array): An array of strings containing the names of databases created in the database cluster. Example: "['doadmin']".
            ui_connection (string): The connection details for OpenSearch dashboard.
            connection (string): connection
            private_connection (string): private_connection
            standby_connection (string): standby_connection
            standby_private_connection (string): standby_private_connection
            users (array): users
            maintenance_window (string): maintenance_window
            project_id (string): The ID of the project that the database cluster is assigned to. If excluded when creating a new database cluster, it will be assigned to your default project. Example: '9cc10173-e9ea-4176-9dbc-a4cee4c4ff30'.
            rules (array): rules
            version_end_of_life (string): A timestamp referring to the date when the particular version will no longer be supported. If null, the version does not have an end of life timeline. Example: '2023-11-09T00:00:00Z'.
            version_end_of_availability (string): A timestamp referring to the date when the particular version will no longer be available for creating new clusters. If null, the version does not have an end of availability timeline. Example: '2023-05-09T00:00:00Z'.
            storage_size_mib (integer): Additional storage added to the cluster, in MiB. If null, no additional storage is added to the cluster, beyond what is provided as a base amount from the 'size' and any previously added additional storage. Example: '61440'.
            metrics_endpoints (array): Public hostname and port of the cluster's metrics endpoint(s). Includes one record for the cluster's primary node and a second entry for the cluster's standby node(s).
            backup_restore (object): backup_restore

        Returns:
            dict[str, Any]: A JSON object with a key of `database`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        request_body_data = None
        request_body_data = {
            "id": id,
            "name": name,
            "engine": engine,
            "version": version,
            "semantic_version": semantic_version,
            "num_nodes": num_nodes,
            "size": size,
            "region": region,
            "status": status,
            "created_at": created_at,
            "private_network_uuid": private_network_uuid,
            "tags": tags,
            "db_names": db_names,
            "ui_connection": ui_connection,
            "connection": connection,
            "private_connection": private_connection,
            "standby_connection": standby_connection,
            "standby_private_connection": standby_private_connection,
            "users": users,
            "maintenance_window": maintenance_window,
            "project_id": project_id,
            "rules": rules,
            "version_end_of_life": version_end_of_life,
            "version_end_of_availability": version_end_of_availability,
            "storage_size_mib": storage_size_mib,
            "metrics_endpoints": metrics_endpoints,
            "backup_restore": backup_restore,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/databases"
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

    def databases_get_cluster(self, database_cluster_uuid: str) -> dict[str, Any]:
        """
        Retrieve an Existing Database Cluster

        Args:
            database_cluster_uuid (string): database_cluster_uuid

        Returns:
            dict[str, Any]: A JSON object with a key of `database`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}"
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

    def databases_destroy_cluster(self, database_cluster_uuid: str) -> Any:
        """
        Destroy a Database Cluster

        Args:
            database_cluster_uuid (string): database_cluster_uuid

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}"
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

    def databases_get_config(self, database_cluster_uuid: str) -> dict[str, Any]:
        """
        Retrieve an Existing Database Cluster Configuration

        Args:
            database_cluster_uuid (string): database_cluster_uuid

        Returns:
            dict[str, Any]: A JSON object with a key of `config`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/config"
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

    def databases_patch_config(
        self, database_cluster_uuid: str, config: Any | None = None
    ) -> Any:
        """
        Update the Database Configuration for an Existing Database

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            config (string): config Example: {'sql_mode': 'ANSI,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION,NO_ZERO_DATE,NO_ZERO_IN_DATE,STRICT_ALL_TABLES', 'sql_require_primary_key': True}.

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        request_body_data = None
        request_body_data = {
            "config": config,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/config"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def databases_get_ca(self, database_cluster_uuid: str) -> dict[str, Any]:
        """
        Retrieve the Public Certificate

        Args:
            database_cluster_uuid (string): database_cluster_uuid

        Returns:
            dict[str, Any]: A JSON object with a key of `ca`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/ca"
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

    def databases_get_migration_status(
        self, database_cluster_uuid: str
    ) -> dict[str, Any]:
        """
        Retrieve the Status of an Online Migration

        Args:
            database_cluster_uuid (string): database_cluster_uuid

        Returns:
            dict[str, Any]: A JSON object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/online-migration"
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

    def start_online_migration(
        self,
        database_cluster_uuid: str,
        source: dict[str, Any],
        disable_ssl: bool | None = None,
        ignore_dbs: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Start an Online Migration

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            source (object): source Example: {'host': 'source-do-user-6607903-0.b.db.ondigitalocean.com', 'dbname': 'defaultdb', 'port': 25060, 'username': 'doadmin', 'password': 'paakjnfe10rsrsmf'}.
            disable_ssl (boolean): Enables SSL encryption when connecting to the source database. Example: 'False'.
            ignore_dbs (array): List of databases that should be ignored during migration. Example: "['db0', 'db1']".

        Returns:
            dict[str, Any]: A JSON object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        request_body_data = None
        request_body_data = {
            "source": source,
            "disable_ssl": disable_ssl,
            "ignore_dbs": ignore_dbs,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/online-migration"
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

    def delete_online_migration_by_id(
        self, database_cluster_uuid: str, migration_id: str
    ) -> Any:
        """
        Stop an Online Migration

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            migration_id (string): migration_id

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        if migration_id is None:
            raise ValueError("Missing required parameter 'migration_id'.")
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/online-migration/{migration_id}"
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

    def databases_update_region(self, database_cluster_uuid: str, region: str) -> Any:
        """
        Migrate a Database Cluster to a New Region

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            region (string): A slug identifier for the region to which the database cluster will be migrated. Example: 'lon1'.

        Returns:
            Any: This does not indicate the success or failure of any operation, just that the request has been accepted for processing.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        request_body_data = None
        request_body_data = {
            "region": region,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/migrate"
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

    def databases_update_cluster_size(
        self,
        database_cluster_uuid: str,
        size: str,
        num_nodes: int,
        storage_size_mib: int | None = None,
    ) -> Any:
        """
        Resize a Database Cluster

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            size (string): A slug identifier representing desired the size of the nodes in the database cluster. Example: 'db-s-4vcpu-8gb'.
            num_nodes (integer): The number of nodes in the database cluster. Valid values are are 1-3. In addition to the primary node, up to two standby nodes may be added for highly available configurations. Example: '3'.
            storage_size_mib (integer): Additional storage added to the cluster, in MiB. If null, no additional storage is added to the cluster, beyond what is provided as a base amount from the 'size' and any previously added additional storage. Example: '61440'.

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        request_body_data = None
        request_body_data = {
            "size": size,
            "num_nodes": num_nodes,
            "storage_size_mib": storage_size_mib,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/resize"
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

    def databases_list_firewall_rules(self, database_cluster_uuid: str) -> Any:
        """
        List Firewall Rules (Trusted Sources) for a Database Cluster

        Args:
            database_cluster_uuid (string): database_cluster_uuid

        Returns:
            Any: A JSON object with a key of `rules`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/firewall"
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

    def update_database_cluster_firewall(
        self, database_cluster_uuid: str, rules: list[dict[str, Any]] | None = None
    ) -> Any:
        """
        Update Firewall Rules (Trusted Sources) for a Database

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            rules (array): rules Example: [{'type': 'ip_addr', 'value': '192.168.1.1'}, {'type': 'k8s', 'value': 'ff2a6c52-5a44-4b63-b99c-0e98e7a63d61'}, {'type': 'droplet', 'value': '163973392'}, {'type': 'tag', 'value': 'backend'}].

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        request_body_data = None
        request_body_data = {
            "rules": rules,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/firewall"
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

    def update_database_maintenance(
        self,
        database_cluster_uuid: str,
        day: str,
        hour: str,
        pending: bool | None = None,
        description: list[str] | None = None,
    ) -> Any:
        """
        Configure a Database Cluster's Maintenance Window

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            day (string): The day of the week on which to apply maintenance updates. Example: 'tuesday'.
            hour (string): The hour in UTC at which maintenance updates will be applied in 24 hour format. Example: '14:00'.
            pending (boolean): A boolean value indicating whether any maintenance is scheduled to be performed in the next window. Example: 'True'.
            description (array): A list of strings, each containing information about a pending maintenance update. Example: "['Update TimescaleDB to version 1.2.1', 'Upgrade to PostgreSQL 11.2 and 10.7 bugfix releases']".

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        request_body_data = None
        request_body_data = {
            "day": day,
            "hour": hour,
            "pending": pending,
            "description": description,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/maintenance"
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

    def databases_install_update(self, database_cluster_uuid: str) -> Any:
        """
        Start Database Maintenance

        Args:
            database_cluster_uuid (string): database_cluster_uuid

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        request_body_data = None
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/install_update"
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

    def databases_list_backups(self, database_cluster_uuid: str) -> dict[str, Any]:
        """
        List Backups for a Database Cluster

        Args:
            database_cluster_uuid (string): database_cluster_uuid

        Returns:
            dict[str, Any]: A JSON object with a key of `database_backups`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/backups"
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

    def databases_list_replicas(self, database_cluster_uuid: str) -> Any:
        """
        List All Read-only Replicas

        Args:
            database_cluster_uuid (string): database_cluster_uuid

        Returns:
            Any: A JSON object with a key of `replicas`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/replicas"
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

    def databases_create_replica(
        self,
        database_cluster_uuid: str,
        id: str | None = None,
        name: str | None = None,
        region: str | None = None,
        size: str | None = None,
        status: str | None = None,
        tags: list[str] | None = None,
        created_at: str | None = None,
        private_network_uuid: str | None = None,
        connection: Any | None = None,
        private_connection: Any | None = None,
        storage_size_mib: int | None = None,
    ) -> dict[str, Any]:
        """
        Create a Read-only Replica

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            id (string): A unique ID that can be used to identify and reference a database replica. Example: '9cc10173-e9ea-4176-9dbc-a4cee4c4ff30'.
            name (string): The name to give the read-only replicating Example: 'read-nyc3-01'.
            region (string): A slug identifier for the region where the read-only replica will be located. If excluded, the replica will be placed in the same region as the cluster. Example: 'nyc3'.
            size (string): A slug identifier representing the size of the node for the read-only replica. The size of the replica must be at least as large as the node size for the database cluster from which it is replicating. Example: 'db-s-2vcpu-4gb'.
            status (string): A string representing the current status of the database cluster. Example: 'creating'.
            tags (array): A flat array of tag names as strings to apply to the read-only replica after it is created. Tag names can either be existing or new tags. Example: "['production']".
            created_at (string): A time value given in ISO8601 combined date and time format that represents when the database cluster was created. Example: '2019-01-11T18:37:36Z'.
            private_network_uuid (string): A string specifying the UUID of the VPC to which the read-only replica will be assigned. If excluded, the replica will be assigned to your account's default VPC for the region. Example: '9423cbad-9211-442f-820b-ef6915e99b5f'.
            connection (string): connection
            private_connection (string): private_connection
            storage_size_mib (integer): Additional storage added to the cluster, in MiB. If null, no additional storage is added to the cluster, beyond what is provided as a base amount from the 'size' and any previously added additional storage. Example: '61440'.

        Returns:
            dict[str, Any]: A JSON object with a key of `replica`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "name": name,
            "region": region,
            "size": size,
            "status": status,
            "tags": tags,
            "created_at": created_at,
            "private_network_uuid": private_network_uuid,
            "connection": connection,
            "private_connection": private_connection,
            "storage_size_mib": storage_size_mib,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/replicas"
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

    def databases_list_events_logs(self, database_cluster_uuid: str) -> Any:
        """
        List all Events Logs

        Args:
            database_cluster_uuid (string): database_cluster_uuid

        Returns:
            Any: A JSON object with a key of `events`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/events"
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

    def databases_get_replica(
        self, database_cluster_uuid: str, replica_name: str
    ) -> dict[str, Any]:
        """
        Retrieve an Existing Read-only Replica

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            replica_name (string): replica_name

        Returns:
            dict[str, Any]: A JSON object with a key of `replica`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        if replica_name is None:
            raise ValueError("Missing required parameter 'replica_name'.")
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/replicas/{replica_name}"
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

    def databases_destroy_replica(
        self, database_cluster_uuid: str, replica_name: str
    ) -> Any:
        """
        Destroy a Read-only Replica

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            replica_name (string): replica_name

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        if replica_name is None:
            raise ValueError("Missing required parameter 'replica_name'.")
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/replicas/{replica_name}"
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

    def databases_promote_replica(
        self, database_cluster_uuid: str, replica_name: str
    ) -> Any:
        """
        Promote a Read-only Replica to become a Primary Cluster

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            replica_name (string): replica_name

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        if replica_name is None:
            raise ValueError("Missing required parameter 'replica_name'.")
        request_body_data = None
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/replicas/{replica_name}/promote"
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

    def databases_list_users(self, database_cluster_uuid: str) -> Any:
        """
        List all Database Users

        Args:
            database_cluster_uuid (string): database_cluster_uuid

        Returns:
            Any: A JSON object with a key of `users`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/users"
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

    def databases_add_user(
        self,
        database_cluster_uuid: str,
        name: str,
        role: str | None = None,
        password: str | None = None,
        access_cert: str | None = None,
        access_key: str | None = None,
        mysql_settings: dict[str, Any] | None = None,
        settings: dict[str, Any] | None = None,
        readonly: bool | None = None,
    ) -> dict[str, Any]:
        """
        Add a Database User

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            name (string): The name of a database user. Example: 'app-01'.
            role (string): A string representing the database user's role. The value will be either
        "primary" or "normal".
         Example: 'normal'.
            password (string): A randomly generated password for the database user. Example: 'jge5lfxtzhx42iff'.
            access_cert (string): Access certificate for TLS client authentication. (Kafka only) Example: '-----BEGIN CERTIFICATE-----\nMIIFFjCCA/6gAwIBAgISA0AznUJmXhu08/89ZuSPC/kRMA0GCSqGSIb3DQEBCwUA\nMEoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQD\nExpMZXQncyBFbmNyeXB0IEF1dGhvcml0eSBYMzAeFw0xNjExMjQwMDIzMDBaFw0x\nNzAyMjIwMDIzMDBaMCQxIjAgBgNVBAMTGWNsb3VkLmFuZHJld3NvbWV0aGluZy5j\nb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDBIZMz8pnK6V52SVf+\nCYssOfCQHAx5f0Ou5rYbq3xNh8VWHIYJCQ1QxQIxKSP6+uODSYrb2KWyurP1DwGb\n8OYm0J3syEDtCUQik1cpCzpeNlAZ2f8FzXyYQAqPopxdRpsFz8DtZnVvu86XwrE4\noFPl9MReICmZfBNWylpV5qgFPoXyJ70ZAsTm3cEe3n+LBXEnY4YrVDRWxA3wZ2mz\nZ03HZ1hHrxK9CMnS829U+8sK+UneZpCO7yLRPuxwhmps0wpK/YuZZfRAKF1FZRna\nk/SIQ28rnWufmdg16YqqHgl5JOgnb3aslKRvL4dI2Gwnkd2IHtpZnTR0gxFXfqqb\nQwuRAgMBAAGjggIaMIICFjAOBgNVHQ8BAf8EBAMCBaAwHQYDVR0lBBYwFAYIKwYB\nBQUHAwEGCCsGAQUFBwMCMAwGA1UdEwEB/wQCMAAwHQYDVR0OBBYEFLsAFcxAhFX1\nMbCnzr9hEO5rL4jqMB8GA1UdIwQYMBaAFKhKamMEfd265tE5t6ZFZe/zqOyhMHAG\nCCsGAQUFBwEBBGQwYjAvBggrBgEFBQcwAYYjaHR0cDovL29jc3AuaW50LXgzLmxl\ndHNlbmNyeXB0Lm9yZy8wLwYIKwYBBQUHMAKGI2h0dHA6Ly9jZXJ0LmludC14My5s\nZXRzZW5jcnlwdC5vcmcvMCQGA1UdEQQdMBuCGWNsb3VkLmFuZHJld3NvbWV0aGlu\nZy5jb20wgf4GA1UdIASB9jCB8zAIBgZngQwBAgWrgeYGCysGAQQBgt8TAQEBMIHW\nMCYGCCsGAQUFBwIBFhpodHRwOi8vY3BzLmxldHNlbmNyeXB0Lm9yZzCBqwYIKwYB\nBQUHAgIwgZ4MgZtUaGlzIENlcnRpZmljYXRlIG1heSBvbmx5IGJlIHJlbGllZCB1\ncG9uIGJ5IFJlbHlpbmcgUGFydGllcyBhbmQgb25seSQ2ziBhY2NvcmRhbmNlIHdp\ndGggdGhlIENlcnRpZmljYXRlIFBvbGljeSBmb3VuZCBhdCBodHRwczovL2xldHNl\nbmNyeXB0Lm9yZy9yZXBvc2l0b3J5LzANBgkqhkiG9w0BAQsFAAOCAQEAOZVQvrjM\nPKXLARTjB5XsgfyDN3/qwLl7SmwGkPe+B+9FJpfScYG1JzVuCj/SoaPaK34G4x/e\niXwlwOXtMOtqjQYzNu2Pr2C+I+rVmaxIrCUXFmC205IMuUBEeWXG9Y/HvXQLPabD\nD3Gdl5+Feink9SDRP7G0HaAwq13hI7ARxkL9p+UIY39X0dV3WOboW2Re8nrkFXJ7\nq9Z6shK5QgpBfsLjtjNsQzaGV3ve1gOg25aTJGearBWOvEjJNA1wGMoKVXOtYwm/\nWyWoVdCQ8HmconcbJB6xc0UZ1EjvzRr5ZIvSa5uHZD0L3m7/kpPWlAlFJ7hHASPu\nUlF1zblDmg2Iaw==\n-----END CERTIFICATE-----'.
            access_key (string): Access key for TLS client authentication. (Kafka only) Example: '-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDBIZMz8pnK6V52\nSVf+CYssOfCQHAx5f0Ou5rYbq3xNh8VHAIYJCQ1QxQIxKSP6+uODSYrb2KWyurP1\nDwGb8OYm0J3syEDtCUQik1cpCzpeNlAZ2f8FzXyYQAqPopxdRpsFz8DtZnVvu86X\nwrE4oFPl9MReICmZfBNWylpV5qgFPoXyJ70ZAsTm3cEe3n+LBXEnY4YrVDRWxA3w\nZ2mzZ03HZ1hHrxK9CMnS829U+8sK+UneZpCO7yLRPuxwhmps0wpK/YuZZfRAKF1F\nZRnak/SIQ28rnWufmdg16YqqHgl5JOgnb3aslKRvL4dI2Gwnkd2IHtpZnTR0gxFX\nfqqbQwuRAgMBAAECggEBAILLmkW0JzOkmLTDNzR0giyRkLoIROqDpfLtjKdwm95l\n9NUBJcU4vCvXQITKt/NhtnNTexcowg8pInb0ksJpg3UGE+4oMNBXVi2UW5MQZ5cm\ncVkQqgXkBF2YAY8FMaB6EML+0En2+dGR/3gIAr221xsFiXe1kHbB8Nb2c/d5HpFt\neRpLVJnK+TxSr78PcZA8DDGlSgwvgimdAaFUNO2OqB9/0E9UPyKk2ycdff/Z6ldF\n0hkCLtdYTTl8Kf/OwjcuTgmA2O3Y8/CoQX/L+oP9Rvt9pWCEfuebiOmHJVPO6Y6x\ngtQVEXwmF1pDHH4Qtz/e6UZTdYeMl9G4aNO2CawwcaYECgYEA57imgSOG4XsJLRh\nGGncV9R/xhy4AbDWLtAMzQRX4ktvKCaHWyQV2XK2we/cu29NLv2Y89WmerTNPOU+\nP8+pB31uty2ELySVn15QhKpQClVEAlxCnnNjXYrii5LOM80+lVmxvQwxVd8Yz8nj\nIntyioXNBEnYS7V2RxxFGgFun1cCgYEA1V3W+Uyamhq8JS5EY0FhyGcXdHd70K49\nW1ou7McIpncf9tM9acLS1hkI98rd2T69Zo8mKoV1V2hjFaKUYfNys6tTkYWeZCcJ\n3rW44j9DTD+FmmjcX6b8DzfybGLehfNbCw6n67/r45DXIV/fk6XZfkx6IEGO4ODt\nNfnvx4TuI1cCgYBACDiKqwSUvmkUuweOo4IuCxyb5Ee8v98P5JIE/VRDxlCbKbpx\npxEam6aBBQVcDi+n8o0H3WjjlKc6UqbW/01YMoMrvzotxNBLz8Y0QtQHZvR6KoCG\nRKCKstxTcWflzKuknbqN4RapAhNbKBDJ8PMSWfyDWNyaXzSmBdvaidbF1QKBgDI0\no4oD0Xkjg1QIYAUu9FBQmb9JAjRnW36saNBEQS/SZg4RRKknM683MtoDvVIKJk0E\nsAlfX+4SXQZRPDMUMtA+Jyrd0xhj6zmhbwClvDMr20crF3fWdgcqtft1BEFmsuyW\nJUMe5OWmRkjPI2+9ncDPRAllA7a8lnSV/Crph5N/AoGBAIK249temKrGe9pmsmAo\nQbNuYSmwpnMoAqdHTrl70HEmK7ob6SIVmsR8QFAkH7xkYZc4Bxbx4h1bdpozGB+/\nAangbiaYJcAOD1QyfiFbflvI1RFeHgrk7VIafeSeQv6qu0LLMi2zUbpgVzxt78Wg\neTuK2xNR0PIM8OI7pRpgyj1I\n-----END PRIVATE KEY-----'.
            mysql_settings (object): mysql_settings
            settings (object): settings
            readonly (boolean): (To be deprecated: use settings.mongo_user_settings.role instead for access controls to MongoDB databases).
        For MongoDB clusters, set to `true` to create a read-only user.
        This option is not currently supported for other database engines.

         Example: 'True'.

        Returns:
            dict[str, Any]: A JSON object with a key of `user`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "role": role,
            "password": password,
            "access_cert": access_cert,
            "access_key": access_key,
            "mysql_settings": mysql_settings,
            "settings": settings,
            "readonly": readonly,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/users"
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

    def databases_get_user(
        self, database_cluster_uuid: str, username: str
    ) -> dict[str, Any]:
        """
        Retrieve an Existing Database User

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            username (string): username

        Returns:
            dict[str, Any]: A JSON object with a key of `user`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        if username is None:
            raise ValueError("Missing required parameter 'username'.")
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/users/{username}"
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

    def databases_delete_user(self, database_cluster_uuid: str, username: str) -> Any:
        """
        Remove a Database User

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            username (string): username

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        if username is None:
            raise ValueError("Missing required parameter 'username'.")
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/users/{username}"
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

    def databases_update_user(
        self, database_cluster_uuid: str, username: str, settings: dict[str, Any]
    ) -> dict[str, Any]:
        """
        Update a Database User

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            username (string): username
            settings (object): settings Example: {'acl': [{'id': 'acl128aaaa99239', 'permission': 'produceconsume', 'topic': 'customer-events'}, {'id': 'acl293098flskdf', 'permission': 'produce', 'topic': 'customer-events.*'}, {'id': 'acl128ajei20123', 'permission': 'consume', 'topic': 'customer-events'}]}.

        Returns:
            dict[str, Any]: A JSON object with a key of `user`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        if username is None:
            raise ValueError("Missing required parameter 'username'.")
        request_body_data = None
        request_body_data = {
            "settings": settings,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/users/{username}"
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

    def databases_reset_auth(
        self,
        database_cluster_uuid: str,
        username: str,
        mysql_settings: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Reset a Database User's Password or Authentication Method

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            username (string): username
            mysql_settings (object): mysql_settings Example: {'auth_plugin': 'caching_sha2_password'}.

        Returns:
            dict[str, Any]: A JSON object with a key of `user`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        if username is None:
            raise ValueError("Missing required parameter 'username'.")
        request_body_data = None
        request_body_data = {
            "mysql_settings": mysql_settings,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/users/{username}/reset_auth"
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

    def databases_list(self, database_cluster_uuid: str) -> Any:
        """
        List All Databases

        Args:
            database_cluster_uuid (string): database_cluster_uuid

        Returns:
            Any: A JSON object with a key of `databases`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases, important
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/dbs"
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

    def databases_add(self, database_cluster_uuid: str, name: str) -> dict[str, Any]:
        """
        Add a New Database

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            name (string): The name of the database. Example: 'alpha'.

        Returns:
            dict[str, Any]: A JSON object with a key of `db`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        request_body_data = None
        request_body_data = {
            "name": name,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/dbs"
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

    def databases_get(
        self, database_cluster_uuid: str, database_name: str
    ) -> dict[str, Any]:
        """
        Retrieve an Existing Database

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            database_name (string): database_name

        Returns:
            dict[str, Any]: A JSON object with a key of `db`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        if database_name is None:
            raise ValueError("Missing required parameter 'database_name'.")
        url = (
            f"{self.base_url}/v2/databases/{database_cluster_uuid}/dbs/{database_name}"
        )
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

    def databases_delete(self, database_cluster_uuid: str, database_name: str) -> Any:
        """
        Delete a Database

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            database_name (string): database_name

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        if database_name is None:
            raise ValueError("Missing required parameter 'database_name'.")
        url = (
            f"{self.base_url}/v2/databases/{database_cluster_uuid}/dbs/{database_name}"
        )
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

    def databases_list_connection_pools(
        self, database_cluster_uuid: str
    ) -> dict[str, Any]:
        """
        List Connection Pools (PostgreSQL)

        Args:
            database_cluster_uuid (string): database_cluster_uuid

        Returns:
            dict[str, Any]: A JSON object with a key of `pools`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/pools"
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

    def databases_add_connection_pool(
        self,
        database_cluster_uuid: str,
        name: str,
        mode: str,
        size: int,
        db: str,
        user: str | None = None,
        connection: Any | None = None,
        private_connection: Any | None = None,
        standby_connection: Any | None = None,
        standby_private_connection: Any | None = None,
    ) -> dict[str, Any]:
        """
        Add a New Connection Pool (PostgreSQL)

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            name (string): A unique name for the connection pool. Must be between 3 and 60 characters. Example: 'backend-pool'.
            mode (string): The PGBouncer transaction mode for the connection pool. The allowed values are session, transaction, and statement. Example: 'transaction'.
            size (integer): The desired size of the PGBouncer connection pool. The maximum allowed size is determined by the size of the cluster's primary node. 25 backend server connections are allowed for every 1GB of RAM. Three are reserved for maintenance. For example, a primary node with 1 GB of RAM allows for a maximum of 22 backend server connections while one with 4 GB would allow for 97. Note that these are shared across all connection pools in a cluster. Example: '10'.
            db (string): The database for use with the connection pool. Example: 'defaultdb'.
            user (string): The name of the user for use with the connection pool. When excluded, all sessions connect to the database as the inbound user. Example: 'doadmin'.
            connection (string): connection
            private_connection (string): private_connection
            standby_connection (string): standby_connection
            standby_private_connection (string): standby_private_connection

        Returns:
            dict[str, Any]: A JSON object with a key of `pool`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "mode": mode,
            "size": size,
            "db": db,
            "user": user,
            "connection": connection,
            "private_connection": private_connection,
            "standby_connection": standby_connection,
            "standby_private_connection": standby_private_connection,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/pools"
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

    def databases_get_connection_pool(
        self, database_cluster_uuid: str, pool_name: str
    ) -> dict[str, Any]:
        """
        Retrieve Existing Connection Pool (PostgreSQL)

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            pool_name (string): pool_name

        Returns:
            dict[str, Any]: A JSON object with a key of `pool`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        if pool_name is None:
            raise ValueError("Missing required parameter 'pool_name'.")
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/pools/{pool_name}"
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

    def update_database_pool(
        self,
        database_cluster_uuid: str,
        pool_name: str,
        mode: str,
        size: int,
        db: str,
        user: str | None = None,
    ) -> Any:
        """
        Update Connection Pools (PostgreSQL)

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            pool_name (string): pool_name
            mode (string): The PGBouncer transaction mode for the connection pool. The allowed values are session, transaction, and statement. Example: 'transaction'.
            size (integer): The desired size of the PGBouncer connection pool. The maximum allowed size is determined by the size of the cluster's primary node. 25 backend server connections are allowed for every 1GB of RAM. Three are reserved for maintenance. For example, a primary node with 1 GB of RAM allows for a maximum of 22 backend server connections while one with 4 GB would allow for 97. Note that these are shared across all connection pools in a cluster. Example: '10'.
            db (string): The database for use with the connection pool. Example: 'defaultdb'.
            user (string): The name of the user for use with the connection pool. When excluded, all sessions connect to the database as the inbound user. Example: 'doadmin'.

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        if pool_name is None:
            raise ValueError("Missing required parameter 'pool_name'.")
        request_body_data = None
        request_body_data = {
            "mode": mode,
            "size": size,
            "db": db,
            "user": user,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/pools/{pool_name}"
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

    def delete_pool(self, database_cluster_uuid: str, pool_name: str) -> Any:
        """
        Delete a Connection Pool (PostgreSQL)

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            pool_name (string): pool_name

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        if pool_name is None:
            raise ValueError("Missing required parameter 'pool_name'.")
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/pools/{pool_name}"
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

    def databases_get_eviction_policy(self, database_cluster_uuid: str) -> Any:
        """
        Retrieve the Eviction Policy for a Redis or Valkey Cluster

        Args:
            database_cluster_uuid (string): database_cluster_uuid

        Returns:
            Any: A JSON string with a key of `eviction_policy`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/eviction_policy"
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

    def update_eviction_policy(
        self, database_cluster_uuid: str, eviction_policy: str
    ) -> Any:
        """
        Configure the Eviction Policy for a Redis or Valkey Cluster

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            eviction_policy (string): A string specifying the desired eviction policy for a Redis or Valkey cluster.

        - `noeviction`: Don't evict any data, returns error when memory limit is reached.
        - `allkeys_lru:` Evict any key, least recently used (LRU) first.
        - `allkeys_random`: Evict keys in a random order.
        - `volatile_lru`: Evict keys with expiration only, least recently used (LRU) first.
        - `volatile_random`: Evict keys with expiration only in a random order.
        - `volatile_ttl`: Evict keys with expiration only, shortest time-to-live (TTL) first. Example: 'allkeys_lru'.

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        request_body_data = None
        request_body_data = {
            "eviction_policy": eviction_policy,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/eviction_policy"
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

    def databases_get_sql_mode(self, database_cluster_uuid: str) -> dict[str, Any]:
        """
        Retrieve the SQL Modes for a MySQL Cluster

        Args:
            database_cluster_uuid (string): database_cluster_uuid

        Returns:
            dict[str, Any]: A JSON string with a key of `sql_mode`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/sql_mode"
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

    def databases_update_sql_mode(
        self, database_cluster_uuid: str, sql_mode: str
    ) -> Any:
        """
        Update SQL Mode for a Cluster

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            sql_mode (string): A string specifying the configured SQL modes for the MySQL cluster. Example: 'ANSI,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION,NO_ZERO_DATE,NO_ZERO_IN_DATE,STRICT_ALL_TABLES'.

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        request_body_data = None
        request_body_data = {
            "sql_mode": sql_mode,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/sql_mode"
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

    def databases_update_major_version(
        self, database_cluster_uuid: str, version: str | None = None
    ) -> Any:
        """
        Upgrade Major Version for a Database

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            version (string): A string representing the version of the database engine in use for the cluster. Example: '8'.

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        request_body_data = None
        request_body_data = {
            "version": version,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/upgrade"
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

    def databases_list_kafka_topics(self, database_cluster_uuid: str) -> Any:
        """
        List Topics for a Kafka Cluster

        Args:
            database_cluster_uuid (string): database_cluster_uuid

        Returns:
            Any: A JSON object with a key of `topics`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/topics"
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

    def databases_create_kafka_topic(
        self,
        database_cluster_uuid: str,
        name: str | None = None,
        replication_factor: int | None = None,
        partition_count: int | None = None,
        config: dict[str, Any] | None = None,
    ) -> Any:
        """
        Create Topic for a Kafka Cluster

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            name (string): The name of the Kafka topic. Example: 'events'.
            replication_factor (integer): The number of nodes to replicate data across the cluster. Example: '2'.
            partition_count (integer): The number of partitions available for the topic. On update, this value can only be increased. Example: '3'.
            config (object): config Example: {'retention_bytes': -1, 'retention_ms': 100000}.

        Returns:
            Any: A JSON object with a key of `topic`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "replication_factor": replication_factor,
            "partition_count": partition_count,
            "config": config,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/topics"
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

    def databases_get_kafka_topic(
        self, database_cluster_uuid: str, topic_name: str
    ) -> Any:
        """
        Get Topic for a Kafka Cluster

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            topic_name (string): topic_name

        Returns:
            Any: A JSON object with a key of `topic`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        if topic_name is None:
            raise ValueError("Missing required parameter 'topic_name'.")
        url = (
            f"{self.base_url}/v2/databases/{database_cluster_uuid}/topics/{topic_name}"
        )
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

    def databases_update_kafka_topic(
        self,
        database_cluster_uuid: str,
        topic_name: str,
        replication_factor: int | None = None,
        partition_count: int | None = None,
        config: dict[str, Any] | None = None,
    ) -> Any:
        """
        Update Topic for a Kafka Cluster

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            topic_name (string): topic_name
            replication_factor (integer): The number of nodes to replicate data across the cluster. Example: '2'.
            partition_count (integer): The number of partitions available for the topic. On update, this value can only be increased. Example: '3'.
            config (object): config Example: {'retention_bytes': -1, 'retention_ms': 100000}.

        Returns:
            Any: A JSON object with a key of `topic`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        if topic_name is None:
            raise ValueError("Missing required parameter 'topic_name'.")
        request_body_data = None
        request_body_data = {
            "replication_factor": replication_factor,
            "partition_count": partition_count,
            "config": config,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = (
            f"{self.base_url}/v2/databases/{database_cluster_uuid}/topics/{topic_name}"
        )
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

    def databases_delete_kafka_topic(
        self, database_cluster_uuid: str, topic_name: str
    ) -> Any:
        """
        Delete Topic for a Kafka Cluster

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            topic_name (string): topic_name

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        if topic_name is None:
            raise ValueError("Missing required parameter 'topic_name'.")
        url = (
            f"{self.base_url}/v2/databases/{database_cluster_uuid}/topics/{topic_name}"
        )
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

    def databases_list_logsink(self, database_cluster_uuid: str) -> Any:
        """
        List Logsinks for a Database Cluster

        Args:
            database_cluster_uuid (string): database_cluster_uuid

        Returns:
            Any: A JSON object with a key of `sinks`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/logsink"
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

    def databases_create_logsink(
        self, database_cluster_uuid: str, sink_name: str, sink_type: str, config: Any
    ) -> Any:
        """
        Create Logsink for a Database Cluster

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            sink_name (string): The name of the Logsink Example: 'prod-logsink'.
            sink_type (string): Type of logsink integration.

        - Use `datadog` for Datadog integration **only with MongoDB clusters**.
        - For non-MongoDB clusters, use `rsyslog` for general syslog forwarding.
        - Other supported types include `elasticsearch` and `opensearch`.

        More details about the configuration can be found in the `config` property.
         Example: 'rsyslog'.
            config (string): config Example: {'url': 'https://user:passwd@192.168.0.1:25060', 'index_prefix': 'opensearch-logs', 'index_days_max': 5}.

        Returns:
            Any: A JSON object with a key of `sink`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        request_body_data = None
        request_body_data = {
            "sink_name": sink_name,
            "sink_type": sink_type,
            "config": config,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/logsink"
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

    def databases_get_logsink(self, database_cluster_uuid: str, logsink_id: str) -> Any:
        """
        Get Logsink for a Database Cluster

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            logsink_id (string): logsink_id

        Returns:
            Any: A JSON object with a key of `sink`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        if logsink_id is None:
            raise ValueError("Missing required parameter 'logsink_id'.")
        url = (
            f"{self.base_url}/v2/databases/{database_cluster_uuid}/logsink/{logsink_id}"
        )
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

    def databases_update_logsink(
        self, database_cluster_uuid: str, logsink_id: str, config: Any
    ) -> Any:
        """
        Update Logsink for a Database Cluster

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            logsink_id (string): logsink_id
            config (string): config Example: {'server': '192.168.0.1', 'port': 514, 'tls': False, 'format': 'rfc3164'}.

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        if logsink_id is None:
            raise ValueError("Missing required parameter 'logsink_id'.")
        request_body_data = None
        request_body_data = {
            "config": config,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = (
            f"{self.base_url}/v2/databases/{database_cluster_uuid}/logsink/{logsink_id}"
        )
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

    def databases_delete_logsink(
        self, database_cluster_uuid: str, logsink_id: str
    ) -> Any:
        """
        Delete Logsink for a Database Cluster

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            logsink_id (string): logsink_id

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        if logsink_id is None:
            raise ValueError("Missing required parameter 'logsink_id'.")
        url = (
            f"{self.base_url}/v2/databases/{database_cluster_uuid}/logsink/{logsink_id}"
        )
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

    def get_database_metrics_credentials(self) -> Any:
        """
        Retrieve Database Clusters' Metrics Endpoint Credentials

        Returns:
            Any: A JSON object with a key of `credentials`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        url = f"{self.base_url}/v2/databases/metrics/credentials"
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

    def update_database_credentials(
        self, credentials: dict[str, Any] | None = None
    ) -> Any:
        """
        Update Database Clusters' Metrics Endpoint Credentials

        Args:
            credentials (object): credentials Example: {'basic_auth_username': 'new_username', 'basic_auth_password': 'new_password'}.

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        request_body_data = None
        request_body_data = {
            "credentials": credentials,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/databases/metrics/credentials"
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

    def list_database_indexes(self, database_cluster_uuid: str) -> Any:
        """
        List Indexes for a OpenSearch Cluster

        Args:
            database_cluster_uuid (string): database_cluster_uuid

        Returns:
            Any: A JSON object with a key of `indexes`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        url = f"{self.base_url}/v2/databases/{database_cluster_uuid}/indexes"
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

    def delete_database_index_by_name(
        self, database_cluster_uuid: str, index_name: str
    ) -> Any:
        """
        Delete Index for OpenSearch Cluster

        Args:
            database_cluster_uuid (string): database_cluster_uuid
            index_name (string): index_name

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Databases
        """
        if database_cluster_uuid is None:
            raise ValueError("Missing required parameter 'database_cluster_uuid'.")
        if index_name is None:
            raise ValueError("Missing required parameter 'index_name'.")
        url = (
            f"{self.base_url}/v2/databases/{database_cluster_uuid}/indexes/{index_name}"
        )
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

    def domains_list(self, per_page: int | None = None, page: int | None = None) -> Any:
        """
        List All Domains

        Args:
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: The response will be a JSON object with a key called `domains`. The value of this will be an array of Domain objects, each of which contain the standard domain attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Domains, important
        """
        url = f"{self.base_url}/v2/domains"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def domains_create(
        self,
        name: str | None = None,
        ip_address: str | None = None,
        ttl: int | None = None,
        zone_file: str | None = None,
    ) -> Any:
        """
        Create a New Domain

        Args:
            name (string): The name of the domain itself. This should follow the standard domain format of domain.TLD. For instance, `example.com` is a valid domain name. Example: 'example.com'.
            ip_address (string): This optional attribute may contain an IP address. When provided, an A record will be automatically created pointing to the apex domain. Example: '192.0.2.1'.
            ttl (integer): This value is the time to live for the records on this domain, in seconds. This defines the time frame that clients can cache queried information before a refresh should be requested. Example: '1800'.
            zone_file (string): This attribute contains the complete contents of the zone file for the selected domain. Individual domain record resources should be used to get more granular control over records. However, this attribute can also be used to get information about the SOA record, which is created automatically and is not accessible as an individual record resource. Example: '$ORIGIN example.com.\n$TTL 1800\nexample.com. IN SOA ns1.digitalocean.com. hostmaster.example.com. 1415982609 10800 3600 604800 1800\nexample.com. 1800 IN NS ns1.digitalocean.com.\nexample.com. 1800 IN NS ns2.digitalocean.com.\nexample.com. 1800 IN NS ns3.digitalocean.com.\nexample.com. 1800 IN A 1.2.3.4\n'.

        Returns:
            Any: The response will be a JSON object with a key called `domain`. The value of this will be an object that contains the standard attributes associated with a domain.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Domains, important
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "ip_address": ip_address,
            "ttl": ttl,
            "zone_file": zone_file,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/domains"
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

    def domains_get(self, domain_name: str) -> Any:
        """
        Retrieve an Existing Domain

        Args:
            domain_name (string): domain_name

        Returns:
            Any: The response will be a JSON object with a key called `domain`. The value of this will be an object that contains the standard attributes defined for a domain.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Domains
        """
        if domain_name is None:
            raise ValueError("Missing required parameter 'domain_name'.")
        url = f"{self.base_url}/v2/domains/{domain_name}"
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

    def domains_delete(self, domain_name: str) -> Any:
        """
        Delete a Domain

        Args:
            domain_name (string): domain_name

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Domains
        """
        if domain_name is None:
            raise ValueError("Missing required parameter 'domain_name'.")
        url = f"{self.base_url}/v2/domains/{domain_name}"
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

    def domains_list_records(
        self,
        domain_name: str,
        name: str | None = None,
        type: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> Any:
        """
        List All Domain Records

        Args:
            domain_name (string): domain_name
            name (string): A fully qualified record name. For example, to only include records matching sub.example.com, send a GET request to `/v2/domains/$DOMAIN_NAME/records?name=sub.example.com`. Example: 'sub.example.com'.
            type (string): The type of the DNS record. For example: A, CNAME, TXT, ... Example: 'A'.
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: The response will be a JSON object with a key called `domain_records`. The value of this will be an array of domain record objects, each of which contains the standard domain record attributes. For attributes that are not used by a specific record type, a value of `null` will be returned. For instance, all records other than SRV will have `null` for the `weight` and `port` attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Domain Records
        """
        if domain_name is None:
            raise ValueError("Missing required parameter 'domain_name'.")
        url = f"{self.base_url}/v2/domains/{domain_name}/records"
        query_params = {
            k: v
            for k, v in [
                ("name", name),
                ("type", type),
                ("per_page", per_page),
                ("page", page),
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

    def domains_create_record(
        self,
        domain_name: str,
        id: int | None = None,
        type: str | None = None,
        name: str | None = None,
        data: str | None = None,
        priority: int | None = None,
        port: int | None = None,
        ttl: int | None = None,
        weight: int | None = None,
        flags: int | None = None,
        tag: str | None = None,
    ) -> Any:
        """
        Create a New Domain Record

        Args:
            domain_name (string): domain_name
            id (integer): A unique identifier for each domain record. Example: '28448429'.
            type (string): The type of the DNS record. For example: A, CNAME, TXT, ... Example: 'NS'.
            name (string): The host name, alias, or service being defined by the record. Example: '@'.
            data (string): Variable data depending on record type. For example, the "data" value for an A record would be the IPv4 address to which the domain will be mapped. For a CAA record, it would contain the domain name of the CA being granted permission to issue certificates. Example: 'ns1.digitalocean.com'.
            priority (integer): The priority for SRV and MX records.
            port (integer): The port for SRV records.
            ttl (integer): This value is the time to live for the record, in seconds. This defines the time frame that clients can cache queried information before a refresh should be requested. Example: '1800'.
            weight (integer): The weight for SRV records.
            flags (integer): An unsigned integer between 0-255 used for CAA records.
            tag (string): The parameter tag for CAA records. Valid values are "issue", "issuewild", or "iodef"

        Returns:
            Any: The response body will be a JSON object with a key called `domain_record`. The value of this will be an object representing the new record. Attributes that are not applicable for the record type will be set to `null`. An `id` attribute is generated for each record as part of the object.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Domain Records
        """
        if domain_name is None:
            raise ValueError("Missing required parameter 'domain_name'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "type": type,
            "name": name,
            "data": data,
            "priority": priority,
            "port": port,
            "ttl": ttl,
            "weight": weight,
            "flags": flags,
            "tag": tag,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/domains/{domain_name}/records"
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

    def domains_get_record(self, domain_name: str, domain_record_id: str) -> Any:
        """
        Retrieve an Existing Domain Record

        Args:
            domain_name (string): domain_name
            domain_record_id (string): domain_record_id

        Returns:
            Any: The response will be a JSON object with a key called `domain_record`. The value of this will be a domain record object which contains the standard domain record attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Domain Records
        """
        if domain_name is None:
            raise ValueError("Missing required parameter 'domain_name'.")
        if domain_record_id is None:
            raise ValueError("Missing required parameter 'domain_record_id'.")
        url = f"{self.base_url}/v2/domains/{domain_name}/records/{domain_record_id}"
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

    def domains_patch_record(
        self,
        domain_name: str,
        domain_record_id: str,
        id: int | None = None,
        type: str | None = None,
        name: str | None = None,
        data: str | None = None,
        priority: int | None = None,
        port: int | None = None,
        ttl: int | None = None,
        weight: int | None = None,
        flags: int | None = None,
        tag: str | None = None,
    ) -> Any:
        """
        Update a Domain Record

        Args:
            domain_name (string): domain_name
            domain_record_id (string): domain_record_id
            id (integer): A unique identifier for each domain record. Example: '28448429'.
            type (string): The type of the DNS record. For example: A, CNAME, TXT, ... Example: 'NS'.
            name (string): The host name, alias, or service being defined by the record. Example: '@'.
            data (string): Variable data depending on record type. For example, the "data" value for an A record would be the IPv4 address to which the domain will be mapped. For a CAA record, it would contain the domain name of the CA being granted permission to issue certificates. Example: 'ns1.digitalocean.com'.
            priority (integer): The priority for SRV and MX records.
            port (integer): The port for SRV records.
            ttl (integer): This value is the time to live for the record, in seconds. This defines the time frame that clients can cache queried information before a refresh should be requested. Example: '1800'.
            weight (integer): The weight for SRV records.
            flags (integer): An unsigned integer between 0-255 used for CAA records.
            tag (string): The parameter tag for CAA records. Valid values are "issue", "issuewild", or "iodef"

        Returns:
            Any: The response will be a JSON object with a key called `domain_record`. The value of this will be a domain record object which contains the standard domain record attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Domain Records
        """
        if domain_name is None:
            raise ValueError("Missing required parameter 'domain_name'.")
        if domain_record_id is None:
            raise ValueError("Missing required parameter 'domain_record_id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "type": type,
            "name": name,
            "data": data,
            "priority": priority,
            "port": port,
            "ttl": ttl,
            "weight": weight,
            "flags": flags,
            "tag": tag,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/domains/{domain_name}/records/{domain_record_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def domains_update_record(
        self,
        domain_name: str,
        domain_record_id: str,
        id: int | None = None,
        type: str | None = None,
        name: str | None = None,
        data: str | None = None,
        priority: int | None = None,
        port: int | None = None,
        ttl: int | None = None,
        weight: int | None = None,
        flags: int | None = None,
        tag: str | None = None,
    ) -> Any:
        """
        Update a Domain Record

        Args:
            domain_name (string): domain_name
            domain_record_id (string): domain_record_id
            id (integer): A unique identifier for each domain record. Example: '28448429'.
            type (string): The type of the DNS record. For example: A, CNAME, TXT, ... Example: 'NS'.
            name (string): The host name, alias, or service being defined by the record. Example: '@'.
            data (string): Variable data depending on record type. For example, the "data" value for an A record would be the IPv4 address to which the domain will be mapped. For a CAA record, it would contain the domain name of the CA being granted permission to issue certificates. Example: 'ns1.digitalocean.com'.
            priority (integer): The priority for SRV and MX records.
            port (integer): The port for SRV records.
            ttl (integer): This value is the time to live for the record, in seconds. This defines the time frame that clients can cache queried information before a refresh should be requested. Example: '1800'.
            weight (integer): The weight for SRV records.
            flags (integer): An unsigned integer between 0-255 used for CAA records.
            tag (string): The parameter tag for CAA records. Valid values are "issue", "issuewild", or "iodef"

        Returns:
            Any: The response will be a JSON object with a key called `domain_record`. The value of this will be a domain record object which contains the standard domain record attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Domain Records
        """
        if domain_name is None:
            raise ValueError("Missing required parameter 'domain_name'.")
        if domain_record_id is None:
            raise ValueError("Missing required parameter 'domain_record_id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "type": type,
            "name": name,
            "data": data,
            "priority": priority,
            "port": port,
            "ttl": ttl,
            "weight": weight,
            "flags": flags,
            "tag": tag,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/domains/{domain_name}/records/{domain_record_id}"
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

    def domains_delete_record(self, domain_name: str, domain_record_id: str) -> Any:
        """
        Delete a Domain Record

        Args:
            domain_name (string): domain_name
            domain_record_id (string): domain_record_id

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Domain Records
        """
        if domain_name is None:
            raise ValueError("Missing required parameter 'domain_name'.")
        if domain_record_id is None:
            raise ValueError("Missing required parameter 'domain_record_id'.")
        url = f"{self.base_url}/v2/domains/{domain_name}/records/{domain_record_id}"
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

    def droplets_list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        tag_name: str | None = None,
        name: str | None = None,
        type: str | None = None,
    ) -> Any:
        """
        List All Droplets

        Args:
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.
            tag_name (string): Used to filter Droplets by a specific tag. Can not be combined with `name` or `type`. Example: 'env:prod'.
            name (string): Used to filter list response by Droplet name returning only exact matches. It is case-insensitive and can not be combined with `tag_name`. Example: 'web-01'.
            type (string): When `type` is set to `gpus`, only GPU Droplets will be returned. By default, only non-GPU Droplets are returned. Can not be combined with `tag_name`. Example: 'droplets'.

        Returns:
            Any: A JSON object with a key of `droplets`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Droplets, important
        """
        url = f"{self.base_url}/v2/droplets"
        query_params = {
            k: v
            for k, v in [
                ("per_page", per_page),
                ("page", page),
                ("tag_name", tag_name),
                ("name", name),
                ("type", type),
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

    def droplets_create(
        self,
        name: str | None = None,
        region: str | None = None,
        size: str | None = None,
        image: Any | None = None,
        ssh_keys: list[Any] | None = None,
        backups: bool | None = None,
        backup_policy: Any | None = None,
        ipv6: bool | None = None,
        monitoring: bool | None = None,
        tags: list[str] | None = None,
        user_data: str | None = None,
        private_networking: bool | None = None,
        volumes: list[str] | None = None,
        vpc_uuid: str | None = None,
        with_droplet_agent: bool | None = None,
        names: list[str] | None = None,
    ) -> Any:
        """
        Create a New Droplet

        Args:
            name (string): The human-readable string you wish to use when displaying the Droplet name. The name, if set to a domain name managed in the DigitalOcean DNS management system, will configure a PTR record for the Droplet. The name set during creation will also determine the hostname for the Droplet in its internal configuration. Example: 'example.com'.
            region (string): The slug identifier for the region that you wish to deploy the Droplet in. If the specific datacenter is not not important, a slug prefix (e.g. `nyc`) can be used to deploy the Droplet in any of the that region's locations (`nyc1`, `nyc2`, or `nyc3`). If the region is omitted from the create request completely, the Droplet may deploy in any region. Example: 'nyc3'.
            size (string): The slug identifier for the size that you wish to select for this Droplet. Example: 's-1vcpu-1gb'.
            image (string): The image ID of a public or private image or the slug identifier for a public image. This image will be the base image for your Droplet. Example: 'ubuntu-20-04-x64'.
            ssh_keys (array): An array containing the IDs or fingerprints of the SSH keys that you wish to embed in the Droplet's root account upon creation. You must add the keys to your team before they can be embedded on a Droplet. Example: "[289794, '3b:16:e4:bf:8b:00:8b:b8:59:8c:a9:d3:f0:19:fa:45']".
            backups (boolean): A boolean indicating whether automated backups should be enabled for the Droplet. Example: 'True'.
            backup_policy (string): backup_policy
            ipv6 (boolean): A boolean indicating whether to enable IPv6 on the Droplet. Example: 'True'.
            monitoring (boolean): A boolean indicating whether to install the DigitalOcean agent for monitoring. Example: 'True'.
            tags (array): A flat array of tag names as strings to apply to the Droplet after it is created. Tag names can either be existing or new tags. Example: "['env:prod', 'web']".
            user_data (string): A string containing 'user data' which may be used to configure the Droplet on first boot, often a 'cloud-config' file or Bash script. It must be plain text and may not exceed 64 KiB in size. Example: '#cloud-config\nruncmd:\n  - touch /test.txt\n'.
            private_networking (boolean): This parameter has been deprecated. Use `vpc_uuid` instead to specify a VPC network for the Droplet. If no `vpc_uuid` is provided, the Droplet will be placed in your account's default VPC for the region. Example: 'True'.
            volumes (array): An array of IDs for block storage volumes that will be attached to the Droplet once created. The volumes must not already be attached to an existing Droplet. Example: "['12e97116-7280-11ed-b3d0-0a58ac146812']".
            vpc_uuid (string): A string specifying the UUID of the VPC to which the Droplet will be assigned. If excluded, the Droplet will be assigned to your account's default VPC for the region. Example: '760e09ef-dc84-11e8-981e-3cfdfeaae000'.
            with_droplet_agent (boolean): A boolean indicating whether to install the DigitalOcean agent used for providing access to the Droplet web console in the control panel. By default, the agent is installed on new Droplets but installation errors (i.e. OS not supported) are ignored. To prevent it from being installed, set to `false`. To make installation errors fatal, explicitly set it to `true`. Example: 'True'.
            names (array): An array of human human-readable strings you wish to use when displaying the Droplet name. Each name, if set to a domain name managed in the DigitalOcean DNS management system, will configure a PTR record for the Droplet. Each name set during creation will also determine the hostname for the Droplet in its internal configuration. Example: "['sub-01.example.com', 'sub-02.example.com']".

        Returns:
            Any: Accepted

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Droplets, important
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "region": region,
            "size": size,
            "image": image,
            "ssh_keys": ssh_keys,
            "backups": backups,
            "backup_policy": backup_policy,
            "ipv6": ipv6,
            "monitoring": monitoring,
            "tags": tags,
            "user_data": user_data,
            "private_networking": private_networking,
            "volumes": volumes,
            "vpc_uuid": vpc_uuid,
            "with_droplet_agent": with_droplet_agent,
            "names": names,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/droplets"
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

    def droplets_destroy_by_tag(self, tag_name: str) -> Any:
        """
        Deleting Droplets by Tag

        Args:
            tag_name (string): Specifies Droplets to be deleted by tag. Example: 'env:test'.

        Returns:
            Any: The action was successful and the response body is empty. This response has content-type set.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Droplets
        """
        url = f"{self.base_url}/v2/droplets"
        query_params = {k: v for k, v in [("tag_name", tag_name)] if v is not None}
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

    def droplets_get(self, droplet_id: str) -> Any:
        """
        Retrieve an Existing Droplet

        Args:
            droplet_id (string): droplet_id

        Returns:
            Any: The response will be a JSON object with a key called `droplet`. This will be
        set to a JSON object that contains the standard Droplet attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Droplets
        """
        if droplet_id is None:
            raise ValueError("Missing required parameter 'droplet_id'.")
        url = f"{self.base_url}/v2/droplets/{droplet_id}"
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

    def droplets_destroy(self, droplet_id: str) -> Any:
        """
        Delete an Existing Droplet

        Args:
            droplet_id (string): droplet_id

        Returns:
            Any: The action was successful and the response body is empty. This response has content-type set.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Droplets
        """
        if droplet_id is None:
            raise ValueError("Missing required parameter 'droplet_id'.")
        url = f"{self.base_url}/v2/droplets/{droplet_id}"
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

    def droplets_list_backups(
        self,
        droplet_id: str,
        per_page: int | None = None,
        page: int | None = None,
    ) -> Any:
        """
        List Backups for a Droplet

        Args:
            droplet_id (string): droplet_id
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: A JSON object with an `backups` key.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Droplets
        """
        if droplet_id is None:
            raise ValueError("Missing required parameter 'droplet_id'.")
        url = f"{self.base_url}/v2/droplets/{droplet_id}/backups"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def droplets_get_backup_policy(self, droplet_id: str) -> Any:
        """
        Retrieve the Backup Policy for an Existing Droplet

        Args:
            droplet_id (string): droplet_id

        Returns:
            Any: The response will be a JSON object with a key called `policy`. This will be
        set to a JSON object that contains the standard Droplet backup policy attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Droplets
        """
        if droplet_id is None:
            raise ValueError("Missing required parameter 'droplet_id'.")
        url = f"{self.base_url}/v2/droplets/{droplet_id}/backups/policy"
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

    def droplets_list_backup_policies(
        self, per_page: int | None = None, page: int | None = None
    ) -> Any:
        """
        List Backup Policies for All Existing Droplets

        Args:
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: A JSON object with a `policies` key set to a map. The keys are Droplet IDs and the values are objects containing the backup policy information for each Droplet.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Droplets
        """
        url = f"{self.base_url}/v2/droplets/backups/policies"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def list_supported_policies(self) -> dict[str, Any]:
        """
        List Supported Droplet Backup Policies

        Returns:
            dict[str, Any]: A JSON object with an `supported_policies` key set to an array of objects describing each supported backup policy.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Droplets
        """
        url = f"{self.base_url}/v2/droplets/backups/supported_policies"
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

    def droplets_list_snapshots(
        self,
        droplet_id: str,
        per_page: int | None = None,
        page: int | None = None,
    ) -> Any:
        """
        List Snapshots for a Droplet

        Args:
            droplet_id (string): droplet_id
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: A JSON object with an `snapshots` key.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Droplets
        """
        if droplet_id is None:
            raise ValueError("Missing required parameter 'droplet_id'.")
        url = f"{self.base_url}/v2/droplets/{droplet_id}/snapshots"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def droplet_actions_list(
        self,
        droplet_id: str,
        per_page: int | None = None,
        page: int | None = None,
    ) -> Any:
        """
        List Actions for a Droplet

        Args:
            droplet_id (string): droplet_id
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: A JSON object with an `actions` key.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Droplet Actions
        """
        if droplet_id is None:
            raise ValueError("Missing required parameter 'droplet_id'.")
        url = f"{self.base_url}/v2/droplets/{droplet_id}/actions"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def droplet_actions_post(
        self,
        droplet_id: str,
        type: str | None = None,
        backup_policy: Any | None = None,
        image: Any | None = None,
        disk: bool | None = None,
        size: str | None = None,
        name: str | None = None,
        kernel: int | None = None,
    ) -> Any:
        """
        Initiate a Droplet Action

        Args:
            droplet_id (string): droplet_id
            type (string): The type of action to initiate for the Droplet. Example: 'reboot'.
            backup_policy (string): backup_policy
            image (string): The image ID of a public or private image or the slug identifier for a public image. The Droplet will be rebuilt using this image as its base. Example: 'ubuntu-20-04-x64'.
            disk (boolean): When `true`, the Droplet's disk will be resized in addition to its RAM and CPU. This is a permanent change and cannot be reversed as a Droplet's disk size cannot be decreased. Example: 'True'.
            size (string): The slug identifier for the size to which you wish to resize the Droplet. Example: 's-2vcpu-2gb'.
            name (string): The name to give the new snapshot of the Droplet. Example: 'Nifty New Snapshot'.
            kernel (integer): A unique number used to identify and reference a specific kernel. Example: '12389723'.

        Returns:
            Any: The response will be a JSON object with a key called `action`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Droplet Actions
        """
        if droplet_id is None:
            raise ValueError("Missing required parameter 'droplet_id'.")
        request_body_data = None
        request_body_data = {
            "type": type,
            "backup_policy": backup_policy,
            "image": image,
            "disk": disk,
            "size": size,
            "name": name,
            "kernel": kernel,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/droplets/{droplet_id}/actions"
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

    def droplet_actions_post_by_tag(
        self,
        tag_name: str | None = None,
        type: str | None = None,
        name: str | None = None,
    ) -> Any:
        """
        Acting on Tagged Droplets

        Args:
            tag_name (string): Used to filter Droplets by a specific tag. Can not be combined with `name` or `type`. Example: 'env:prod'.
            type (string): The type of action to initiate for the Droplet. Example: 'reboot'.
            name (string): The name to give the new snapshot of the Droplet. Example: 'Nifty New Snapshot'.

        Returns:
            Any: The response will be a JSON object with a key called `actions`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Droplet Actions
        """
        request_body_data = None
        request_body_data = {
            "type": type,
            "name": name,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/droplets/actions"
        query_params = {k: v for k, v in [("tag_name", tag_name)] if v is not None}
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

    def droplet_actions_get(self, droplet_id: str, action_id: str) -> Any:
        """
        Retrieve a Droplet Action

        Args:
            droplet_id (string): droplet_id
            action_id (string): action_id

        Returns:
            Any: The result will be a JSON object with an action key.  This will be set to an action object containing the standard action attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Droplet Actions
        """
        if droplet_id is None:
            raise ValueError("Missing required parameter 'droplet_id'.")
        if action_id is None:
            raise ValueError("Missing required parameter 'action_id'.")
        url = f"{self.base_url}/v2/droplets/{droplet_id}/actions/{action_id}"
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

    def droplets_list_kernels(
        self,
        droplet_id: str,
        per_page: int | None = None,
        page: int | None = None,
    ) -> Any:
        """
        List All Available Kernels for a Droplet

        Args:
            droplet_id (string): droplet_id
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: A JSON object that has a key called `kernels`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Droplets
        """
        if droplet_id is None:
            raise ValueError("Missing required parameter 'droplet_id'.")
        url = f"{self.base_url}/v2/droplets/{droplet_id}/kernels"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def droplets_list_firewalls(
        self,
        droplet_id: str,
        per_page: int | None = None,
        page: int | None = None,
    ) -> Any:
        """
        List all Firewalls Applied to a Droplet

        Args:
            droplet_id (string): droplet_id
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: A JSON object that has a key called `firewalls`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Droplets
        """
        if droplet_id is None:
            raise ValueError("Missing required parameter 'droplet_id'.")
        url = f"{self.base_url}/v2/droplets/{droplet_id}/firewalls"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def droplets_list_neighbors(self, droplet_id: str) -> Any:
        """
        List Neighbors for a Droplet

        Args:
            droplet_id (string): droplet_id

        Returns:
            Any: A JSON object with an `droplets` key.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Droplets
        """
        if droplet_id is None:
            raise ValueError("Missing required parameter 'droplet_id'.")
        url = f"{self.base_url}/v2/droplets/{droplet_id}/neighbors"
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

    def destroy_droplet_with_resources(self, droplet_id: str) -> Any:
        """
        List Associated Resources for a Droplet

        Args:
            droplet_id (string): droplet_id

        Returns:
            Any: A JSON object containing `snapshots`, `volumes`, and `volume_snapshots` keys.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Droplets
        """
        if droplet_id is None:
            raise ValueError("Missing required parameter 'droplet_id'.")
        url = f"{self.base_url}/v2/droplets/{droplet_id}/destroy_with_associated_resources"
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

    def destroy_select(
        self,
        droplet_id: str,
        floating_ips: list[str] | None = None,
        reserved_ips: list[str] | None = None,
        snapshots: list[str] | None = None,
        volumes: list[str] | None = None,
        volume_snapshots: list[str] | None = None,
    ) -> Any:
        """
        Selectively Destroy a Droplet and its Associated Resources

        Args:
            droplet_id (string): droplet_id
            floating_ips (array): An array of unique identifiers for the floating IPs to be scheduled for deletion. Example: "['6186916']".
            reserved_ips (array): An array of unique identifiers for the reserved IPs to be scheduled for deletion. Example: "['6186916']".
            snapshots (array): An array of unique identifiers for the snapshots to be scheduled for deletion. Example: "['61486916']".
            volumes (array): An array of unique identifiers for the volumes to be scheduled for deletion. Example: "['ba49449a-7435-11ea-b89e-0a58ac14480f']".
            volume_snapshots (array): An array of unique identifiers for the volume snapshots to be scheduled for deletion. Example: "['edb0478d-7436-11ea-86e6-0a58ac144b91']".

        Returns:
            Any: This does not indicate the success or failure of any operation, just that the request has been accepted for processing.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Droplets
        """
        if droplet_id is None:
            raise ValueError("Missing required parameter 'droplet_id'.")
        request_body_data = {
            "floating_ips": floating_ips,
            "reserved_ips": reserved_ips,
            "snapshots": snapshots,
            "volumes": volumes,
            "volume_snapshots": volume_snapshots,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/droplets/{droplet_id}/destroy_with_associated_resources/selective"
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

    def delete_droplet_resources(self, droplet_id: str) -> Any:
        """
        Destroy a Droplet and All of its Associated Resources (Dangerous)

        Args:
            droplet_id (string): droplet_id

        Returns:
            Any: This does not indicate the success or failure of any operation, just that the request has been accepted for processing.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Droplets
        """
        if droplet_id is None:
            raise ValueError("Missing required parameter 'droplet_id'.")
        url = f"{self.base_url}/v2/droplets/{droplet_id}/destroy_with_associated_resources/dangerous"
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

    def get_droplet_status(self, droplet_id: str) -> dict[str, Any]:
        """
        Check Status of a Droplet Destroy with Associated Resources Request

        Args:
            droplet_id (string): droplet_id

        Returns:
            dict[str, Any]: A JSON object containing containing the status of a request to destroy a Droplet and its associated resources.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Droplets
        """
        if droplet_id is None:
            raise ValueError("Missing required parameter 'droplet_id'.")
        url = f"{self.base_url}/v2/droplets/{droplet_id}/destroy_with_associated_resources/status"
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

    def retry_droplet_with_resources(self, droplet_id: str) -> Any:
        """
        Retry a Droplet Destroy with Associated Resources Request

        Args:
            droplet_id (string): droplet_id

        Returns:
            Any: This does not indicate the success or failure of any operation, just that the request has been accepted for processing.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Droplets
        """
        if droplet_id is None:
            raise ValueError("Missing required parameter 'droplet_id'.")
        request_body_data = None
        url = f"{self.base_url}/v2/droplets/{droplet_id}/destroy_with_associated_resources/retry"
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

    def autoscalepools_list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        name: str | None = None,
    ) -> Any:
        """
        List All Autoscale Pools

        Args:
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.
            name (string): The name of the autoscale pool Example: 'my-autoscale-pool'.

        Returns:
            Any: A JSON object with a key of `autoscale_pools`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Droplet Autoscale Pools
        """
        url = f"{self.base_url}/v2/droplets/autoscale"
        query_params = {
            k: v
            for k, v in [("per_page", per_page), ("page", page), ("name", name)]
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

    def autoscalepools_create(
        self,
        name: str | None = None,
        config: dict[str, Any] | None = None,
        droplet_template: dict[str, Any] | None = None,
    ) -> Any:
        """
        Create a New Autoscale Pool

        Args:
            name (string): The human-readable name of the autoscale pool. This field cannot be updated Example: 'my-autoscale-pool'.
            config (object): The scaling configuration for an autoscale pool, which is how the pool scales up and down (either by resource utilization or static configuration). Example: {'min_instances': 1, 'max_instances': 5, 'target_cpu_utilization': 0.5, 'cooldown_minutes': 10}.
            droplet_template (object): droplet_template Example: {'name': 'example.com', 'region': 'nyc3', 'size': 'c-2', 'image': 'ubuntu-20-04-x64', 'ssh_keys': ['3b:16:e4:bf:8b:00:8b:b8:59:8c:a9:d3:f0:19:fa:45'], 'backups': True, 'ipv6': True, 'monitoring': True, 'tags': ['env:prod', 'web'], 'user_data': '#cloud-config\nruncmd:\n  - touch /test.txt\n', 'vpc_uuid': '760e09ef-dc84-11e8-981e-3cfdfeaae000'}.

        Returns:
            Any: Accepted

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Droplet Autoscale Pools
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "config": config,
            "droplet_template": droplet_template,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/droplets/autoscale"
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

    def autoscalepools_get(self, autoscale_pool_id: str) -> Any:
        """
        Retrieve an Existing Autoscale Pool

        Args:
            autoscale_pool_id (string): autoscale_pool_id

        Returns:
            Any: The response will be a JSON object with a key called `autoscale_pool`. This will be
        set to a JSON object that contains the standard autoscale pool attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Droplet Autoscale Pools
        """
        if autoscale_pool_id is None:
            raise ValueError("Missing required parameter 'autoscale_pool_id'.")
        url = f"{self.base_url}/v2/droplets/autoscale/{autoscale_pool_id}"
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

    def autoscalepools_update(
        self,
        autoscale_pool_id: str,
        name: str | None = None,
        config: dict[str, Any] | None = None,
        droplet_template: dict[str, Any] | None = None,
    ) -> Any:
        """
        Update Autoscale Pool

        Args:
            autoscale_pool_id (string): autoscale_pool_id
            name (string): The human-readable name of the autoscale pool. This field cannot be updated Example: 'my-autoscale-pool'.
            config (object): The scaling configuration for an autoscale pool, which is how the pool scales up and down (either by resource utilization or static configuration). Example: {'target_number_instances': 2}.
            droplet_template (object): droplet_template Example: {'name': 'example.com', 'region': 'nyc3', 'size': 'c-2', 'image': 'ubuntu-20-04-x64', 'ssh_keys': ['3b:16:e4:bf:8b:00:8b:b8:59:8c:a9:d3:f0:19:fa:45'], 'backups': True, 'ipv6': True, 'monitoring': True, 'tags': ['env:prod', 'web'], 'user_data': '#cloud-config\nruncmd:\n  - touch /test.txt\n', 'vpc_uuid': '760e09ef-dc84-11e8-981e-3cfdfeaae000'}.

        Returns:
            Any: Accepted

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Droplet Autoscale Pools
        """
        if autoscale_pool_id is None:
            raise ValueError("Missing required parameter 'autoscale_pool_id'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "config": config,
            "droplet_template": droplet_template,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/droplets/autoscale/{autoscale_pool_id}"
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

    def autoscalepools_delete(self, autoscale_pool_id: str) -> Any:
        """
        Delete autoscale pool

        Args:
            autoscale_pool_id (string): autoscale_pool_id

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Droplet Autoscale Pools
        """
        if autoscale_pool_id is None:
            raise ValueError("Missing required parameter 'autoscale_pool_id'.")
        url = f"{self.base_url}/v2/droplets/autoscale/{autoscale_pool_id}"
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

    def delete_autoscale_pool_dangerously(self, autoscale_pool_id: str) -> Any:
        """
        Delete autoscale pool and resources

        Args:
            autoscale_pool_id (string): autoscale_pool_id

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Droplet Autoscale Pools
        """
        if autoscale_pool_id is None:
            raise ValueError("Missing required parameter 'autoscale_pool_id'.")
        url = f"{self.base_url}/v2/droplets/autoscale/{autoscale_pool_id}/dangerous"
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

    def autoscalepools_list_members(
        self,
        autoscale_pool_id: str,
        per_page: int | None = None,
        page: int | None = None,
    ) -> Any:
        """
        List members

        Args:
            autoscale_pool_id (string): autoscale_pool_id
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: A JSON object with a key of `droplets`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Droplet Autoscale Pools
        """
        if autoscale_pool_id is None:
            raise ValueError("Missing required parameter 'autoscale_pool_id'.")
        url = f"{self.base_url}/v2/droplets/autoscale/{autoscale_pool_id}/members"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def autoscalepools_list_history(
        self,
        autoscale_pool_id: str,
        per_page: int | None = None,
        page: int | None = None,
    ) -> Any:
        """
        List history events

        Args:
            autoscale_pool_id (string): autoscale_pool_id
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: A JSON object with a key of `history`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Droplet Autoscale Pools
        """
        if autoscale_pool_id is None:
            raise ValueError("Missing required parameter 'autoscale_pool_id'.")
        url = f"{self.base_url}/v2/droplets/autoscale/{autoscale_pool_id}/history"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def firewalls_list(
        self, per_page: int | None = None, page: int | None = None
    ) -> Any:
        """
        List All Firewalls

        Args:
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: To list all of the firewalls available on your account, send a GET request to `/v2/firewalls`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Firewalls
        """
        url = f"{self.base_url}/v2/firewalls"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def firewalls_create(
        self,
        id: str | None = None,
        status: str | None = None,
        created_at: str | None = None,
        pending_changes: list[dict[str, Any]] | None = None,
        name: str | None = None,
        droplet_ids: list[int] | None = None,
        tags: Any | None = None,
        inbound_rules: list[Any] | None = None,
        outbound_rules: list[Any] | None = None,
    ) -> Any:
        """
        Create a New Firewall

        Args:
            id (string): A unique ID that can be used to identify and reference a firewall. Example: 'bb4b2611-3d72-467b-8602-280330ecd65c'.
            status (string): A status string indicating the current state of the firewall. This can be "waiting", "succeeded", or "failed". Example: 'waiting'.
            created_at (string): A time value given in ISO8601 combined date and time format that represents when the firewall was created. Example: '2020-05-23T21:24:00Z'.
            pending_changes (array): An array of objects each containing the fields "droplet_id", "removing", and "status". It is provided to detail exactly which Droplets are having their security policies updated. When empty, all changes have been successfully applied. Example: "[{'droplet_id': 8043964, 'removing': False, 'status': 'waiting'}]".
            name (string): A human-readable name for a firewall. The name must begin with an alphanumeric character. Subsequent characters must either be alphanumeric characters, a period (.), or a dash (-). Example: 'firewall'.
            droplet_ids (array): An array containing the IDs of the Droplets assigned to the firewall. Example: '[8043964]'.
            tags (string): tags
            inbound_rules (array): inbound_rules Example: [{'protocol': 'tcp', 'ports': '80', 'sources': {'load_balancer_uids': ['4de7ac8b-495b-4884-9a69-1050c6793cd6']}}, {'protocol': 'tcp', 'ports': '22', 'sources': {'tags': ['gateway'], 'addresses': ['18.0.0.0/8']}}].
            outbound_rules (array): outbound_rules Example: [{'protocol': 'tcp', 'ports': '80', 'destinations': {'addresses': ['0.0.0.0/0', '::/0']}}].

        Returns:
            Any: The response will be a JSON object with a firewall key. This will be set to an object containing the standard firewall attributes

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Firewalls
        """
        request_body_data = None
        request_body_data = {
            "id": id,
            "status": status,
            "created_at": created_at,
            "pending_changes": pending_changes,
            "name": name,
            "droplet_ids": droplet_ids,
            "tags": tags,
            "inbound_rules": inbound_rules,
            "outbound_rules": outbound_rules,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/firewalls"
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

    def firewalls_get(self, firewall_id: str) -> Any:
        """
        Retrieve an Existing Firewall

        Args:
            firewall_id (string): firewall_id

        Returns:
            Any: The response will be a JSON object with a firewall key. This will be set to an object containing the standard firewall attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Firewalls
        """
        if firewall_id is None:
            raise ValueError("Missing required parameter 'firewall_id'.")
        url = f"{self.base_url}/v2/firewalls/{firewall_id}"
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

    def firewalls_update(
        self,
        firewall_id: str,
        id: str | None = None,
        status: str | None = None,
        created_at: str | None = None,
        pending_changes: list[dict[str, Any]] | None = None,
        name: str | None = None,
        droplet_ids: list[int] | None = None,
        tags: Any | None = None,
        inbound_rules: list[Any] | None = None,
        outbound_rules: list[Any] | None = None,
    ) -> Any:
        """
        Update a Firewall

        Args:
            firewall_id (string): firewall_id
            id (string): A unique ID that can be used to identify and reference a firewall. Example: 'bb4b2611-3d72-467b-8602-280330ecd65c'.
            status (string): A status string indicating the current state of the firewall. This can be "waiting", "succeeded", or "failed". Example: 'waiting'.
            created_at (string): A time value given in ISO8601 combined date and time format that represents when the firewall was created. Example: '2020-05-23T21:24:00Z'.
            pending_changes (array): An array of objects each containing the fields "droplet_id", "removing", and "status". It is provided to detail exactly which Droplets are having their security policies updated. When empty, all changes have been successfully applied. Example: "[{'droplet_id': 8043964, 'removing': False, 'status': 'waiting'}]".
            name (string): A human-readable name for a firewall. The name must begin with an alphanumeric character. Subsequent characters must either be alphanumeric characters, a period (.), or a dash (-). Example: 'firewall'.
            droplet_ids (array): An array containing the IDs of the Droplets assigned to the firewall. Example: '[8043964]'.
            tags (string): tags Example: ['frontend'].
            inbound_rules (array): inbound_rules Example: [{'protocol': 'tcp', 'ports': '8080', 'sources': {'load_balancer_uids': ['4de7ac8b-495b-4884-9a69-1050c6793cd6']}}, {'protocol': 'tcp', 'ports': '22', 'sources': {'tags': ['gateway'], 'addresses': ['18.0.0.0/8']}}].
            outbound_rules (array): outbound_rules Example: [{'protocol': 'tcp', 'ports': '8080', 'destinations': {'addresses': ['0.0.0.0/0', '::/0']}}].

        Returns:
            Any: The response will be a JSON object with a `firewall` key. This will be set to an object containing the standard firewall attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Firewalls
        """
        if firewall_id is None:
            raise ValueError("Missing required parameter 'firewall_id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "status": status,
            "created_at": created_at,
            "pending_changes": pending_changes,
            "name": name,
            "droplet_ids": droplet_ids,
            "tags": tags,
            "inbound_rules": inbound_rules,
            "outbound_rules": outbound_rules,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/firewalls/{firewall_id}"
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

    def firewalls_delete(self, firewall_id: str) -> Any:
        """
        Delete a Firewall

        Args:
            firewall_id (string): firewall_id

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Firewalls
        """
        if firewall_id is None:
            raise ValueError("Missing required parameter 'firewall_id'.")
        url = f"{self.base_url}/v2/firewalls/{firewall_id}"
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

    def firewalls_assign_droplets(
        self, firewall_id: str, droplet_ids: list[int] | None = None
    ) -> Any:
        """
        Add Droplets to a Firewall

        Args:
            firewall_id (string): firewall_id
            droplet_ids (array): An array containing the IDs of the Droplets to be assigned to the firewall. Example: '[49696269]'.

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Firewalls
        """
        if firewall_id is None:
            raise ValueError("Missing required parameter 'firewall_id'.")
        request_body_data = None
        request_body_data = {
            "droplet_ids": droplet_ids,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/firewalls/{firewall_id}/droplets"
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

    def firewalls_delete_droplets(
        self, firewall_id: str, droplet_ids: list[int] | None = None
    ) -> Any:
        """
        Remove Droplets from a Firewall

        Args:
            firewall_id (string): firewall_id
            droplet_ids (array): An array containing the IDs of the Droplets to be removed from the firewall. Example: '[49696269]'.

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Firewalls
        """
        if firewall_id is None:
            raise ValueError("Missing required parameter 'firewall_id'.")
        request_body_data = {
            "droplet_ids": droplet_ids,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/firewalls/{firewall_id}/droplets"
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

    def firewalls_add_tags(self, firewall_id: str, tags: Any | None = None) -> Any:
        """
        Add Tags to a Firewall

        Args:
            firewall_id (string): firewall_id
            tags (string): tags Example: ['frontend'].

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Firewalls
        """
        if firewall_id is None:
            raise ValueError("Missing required parameter 'firewall_id'.")
        request_body_data = None
        request_body_data = {
            "tags": tags,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/firewalls/{firewall_id}/tags"
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

    def firewalls_delete_tags(self, firewall_id: str, tags: Any | None = None) -> Any:
        """
        Remove Tags from a Firewall

        Args:
            firewall_id (string): firewall_id
            tags (string): tags Example: ['frontend'].

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Firewalls
        """
        if firewall_id is None:
            raise ValueError("Missing required parameter 'firewall_id'.")
        request_body_data = {
            "tags": tags,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/firewalls/{firewall_id}/tags"
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

    def firewalls_add_rules(
        self,
        firewall_id: str,
        inbound_rules: list[Any] | None = None,
        outbound_rules: list[Any] | None = None,
    ) -> Any:
        """
        Add Rules to a Firewall

        Args:
            firewall_id (string): firewall_id
            inbound_rules (array): inbound_rules Example: [{'protocol': 'tcp', 'ports': '3306', 'sources': {'droplet_ids': [49696269]}}].
            outbound_rules (array): outbound_rules Example: [{'protocol': 'tcp', 'ports': '3306', 'destinations': {'droplet_ids': [49696269]}}].

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Firewalls
        """
        if firewall_id is None:
            raise ValueError("Missing required parameter 'firewall_id'.")
        request_body_data = None
        request_body_data = {
            "inbound_rules": inbound_rules,
            "outbound_rules": outbound_rules,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/firewalls/{firewall_id}/rules"
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

    def firewalls_delete_rules(
        self,
        firewall_id: str,
        inbound_rules: list[Any] | None = None,
        outbound_rules: list[Any] | None = None,
    ) -> Any:
        """
        Remove Rules from a Firewall

        Args:
            firewall_id (string): firewall_id
            inbound_rules (array): inbound_rules Example: [{'protocol': 'tcp', 'ports': '3306', 'sources': {'droplet_ids': [49696269]}}].
            outbound_rules (array): outbound_rules Example: [{'protocol': 'tcp', 'ports': '3306', 'destinations': {'droplet_ids': [49696269]}}].

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Firewalls
        """
        if firewall_id is None:
            raise ValueError("Missing required parameter 'firewall_id'.")
        request_body_data = {
            "inbound_rules": inbound_rules,
            "outbound_rules": outbound_rules,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/firewalls/{firewall_id}/rules"
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

    def floating_ips_list(
        self, per_page: int | None = None, page: int | None = None
    ) -> Any:
        """
        List All Floating IPs

        Args:
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: The response will be a JSON object with a key called `floating_ips`. This will be set to an array of floating IP objects, each of which will contain the standard floating IP attributes

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Floating IPs
        """
        url = f"{self.base_url}/v2/floating_ips"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def floating_ips_create(
        self,
        droplet_id: int | None = None,
        region: str | None = None,
        project_id: str | None = None,
    ) -> dict[str, Any]:
        """
        Create a New Floating IP

        Args:
            droplet_id (integer): The ID of the Droplet that the floating IP will be assigned to. Example: '2457247'.
            region (string): The slug identifier for the region the floating IP will be reserved to. Example: 'nyc3'.
            project_id (string): The UUID of the project to which the floating IP will be assigned. Example: '746c6152-2fa2-11ed-92d3-27aaa54e4988'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `floating_ip`. The value of this will be an object that contains the standard attributes associated with a floating IP.
        When assigning a floating IP to a Droplet at same time as it created, the response's `links` object will contain links to both the Droplet and the assignment action. The latter can be used to check the status of the action.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Floating IPs
        """
        request_body_data = None
        request_body_data = {
            "droplet_id": droplet_id,
            "region": region,
            "project_id": project_id,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/floating_ips"
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

    def floating_ips_get(self, floating_ip: str) -> dict[str, Any]:
        """
        Retrieve an Existing Floating IP

        Args:
            floating_ip (string): floating_ip

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `floating_ip`. The value of this will be an object that contains the standard attributes associated with a floating IP.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Floating IPs
        """
        if floating_ip is None:
            raise ValueError("Missing required parameter 'floating_ip'.")
        url = f"{self.base_url}/v2/floating_ips/{floating_ip}"
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

    def floating_ips_delete(self, floating_ip: str) -> Any:
        """
        Delete a Floating IP

        Args:
            floating_ip (string): floating_ip

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Floating IPs
        """
        if floating_ip is None:
            raise ValueError("Missing required parameter 'floating_ip'.")
        url = f"{self.base_url}/v2/floating_ips/{floating_ip}"
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

    def floating_ips_action_list(self, floating_ip: str) -> Any:
        """
        List All Actions for a Floating IP

        Args:
            floating_ip (string): floating_ip

        Returns:
            Any: The results will be returned as a JSON object with an `actions` key. This will be set to an array filled with action objects containing the standard floating IP action attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Floating IP Actions
        """
        if floating_ip is None:
            raise ValueError("Missing required parameter 'floating_ip'.")
        url = f"{self.base_url}/v2/floating_ips/{floating_ip}/actions"
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

    def floating_ips_action_post(
        self,
        floating_ip: str,
        type: str | None = None,
        droplet_id: int | None = None,
    ) -> Any:
        """
        Initiate a Floating IP Action

        Args:
            floating_ip (string): floating_ip
            type (string): The type of action to initiate for the floating IP.
            droplet_id (integer): The ID of the Droplet that the floating IP will be assigned to. Example: '758604968'.

        Returns:
            Any: The response will be an object with a key called `action`. The value of this will be an object that contains the standard floating IP action attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Floating IP Actions
        """
        if floating_ip is None:
            raise ValueError("Missing required parameter 'floating_ip'.")
        request_body_data = None
        request_body_data = {
            "type": type,
            "droplet_id": droplet_id,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/floating_ips/{floating_ip}/actions"
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

    def floating_ips_action_get(self, floating_ip: str, action_id: str) -> Any:
        """
        Retrieve an Existing Floating IP Action

        Args:
            floating_ip (string): floating_ip
            action_id (string): action_id

        Returns:
            Any: The response will be an object with a key called `action`. The value of this will be an object that contains the standard floating IP action attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Floating IP Actions
        """
        if floating_ip is None:
            raise ValueError("Missing required parameter 'floating_ip'.")
        if action_id is None:
            raise ValueError("Missing required parameter 'action_id'.")
        url = f"{self.base_url}/v2/floating_ips/{floating_ip}/actions/{action_id}"
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

    def functions_list_namespaces(self) -> Any:
        """
        List Namespaces

        Returns:
            Any: An array of JSON objects with a key called `namespaces`.  Each object represents a namespace and contains
        the properties associated with it.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Functions
        """
        url = f"{self.base_url}/v2/functions/namespaces"
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

    def functions_create_namespace(self, region: str, label: str) -> dict[str, Any]:
        """
        Create Namespace

        Args:
            region (string): The [datacenter region](https://docs.digitalocean.com/products/platform/availability-matrix/#available-datacenters) in which to create the namespace. Example: 'nyc1'.
            label (string): The namespace's unique name. Example: 'my namespace'.

        Returns:
            dict[str, Any]: A JSON response object with a key called `namespace`. The object contains the properties associated
        with the namespace.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Functions
        """
        request_body_data = None
        request_body_data = {
            "region": region,
            "label": label,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/functions/namespaces"
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

    def functions_get_namespace(self, namespace_id: str) -> dict[str, Any]:
        """
        Get Namespace

        Args:
            namespace_id (string): namespace_id

        Returns:
            dict[str, Any]: A JSON response object with a key called `namespace`. The object contains the properties associated
        with the namespace.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Functions
        """
        if namespace_id is None:
            raise ValueError("Missing required parameter 'namespace_id'.")
        url = f"{self.base_url}/v2/functions/namespaces/{namespace_id}"
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

    def functions_delete_namespace(self, namespace_id: str) -> Any:
        """
        Delete Namespace

        Args:
            namespace_id (string): namespace_id

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Functions
        """
        if namespace_id is None:
            raise ValueError("Missing required parameter 'namespace_id'.")
        url = f"{self.base_url}/v2/functions/namespaces/{namespace_id}"
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

    def functions_list_triggers(self, namespace_id: str) -> Any:
        """
        List Triggers

        Args:
            namespace_id (string): namespace_id

        Returns:
            Any: An array of JSON objects with a key called `namespaces`.  Each object represents a namespace and contains
        the properties associated with it.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Functions
        """
        if namespace_id is None:
            raise ValueError("Missing required parameter 'namespace_id'.")
        url = f"{self.base_url}/v2/functions/namespaces/{namespace_id}/triggers"
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

    def functions_create_trigger(
        self,
        namespace_id: str,
        name: str,
        function: str,
        type: str,
        is_enabled: bool,
        scheduled_details: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Create Trigger

        Args:
            namespace_id (string): namespace_id
            name (string): The trigger's unique name within the namespace. Example: 'my trigger'.
            function (string): Name of function(action) that exists in the given namespace. Example: 'hello'.
            type (string): One of different type of triggers. Currently only SCHEDULED is supported. Example: 'SCHEDULED'.
            is_enabled (boolean): Indicates weather the trigger is paused or unpaused. Example: 'True'.
            scheduled_details (object): Trigger details for SCHEDULED type, where body is optional.


        Returns:
            dict[str, Any]: A JSON response object with a key called `trigger`. The object contains the properties associated
        with the trigger.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Functions
        """
        if namespace_id is None:
            raise ValueError("Missing required parameter 'namespace_id'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "function": function,
            "type": type,
            "is_enabled": is_enabled,
            "scheduled_details": scheduled_details,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/functions/namespaces/{namespace_id}/triggers"
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

    def functions_get_trigger(
        self, namespace_id: str, trigger_name: str
    ) -> dict[str, Any]:
        """
        Get Trigger

        Args:
            namespace_id (string): namespace_id
            trigger_name (string): trigger_name

        Returns:
            dict[str, Any]: A JSON response object with a key called `trigger`. The object contains the properties associated
        with the trigger.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Functions
        """
        if namespace_id is None:
            raise ValueError("Missing required parameter 'namespace_id'.")
        if trigger_name is None:
            raise ValueError("Missing required parameter 'trigger_name'.")
        url = f"{self.base_url}/v2/functions/namespaces/{namespace_id}/triggers/{trigger_name}"
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

    def functions_update_trigger(
        self,
        namespace_id: str,
        trigger_name: str,
        is_enabled: bool | None = None,
        scheduled_details: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Update Trigger

        Args:
            namespace_id (string): namespace_id
            trigger_name (string): trigger_name
            is_enabled (boolean): Indicates weather the trigger is paused or unpaused. Example: 'True'.
            scheduled_details (object): Trigger details for SCHEDULED type, where body is optional.


        Returns:
            dict[str, Any]: A JSON response object with a key called `trigger`. The object contains the properties associated
        with the trigger.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Functions
        """
        if namespace_id is None:
            raise ValueError("Missing required parameter 'namespace_id'.")
        if trigger_name is None:
            raise ValueError("Missing required parameter 'trigger_name'.")
        request_body_data = None
        request_body_data = {
            "is_enabled": is_enabled,
            "scheduled_details": scheduled_details,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/functions/namespaces/{namespace_id}/triggers/{trigger_name}"
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

    def functions_delete_trigger(self, namespace_id: str, trigger_name: str) -> Any:
        """
        Delete Trigger

        Args:
            namespace_id (string): namespace_id
            trigger_name (string): trigger_name

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Functions
        """
        if namespace_id is None:
            raise ValueError("Missing required parameter 'namespace_id'.")
        if trigger_name is None:
            raise ValueError("Missing required parameter 'trigger_name'.")
        url = f"{self.base_url}/v2/functions/namespaces/{namespace_id}/triggers/{trigger_name}"
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

    def images_list(
        self,
        type: str | None = None,
        private: bool | None = None,
        tag_name: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> Any:
        """
        List All Images

        Args:
            type (string): Filters results based on image type which can be either `application` or `distribution`. Example: 'distribution'.
            private (boolean): Used to filter only user images. Example: 'True'.
            tag_name (string): Used to filter images by a specific tag. Example: 'base-image'.
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: The response will be a JSON object with a key called `images`.  This will be set to an array of image objects, each of which will contain the standard image attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Images, important
        """
        url = f"{self.base_url}/v2/images"
        query_params = {
            k: v
            for k, v in [
                ("type", type),
                ("private", private),
                ("tag_name", tag_name),
                ("per_page", per_page),
                ("page", page),
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

    def images_create_custom(
        self,
        name: str,
        url: str,
        region: str,
        distribution: str | None = None,
        description: str | None = None,
        tags: list[str] | None = None,
    ) -> Any:
        """
        Create a Custom Image

        Args:
            name (string): The display name that has been given to an image.  This is what is shown in the control panel and is generally a descriptive title for the image in question. Example: 'Nifty New Snapshot'.
            url (string): A URL from which the custom Linux virtual machine image may be retrieved.  The image it points to must be in the raw, qcow2, vhdx, vdi, or vmdk format.  It may be compressed using gzip or bzip2 and must be smaller than 100 GB after being decompressed. Example: 'http://cloud-images.ubuntu.com/minimal/releases/bionic/release/ubuntu-18.04-minimal-cloudimg-amd64.img'.
            region (string): The slug identifier for the region where the resource will initially be  available. Example: 'nyc3'.
            distribution (string): The name of a custom image's distribution. Currently, the valid values are  `Arch Linux`, `CentOS`, `CoreOS`, `Debian`, `Fedora`, `Fedora Atomic`,  `FreeBSD`, `Gentoo`, `openSUSE`, `RancherOS`, `Rocky Linux`, `Ubuntu`, and `Unknown`.  Any other value will be accepted but ignored, and `Unknown` will be used in its place. Example: 'Ubuntu'.
            description (string): An optional free-form text field to describe an image. Example: ' '.
            tags (array): A flat array of tag names as strings to be applied to the resource. Tag names may be for either existing or new tags. Example: "['base-image', 'prod']".

        Returns:
            Any: The response will be a JSON object with a key set to `image`.  The value of this will be an image object containing a subset of the standard  image attributes as listed below, including the image's `id` and `status`.  After initial creation, the `status` will be `NEW`. Using the image's id, you  may query the image's status by sending a `GET` request to the  `/v2/images/$IMAGE_ID` endpoint.  When the `status` changes to `available`, the image will be ready for use.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Images
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "distribution": distribution,
            "description": description,
            "url": url,
            "region": region,
            "tags": tags,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/images"
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

    def images_get(self, image_id: str) -> dict[str, Any]:
        """
        Retrieve an Existing Image

        Args:
            image_id (string): image_id

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `image`.  The value of this will be an image object containing the standard image attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Images
        """
        if image_id is None:
            raise ValueError("Missing required parameter 'image_id'.")
        url = f"{self.base_url}/v2/images/{image_id}"
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

    def images_update(
        self,
        image_id: str,
        name: str | None = None,
        distribution: str | None = None,
        description: str | None = None,
    ) -> dict[str, Any]:
        """
        Update an Image

        Args:
            image_id (string): image_id
            name (string): The display name that has been given to an image.  This is what is shown in the control panel and is generally a descriptive title for the image in question. Example: 'Nifty New Snapshot'.
            distribution (string): The name of a custom image's distribution. Currently, the valid values are  `Arch Linux`, `CentOS`, `CoreOS`, `Debian`, `Fedora`, `Fedora Atomic`,  `FreeBSD`, `Gentoo`, `openSUSE`, `RancherOS`, `Rocky Linux`, `Ubuntu`, and `Unknown`.  Any other value will be accepted but ignored, and `Unknown` will be used in its place. Example: 'Ubuntu'.
            description (string): An optional free-form text field to describe an image. Example: ' '.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key set to `image`.  The value of this will be an image object containing the standard image attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Images
        """
        if image_id is None:
            raise ValueError("Missing required parameter 'image_id'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "distribution": distribution,
            "description": description,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/images/{image_id}"
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

    def images_delete(self, image_id: str) -> Any:
        """
        Delete an Image

        Args:
            image_id (string): image_id

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Images
        """
        if image_id is None:
            raise ValueError("Missing required parameter 'image_id'.")
        url = f"{self.base_url}/v2/images/{image_id}"
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

    def image_actions_list(self, image_id: str) -> Any:
        """
        List All Actions for an Image

        Args:
            image_id (string): image_id

        Returns:
            Any: The results will be returned as a JSON object with an `actions` key. This will be set to an array filled with action objects containing the standard action attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Image Actions
        """
        if image_id is None:
            raise ValueError("Missing required parameter 'image_id'.")
        url = f"{self.base_url}/v2/images/{image_id}/actions"
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

    def image_actions_post(
        self, image_id: str, type: str | None = None, region: str | None = None
    ) -> dict[str, Any]:
        """
        Initiate an Image Action

        Args:
            image_id (string): image_id
            type (string): The action to be taken on the image. Can be either `convert` or `transfer`. Example: 'convert'.
            region (string): The slug identifier for the region where the resource will initially be  available. Example: 'nyc3'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `action`. The value of this will be an object containing the standard image action attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Image Actions
        """
        if image_id is None:
            raise ValueError("Missing required parameter 'image_id'.")
        request_body_data = None
        request_body_data = {
            "type": type,
            "region": region,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/images/{image_id}/actions"
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

    def image_actions_get(self, image_id: str, action_id: str) -> dict[str, Any]:
        """
        Retrieve an Existing Action

        Args:
            image_id (string): image_id
            action_id (string): action_id

        Returns:
            dict[str, Any]: The response will be an object with a key called `action`. The value of this will be an object that contains the standard image action attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Image Actions
        """
        if image_id is None:
            raise ValueError("Missing required parameter 'image_id'.")
        if action_id is None:
            raise ValueError("Missing required parameter 'action_id'.")
        url = f"{self.base_url}/v2/images/{image_id}/actions/{action_id}"
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

    def kubernetes_list_clusters(
        self, per_page: int | None = None, page: int | None = None
    ) -> Any:
        """
        List All Kubernetes Clusters

        Args:
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: The response will be a JSON object with a key called `kubernetes_clusters`.
        This will be set to an array of objects, each of which will contain the
        standard Kubernetes cluster attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Kubernetes
        """
        url = f"{self.base_url}/v2/kubernetes/clusters"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def kubernetes_create_cluster(
        self,
        name: str,
        region: str,
        version: str,
        node_pools: list[dict[str, Any]],
        id: str | None = None,
        cluster_subnet: str | None = None,
        service_subnet: str | None = None,
        vpc_uuid: str | None = None,
        ipv4: str | None = None,
        endpoint: str | None = None,
        tags: list[str] | None = None,
        maintenance_policy: dict[str, Any] | None = None,
        auto_upgrade: bool | None = None,
        status: dict[str, Any] | None = None,
        created_at: str | None = None,
        updated_at: str | None = None,
        surge_upgrade: bool | None = None,
        ha: bool | None = None,
        registry_enabled: bool | None = None,
        control_plane_firewall: dict[str, Any] | None = None,
        cluster_autoscaler_configuration: dict[str, Any] | None = None,
        routing_agent: dict[str, Any] | None = None,
    ) -> Any:
        """
        Create a New Kubernetes Cluster

        Args:
            name (string): A human-readable name for a Kubernetes cluster. Example: 'prod-cluster-01'.
            region (string): The slug identifier for the region where the Kubernetes cluster is located. Example: 'nyc1'.
            version (string): The slug identifier for the version of Kubernetes used for the cluster. If set to a minor version (e.g. "1.14"), the latest version within it will be used (e.g. "1.14.6-do.1"); if set to "latest", the latest published version will be used. See the `/v2/kubernetes/options` endpoint to find all currently available versions. Example: '1.18.6-do.0'.
            node_pools (array): An object specifying the details of the worker nodes available to the Kubernetes cluster. Example: [{'size': 's-1vcpu-2gb', 'count': 3, 'name': 'worker-pool'}].
            id (string): A unique ID that can be used to identify and reference a Kubernetes cluster. Example: 'bd5f5959-5e1e-4205-a714-a914373942af'.
            cluster_subnet (string): The range of IP addresses for the overlay network of the Kubernetes cluster in CIDR notation. Example: '192.168.0.0/20'.
            service_subnet (string): The range of assignable IP addresses for services running in the Kubernetes cluster in CIDR notation. Example: '192.168.16.0/24'.
            vpc_uuid (string): A string specifying the UUID of the VPC to which the Kubernetes cluster is assigned. Example: 'c33931f2-a26a-4e61-b85c-4e95a2ec431b'.
            ipv4 (string): The public IPv4 address of the Kubernetes master node. This will not be set if high availability is configured on the cluster (v1.21+) Example: '68.183.121.157'.
            endpoint (string): The base URL of the API server on the Kubernetes master node. Example: 'https://bd5f5959-5e1e-4205-a714-a914373942af.k8s.ondigitalocean.com'.
            tags (array): An array of tags applied to the Kubernetes cluster. All clusters are automatically tagged `k8s` and `k8s:$K8S_CLUSTER_ID`. Example: "['k8s', 'k8s:bd5f5959-5e1e-4205-a714-a914373942af', 'production', 'web-team']".
            maintenance_policy (object): An object specifying the maintenance window policy for the Kubernetes cluster.
            auto_upgrade (boolean): A boolean value indicating whether the cluster will be automatically upgraded to new patch releases during its maintenance window. Example: 'True'.
            status (object): An object containing a `state` attribute whose value is set to a string indicating the current status of the cluster.
            created_at (string): A time value given in ISO8601 combined date and time format that represents when the Kubernetes cluster was created. Example: '2018-11-15T16:00:11Z'.
            updated_at (string): A time value given in ISO8601 combined date and time format that represents when the Kubernetes cluster was last updated. Example: '2018-11-15T16:00:11Z'.
            surge_upgrade (boolean): A boolean value indicating whether surge upgrade is enabled/disabled for the cluster. Surge upgrade makes cluster upgrades fast and reliable by bringing up new nodes before destroying the outdated nodes. Example: 'True'.
            ha (boolean): A boolean value indicating whether the control plane is run in a highly available configuration in the cluster. Highly available control planes incur less downtime. The property cannot be disabled. Example: 'True'.
            registry_enabled (boolean): A read-only boolean value indicating if a container registry is integrated with the cluster. Example: 'True'.
            control_plane_firewall (object): An object specifying the control plane firewall for the Kubernetes cluster. Control plane firewall is in early availability (invite only).
            cluster_autoscaler_configuration (object): An object specifying custom cluster autoscaler configuration.
            routing_agent (object): An object specifying whether the routing-agent component should be enabled for the Kubernetes cluster.

        Returns:
            Any: The response will be a JSON object with a key called `kubernetes_cluster`. The
        value of this will be an object containing the standard attributes of a
        Kubernetes cluster.

        The IP address and cluster API server endpoint will not be available until the
        cluster has finished provisioning. The initial value of the cluster's
        `status.state` attribute will be `provisioning`. When the cluster is ready,
        this will transition to `running`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Kubernetes
        """
        request_body_data = None
        request_body_data = {
            "id": id,
            "name": name,
            "region": region,
            "version": version,
            "cluster_subnet": cluster_subnet,
            "service_subnet": service_subnet,
            "vpc_uuid": vpc_uuid,
            "ipv4": ipv4,
            "endpoint": endpoint,
            "tags": tags,
            "node_pools": node_pools,
            "maintenance_policy": maintenance_policy,
            "auto_upgrade": auto_upgrade,
            "status": status,
            "created_at": created_at,
            "updated_at": updated_at,
            "surge_upgrade": surge_upgrade,
            "ha": ha,
            "registry_enabled": registry_enabled,
            "control_plane_firewall": control_plane_firewall,
            "cluster_autoscaler_configuration": cluster_autoscaler_configuration,
            "routing_agent": routing_agent,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/kubernetes/clusters"
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

    def kubernetes_get_cluster(self, cluster_id: str) -> Any:
        """
        Retrieve an Existing Kubernetes Cluster

        Args:
            cluster_id (string): cluster_id

        Returns:
            Any: The response will be a JSON object with a key called `kubernetes_cluster`. The
        value of this will be an object containing the standard attributes of a
        Kubernetes cluster.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Kubernetes
        """
        if cluster_id is None:
            raise ValueError("Missing required parameter 'cluster_id'.")
        url = f"{self.base_url}/v2/kubernetes/clusters/{cluster_id}"
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

    def kubernetes_update_cluster(
        self,
        cluster_id: str,
        name: str,
        tags: list[str] | None = None,
        maintenance_policy: dict[str, Any] | None = None,
        auto_upgrade: bool | None = None,
        surge_upgrade: bool | None = None,
        ha: bool | None = None,
        control_plane_firewall: dict[str, Any] | None = None,
        cluster_autoscaler_configuration: dict[str, Any] | None = None,
        routing_agent: dict[str, Any] | None = None,
    ) -> Any:
        """
        Update a Kubernetes Cluster

        Args:
            cluster_id (string): cluster_id
            name (string): A human-readable name for a Kubernetes cluster. Example: 'prod-cluster-01'.
            tags (array): An array of tags applied to the Kubernetes cluster. All clusters are automatically tagged `k8s` and `k8s:$K8S_CLUSTER_ID`. Example: "['k8s', 'k8s:bd5f5959-5e1e-4205-a714-a914373942af', 'production', 'web-team']".
            maintenance_policy (object): An object specifying the maintenance window policy for the Kubernetes cluster.
            auto_upgrade (boolean): A boolean value indicating whether the cluster will be automatically upgraded to new patch releases during its maintenance window. Example: 'True'.
            surge_upgrade (boolean): A boolean value indicating whether surge upgrade is enabled/disabled for the cluster. Surge upgrade makes cluster upgrades fast and reliable by bringing up new nodes before destroying the outdated nodes. Example: 'True'.
            ha (boolean): A boolean value indicating whether the control plane is run in a highly available configuration in the cluster. Highly available control planes incur less downtime. The property cannot be disabled. Example: 'True'.
            control_plane_firewall (object): An object specifying the control plane firewall for the Kubernetes cluster. Control plane firewall is in early availability (invite only).
            cluster_autoscaler_configuration (object): An object specifying custom cluster autoscaler configuration.
            routing_agent (object): An object specifying whether the routing-agent component should be enabled for the Kubernetes cluster.

        Returns:
            Any: The response will be a JSON object with a key called `kubernetes_cluster`. The
        value of this will be an object containing the standard attributes of a
        Kubernetes cluster.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Kubernetes
        """
        if cluster_id is None:
            raise ValueError("Missing required parameter 'cluster_id'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "tags": tags,
            "maintenance_policy": maintenance_policy,
            "auto_upgrade": auto_upgrade,
            "surge_upgrade": surge_upgrade,
            "ha": ha,
            "control_plane_firewall": control_plane_firewall,
            "cluster_autoscaler_configuration": cluster_autoscaler_configuration,
            "routing_agent": routing_agent,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/kubernetes/clusters/{cluster_id}"
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

    def kubernetes_delete_cluster(self, cluster_id: str) -> Any:
        """
        Delete a Kubernetes Cluster

        Args:
            cluster_id (string): cluster_id

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Kubernetes
        """
        if cluster_id is None:
            raise ValueError("Missing required parameter 'cluster_id'.")
        url = f"{self.base_url}/v2/kubernetes/clusters/{cluster_id}"
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

    def destroy_cluster_resources(self, cluster_id: str) -> dict[str, Any]:
        """
        List Associated Resources for Cluster Deletion

        Args:
            cluster_id (string): cluster_id

        Returns:
            dict[str, Any]: The response will be a JSON object containing `load_balancers`, `volumes`, and `volume_snapshots` keys. Each will be set to an array of objects containing the standard attributes for associated resources.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Kubernetes
        """
        if cluster_id is None:
            raise ValueError("Missing required parameter 'cluster_id'.")
        url = f"{self.base_url}/v2/kubernetes/clusters/{cluster_id}/destroy_with_associated_resources"
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

    def delete_cluster_resources(
        self,
        cluster_id: str,
        load_balancers: list[str] | None = None,
        volumes: list[str] | None = None,
        volume_snapshots: list[str] | None = None,
    ) -> Any:
        """
        Selectively Delete a Cluster and its Associated Resources

        Args:
            cluster_id (string): cluster_id
            load_balancers (array): A list of IDs for associated load balancers to destroy along with the cluster. Example: "['4de7ac8b-495b-4884-9a69-1050c6793cd6']".
            volumes (array): A list of IDs for associated volumes to destroy along with the cluster. Example: "['ba49449a-7435-11ea-b89e-0a58ac14480f']".
            volume_snapshots (array): A list of IDs for associated volume snapshots to destroy along with the cluster. Example: "['edb0478d-7436-11ea-86e6-0a58ac144b91']".

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Kubernetes
        """
        if cluster_id is None:
            raise ValueError("Missing required parameter 'cluster_id'.")
        request_body_data = {
            "load_balancers": load_balancers,
            "volumes": volumes,
            "volume_snapshots": volume_snapshots,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/kubernetes/clusters/{cluster_id}/destroy_with_associated_resources/selective"
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

    def destroy_cluster_with_resources(self, cluster_id: str) -> Any:
        """
        Delete a Cluster and All of its Associated Resources (Dangerous)

        Args:
            cluster_id (string): cluster_id

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Kubernetes
        """
        if cluster_id is None:
            raise ValueError("Missing required parameter 'cluster_id'.")
        url = f"{self.base_url}/v2/kubernetes/clusters/{cluster_id}/destroy_with_associated_resources/dangerous"
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

    def kubernetes_get_kubeconfig(
        self, cluster_id: str, expiry_seconds: int | None = None
    ) -> Any:
        """
        Retrieve the kubeconfig for a Kubernetes Cluster

        Args:
            cluster_id (string): cluster_id
            expiry_seconds (integer): The duration in seconds that the returned Kubernetes credentials will be valid. If not set or 0, the credentials will have a 7 day expiry. Example: '300'.

        Returns:
            Any: A kubeconfig file for the cluster in YAML format.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Kubernetes
        """
        if cluster_id is None:
            raise ValueError("Missing required parameter 'cluster_id'.")
        url = f"{self.base_url}/v2/kubernetes/clusters/{cluster_id}/kubeconfig"
        query_params = {
            k: v for k, v in [("expiry_seconds", expiry_seconds)] if v is not None
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

    def kubernetes_get_credentials(
        self, cluster_id: str, expiry_seconds: int | None = None
    ) -> dict[str, Any]:
        """
        Retrieve Credentials for a Kubernetes Cluster

        Args:
            cluster_id (string): cluster_id
            expiry_seconds (integer): The duration in seconds that the returned Kubernetes credentials will be valid. If not set or 0, the credentials will have a 7 day expiry. Example: '300'.

        Returns:
            dict[str, Any]: A JSON object containing credentials for a cluster.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Kubernetes
        """
        if cluster_id is None:
            raise ValueError("Missing required parameter 'cluster_id'.")
        url = f"{self.base_url}/v2/kubernetes/clusters/{cluster_id}/credentials"
        query_params = {
            k: v for k, v in [("expiry_seconds", expiry_seconds)] if v is not None
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

    def get_cluster_upgrades(self, cluster_id: str) -> dict[str, Any]:
        """
        Retrieve Available Upgrades for an Existing Kubernetes Cluster

        Args:
            cluster_id (string): cluster_id

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called
        `available_upgrade_versions`. The value of this will be an array of objects,
        representing the upgrade versions currently available for this cluster.

        If the cluster is up-to-date (i.e. there are no upgrades currently available)
        `available_upgrade_versions` will be `null`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Kubernetes
        """
        if cluster_id is None:
            raise ValueError("Missing required parameter 'cluster_id'.")
        url = f"{self.base_url}/v2/kubernetes/clusters/{cluster_id}/upgrades"
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

    def kubernetes_upgrade_cluster(
        self, cluster_id: str, version: str | None = None
    ) -> Any:
        """
        Upgrade a Kubernetes Cluster

        Args:
            cluster_id (string): cluster_id
            version (string): The slug identifier for the version of Kubernetes that the cluster will be upgraded to. Example: '1.16.13-do.0'.

        Returns:
            Any: This does not indicate the success or failure of any operation, just that the request has been accepted for processing.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Kubernetes
        """
        if cluster_id is None:
            raise ValueError("Missing required parameter 'cluster_id'.")
        request_body_data = None
        request_body_data = {
            "version": version,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/kubernetes/clusters/{cluster_id}/upgrade"
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

    def kubernetes_list_node_pools(self, cluster_id: str) -> Any:
        """
        List All Node Pools in a Kubernetes Clusters

        Args:
            cluster_id (string): cluster_id

        Returns:
            Any: The response will be a JSON object with a key called `node_pools`. This will
        be set to an array of objects, each of which will contain the standard node
        pool attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Kubernetes
        """
        if cluster_id is None:
            raise ValueError("Missing required parameter 'cluster_id'.")
        url = f"{self.base_url}/v2/kubernetes/clusters/{cluster_id}/node_pools"
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

    def kubernetes_add_node_pool(
        self,
        cluster_id: str,
        size: str,
        name: str,
        count: int,
        id: str | None = None,
        tags: list[str] | None = None,
        labels: dict[str, Any] | None = None,
        taints: list[dict[str, Any]] | None = None,
        auto_scale: bool | None = None,
        min_nodes: int | None = None,
        max_nodes: int | None = None,
        nodes: list[dict[str, Any]] | None = None,
    ) -> Any:
        """
        Add a Node Pool to a Kubernetes Cluster

        Args:
            cluster_id (string): cluster_id
            size (string): The slug identifier for the type of Droplet used as workers in the node pool. Example: 's-1vcpu-2gb'.
            name (string): A human-readable name for the node pool. Example: 'frontend-pool'.
            count (integer): The number of Droplet instances in the node pool. Example: '3'.
            id (string): A unique ID that can be used to identify and reference a specific node pool. Example: 'cdda885e-7663-40c8-bc74-3a036c66545d'.
            tags (array): An array containing the tags applied to the node pool. All node pools are automatically tagged `k8s`, `k8s-worker`, and `k8s:$K8S_CLUSTER_ID`. Example: "['k8s', 'k8s:bd5f5959-5e1e-4205-a714-a914373942af', 'k8s-worker', 'production', 'web-team']".
            labels (object): An object of key/value mappings specifying labels to apply to all nodes in a pool. Labels will automatically be applied to all existing nodes and any subsequent nodes added to the pool. Note that when a label is removed, it is not deleted from the nodes in the pool.
            taints (array): An array of taints to apply to all nodes in a pool. Taints will automatically be applied to all existing nodes and any subsequent nodes added to the pool. When a taint is removed, it is deleted from all nodes in the pool.
            auto_scale (boolean): A boolean value indicating whether auto-scaling is enabled for this node pool. Example: 'True'.
            min_nodes (integer): The minimum number of nodes that this node pool can be auto-scaled to. The value will be `0` if `auto_scale` is set to `false`. Example: '3'.
            max_nodes (integer): The maximum number of nodes that this node pool can be auto-scaled to. The value will be `0` if `auto_scale` is set to `false`. Example: '6'.
            nodes (array): An object specifying the details of a specific worker node in a node pool.

        Returns:
            Any: The response will be a JSON object with a key called `node_pool`. The value of
        this will be an object containing the standard attributes of a node pool.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Kubernetes
        """
        if cluster_id is None:
            raise ValueError("Missing required parameter 'cluster_id'.")
        request_body_data = None
        request_body_data = {
            "size": size,
            "id": id,
            "name": name,
            "count": count,
            "tags": tags,
            "labels": labels,
            "taints": taints,
            "auto_scale": auto_scale,
            "min_nodes": min_nodes,
            "max_nodes": max_nodes,
            "nodes": nodes,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/kubernetes/clusters/{cluster_id}/node_pools"
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

    def kubernetes_get_node_pool(self, cluster_id: str, node_pool_id: str) -> Any:
        """
        Retrieve a Node Pool for a Kubernetes Cluster

        Args:
            cluster_id (string): cluster_id
            node_pool_id (string): node_pool_id

        Returns:
            Any: The response will be a JSON object with a key called `node_pool`. The value
        of this will be an object containing the standard attributes of a node pool.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Kubernetes
        """
        if cluster_id is None:
            raise ValueError("Missing required parameter 'cluster_id'.")
        if node_pool_id is None:
            raise ValueError("Missing required parameter 'node_pool_id'.")
        url = f"{self.base_url}/v2/kubernetes/clusters/{cluster_id}/node_pools/{node_pool_id}"
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

    def kubernetes_update_node_pool(
        self,
        cluster_id: str,
        node_pool_id: str,
        name: str,
        count: int,
        id: str | None = None,
        tags: list[str] | None = None,
        labels: dict[str, Any] | None = None,
        taints: list[dict[str, Any]] | None = None,
        auto_scale: bool | None = None,
        min_nodes: int | None = None,
        max_nodes: int | None = None,
        nodes: list[dict[str, Any]] | None = None,
    ) -> Any:
        """
        Update a Node Pool in a Kubernetes Cluster

        Args:
            cluster_id (string): cluster_id
            node_pool_id (string): node_pool_id
            name (string): A human-readable name for the node pool. Example: 'frontend-pool'.
            count (integer): The number of Droplet instances in the node pool. Example: '3'.
            id (string): A unique ID that can be used to identify and reference a specific node pool. Example: 'cdda885e-7663-40c8-bc74-3a036c66545d'.
            tags (array): An array containing the tags applied to the node pool. All node pools are automatically tagged `k8s`, `k8s-worker`, and `k8s:$K8S_CLUSTER_ID`. Example: "['k8s', 'k8s:bd5f5959-5e1e-4205-a714-a914373942af', 'k8s-worker', 'production', 'web-team']".
            labels (object): An object of key/value mappings specifying labels to apply to all nodes in a pool. Labels will automatically be applied to all existing nodes and any subsequent nodes added to the pool. Note that when a label is removed, it is not deleted from the nodes in the pool.
            taints (array): An array of taints to apply to all nodes in a pool. Taints will automatically be applied to all existing nodes and any subsequent nodes added to the pool. When a taint is removed, it is deleted from all nodes in the pool.
            auto_scale (boolean): A boolean value indicating whether auto-scaling is enabled for this node pool. Example: 'True'.
            min_nodes (integer): The minimum number of nodes that this node pool can be auto-scaled to. The value will be `0` if `auto_scale` is set to `false`. Example: '3'.
            max_nodes (integer): The maximum number of nodes that this node pool can be auto-scaled to. The value will be `0` if `auto_scale` is set to `false`. Example: '6'.
            nodes (array): An object specifying the details of a specific worker node in a node pool.

        Returns:
            Any: The response will be a JSON object with a key called `node_pool`. The value of
        this will be an object containing the standard attributes of a node pool.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Kubernetes
        """
        if cluster_id is None:
            raise ValueError("Missing required parameter 'cluster_id'.")
        if node_pool_id is None:
            raise ValueError("Missing required parameter 'node_pool_id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "name": name,
            "count": count,
            "tags": tags,
            "labels": labels,
            "taints": taints,
            "auto_scale": auto_scale,
            "min_nodes": min_nodes,
            "max_nodes": max_nodes,
            "nodes": nodes,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/kubernetes/clusters/{cluster_id}/node_pools/{node_pool_id}"
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

    def kubernetes_delete_node_pool(self, cluster_id: str, node_pool_id: str) -> Any:
        """
        Delete a Node Pool in a Kubernetes Cluster

        Args:
            cluster_id (string): cluster_id
            node_pool_id (string): node_pool_id

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Kubernetes
        """
        if cluster_id is None:
            raise ValueError("Missing required parameter 'cluster_id'.")
        if node_pool_id is None:
            raise ValueError("Missing required parameter 'node_pool_id'.")
        url = f"{self.base_url}/v2/kubernetes/clusters/{cluster_id}/node_pools/{node_pool_id}"
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

    def kubernetes_delete_node(
        self,
        cluster_id: str,
        node_pool_id: str,
        node_id: str,
        skip_drain: int | None = None,
        replace: int | None = None,
    ) -> Any:
        """
        Delete a Node in a Kubernetes Cluster

        Args:
            cluster_id (string): cluster_id
            node_pool_id (string): node_pool_id
            node_id (string): node_id
            skip_drain (integer): Specifies whether or not to drain workloads from a node before it is deleted. Setting it to `1` causes node draining to be skipped. Omitting the query parameter or setting its value to `0` carries out draining prior to deletion. Example: '1'.
            replace (integer): Specifies whether or not to replace a node after it has been deleted. Setting it to `1` causes the node to be replaced by a new one after deletion. Omitting the query parameter or setting its value to `0` deletes without replacement. Example: '1'.

        Returns:
            Any: This does not indicate the success or failure of any operation, just that the request has been accepted for processing.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Kubernetes
        """
        if cluster_id is None:
            raise ValueError("Missing required parameter 'cluster_id'.")
        if node_pool_id is None:
            raise ValueError("Missing required parameter 'node_pool_id'.")
        if node_id is None:
            raise ValueError("Missing required parameter 'node_id'.")
        url = f"{self.base_url}/v2/kubernetes/clusters/{cluster_id}/node_pools/{node_pool_id}/nodes/{node_id}"
        query_params = {
            k: v
            for k, v in [("skip_drain", skip_drain), ("replace", replace)]
            if v is not None
        }
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

    def kubernetes_recycle_node_pool(
        self, cluster_id: str, node_pool_id: str, nodes: list[str] | None = None
    ) -> Any:
        """
        Recycle a Kubernetes Node Pool

        Args:
            cluster_id (string): cluster_id
            node_pool_id (string): node_pool_id
            nodes (array): nodes Example: "['d8db5e1a-6103-43b5-a7b3-8a948210a9fc']".

        Returns:
            Any: This does not indicate the success or failure of any operation, just that the request has been accepted for processing.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Kubernetes
        """
        if cluster_id is None:
            raise ValueError("Missing required parameter 'cluster_id'.")
        if node_pool_id is None:
            raise ValueError("Missing required parameter 'node_pool_id'.")
        request_body_data = None
        request_body_data = {
            "nodes": nodes,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/kubernetes/clusters/{cluster_id}/node_pools/{node_pool_id}/recycle"
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

    def kubernetes_get_cluster_user(self, cluster_id: str) -> dict[str, Any]:
        """
        Retrieve User Information for a Kubernetes Cluster

        Args:
            cluster_id (string): cluster_id

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `kubernetes_cluster_user`
        containing the username and in-cluster groups that it belongs to.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Kubernetes
        """
        if cluster_id is None:
            raise ValueError("Missing required parameter 'cluster_id'.")
        url = f"{self.base_url}/v2/kubernetes/clusters/{cluster_id}/user"
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

    def kubernetes_list_options(self) -> dict[str, Any]:
        """
        List Available Regions, Node Sizes, and Versions of Kubernetes

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `options` which contains
        `regions`, `versions`, and `sizes` objects listing the available options and
        the matching slugs for use when creating a new cluster.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Kubernetes
        """
        url = f"{self.base_url}/v2/kubernetes/options"
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

    def kubernetes_run_cluster_lint(
        self,
        cluster_id: str,
        include_groups: list[str] | None = None,
        include_checks: list[str] | None = None,
        exclude_groups: list[str] | None = None,
        exclude_checks: list[str] | None = None,
    ) -> Any:
        """
        Run Clusterlint Checks on a Kubernetes Cluster

        Args:
            cluster_id (string): cluster_id
            include_groups (array): An array of check groups that will be run when clusterlint executes checks. Example: "['basic', 'doks', 'security']".
            include_checks (array): An array of checks that will be run when clusterlint executes checks. Example: "['bare-pods', 'resource-requirements']".
            exclude_groups (array): An array of check groups that will be omitted when clusterlint executes checks. Example: "['workload-health']".
            exclude_checks (array): An array of checks that will be run when clusterlint executes checks. Example: "['default-namespace']".

        Returns:
            Any: The response is a JSON object with a key called `run_id` that you can later use to fetch the run results.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Kubernetes
        """
        if cluster_id is None:
            raise ValueError("Missing required parameter 'cluster_id'.")
        request_body_data = None
        request_body_data = {
            "include_groups": include_groups,
            "include_checks": include_checks,
            "exclude_groups": exclude_groups,
            "exclude_checks": exclude_checks,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/kubernetes/clusters/{cluster_id}/clusterlint"
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

    def get_cluster_lint(
        self, cluster_id: str, run_id: str | None = None
    ) -> dict[str, Any]:
        """
        Fetch Clusterlint Diagnostics for a Kubernetes Cluster

        Args:
            cluster_id (string): cluster_id
            run_id (string): Specifies the clusterlint run whose results will be retrieved. Example: '50c2f44c-011d-493e-aee5-361a4a0d1844'.

        Returns:
            dict[str, Any]: The response is a JSON object which contains the diagnostics on Kubernetes
        objects in the cluster. Each diagnostic will contain some metadata information
        about the object and feedback for users to act upon.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Kubernetes
        """
        if cluster_id is None:
            raise ValueError("Missing required parameter 'cluster_id'.")
        url = f"{self.base_url}/v2/kubernetes/clusters/{cluster_id}/clusterlint"
        query_params = {k: v for k, v in [("run_id", run_id)] if v is not None}
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

    def kubernetes_add_registry(self, cluster_uuids: list[str] | None = None) -> Any:
        """
        Add Container Registry to Kubernetes Clusters

        Args:
            cluster_uuids (array): An array containing the UUIDs of Kubernetes clusters. Example: "['bd5f5959-5e1e-4205-a714-a914373942af', '50c2f44c-011d-493e-aee5-361a4a0d1844']".

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Kubernetes
        """
        request_body_data = None
        request_body_data = {
            "cluster_uuids": cluster_uuids,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/kubernetes/registry"
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

    def kubernetes_remove_registry(self, cluster_uuids: list[str] | None = None) -> Any:
        """
        Remove Container Registry from Kubernetes Clusters

        Args:
            cluster_uuids (array): An array containing the UUIDs of Kubernetes clusters. Example: "['bd5f5959-5e1e-4205-a714-a914373942af', '50c2f44c-011d-493e-aee5-361a4a0d1844']".

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Kubernetes
        """
        request_body_data = {
            "cluster_uuids": cluster_uuids,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/kubernetes/registry"
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

    def kubernetes_get_status_messages(
        self, cluster_id: str, since: str | None = None
    ) -> Any:
        """
        Fetch Status Messages for a Kubernetes Cluster

        Args:
            cluster_id (string): cluster_id
            since (string): A timestamp used to return status messages emitted since the specified time. The timestamp should be in ISO8601 format. Example: '2018-11-15T16:00:11Z'.

        Returns:
            Any: The response is a JSON object which contains status messages for a Kubernetes cluster. Each message object contains a timestamp and an indication of what issue the cluster is experiencing at a given time.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Kubernetes
        """
        if cluster_id is None:
            raise ValueError("Missing required parameter 'cluster_id'.")
        url = f"{self.base_url}/v2/kubernetes/clusters/{cluster_id}/status_messages"
        query_params = {k: v for k, v in [("since", since)] if v is not None}
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

    def load_balancers_create(
        self,
        droplet_ids: list[int] | None = None,
        region: str | None = None,
        id: str | None = None,
        name: str | None = None,
        project_id: str | None = None,
        ip: str | None = None,
        ipv6: str | None = None,
        size_unit: int | None = None,
        size: str | None = None,
        algorithm: str | None = None,
        status: str | None = None,
        created_at: str | None = None,
        forwarding_rules: list[dict[str, Any]] | None = None,
        health_check: dict[str, Any] | None = None,
        sticky_sessions: dict[str, Any] | None = None,
        redirect_http_to_https: bool | None = None,
        enable_proxy_protocol: bool | None = None,
        enable_backend_keepalive: bool | None = None,
        http_idle_timeout_seconds: int | None = None,
        vpc_uuid: str | None = None,
        disable_lets_encrypt_dns_records: bool | None = None,
        firewall: dict[str, Any] | None = None,
        network: str | None = None,
        network_stack: str | None = None,
        type: str | None = None,
        domains: list[dict[str, Any]] | None = None,
        glb_settings: dict[str, Any] | None = None,
        target_load_balancer_ids: list[str] | None = None,
        tls_cipher_policy: str | None = None,
        tag: str | None = None,
    ) -> Any:
        """
        Create a New Load Balancer

        Args:
            droplet_ids (array): An array containing the IDs of the Droplets assigned to the load balancer. Example: '[3164444, 3164445]'.
            region (string): The slug identifier for the region where the resource will initially be  available. Example: 'nyc3'.
            id (string): A unique ID that can be used to identify and reference a load balancer. Example: '4de7ac8b-495b-4884-9a69-1050c6793cd6'.
            name (string): A human-readable name for a load balancer instance. Example: 'example-lb-01'.
            project_id (string): The ID of the project that the load balancer is associated with. If no ID is provided at creation, the load balancer associates with the user's default project. If an invalid project ID is provided, the load balancer will not be created. Example: '4de7ac8b-495b-4884-9a69-1050c6793cd6'.
            ip (string): An attribute containing the public-facing IP address of the load balancer. Example: '104.131.186.241'.
            ipv6 (string): An attribute containing the public-facing IPv6 address of the load balancer. Example: '2604:a880:800:14::85f5:c000'.
            size_unit (integer): How many nodes the load balancer contains. Each additional node increases the load balancer's ability to manage more connections. Load balancers can be scaled up or down, and you can change the number of nodes after creation up to once per hour. This field is currently not available in the AMS2, NYC2, or SFO1 regions. Use the `size` field to scale load balancers that reside in these regions. Example: '3'.
            size (string): This field has been replaced by the `size_unit` field for all regions except in AMS2, NYC2, and SFO1. Each available load balancer size now equates to the load balancer having a set number of nodes.
        * `lb-small` = 1 node
        * `lb-medium` = 3 nodes
        * `lb-large` = 6 nodes

        You can resize load balancers after creation up to once per hour. You cannot resize a load balancer within the first hour of its creation. Example: 'lb-small'.
            algorithm (string): This field has been deprecated. You can no longer specify an algorithm for load balancers. Example: 'round_robin'.
            status (string): A status string indicating the current state of the load balancer. This can be `new`, `active`, or `errored`. Example: 'new'.
            created_at (string): A time value given in ISO8601 combined date and time format that represents when the load balancer was created. Example: '2017-02-01T22:22:58Z'.
            forwarding_rules (array): An array of objects specifying the forwarding rules for a load balancer. Example: [{'entry_protocol': 'http', 'entry_port': 80, 'target_protocol': 'http', 'target_port': 80}, {'entry_protocol': 'https', 'entry_port': 443, 'target_protocol': 'https', 'target_port': 443, 'tls_passthrough': True}].
            health_check (object): An object specifying health check settings for the load balancer.
            sticky_sessions (object): An object specifying sticky sessions settings for the load balancer.
            redirect_http_to_https (boolean): A boolean value indicating whether HTTP requests to the load balancer on port 80 will be redirected to HTTPS on port 443. Example: 'True'.
            enable_proxy_protocol (boolean): A boolean value indicating whether PROXY Protocol is in use. Example: 'True'.
            enable_backend_keepalive (boolean): A boolean value indicating whether HTTP keepalive connections are maintained to target Droplets. Example: 'True'.
            http_idle_timeout_seconds (integer): An integer value which configures the idle timeout for HTTP requests to the target droplets. Example: '90'.
            vpc_uuid (string): A string specifying the UUID of the VPC to which the load balancer is assigned. Example: 'c33931f2-a26a-4e61-b85c-4e95a2ec431b'.
            disable_lets_encrypt_dns_records (boolean): A boolean value indicating whether to disable automatic DNS record creation for Let's Encrypt certificates that are added to the load balancer. Example: 'True'.
            firewall (object): An object specifying allow and deny rules to control traffic to the load balancer. Example: {'deny': ['cidr:1.2.0.0/16', 'ip:2.3.4.5'], 'allow': ['ip:1.2.3.4', 'cidr:2.3.4.0/24']}.
            network (string): A string indicating whether the load balancer should be external or internal. Internal load balancers have no public IPs and are only accessible to resources on the same VPC network. This property cannot be updated after creating the load balancer. Example: 'EXTERNAL'.
            network_stack (string): A string indicating whether the load balancer will support IPv4 or both IPv4 and IPv6 networking. This property cannot be updated after creating the load balancer. Example: 'IPV4'.
            type (string): A string indicating whether the load balancer should be a standard regional HTTP load balancer, a regional network load balancer that routes traffic at the TCP/UDP transport layer, or a global load balancer. Example: 'REGIONAL'.
            domains (array): An array of objects specifying the domain configurations for a Global load balancer.
            glb_settings (object): An object specifying forwarding configurations for a Global load balancer.
            target_load_balancer_ids (array): An array containing the UUIDs of the Regional load balancers to be used as target backends for a Global load balancer. Example: "['7dbf91fe-cbdb-48dc-8290-c3a181554905', '996fa239-fac3-42a2-b9a1-9fa822268b7a']".
            tls_cipher_policy (string): A string indicating the policy for the TLS cipher suites used by the load balancer. The possible values are `DEFAULT` or `STRONG`. The default value is `DEFAULT`. Example: 'STRONG'.
            tag (string): The name of a Droplet tag corresponding to Droplets assigned to the load balancer. Example: 'prod:web'.

        Returns:
            Any: Accepted

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Load Balancers
        """
        request_body_data = None
        request_body_data = {
            "droplet_ids": droplet_ids,
            "region": region,
            "id": id,
            "name": name,
            "project_id": project_id,
            "ip": ip,
            "ipv6": ipv6,
            "size_unit": size_unit,
            "size": size,
            "algorithm": algorithm,
            "status": status,
            "created_at": created_at,
            "forwarding_rules": forwarding_rules,
            "health_check": health_check,
            "sticky_sessions": sticky_sessions,
            "redirect_http_to_https": redirect_http_to_https,
            "enable_proxy_protocol": enable_proxy_protocol,
            "enable_backend_keepalive": enable_backend_keepalive,
            "http_idle_timeout_seconds": http_idle_timeout_seconds,
            "vpc_uuid": vpc_uuid,
            "disable_lets_encrypt_dns_records": disable_lets_encrypt_dns_records,
            "firewall": firewall,
            "network": network,
            "network_stack": network_stack,
            "type": type,
            "domains": domains,
            "glb_settings": glb_settings,
            "target_load_balancer_ids": target_load_balancer_ids,
            "tls_cipher_policy": tls_cipher_policy,
            "tag": tag,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/load_balancers"
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

    def load_balancers_list(
        self, per_page: int | None = None, page: int | None = None
    ) -> Any:
        """
        List All Load Balancers

        Args:
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: A JSON object with a key of `load_balancers`. This will be set to an array of objects, each of which will contain the standard load balancer attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Load Balancers
        """
        url = f"{self.base_url}/v2/load_balancers"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def load_balancers_get(self, lb_id: str) -> Any:
        """
        Retrieve an Existing Load Balancer

        Args:
            lb_id (string): lb_id

        Returns:
            Any: The response will be a JSON object with a key called `load_balancer`. The
        value of this will be an object that contains the standard attributes
        associated with a load balancer

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Load Balancers
        """
        if lb_id is None:
            raise ValueError("Missing required parameter 'lb_id'.")
        url = f"{self.base_url}/v2/load_balancers/{lb_id}"
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

    def load_balancers_update(
        self,
        lb_id: str,
        droplet_ids: list[int] | None = None,
        region: str | None = None,
        id: str | None = None,
        name: str | None = None,
        project_id: str | None = None,
        ip: str | None = None,
        ipv6: str | None = None,
        size_unit: int | None = None,
        size: str | None = None,
        algorithm: str | None = None,
        status: str | None = None,
        created_at: str | None = None,
        forwarding_rules: list[dict[str, Any]] | None = None,
        health_check: dict[str, Any] | None = None,
        sticky_sessions: dict[str, Any] | None = None,
        redirect_http_to_https: bool | None = None,
        enable_proxy_protocol: bool | None = None,
        enable_backend_keepalive: bool | None = None,
        http_idle_timeout_seconds: int | None = None,
        vpc_uuid: str | None = None,
        disable_lets_encrypt_dns_records: bool | None = None,
        firewall: dict[str, Any] | None = None,
        network: str | None = None,
        network_stack: str | None = None,
        type: str | None = None,
        domains: list[dict[str, Any]] | None = None,
        glb_settings: dict[str, Any] | None = None,
        target_load_balancer_ids: list[str] | None = None,
        tls_cipher_policy: str | None = None,
        tag: str | None = None,
    ) -> Any:
        """
        Update a Load Balancer

        Args:
            lb_id (string): lb_id
            droplet_ids (array): An array containing the IDs of the Droplets assigned to the load balancer. Example: '[3164444, 3164445]'.
            region (string): The slug identifier for the region where the resource will initially be  available. Example: 'nyc3'.
            id (string): A unique ID that can be used to identify and reference a load balancer. Example: '4de7ac8b-495b-4884-9a69-1050c6793cd6'.
            name (string): A human-readable name for a load balancer instance. Example: 'example-lb-01'.
            project_id (string): The ID of the project that the load balancer is associated with. If no ID is provided at creation, the load balancer associates with the user's default project. If an invalid project ID is provided, the load balancer will not be created. Example: '4de7ac8b-495b-4884-9a69-1050c6793cd6'.
            ip (string): An attribute containing the public-facing IP address of the load balancer. Example: '104.131.186.241'.
            ipv6 (string): An attribute containing the public-facing IPv6 address of the load balancer. Example: '2604:a880:800:14::85f5:c000'.
            size_unit (integer): How many nodes the load balancer contains. Each additional node increases the load balancer's ability to manage more connections. Load balancers can be scaled up or down, and you can change the number of nodes after creation up to once per hour. This field is currently not available in the AMS2, NYC2, or SFO1 regions. Use the `size` field to scale load balancers that reside in these regions. Example: '3'.
            size (string): This field has been replaced by the `size_unit` field for all regions except in AMS2, NYC2, and SFO1. Each available load balancer size now equates to the load balancer having a set number of nodes.
        * `lb-small` = 1 node
        * `lb-medium` = 3 nodes
        * `lb-large` = 6 nodes

        You can resize load balancers after creation up to once per hour. You cannot resize a load balancer within the first hour of its creation. Example: 'lb-small'.
            algorithm (string): This field has been deprecated. You can no longer specify an algorithm for load balancers. Example: 'round_robin'.
            status (string): A status string indicating the current state of the load balancer. This can be `new`, `active`, or `errored`. Example: 'new'.
            created_at (string): A time value given in ISO8601 combined date and time format that represents when the load balancer was created. Example: '2017-02-01T22:22:58Z'.
            forwarding_rules (array): An array of objects specifying the forwarding rules for a load balancer. Example: [{'entry_protocol': 'http', 'entry_port': 80, 'target_protocol': 'http', 'target_port': 80, 'certificate_id': '', 'tls_passthrough': False}, {'entry_protocol': 'https', 'entry_port': 443, 'target_protocol': 'https', 'target_port': 443, 'certificate_id': '', 'tls_passthrough': True}].
            health_check (object): An object specifying health check settings for the load balancer. Example: {'protocol': 'http', 'port': 80, 'path': '/', 'check_interval_seconds': 10, 'response_timeout_seconds': 5, 'healthy_threshold': 5, 'unhealthy_threshold': 3}.
            sticky_sessions (object): An object specifying sticky sessions settings for the load balancer. Example: {'type': 'none'}.
            redirect_http_to_https (boolean): A boolean value indicating whether HTTP requests to the load balancer on port 80 will be redirected to HTTPS on port 443. Example: 'True'.
            enable_proxy_protocol (boolean): A boolean value indicating whether PROXY Protocol is in use. Example: 'True'.
            enable_backend_keepalive (boolean): A boolean value indicating whether HTTP keepalive connections are maintained to target Droplets. Example: 'True'.
            http_idle_timeout_seconds (integer): An integer value which configures the idle timeout for HTTP requests to the target droplets. Example: '90'.
            vpc_uuid (string): A string specifying the UUID of the VPC to which the load balancer is assigned. Example: 'c33931f2-a26a-4e61-b85c-4e95a2ec431b'.
            disable_lets_encrypt_dns_records (boolean): A boolean value indicating whether to disable automatic DNS record creation for Let's Encrypt certificates that are added to the load balancer. Example: 'True'.
            firewall (object): An object specifying allow and deny rules to control traffic to the load balancer. Example: {'deny': ['cidr:1.2.0.0/16', 'ip:2.3.4.5'], 'allow': ['ip:1.2.3.4', 'cidr:2.3.4.0/24']}.
            network (string): A string indicating whether the load balancer should be external or internal. Internal load balancers have no public IPs and are only accessible to resources on the same VPC network. This property cannot be updated after creating the load balancer. Example: 'EXTERNAL'.
            network_stack (string): A string indicating whether the load balancer will support IPv4 or both IPv4 and IPv6 networking. This property cannot be updated after creating the load balancer. Example: 'IPV4'.
            type (string): A string indicating whether the load balancer should be a standard regional HTTP load balancer, a regional network load balancer that routes traffic at the TCP/UDP transport layer, or a global load balancer. Example: 'REGIONAL'.
            domains (array): An array of objects specifying the domain configurations for a Global load balancer.
            glb_settings (object): An object specifying forwarding configurations for a Global load balancer.
            target_load_balancer_ids (array): An array containing the UUIDs of the Regional load balancers to be used as target backends for a Global load balancer. Example: "['7dbf91fe-cbdb-48dc-8290-c3a181554905', '996fa239-fac3-42a2-b9a1-9fa822268b7a']".
            tls_cipher_policy (string): A string indicating the policy for the TLS cipher suites used by the load balancer. The possible values are `DEFAULT` or `STRONG`. The default value is `DEFAULT`. Example: 'STRONG'.
            tag (string): The name of a Droplet tag corresponding to Droplets assigned to the load balancer. Example: 'prod:web'.

        Returns:
            Any: The response will be a JSON object with a key called `load_balancer`. The
        value of this will be an object containing the standard attributes of a
        load balancer.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Load Balancers
        """
        if lb_id is None:
            raise ValueError("Missing required parameter 'lb_id'.")
        request_body_data = None
        request_body_data = {
            "droplet_ids": droplet_ids,
            "region": region,
            "id": id,
            "name": name,
            "project_id": project_id,
            "ip": ip,
            "ipv6": ipv6,
            "size_unit": size_unit,
            "size": size,
            "algorithm": algorithm,
            "status": status,
            "created_at": created_at,
            "forwarding_rules": forwarding_rules,
            "health_check": health_check,
            "sticky_sessions": sticky_sessions,
            "redirect_http_to_https": redirect_http_to_https,
            "enable_proxy_protocol": enable_proxy_protocol,
            "enable_backend_keepalive": enable_backend_keepalive,
            "http_idle_timeout_seconds": http_idle_timeout_seconds,
            "vpc_uuid": vpc_uuid,
            "disable_lets_encrypt_dns_records": disable_lets_encrypt_dns_records,
            "firewall": firewall,
            "network": network,
            "network_stack": network_stack,
            "type": type,
            "domains": domains,
            "glb_settings": glb_settings,
            "target_load_balancer_ids": target_load_balancer_ids,
            "tls_cipher_policy": tls_cipher_policy,
            "tag": tag,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/load_balancers/{lb_id}"
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

    def load_balancers_delete(self, lb_id: str) -> Any:
        """
        Delete a Load Balancer

        Args:
            lb_id (string): lb_id

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Load Balancers
        """
        if lb_id is None:
            raise ValueError("Missing required parameter 'lb_id'.")
        url = f"{self.base_url}/v2/load_balancers/{lb_id}"
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

    def load_balancers_delete_cache(self, lb_id: str) -> Any:
        """
        Delete a Global Load Balancer CDN Cache

        Args:
            lb_id (string): lb_id

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Load Balancers
        """
        if lb_id is None:
            raise ValueError("Missing required parameter 'lb_id'.")
        url = f"{self.base_url}/v2/load_balancers/{lb_id}/cache"
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

    def load_balancers_add_droplets(self, lb_id: str, droplet_ids: list[int]) -> Any:
        """
        Add Droplets to a Load Balancer

        Args:
            lb_id (string): lb_id
            droplet_ids (array): An array containing the IDs of the Droplets assigned to the load balancer. Example: '[3164444, 3164445]'.

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Load Balancers
        """
        if lb_id is None:
            raise ValueError("Missing required parameter 'lb_id'.")
        request_body_data = None
        request_body_data = {
            "droplet_ids": droplet_ids,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/load_balancers/{lb_id}/droplets"
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

    def load_balancers_remove_droplets(self, lb_id: str, droplet_ids: list[int]) -> Any:
        """
        Remove Droplets from a Load Balancer

        Args:
            lb_id (string): lb_id
            droplet_ids (array): An array containing the IDs of the Droplets assigned to the load balancer. Example: '[3164444, 3164445]'.

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Load Balancers
        """
        if lb_id is None:
            raise ValueError("Missing required parameter 'lb_id'.")
        request_body_data = {
            "droplet_ids": droplet_ids,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/load_balancers/{lb_id}/droplets"
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

    def add_forwarding_rule(
        self, lb_id: str, forwarding_rules: list[dict[str, Any]]
    ) -> Any:
        """
        Add Forwarding Rules to a Load Balancer

        Args:
            lb_id (string): lb_id
            forwarding_rules (array): forwarding_rules

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Load Balancers
        """
        if lb_id is None:
            raise ValueError("Missing required parameter 'lb_id'.")
        request_body_data = None
        request_body_data = {
            "forwarding_rules": forwarding_rules,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/load_balancers/{lb_id}/forwarding_rules"
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

    def delete_lb_forwarding_rules(
        self, lb_id: str, forwarding_rules: list[dict[str, Any]]
    ) -> Any:
        """
        Remove Forwarding Rules from a Load Balancer

        Args:
            lb_id (string): lb_id
            forwarding_rules (array): forwarding_rules

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Load Balancers
        """
        if lb_id is None:
            raise ValueError("Missing required parameter 'lb_id'.")
        request_body_data = {
            "forwarding_rules": forwarding_rules,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/load_balancers/{lb_id}/forwarding_rules"
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

    def monitoring_list_alert_policy(
        self, per_page: int | None = None, page: int | None = None
    ) -> Any:
        """
        List Alert Policies

        Args:
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: A list of alert policies.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/alerts"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def monitoring_create_alert_policy(
        self,
        alerts: dict[str, Any],
        compare: str,
        description: str,
        enabled: bool,
        entities: list[str],
        tags: list[str],
        type: str,
        value: float,
        window: str,
    ) -> Any:
        """
        Create Alert Policy

        Args:
            alerts (object): alerts
            compare (string): compare Example: 'GreaterThan'.
            description (string): description Example: 'CPU Alert'.
            enabled (boolean): enabled Example: 'True'.
            entities (array): entities Example: "['192018292']".
            tags (array): tags Example: "['droplet_tag']".
            type (string): type Example: 'v1/insights/droplet/cpu'.
            value (number): value Example: '80'.
            window (string): window Example: '5m'.

        Returns:
            Any: An alert policy.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        request_body_data = None
        request_body_data = {
            "alerts": alerts,
            "compare": compare,
            "description": description,
            "enabled": enabled,
            "entities": entities,
            "tags": tags,
            "type": type,
            "value": value,
            "window": window,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/monitoring/alerts"
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

    def monitoring_get_alert_policy(self, alert_uuid: str) -> Any:
        """
        Retrieve an Existing Alert Policy

        Args:
            alert_uuid (string): alert_uuid

        Returns:
            Any: An alert policy.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        if alert_uuid is None:
            raise ValueError("Missing required parameter 'alert_uuid'.")
        url = f"{self.base_url}/v2/monitoring/alerts/{alert_uuid}"
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

    def monitoring_update_alert_policy(
        self,
        alert_uuid: str,
        alerts: dict[str, Any],
        compare: str,
        description: str,
        enabled: bool,
        entities: list[str],
        tags: list[str],
        type: str,
        value: float,
        window: str,
    ) -> Any:
        """
        Update an Alert Policy

        Args:
            alert_uuid (string): alert_uuid
            alerts (object): alerts
            compare (string): compare Example: 'GreaterThan'.
            description (string): description Example: 'CPU Alert'.
            enabled (boolean): enabled Example: 'True'.
            entities (array): entities Example: "['192018292']".
            tags (array): tags Example: "['droplet_tag']".
            type (string): type Example: 'v1/insights/droplet/cpu'.
            value (number): value Example: '80'.
            window (string): window Example: '5m'.

        Returns:
            Any: An alert policy.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        if alert_uuid is None:
            raise ValueError("Missing required parameter 'alert_uuid'.")
        request_body_data = None
        request_body_data = {
            "alerts": alerts,
            "compare": compare,
            "description": description,
            "enabled": enabled,
            "entities": entities,
            "tags": tags,
            "type": type,
            "value": value,
            "window": window,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/monitoring/alerts/{alert_uuid}"
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

    def monitoring_delete_alert_policy(self, alert_uuid: str) -> Any:
        """
        Delete an Alert Policy

        Args:
            alert_uuid (string): alert_uuid

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        if alert_uuid is None:
            raise ValueError("Missing required parameter 'alert_uuid'.")
        url = f"{self.base_url}/v2/monitoring/alerts/{alert_uuid}"
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

    def get_droplet_bandwidth_metrics(
        self, host_id: str, interface: str, direction: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Droplet Bandwidth Metrics

        Args:
            host_id (string): The droplet ID. Example: '17209102'.
            interface (string): The network interface. Example: 'private'.
            direction (string): The traffic direction. Example: 'inbound'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/droplet/bandwidth"
        query_params = {
            k: v
            for k, v in [
                ("host_id", host_id),
                ("interface", interface),
                ("direction", direction),
                ("start", start),
                ("end", end),
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

    def get_droplet_cpu_metrics(
        self, host_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Droplet CPU Metrics

        Args:
            host_id (string): The droplet ID. Example: '17209102'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/droplet/cpu"
        query_params = {
            k: v
            for k, v in [("host_id", host_id), ("start", start), ("end", end)]
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

    def get_droplet_filesystem_free(
        self, host_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Droplet Filesystem Free Metrics

        Args:
            host_id (string): The droplet ID. Example: '17209102'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/droplet/filesystem_free"
        query_params = {
            k: v
            for k, v in [("host_id", host_id), ("start", start), ("end", end)]
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

    def get_droplet_filesystem_size(
        self, host_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Droplet Filesystem Size Metrics

        Args:
            host_id (string): The droplet ID. Example: '17209102'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/droplet/filesystem_size"
        query_params = {
            k: v
            for k, v in [("host_id", host_id), ("start", start), ("end", end)]
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

    def get_droplet_load_metrics(
        self, host_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Droplet Load1 Metrics

        Args:
            host_id (string): The droplet ID. Example: '17209102'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/droplet/load_1"
        query_params = {
            k: v
            for k, v in [("host_id", host_id), ("start", start), ("end", end)]
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

    def get_droplet_load5_metrics(
        self, host_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Droplet Load5 Metrics

        Args:
            host_id (string): The droplet ID. Example: '17209102'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/droplet/load_5"
        query_params = {
            k: v
            for k, v in [("host_id", host_id), ("start", start), ("end", end)]
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

    def get_droplet_load_metric(
        self, host_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Droplet Load15 Metrics

        Args:
            host_id (string): The droplet ID. Example: '17209102'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/droplet/load_15"
        query_params = {
            k: v
            for k, v in [("host_id", host_id), ("start", start), ("end", end)]
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

    def get_droplet_memory_cached(
        self, host_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Droplet Cached Memory Metrics

        Args:
            host_id (string): The droplet ID. Example: '17209102'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/droplet/memory_cached"
        query_params = {
            k: v
            for k, v in [("host_id", host_id), ("start", start), ("end", end)]
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

    def get_droplet_memory_free(
        self, host_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Droplet Free Memory Metrics

        Args:
            host_id (string): The droplet ID. Example: '17209102'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/droplet/memory_free"
        query_params = {
            k: v
            for k, v in [("host_id", host_id), ("start", start), ("end", end)]
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

    def get_droplet_memory_total(
        self, host_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Droplet Total Memory Metrics

        Args:
            host_id (string): The droplet ID. Example: '17209102'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/droplet/memory_total"
        query_params = {
            k: v
            for k, v in [("host_id", host_id), ("start", start), ("end", end)]
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

    def get_droplet_memory_available(
        self, host_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Droplet Available Memory Metrics

        Args:
            host_id (string): The droplet ID. Example: '17209102'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/droplet/memory_available"
        query_params = {
            k: v
            for k, v in [("host_id", host_id), ("start", start), ("end", end)]
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

    def get_app_memory_percentage(
        self, app_id: str, start: str, end: str, app_component: str | None = None
    ) -> dict[str, Any]:
        """
        Get App Memory Percentage Metrics

        Args:
            app_id (string): The app UUID. Example: '2db3c021-15ad-4088-bfe8-99dc972b9cf6'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.
            app_component (string): The app component name. Example: 'sample-application'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/apps/memory_percentage"
        query_params = {
            k: v
            for k, v in [
                ("app_id", app_id),
                ("app_component", app_component),
                ("start", start),
                ("end", end),
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

    def get_app_cpu_metrics(
        self, app_id: str, start: str, end: str, app_component: str | None = None
    ) -> dict[str, Any]:
        """
        Get App CPU Percentage Metrics

        Args:
            app_id (string): The app UUID. Example: '2db3c021-15ad-4088-bfe8-99dc972b9cf6'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.
            app_component (string): The app component name. Example: 'sample-application'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/apps/cpu_percentage"
        query_params = {
            k: v
            for k, v in [
                ("app_id", app_id),
                ("app_component", app_component),
                ("start", start),
                ("end", end),
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

    def get_app_restart_count(
        self, app_id: str, start: str, end: str, app_component: str | None = None
    ) -> dict[str, Any]:
        """
        Get App Restart Count Metrics

        Args:
            app_id (string): The app UUID. Example: '2db3c021-15ad-4088-bfe8-99dc972b9cf6'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.
            app_component (string): The app component name. Example: 'sample-application'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/apps/restart_count"
        query_params = {
            k: v
            for k, v in [
                ("app_id", app_id),
                ("app_component", app_component),
                ("start", start),
                ("end", end),
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

    def get_frontend_connections(
        self, lb_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Load Balancer Frontend Total Current Active Connections Metrics

        Args:
            lb_id (string): A unique identifier for a load balancer. Example: '4de7ac8b-495b-4884-9a69-1050c6793cd6'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/load_balancer/frontend_connections_current"
        query_params = {
            k: v
            for k, v in [("lb_id", lb_id), ("start", start), ("end", end)]
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

    def get_lb_frontend_connections_limit(
        self, lb_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Load Balancer Frontend Max Connections Limit Metrics

        Args:
            lb_id (string): A unique identifier for a load balancer. Example: '4de7ac8b-495b-4884-9a69-1050c6793cd6'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/load_balancer/frontend_connections_limit"
        query_params = {
            k: v
            for k, v in [("lb_id", lb_id), ("start", start), ("end", end)]
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

    def get_frontend_cpu_utilization(
        self, lb_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Load Balancer Frontend Average Percentage CPU Utilization Metrics

        Args:
            lb_id (string): A unique identifier for a load balancer. Example: '4de7ac8b-495b-4884-9a69-1050c6793cd6'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/load_balancer/frontend_cpu_utilization"
        query_params = {
            k: v
            for k, v in [("lb_id", lb_id), ("start", start), ("end", end)]
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

    def get_frontend_firewall_bytes(
        self, lb_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Load Balancer Frontend Firewall Dropped Bytes Metrics

        Args:
            lb_id (string): A unique identifier for a load balancer. Example: '4de7ac8b-495b-4884-9a69-1050c6793cd6'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/load_balancer/frontend_firewall_dropped_bytes"
        query_params = {
            k: v
            for k, v in [("lb_id", lb_id), ("start", start), ("end", end)]
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

    def get_lb_frontend_fw_dropped_pkts(
        self, lb_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Load Balancer Frontend Firewall Dropped Packets Metrics

        Args:
            lb_id (string): A unique identifier for a load balancer. Example: '4de7ac8b-495b-4884-9a69-1050c6793cd6'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/load_balancer/frontend_firewall_dropped_packets"
        query_params = {
            k: v
            for k, v in [("lb_id", lb_id), ("start", start), ("end", end)]
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

    def get_load_balancer_responses(
        self, lb_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Load Balancer Frontend HTTP Rate Of Response Code Metrics

        Args:
            lb_id (string): A unique identifier for a load balancer. Example: '4de7ac8b-495b-4884-9a69-1050c6793cd6'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/load_balancer/frontend_http_responses"
        query_params = {
            k: v
            for k, v in [("lb_id", lb_id), ("start", start), ("end", end)]
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

    def fetch_frontend_request_rate(
        self, lb_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Load Balancer Frontend HTTP Requests Metrics

        Args:
            lb_id (string): A unique identifier for a load balancer. Example: '4de7ac8b-495b-4884-9a69-1050c6793cd6'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/load_balancer/frontend_http_requests_per_second"
        query_params = {
            k: v
            for k, v in [("lb_id", lb_id), ("start", start), ("end", end)]
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

    def get_frontend_network_throughput(
        self, lb_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Load Balancer Frontend HTTP Throughput Metrics

        Args:
            lb_id (string): A unique identifier for a load balancer. Example: '4de7ac8b-495b-4884-9a69-1050c6793cd6'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/load_balancer/frontend_network_throughput_http"
        query_params = {
            k: v
            for k, v in [("lb_id", lb_id), ("start", start), ("end", end)]
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

    def get_frontend_udp_throughput(
        self, lb_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Load Balancer Frontend UDP Throughput Metrics

        Args:
            lb_id (string): A unique identifier for a load balancer. Example: '4de7ac8b-495b-4884-9a69-1050c6793cd6'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/load_balancer/frontend_network_throughput_udp"
        query_params = {
            k: v
            for k, v in [("lb_id", lb_id), ("start", start), ("end", end)]
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

    def get_frontend_tcp_throughput(
        self, lb_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Load Balancer Frontend TCP Throughput Metrics

        Args:
            lb_id (string): A unique identifier for a load balancer. Example: '4de7ac8b-495b-4884-9a69-1050c6793cd6'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/load_balancer/frontend_network_throughput_tcp"
        query_params = {
            k: v
            for k, v in [("lb_id", lb_id), ("start", start), ("end", end)]
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

    def get_frontend_nlb_tcp_throughput(
        self, lb_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Network Load Balancer Frontend TCP Throughput Metrics

        Args:
            lb_id (string): A unique identifier for a load balancer. Example: '4de7ac8b-495b-4884-9a69-1050c6793cd6'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/load_balancer/frontend_nlb_tcp_network_throughput"
        query_params = {
            k: v
            for k, v in [("lb_id", lb_id), ("start", start), ("end", end)]
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

    def get_nlb_udp_throughput(
        self, lb_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Network Load Balancer Frontend UDP Throughput Metrics

        Args:
            lb_id (string): A unique identifier for a load balancer. Example: '4de7ac8b-495b-4884-9a69-1050c6793cd6'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/load_balancer/frontend_nlb_udp_network_throughput"
        query_params = {
            k: v
            for k, v in [("lb_id", lb_id), ("start", start), ("end", end)]
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

    def get_frontend_tls_connections(
        self, lb_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Load Balancer Frontend Current TLS Connections Rate Metrics

        Args:
            lb_id (string): A unique identifier for a load balancer. Example: '4de7ac8b-495b-4884-9a69-1050c6793cd6'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/load_balancer/frontend_tls_connections_current"
        query_params = {
            k: v
            for k, v in [("lb_id", lb_id), ("start", start), ("end", end)]
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

    def get_frontend_tls_connections_limit(
        self, lb_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Load Balancer Frontend Max TLS Connections Limit Metrics

        Args:
            lb_id (string): A unique identifier for a load balancer. Example: '4de7ac8b-495b-4884-9a69-1050c6793cd6'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/load_balancer/frontend_tls_connections_limit"
        query_params = {
            k: v
            for k, v in [("lb_id", lb_id), ("start", start), ("end", end)]
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

    def get_tls_exceeding_rate_limit(
        self, lb_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Load Balancer Frontend Closed TLS Connections For Exceeded Rate Limit Metrics

        Args:
            lb_id (string): A unique identifier for a load balancer. Example: '4de7ac8b-495b-4884-9a69-1050c6793cd6'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/load_balancer/frontend_tls_connections_exceeding_rate_limit"
        query_params = {
            k: v
            for k, v in [("lb_id", lb_id), ("start", start), ("end", end)]
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

    def get_droplet_session_duration_avg(
        self, lb_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Load Balancer Droplets Average HTTP Session Duration Metrics

        Args:
            lb_id (string): A unique identifier for a load balancer. Example: '4de7ac8b-495b-4884-9a69-1050c6793cd6'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/load_balancer/droplets_http_session_duration_avg"
        query_params = {
            k: v
            for k, v in [("lb_id", lb_id), ("start", start), ("end", end)]
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

    def get_droplet_session_duration_50p(
        self, lb_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Load Balancer Droplets 50th Percentile HTTP Session Duration Metrics

        Args:
            lb_id (string): A unique identifier for a load balancer. Example: '4de7ac8b-495b-4884-9a69-1050c6793cd6'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/load_balancer/droplets_http_session_duration_50p"
        query_params = {
            k: v
            for k, v in [("lb_id", lb_id), ("start", start), ("end", end)]
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

    def get_droplet_session_duration_95p(
        self, lb_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Load Balancer Droplets 95th Percentile HTTP Session Duration Metrics

        Args:
            lb_id (string): A unique identifier for a load balancer. Example: '4de7ac8b-495b-4884-9a69-1050c6793cd6'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/load_balancer/droplets_http_session_duration_95p"
        query_params = {
            k: v
            for k, v in [("lb_id", lb_id), ("start", start), ("end", end)]
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

    def get_droplet_response_time(
        self, lb_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Load Balancer Droplets Average HTTP Response Time Metrics

        Args:
            lb_id (string): A unique identifier for a load balancer. Example: '4de7ac8b-495b-4884-9a69-1050c6793cd6'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/load_balancer/droplets_http_response_time_avg"
        query_params = {
            k: v
            for k, v in [("lb_id", lb_id), ("start", start), ("end", end)]
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

    def get_droplet_http_response_time(
        self, lb_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Load Balancer Droplets 50th Percentile HTTP Response Time Metrics

        Args:
            lb_id (string): A unique identifier for a load balancer. Example: '4de7ac8b-495b-4884-9a69-1050c6793cd6'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/load_balancer/droplets_http_response_time_50p"
        query_params = {
            k: v
            for k, v in [("lb_id", lb_id), ("start", start), ("end", end)]
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

    def get_droplets_http_response_timep_95p(
        self, lb_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Load Balancer Droplets 95th Percentile HTTP Response Time Metrics

        Args:
            lb_id (string): A unique identifier for a load balancer. Example: '4de7ac8b-495b-4884-9a69-1050c6793cd6'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/load_balancer/droplets_http_response_time_95p"
        query_params = {
            k: v
            for k, v in [("lb_id", lb_id), ("start", start), ("end", end)]
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

    def get_droplets_http_response_timep_99p(
        self, lb_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Load Balancer Droplets 99th Percentile HTTP Response Time Metrics

        Args:
            lb_id (string): A unique identifier for a load balancer. Example: '4de7ac8b-495b-4884-9a69-1050c6793cd6'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/load_balancer/droplets_http_response_time_99p"
        query_params = {
            k: v
            for k, v in [("lb_id", lb_id), ("start", start), ("end", end)]
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

    def get_droplet_queue_size(
        self, lb_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Load Balancer Droplets Queue Size Metrics

        Args:
            lb_id (string): A unique identifier for a load balancer. Example: '4de7ac8b-495b-4884-9a69-1050c6793cd6'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/load_balancer/droplets_queue_size"
        query_params = {
            k: v
            for k, v in [("lb_id", lb_id), ("start", start), ("end", end)]
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

    def get_droplet_responses(self, lb_id: str, start: str, end: str) -> dict[str, Any]:
        """
        Get Load Balancer Droplets HTTP Rate Of Response Code Metrics

        Args:
            lb_id (string): A unique identifier for a load balancer. Example: '4de7ac8b-495b-4884-9a69-1050c6793cd6'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/load_balancer/droplets_http_responses"
        query_params = {
            k: v
            for k, v in [("lb_id", lb_id), ("start", start), ("end", end)]
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

    def get_droplet_connections(
        self, lb_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Load Balancer Droplets Active Connections Metrics

        Args:
            lb_id (string): A unique identifier for a load balancer. Example: '4de7ac8b-495b-4884-9a69-1050c6793cd6'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = (
            f"{self.base_url}/v2/monitoring/metrics/load_balancer/droplets_connections"
        )
        query_params = {
            k: v
            for k, v in [("lb_id", lb_id), ("start", start), ("end", end)]
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

    def get_droplet_health_checks(
        self, lb_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Load Balancer Droplets Health Check Status Metrics

        Args:
            lb_id (string): A unique identifier for a load balancer. Example: '4de7ac8b-495b-4884-9a69-1050c6793cd6'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/load_balancer/droplets_health_checks"
        query_params = {
            k: v
            for k, v in [("lb_id", lb_id), ("start", start), ("end", end)]
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

    def get_load_balancer_downtime(
        self, lb_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Load Balancer Droplets Downtime Status Metrics

        Args:
            lb_id (string): A unique identifier for a load balancer. Example: '4de7ac8b-495b-4884-9a69-1050c6793cd6'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/load_balancer/droplets_downtime"
        query_params = {
            k: v
            for k, v in [("lb_id", lb_id), ("start", start), ("end", end)]
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

    def get_current_autoscale_instances(
        self, autoscale_pool_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Droplet Autoscale Pool Current Size

        Args:
            autoscale_pool_id (string): A unique identifier for an autoscale pool. Example: '0d3db13e-a604-4944-9827-7ec2642d32ac'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = (
            f"{self.base_url}/v2/monitoring/metrics/droplet_autoscale/current_instances"
        )
        query_params = {
            k: v
            for k, v in [
                ("autoscale_pool_id", autoscale_pool_id),
                ("start", start),
                ("end", end),
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

    def list_target_instances(
        self, autoscale_pool_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Droplet Autoscale Pool Target Size

        Args:
            autoscale_pool_id (string): A unique identifier for an autoscale pool. Example: '0d3db13e-a604-4944-9827-7ec2642d32ac'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = (
            f"{self.base_url}/v2/monitoring/metrics/droplet_autoscale/target_instances"
        )
        query_params = {
            k: v
            for k, v in [
                ("autoscale_pool_id", autoscale_pool_id),
                ("start", start),
                ("end", end),
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

    def get_droplet_cpu_utilization(
        self, autoscale_pool_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Droplet Autoscale Pool Current Average CPU utilization

        Args:
            autoscale_pool_id (string): A unique identifier for an autoscale pool. Example: '0d3db13e-a604-4944-9827-7ec2642d32ac'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/droplet_autoscale/current_cpu_utilization"
        query_params = {
            k: v
            for k, v in [
                ("autoscale_pool_id", autoscale_pool_id),
                ("start", start),
                ("end", end),
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

    def get_droplet_target_cpu_utilization(
        self, autoscale_pool_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Droplet Autoscale Pool Target Average CPU utilization

        Args:
            autoscale_pool_id (string): A unique identifier for an autoscale pool. Example: '0d3db13e-a604-4944-9827-7ec2642d32ac'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/droplet_autoscale/target_cpu_utilization"
        query_params = {
            k: v
            for k, v in [
                ("autoscale_pool_id", autoscale_pool_id),
                ("start", start),
                ("end", end),
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

    def get_droplet_memory_utilization(
        self, autoscale_pool_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Droplet Autoscale Pool Current Average Memory utilization

        Args:
            autoscale_pool_id (string): A unique identifier for an autoscale pool. Example: '0d3db13e-a604-4944-9827-7ec2642d32ac'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/droplet_autoscale/current_memory_utilization"
        query_params = {
            k: v
            for k, v in [
                ("autoscale_pool_id", autoscale_pool_id),
                ("start", start),
                ("end", end),
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

    def get_autoscale_memory_target(
        self, autoscale_pool_id: str, start: str, end: str
    ) -> dict[str, Any]:
        """
        Get Droplet Autoscale Pool Target Average Memory utilization

        Args:
            autoscale_pool_id (string): A unique identifier for an autoscale pool. Example: '0d3db13e-a604-4944-9827-7ec2642d32ac'.
            start (string): UNIX timestamp to start metric window. Example: '1620683817'.
            end (string): UNIX timestamp to end metric window. Example: '1620705417'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `data` and `status`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/metrics/droplet_autoscale/target_memory_utilization"
        query_params = {
            k: v
            for k, v in [
                ("autoscale_pool_id", autoscale_pool_id),
                ("start", start),
                ("end", end),
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

    def monitoring_create_destination(
        self, type: Any, config: dict[str, Any], name: str | None = None
    ) -> Any:
        """
        Create Logging Destination

        Args:
            type (string): The destination type. `opensearch_dbaas` for a DigitalOcean managed OpenSearch
        cluster or `opensearch_ext` for an externally managed one.
         Example: 'opensearch_dbaas'.
            config (object): config Example: {'endpoint': 'db-opensearch-nyc3-123456-do-user-123456-0.g.db.ondigitalocean.com', 'cluster_uuid': '85148069-7e35-4999-80bd-6fa1637ca385', 'cluster_name': 'managed_dbaas_cluster', 'index_name': 'logs', 'retention_days': 14}.
            name (string): destination name Example: 'managed_opensearch_cluster'.

        Returns:
            Any: The response is a JSON object with a `destination` key.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "type": type,
            "config": config,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/monitoring/sinks/destinations"
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

    def monitoring_list_destinations(self) -> Any:
        """
        List Logging Destinations

        Returns:
            Any: The response is a JSON object with a `destinations` key.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/sinks/destinations"
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

    def monitoring_get_destination(self, destination_uuid: str) -> Any:
        """
        Get Logging Destination

        Args:
            destination_uuid (string): destination_uuid

        Returns:
            Any: The response is a JSON object with a `destination` key.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        if destination_uuid is None:
            raise ValueError("Missing required parameter 'destination_uuid'.")
        url = f"{self.base_url}/v2/monitoring/sinks/destinations/{destination_uuid}"
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

    def monitoring_update_destination(
        self,
        destination_uuid: str,
        type: Any,
        config: dict[str, Any],
        name: str | None = None,
    ) -> Any:
        """
        Update Logging Destination

        Args:
            destination_uuid (string): destination_uuid
            type (string): The destination type. `opensearch_dbaas` for a DigitalOcean managed OpenSearch
        cluster or `opensearch_ext` for an externally managed one.

            config (object): config
            name (string): destination name Example: 'managed_opensearch_cluster'.

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        if destination_uuid is None:
            raise ValueError("Missing required parameter 'destination_uuid'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "type": type,
            "config": config,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/monitoring/sinks/destinations/{destination_uuid}"
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

    def monitoring_delete_destination(self, destination_uuid: str) -> Any:
        """
        Delete Logging Destination

        Args:
            destination_uuid (string): destination_uuid

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        if destination_uuid is None:
            raise ValueError("Missing required parameter 'destination_uuid'.")
        url = f"{self.base_url}/v2/monitoring/sinks/destinations/{destination_uuid}"
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

    def monitoring_create_sink(
        self,
        destination_uuid: str | None = None,
        resources: list[dict[str, Any]] | None = None,
    ) -> Any:
        """
        Create Sink

        Args:
            destination_uuid (string): A unique identifier for an already-existing destination. Example: '9df2b7e9-3fb2-4577-b60a-e9c0d53f9a99'.
            resources (array): List of resources identified by their URNs.

        Returns:
            Any: This does not indicate the success or failure of any operation, just that the request has been accepted for processing.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        request_body_data = None
        request_body_data = {
            "destination_uuid": destination_uuid,
            "resources": resources,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/monitoring/sinks"
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

    def monitoring_list_sinks(self, resource_id: str | None = None) -> Any:
        """
        Lists all sinks

        Args:
            resource_id (string): A unique URN for a resource. Example: 'do:kubernetes:5ba4518b-b9e2-4978-aa92-2d4c727e8824'.

        Returns:
            Any: The response is a JSON object with a `sinks` key.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        url = f"{self.base_url}/v2/monitoring/sinks"
        query_params = {
            k: v for k, v in [("resource_id", resource_id)] if v is not None
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

    def monitoring_get_sink(self, sink_uuid: str) -> Any:
        """
        Get Sink

        Args:
            sink_uuid (string): sink_uuid

        Returns:
            Any: The response is a JSON object with a `sink` key.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        if sink_uuid is None:
            raise ValueError("Missing required parameter 'sink_uuid'.")
        url = f"{self.base_url}/v2/monitoring/sinks/{sink_uuid}"
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

    def monitoring_delete_sink(self, sink_uuid: str) -> Any:
        """
        Delete Sink

        Args:
            sink_uuid (string): sink_uuid

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Monitoring
        """
        if sink_uuid is None:
            raise ValueError("Missing required parameter 'sink_uuid'.")
        url = f"{self.base_url}/v2/monitoring/sinks/{sink_uuid}"
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

    def partner_attachments_list(
        self, per_page: int | None = None, page: int | None = None
    ) -> Any:
        """
        List all partner attachments

        Args:
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: The response will be a JSON object with a `partner_attachments` key
        that contains an array of all partner attachments

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Partner Network Connect
        """
        url = f"{self.base_url}/v2/partner_network_connect/attachments"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def partner_attachments_create(
        self,
        name: str | None = None,
        connection_bandwidth_in_mbps: int | None = None,
        region: str | None = None,
        naas_provider: str | None = None,
        vpc_ids: list[str] | None = None,
        parent_uuid: str | None = None,
        bgp: dict[str, Any] | None = None,
    ) -> Any:
        """
        Create a new partner attachment

        Args:
            name (string): The name of the partner attachment. Must be unique and may only contain alphanumeric characters, dashes, and periods. Example: 'env.prod-partner-network-connect'.
            connection_bandwidth_in_mbps (integer): Bandwidth (in Mbps) of the connection. Example: '1000'.
            region (string): region Example: 'nyc'.
            naas_provider (string): naas_provider Example: 'megaport'.
            vpc_ids (array): An array of VPCs IDs. Example: "['c140286f-e6ce-4131-8b7b-df4590ce8d6a', '994a2735-dc84-11e8-80bc-3cfdfea9fba1']".
            parent_uuid (string): Optional associated partner attachment UUID Example: 'd594cf8d-8c79-4bc5-aec1-6f9b211506b3'.
            bgp (object): Optional BGP configurations

        Returns:
            Any: The response will be a JSON object with details about the partner attachment
        including attached VPC network IDs and BGP configuration information

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Partner Network Connect
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "connection_bandwidth_in_mbps": connection_bandwidth_in_mbps,
            "region": region,
            "naas_provider": naas_provider,
            "vpc_ids": vpc_ids,
            "parent_uuid": parent_uuid,
            "bgp": bgp,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/partner_network_connect/attachments"
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

    def partner_attachments_get(self, pa_id: str) -> Any:
        """
        Retrieve an existing partner attachment

        Args:
            pa_id (string): pa_id

        Returns:
            Any: The response will be a JSON object with details about the partner attachment
        including attached VPC network IDs and BGP configuration information

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Partner Network Connect
        """
        if pa_id is None:
            raise ValueError("Missing required parameter 'pa_id'.")
        url = f"{self.base_url}/v2/partner_network_connect/attachments/{pa_id}"
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

    def partner_attachments_patch(
        self,
        pa_id: str,
        name: str | None = None,
        vpc_ids: list[str] | None = None,
        bgp: dict[str, Any] | None = None,
    ) -> Any:
        """
        Update an existing partner attachment

        Args:
            pa_id (string): pa_id
            name (string): The name of the partner attachment. Must be unique and may only contain alphanumeric characters, dashes, and periods. Example: 'env.prod-partner-network-connect'.
            vpc_ids (array): An array of VPCs IDs. Example: "['c140286f-e6ce-4131-8b7b-df4590ce8d6a', '994a2735-dc84-11e8-80bc-3cfdfea9fba1']".
            bgp (object): BGP configurations

        Returns:
            Any: The response will be a JSON object with details about the partner attachment
        including attached VPC network IDs and BGP configuration information

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Partner Network Connect
        """
        if pa_id is None:
            raise ValueError("Missing required parameter 'pa_id'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "vpc_ids": vpc_ids,
            "bgp": bgp,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/partner_network_connect/attachments/{pa_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def partner_attachments_delete(self, pa_id: str) -> Any:
        """
        Delete an existing partner attachment

        Args:
            pa_id (string): pa_id

        Returns:
            Any: The response will be a JSON object with details about the partner attachment
        and `"state": "DELETING"` to indicate that the partner attachment is being deleted.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Partner Network Connect
        """
        if pa_id is None:
            raise ValueError("Missing required parameter 'pa_id'.")
        url = f"{self.base_url}/v2/partner_network_connect/attachments/{pa_id}"
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

    def get_bgp_auth_key_by_pa_id(self, pa_id: str) -> Any:
        """
        Get current BGP auth key for the partner attachment

        Args:
            pa_id (string): pa_id

        Returns:
            Any: The response will be a JSON object with a `bgp_auth_key` object containing a
        `value` field with the BGP auth key value

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Partner Network Connect
        """
        if pa_id is None:
            raise ValueError("Missing required parameter 'pa_id'.")
        url = f"{self.base_url}/v2/partner_network_connect/attachments/{pa_id}/bgp_auth_key"
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

    def get_partner_network_remote_routes(
        self, pa_id: str, per_page: int | None = None, page: int | None = None
    ) -> Any:
        """
        List remote routes for a partner attachment

        Args:
            pa_id (string): pa_id
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: The response will be a JSON object with a `remote_routes` array containing
        information on all the remote routes associated with the partner attachment

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Partner Network Connect
        """
        if pa_id is None:
            raise ValueError("Missing required parameter 'pa_id'.")
        url = f"{self.base_url}/v2/partner_network_connect/attachments/{pa_id}/remote_routes"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def update_remote_routes(
        self, pa_id: str, remote_routes: list[dict[str, Any]] | None = None
    ) -> Any:
        """
        Set remote routes for a partner attachment

        Args:
            pa_id (string): pa_id
            remote_routes (array): remote_routes Example: [{'cidr': '10.10.10.0/24'}, {'cidr': '10.10.10.10/24'}].

        Returns:
            Any: The response will be a JSON object with a `remote_routes` array containing
        information on all the remote routes associated with the partner attachment

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Partner Network Connect
        """
        if pa_id is None:
            raise ValueError("Missing required parameter 'pa_id'.")
        request_body_data = None
        request_body_data = {
            "remote_routes": remote_routes,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/partner_network_connect/attachments/{pa_id}/remote_routes"
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

    def get_partner_service_key(self, pa_id: str) -> Any:
        """
        Get the current service key for the partner attachment

        Args:
            pa_id (string): pa_id

        Returns:
            Any: The response will be a JSON object with a `service_key` object containing
        the service key value and creation information

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Partner Network Connect
        """
        if pa_id is None:
            raise ValueError("Missing required parameter 'pa_id'.")
        url = f"{self.base_url}/v2/partner_network_connect/attachments/{pa_id}/service_key"
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

    def create_service_key(self, pa_id: str) -> Any:
        """
        Regenerate the service key for the partner attachment

        Args:
            pa_id (string): pa_id

        Returns:
            Any: The response will be a JSON object with a `service_key` object containing
        the service key value and creation information

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Partner Network Connect
        """
        if pa_id is None:
            raise ValueError("Missing required parameter 'pa_id'.")
        request_body_data = None
        url = f"{self.base_url}/v2/partner_network_connect/attachments/{pa_id}/service_key"
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

    def projects_list(
        self, per_page: int | None = None, page: int | None = None
    ) -> Any:
        """
        List All Projects

        Args:
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: The response will be a JSON object with a key called `projects`. The value of this will be an object with the standard project attributes

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Projects, important
        """
        url = f"{self.base_url}/v2/projects"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def projects_create(
        self,
        name: str,
        purpose: str,
        id: str | None = None,
        owner_uuid: str | None = None,
        owner_id: int | None = None,
        description: str | None = None,
        environment: str | None = None,
        created_at: str | None = None,
        updated_at: str | None = None,
    ) -> Any:
        """
        Create a Project

        Args:
            name (string): The human-readable name for the project. The maximum length is 175 characters and the name must be unique. Example: 'my-web-api'.
            purpose (string): The purpose of the project. The maximum length is 255 characters. It can
        have one of the following values:

        - Just trying out DigitalOcean
        - Class project / Educational purposes
        - Website or blog
        - Web Application
        - Service or API
        - Mobile Application
        - Machine learning / AI / Data processing
        - IoT
        - Operational / Developer tooling

        If another value for purpose is specified, for example, "your custom purpose",
        your purpose will be stored as `Other: your custom purpose`.
         Example: 'Service or API'.
            id (string): The unique universal identifier of this project. Example: '4e1bfbc3-dc3e-41f2-a18f-1b4d7ba71679'.
            owner_uuid (string): The unique universal identifier of the project owner. Example: '99525febec065ca37b2ffe4f852fd2b2581895e7'.
            owner_id (integer): The integer id of the project owner. Example: '258992'.
            description (string): The description of the project. The maximum length is 255 characters. Example: 'My website API'.
            environment (string): The environment of the project's resources. Example: 'Production'.
            created_at (string): A time value given in ISO8601 combined date and time format that represents when the project was created. Example: '2018-09-27T20:10:35Z'.
            updated_at (string): A time value given in ISO8601 combined date and time format that represents when the project was updated. Example: '2018-09-27T20:10:35Z'.

        Returns:
            Any: The response will be a JSON object with a key called `project`. The value of this will be an object with the standard project attributes

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Projects, important
        """
        request_body_data = None
        request_body_data = {
            "id": id,
            "owner_uuid": owner_uuid,
            "owner_id": owner_id,
            "name": name,
            "description": description,
            "purpose": purpose,
            "environment": environment,
            "created_at": created_at,
            "updated_at": updated_at,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/projects"
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

    def projects_get_default(self) -> Any:
        """
        Retrieve the Default Project

        Returns:
            Any: The response will be a JSON object with a key called `project`. The value of this will be an object with the standard project attributes

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Projects
        """
        url = f"{self.base_url}/v2/projects/default"
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

    def projects_update_default(
        self,
        name: str,
        description: str,
        purpose: str,
        environment: str,
        is_default: bool,
        id: str | None = None,
        owner_uuid: str | None = None,
        owner_id: int | None = None,
        created_at: str | None = None,
        updated_at: str | None = None,
    ) -> Any:
        """
        Update the Default Project

        Args:
            name (string): The human-readable name for the project. The maximum length is 175 characters and the name must be unique. Example: 'my-web-api'.
            description (string): The description of the project. The maximum length is 255 characters. Example: 'My website API'.
            purpose (string): The purpose of the project. The maximum length is 255 characters. It can
        have one of the following values:

        - Just trying out DigitalOcean
        - Class project / Educational purposes
        - Website or blog
        - Web Application
        - Service or API
        - Mobile Application
        - Machine learning / AI / Data processing
        - IoT
        - Operational / Developer tooling

        If another value for purpose is specified, for example, "your custom purpose",
        your purpose will be stored as `Other: your custom purpose`.
         Example: 'Service or API'.
            environment (string): The environment of the project's resources. Example: 'Production'.
            is_default (boolean): If true, all resources will be added to this project if no project is specified. Example: 'False'.
            id (string): The unique universal identifier of this project. Example: '4e1bfbc3-dc3e-41f2-a18f-1b4d7ba71679'.
            owner_uuid (string): The unique universal identifier of the project owner. Example: '99525febec065ca37b2ffe4f852fd2b2581895e7'.
            owner_id (integer): The integer id of the project owner. Example: '258992'.
            created_at (string): A time value given in ISO8601 combined date and time format that represents when the project was created. Example: '2018-09-27T20:10:35Z'.
            updated_at (string): A time value given in ISO8601 combined date and time format that represents when the project was updated. Example: '2018-09-27T20:10:35Z'.

        Returns:
            Any: The response will be a JSON object with a key called `project`. The value of this will be an object with the standard project attributes

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Projects
        """
        request_body_data = None
        request_body_data = {
            "id": id,
            "owner_uuid": owner_uuid,
            "owner_id": owner_id,
            "name": name,
            "description": description,
            "purpose": purpose,
            "environment": environment,
            "created_at": created_at,
            "updated_at": updated_at,
            "is_default": is_default,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/projects/default"
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

    def projects_patch_default(
        self,
        id: str | None = None,
        owner_uuid: str | None = None,
        owner_id: int | None = None,
        name: str | None = None,
        description: str | None = None,
        purpose: str | None = None,
        environment: str | None = None,
        created_at: str | None = None,
        updated_at: str | None = None,
        is_default: bool | None = None,
    ) -> Any:
        """
        Patch the Default Project

        Args:
            id (string): The unique universal identifier of this project. Example: '4e1bfbc3-dc3e-41f2-a18f-1b4d7ba71679'.
            owner_uuid (string): The unique universal identifier of the project owner. Example: '99525febec065ca37b2ffe4f852fd2b2581895e7'.
            owner_id (integer): The integer id of the project owner. Example: '258992'.
            name (string): The human-readable name for the project. The maximum length is 175 characters and the name must be unique. Example: 'my-web-api'.
            description (string): The description of the project. The maximum length is 255 characters. Example: 'My website API'.
            purpose (string): The purpose of the project. The maximum length is 255 characters. It can
        have one of the following values:

        - Just trying out DigitalOcean
        - Class project / Educational purposes
        - Website or blog
        - Web Application
        - Service or API
        - Mobile Application
        - Machine learning / AI / Data processing
        - IoT
        - Operational / Developer tooling

        If another value for purpose is specified, for example, "your custom purpose",
        your purpose will be stored as `Other: your custom purpose`.
         Example: 'Service or API'.
            environment (string): The environment of the project's resources. Example: 'Production'.
            created_at (string): A time value given in ISO8601 combined date and time format that represents when the project was created. Example: '2018-09-27T20:10:35Z'.
            updated_at (string): A time value given in ISO8601 combined date and time format that represents when the project was updated. Example: '2018-09-27T20:10:35Z'.
            is_default (boolean): If true, all resources will be added to this project if no project is specified. Example: 'False'.

        Returns:
            Any: The response will be a JSON object with a key called `project`. The value of this will be an object with the standard project attributes

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Projects
        """
        request_body_data = None
        request_body_data = {
            "id": id,
            "owner_uuid": owner_uuid,
            "owner_id": owner_id,
            "name": name,
            "description": description,
            "purpose": purpose,
            "environment": environment,
            "created_at": created_at,
            "updated_at": updated_at,
            "is_default": is_default,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/projects/default"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def projects_get(self, project_id: str) -> Any:
        """
        Retrieve an Existing Project

        Args:
            project_id (string): project_id

        Returns:
            Any: The response will be a JSON object with a key called `project`. The value of this will be an object with the standard project attributes

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Projects
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'.")
        url = f"{self.base_url}/v2/projects/{project_id}"
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

    def projects_update(
        self,
        project_id: str,
        name: str,
        description: str,
        purpose: str,
        environment: str,
        is_default: bool,
        id: str | None = None,
        owner_uuid: str | None = None,
        owner_id: int | None = None,
        created_at: str | None = None,
        updated_at: str | None = None,
    ) -> Any:
        """
        Update a Project

        Args:
            project_id (string): project_id
            name (string): The human-readable name for the project. The maximum length is 175 characters and the name must be unique. Example: 'my-web-api'.
            description (string): The description of the project. The maximum length is 255 characters. Example: 'My website API'.
            purpose (string): The purpose of the project. The maximum length is 255 characters. It can
        have one of the following values:

        - Just trying out DigitalOcean
        - Class project / Educational purposes
        - Website or blog
        - Web Application
        - Service or API
        - Mobile Application
        - Machine learning / AI / Data processing
        - IoT
        - Operational / Developer tooling

        If another value for purpose is specified, for example, "your custom purpose",
        your purpose will be stored as `Other: your custom purpose`.
         Example: 'Service or API'.
            environment (string): The environment of the project's resources. Example: 'Production'.
            is_default (boolean): If true, all resources will be added to this project if no project is specified. Example: 'False'.
            id (string): The unique universal identifier of this project. Example: '4e1bfbc3-dc3e-41f2-a18f-1b4d7ba71679'.
            owner_uuid (string): The unique universal identifier of the project owner. Example: '99525febec065ca37b2ffe4f852fd2b2581895e7'.
            owner_id (integer): The integer id of the project owner. Example: '258992'.
            created_at (string): A time value given in ISO8601 combined date and time format that represents when the project was created. Example: '2018-09-27T20:10:35Z'.
            updated_at (string): A time value given in ISO8601 combined date and time format that represents when the project was updated. Example: '2018-09-27T20:10:35Z'.

        Returns:
            Any: The response will be a JSON object with a key called `project`. The value of this will be an object with the standard project attributes

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Projects
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "owner_uuid": owner_uuid,
            "owner_id": owner_id,
            "name": name,
            "description": description,
            "purpose": purpose,
            "environment": environment,
            "created_at": created_at,
            "updated_at": updated_at,
            "is_default": is_default,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/projects/{project_id}"
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

    def projects_patch(
        self,
        project_id: str,
        id: str | None = None,
        owner_uuid: str | None = None,
        owner_id: int | None = None,
        name: str | None = None,
        description: str | None = None,
        purpose: str | None = None,
        environment: str | None = None,
        created_at: str | None = None,
        updated_at: str | None = None,
        is_default: bool | None = None,
    ) -> Any:
        """
        Patch a Project

        Args:
            project_id (string): project_id
            id (string): The unique universal identifier of this project. Example: '4e1bfbc3-dc3e-41f2-a18f-1b4d7ba71679'.
            owner_uuid (string): The unique universal identifier of the project owner. Example: '99525febec065ca37b2ffe4f852fd2b2581895e7'.
            owner_id (integer): The integer id of the project owner. Example: '258992'.
            name (string): The human-readable name for the project. The maximum length is 175 characters and the name must be unique. Example: 'my-web-api'.
            description (string): The description of the project. The maximum length is 255 characters. Example: 'My website API'.
            purpose (string): The purpose of the project. The maximum length is 255 characters. It can
        have one of the following values:

        - Just trying out DigitalOcean
        - Class project / Educational purposes
        - Website or blog
        - Web Application
        - Service or API
        - Mobile Application
        - Machine learning / AI / Data processing
        - IoT
        - Operational / Developer tooling

        If another value for purpose is specified, for example, "your custom purpose",
        your purpose will be stored as `Other: your custom purpose`.
         Example: 'Service or API'.
            environment (string): The environment of the project's resources. Example: 'Production'.
            created_at (string): A time value given in ISO8601 combined date and time format that represents when the project was created. Example: '2018-09-27T20:10:35Z'.
            updated_at (string): A time value given in ISO8601 combined date and time format that represents when the project was updated. Example: '2018-09-27T20:10:35Z'.
            is_default (boolean): If true, all resources will be added to this project if no project is specified. Example: 'False'.

        Returns:
            Any: The response will be a JSON object with a key called `project`. The value of this will be an object with the standard project attributes

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Projects
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "owner_uuid": owner_uuid,
            "owner_id": owner_id,
            "name": name,
            "description": description,
            "purpose": purpose,
            "environment": environment,
            "created_at": created_at,
            "updated_at": updated_at,
            "is_default": is_default,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/projects/{project_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def projects_delete(self, project_id: str) -> Any:
        """
        Delete an Existing Project

        Args:
            project_id (string): project_id

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Projects
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'.")
        url = f"{self.base_url}/v2/projects/{project_id}"
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

    def projects_list_resources(
        self,
        project_id: str,
        per_page: int | None = None,
        page: int | None = None,
    ) -> Any:
        """
        List Project Resources

        Args:
            project_id (string): project_id
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: The response will be a JSON object with a key called `resources`. The value of this will be an object with the standard resource attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Project Resources
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'.")
        url = f"{self.base_url}/v2/projects/{project_id}/resources"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def projects_assign_resources(
        self, project_id: str, resources: list[str] | None = None
    ) -> dict[str, Any]:
        """
        Assign Resources to a Project

        Args:
            project_id (string): project_id
            resources (array): A list of uniform resource names (URNs) to be added to a project. Example: "['do:droplet:13457723']".

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `resources`. The value of this will be an object with the standard resource attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Project Resources
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'.")
        request_body_data = None
        request_body_data = {
            "resources": resources,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/projects/{project_id}/resources"
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

    def list_project_resources(self) -> Any:
        """
        List Default Project Resources

        Returns:
            Any: The response will be a JSON object with a key called `resources`. The value of this will be an object with the standard resource attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Project Resources
        """
        url = f"{self.base_url}/v2/projects/default/resources"
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

    def create_default_project_resource(
        self, resources: list[str] | None = None
    ) -> dict[str, Any]:
        """
        Assign Resources to Default Project

        Args:
            resources (array): A list of uniform resource names (URNs) to be added to a project. Example: "['do:droplet:13457723']".

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `resources`. The value of this will be an object with the standard resource attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Project Resources
        """
        request_body_data = None
        request_body_data = {
            "resources": resources,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/projects/default/resources"
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

    def regions_list(self, per_page: int | None = None, page: int | None = None) -> Any:
        """
        List All Data Center Regions

        Args:
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: A JSON object with a key set to `regions`. The value is an array of `region` objects, each of which contain the standard `region` attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Regions
        """
        url = f"{self.base_url}/v2/regions"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def registry_get(self) -> Any:
        """
        Get Container Registry Information

        Returns:
            Any: The response will be a JSON object with the key `registry` containing information about your registry.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Container Registry
        """
        url = f"{self.base_url}/v2/registry"
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

    def registry_create(
        self, name: str, subscription_tier_slug: str, region: str | None = None
    ) -> Any:
        """
        Create Container Registry

        Args:
            name (string): A globally unique name for the container registry. Must be lowercase and be composed only of numbers, letters and `-`, up to a limit of 63 characters. Example: 'example'.
            subscription_tier_slug (string): The slug of the subscription tier to sign up for. Valid values can be retrieved using the options endpoint. Example: 'basic'.
            region (string): Slug of the region where registry data is stored. When not provided, a region will be selected. Example: 'fra1'.

        Returns:
            Any: The response will be a JSON object with the key `registry` containing information about your registry.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Container Registry
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "subscription_tier_slug": subscription_tier_slug,
            "region": region,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/registry"
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

    def registry_delete(self) -> Any:
        """
        Delete Container Registry

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Container Registry
        """
        url = f"{self.base_url}/v2/registry"
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

    def registry_get_subscription(self) -> Any:
        """
        Get Subscription Information

        Returns:
            Any: The response will be a JSON object with a key called `subscription` containing information about your subscription.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Container Registry
        """
        url = f"{self.base_url}/v2/registry/subscription"
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

    def registry_update_subscription(self, tier_slug: str | None = None) -> Any:
        """
        Update Subscription Tier

        Args:
            tier_slug (string): The slug of the subscription tier to sign up for. Example: 'basic'.

        Returns:
            Any: The response will be a JSON object with a key called `subscription` containing information about your subscription.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Container Registry
        """
        request_body_data = None
        request_body_data = {
            "tier_slug": tier_slug,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/registry/subscription"
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

    def registry_get_docker_credentials(
        self, expiry_seconds: int | None = None, read_write: bool | None = None
    ) -> dict[str, Any]:
        """
        Get Docker Credentials for Container Registry

        Args:
            expiry_seconds (integer): The duration in seconds that the returned registry credentials will be valid. If not set or 0, the credentials will not expire. Example: '3600'.
            read_write (boolean): By default, the registry credentials allow for read-only access. Set this query parameter to `true` to obtain read-write credentials. Example: 'True'.

        Returns:
            dict[str, Any]: A Docker `config.json` file for the container registry.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Container Registry
        """
        url = f"{self.base_url}/v2/registry/docker-credentials"
        query_params = {
            k: v
            for k, v in [("expiry_seconds", expiry_seconds), ("read_write", read_write)]
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

    def registry_validate_name(self, name: str) -> Any:
        """
        Validate a Container Registry Name

        Args:
            name (string): A globally unique name for the container registry. Must be lowercase and be composed only of numbers, letters and `-`, up to a limit of 63 characters. Example: 'example'.

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Container Registry
        """
        request_body_data = None
        request_body_data = {
            "name": name,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/registry/validate-name"
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

    def registry_list_repositories(
        self,
        registry_name: str,
        per_page: int | None = None,
        page: int | None = None,
    ) -> Any:
        """
        List All Container Registry Repositories

        Args:
            registry_name (string): registry_name
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: The response body will be a JSON object with a key of `repositories`. This will be set to an array containing objects each representing a repository.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Container Registry
        """
        if registry_name is None:
            raise ValueError("Missing required parameter 'registry_name'.")
        url = f"{self.base_url}/v2/registry/{registry_name}/repositories"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def registry_list_repositories_v(
        self,
        registry_name: str,
        per_page: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
    ) -> Any:
        """
        List All Container Registry Repositories (V2)

        Args:
            registry_name (string): registry_name
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Ignored when 'page_token' is provided. Example: '1'.
            page_token (string): Token to retrieve of the next or previous set of results more quickly than using 'page'. Example: 'eyJUb2tlbiI6IkNnZGpiMjlz'.

        Returns:
            Any: The response body will be a JSON object with a key of `repositories`. This will be set to an array containing objects each representing a repository.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Container Registry
        """
        if registry_name is None:
            raise ValueError("Missing required parameter 'registry_name'.")
        url = f"{self.base_url}/v2/registry/{registry_name}/repositoriesV2"
        query_params = {
            k: v
            for k, v in [
                ("per_page", per_page),
                ("page", page),
                ("page_token", page_token),
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

    def registry_list_repository_tags(
        self,
        registry_name: str,
        repository_name: str,
        per_page: int | None = None,
        page: int | None = None,
    ) -> Any:
        """
        List All Container Registry Repository Tags

        Args:
            registry_name (string): registry_name
            repository_name (string): repository_name
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: The response body will be a JSON object with a key of `tags`. This will be set to an array containing objects each representing a tag.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Container Registry
        """
        if registry_name is None:
            raise ValueError("Missing required parameter 'registry_name'.")
        if repository_name is None:
            raise ValueError("Missing required parameter 'repository_name'.")
        url = f"{self.base_url}/v2/registry/{registry_name}/repositories/{repository_name}/tags"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def registry_delete_repository_tag(
        self, registry_name: str, repository_name: str, repository_tag: str
    ) -> Any:
        """
        Delete Container Registry Repository Tag

        Args:
            registry_name (string): registry_name
            repository_name (string): repository_name
            repository_tag (string): repository_tag

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Container Registry
        """
        if registry_name is None:
            raise ValueError("Missing required parameter 'registry_name'.")
        if repository_name is None:
            raise ValueError("Missing required parameter 'repository_name'.")
        if repository_tag is None:
            raise ValueError("Missing required parameter 'repository_tag'.")
        url = f"{self.base_url}/v2/registry/{registry_name}/repositories/{repository_name}/tags/{repository_tag}"
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

    def get_repository_digests(
        self,
        registry_name: str,
        repository_name: str,
        per_page: int | None = None,
        page: int | None = None,
    ) -> Any:
        """
        List All Container Registry Repository Manifests

        Args:
            registry_name (string): registry_name
            repository_name (string): repository_name
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: The response body will be a JSON object with a key of `manifests`. This will be set to an array containing objects each representing a manifest.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Container Registry
        """
        if registry_name is None:
            raise ValueError("Missing required parameter 'registry_name'.")
        if repository_name is None:
            raise ValueError("Missing required parameter 'repository_name'.")
        url = f"{self.base_url}/v2/registry/{registry_name}/repositories/{repository_name}/digests"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def delete_manifest_digest(
        self, registry_name: str, repository_name: str, manifest_digest: str
    ) -> Any:
        """
        Delete Container Registry Repository Manifest

        Args:
            registry_name (string): registry_name
            repository_name (string): repository_name
            manifest_digest (string): manifest_digest

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Container Registry
        """
        if registry_name is None:
            raise ValueError("Missing required parameter 'registry_name'.")
        if repository_name is None:
            raise ValueError("Missing required parameter 'repository_name'.")
        if manifest_digest is None:
            raise ValueError("Missing required parameter 'manifest_digest'.")
        url = f"{self.base_url}/v2/registry/{registry_name}/repositories/{repository_name}/digests/{manifest_digest}"
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

    def registry_run_garbage_collection(
        self, registry_name: str, type: str | None = None
    ) -> dict[str, Any]:
        """
        Start Garbage Collection

        Args:
            registry_name (string): registry_name
            type (string): Type of the garbage collection to run against this registry Example: 'unreferenced blobs only'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key of `garbage_collection`. This will be a json object with attributes representing the currently-active garbage collection.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Container Registry
        """
        if registry_name is None:
            raise ValueError("Missing required parameter 'registry_name'.")
        request_body_data = None
        request_body_data = {
            "type": type,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/registry/{registry_name}/garbage-collection"
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

    def registry_get_garbage_collection(self, registry_name: str) -> dict[str, Any]:
        """
        Get Active Garbage Collection

        Args:
            registry_name (string): registry_name

        Returns:
            dict[str, Any]: The response will be a JSON object with a key of `garbage_collection`. This will be a json object with attributes representing the currently-active garbage collection.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Container Registry
        """
        if registry_name is None:
            raise ValueError("Missing required parameter 'registry_name'.")
        url = f"{self.base_url}/v2/registry/{registry_name}/garbage-collection"
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

    def list_registry_garbage_collections(
        self,
        registry_name: str,
        per_page: int | None = None,
        page: int | None = None,
    ) -> dict[str, Any]:
        """
        List Garbage Collections

        Args:
            registry_name (string): registry_name
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key of `garbage_collections`. This will be set to an array containing objects representing each past garbage collection. Each will contain the standard Garbage Collection attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Container Registry
        """
        if registry_name is None:
            raise ValueError("Missing required parameter 'registry_name'.")
        url = f"{self.base_url}/v2/registry/{registry_name}/garbage-collections"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def update_garbage_collection(
        self,
        registry_name: str,
        garbage_collection_uuid: str,
        cancel: bool | None = None,
    ) -> dict[str, Any]:
        """
        Update Garbage Collection

        Args:
            registry_name (string): registry_name
            garbage_collection_uuid (string): garbage_collection_uuid
            cancel (boolean): A boolean value indicating that the garbage collection should be cancelled. Example: 'True'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key of `garbage_collection`. This will be a json object with attributes representing the currently-active garbage collection.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Container Registry
        """
        if registry_name is None:
            raise ValueError("Missing required parameter 'registry_name'.")
        if garbage_collection_uuid is None:
            raise ValueError("Missing required parameter 'garbage_collection_uuid'.")
        request_body_data = None
        request_body_data = {
            "cancel": cancel,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/registry/{registry_name}/garbage-collection/{garbage_collection_uuid}"
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

    def registry_get_options(self) -> dict[str, Any]:
        """
        List Registry Options (Subscription Tiers and Available Regions)

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `options` which contains a key called `subscription_tiers` listing the available tiers.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Container Registry
        """
        url = f"{self.base_url}/v2/registry/options"
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

    def droplets_list_neighbors_ids(self) -> dict[str, Any]:
        """
        List All Droplet Neighbors

        Returns:
            dict[str, Any]: A JSON object with an `neighbor_ids` key.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Droplets
        """
        url = f"{self.base_url}/v2/reports/droplet_neighbors_ids"
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

    def reserved_ips_list(
        self, per_page: int | None = None, page: int | None = None
    ) -> Any:
        """
        List All Reserved IPs

        Args:
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: The response will be a JSON object with a key called `reserved_ips`. This will be set to an array of reserved IP objects, each of which will contain the standard reserved IP attributes

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Reserved IPs
        """
        url = f"{self.base_url}/v2/reserved_ips"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def reserved_ips_create(
        self,
        droplet_id: int | None = None,
        region: str | None = None,
        project_id: str | None = None,
    ) -> dict[str, Any]:
        """
        Create a New Reserved IP

        Args:
            droplet_id (integer): The ID of the Droplet that the reserved IP will be assigned to. Example: '2457247'.
            region (string): The slug identifier for the region the reserved IP will be reserved to. Example: 'nyc3'.
            project_id (string): The UUID of the project to which the reserved IP will be assigned. Example: '746c6152-2fa2-11ed-92d3-27aaa54e4988'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `reserved_ip`. The value of this will be an object that contains the standard attributes associated with a reserved IP.
        When assigning a reserved IP to a Droplet at same time as it created, the response's `links` object will contain links to both the Droplet and the assignment action. The latter can be used to check the status of the action.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Reserved IPs
        """
        request_body_data = None
        request_body_data = {
            "droplet_id": droplet_id,
            "region": region,
            "project_id": project_id,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/reserved_ips"
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

    def reserved_ips_get(self, reserved_ip: str) -> dict[str, Any]:
        """
        Retrieve an Existing Reserved IP

        Args:
            reserved_ip (string): reserved_ip

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `reserved_ip`. The value of this will be an object that contains the standard attributes associated with a reserved IP.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Reserved IPs
        """
        if reserved_ip is None:
            raise ValueError("Missing required parameter 'reserved_ip'.")
        url = f"{self.base_url}/v2/reserved_ips/{reserved_ip}"
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

    def reserved_ips_delete(self, reserved_ip: str) -> Any:
        """
        Delete a Reserved IP

        Args:
            reserved_ip (string): reserved_ip

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Reserved IPs
        """
        if reserved_ip is None:
            raise ValueError("Missing required parameter 'reserved_ip'.")
        url = f"{self.base_url}/v2/reserved_ips/{reserved_ip}"
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

    def reserved_ips_actions_list(self, reserved_ip: str) -> Any:
        """
        List All Actions for a Reserved IP

        Args:
            reserved_ip (string): reserved_ip

        Returns:
            Any: The results will be returned as a JSON object with an `actions` key. This will be set to an array filled with action objects containing the standard reserved IP action attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Reserved IP Actions
        """
        if reserved_ip is None:
            raise ValueError("Missing required parameter 'reserved_ip'.")
        url = f"{self.base_url}/v2/reserved_ips/{reserved_ip}/actions"
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

    def reserved_ips_actions_post(
        self,
        reserved_ip: str,
        type: str | None = None,
        droplet_id: int | None = None,
    ) -> Any:
        """
        Initiate a Reserved IP Action

        Args:
            reserved_ip (string): reserved_ip
            type (string): The type of action to initiate for the reserved IP.
            droplet_id (integer): The ID of the Droplet that the reserved IP will be assigned to. Example: '758604968'.

        Returns:
            Any: The response will be an object with a key called `action`. The value of this will be an object that contains the standard reserved IP action attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Reserved IP Actions
        """
        if reserved_ip is None:
            raise ValueError("Missing required parameter 'reserved_ip'.")
        request_body_data = None
        request_body_data = {
            "type": type,
            "droplet_id": droplet_id,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/reserved_ips/{reserved_ip}/actions"
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

    def reserved_ips_actions_get(self, reserved_ip: str, action_id: str) -> Any:
        """
        Retrieve an Existing Reserved IP Action

        Args:
            reserved_ip (string): reserved_ip
            action_id (string): action_id

        Returns:
            Any: The response will be an object with a key called `action`. The value of this will be an object that contains the standard reserved IP action attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Reserved IP Actions
        """
        if reserved_ip is None:
            raise ValueError("Missing required parameter 'reserved_ip'.")
        if action_id is None:
            raise ValueError("Missing required parameter 'action_id'.")
        url = f"{self.base_url}/v2/reserved_ips/{reserved_ip}/actions/{action_id}"
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

    def reserved_ipv_list(
        self, per_page: int | None = None, page: int | None = None
    ) -> Any:
        """
        [Public Preview] List All Reserved IPv6s

        Args:
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: The response will be a JSON object with a key called `reserved_ipv6s`. This will be set to an array of reserved IP objects, each of which will contain the standard reserved IP attributes

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            [Public Preview] Reserved IPv6
        """
        url = f"{self.base_url}/v2/reserved_ipv6"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def reserved_ipv_create(self, region_slug: str) -> Any:
        """
        [Public Preview] Create a New Reserved IPv6

        Args:
            region_slug (string): The slug identifier for the region the reserved IPv6 will be reserved to. Example: 'nyc3'.

        Returns:
            Any: The response will be a JSON object with key `reserved_ipv6`. The value of this will be an object that contains the standard attributes associated with a reserved IPv6.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            [Public Preview] Reserved IPv6
        """
        request_body_data = None
        request_body_data = {
            "region_slug": region_slug,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/reserved_ipv6"
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

    def reserved_ipv_get(self, reserved_ipv6: str) -> dict[str, Any]:
        """
        [Public Preview] Retrieve an Existing Reserved IPv6

        Args:
            reserved_ipv6 (string): reserved_ipv6

        Returns:
            dict[str, Any]: The response will be a JSON object with key `reserved_ipv6`. The value of this will be an object that contains the standard attributes associated with a reserved IPv6.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            [Public Preview] Reserved IPv6
        """
        if reserved_ipv6 is None:
            raise ValueError("Missing required parameter 'reserved_ipv6'.")
        url = f"{self.base_url}/v2/reserved_ipv6/{reserved_ipv6}"
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

    def reserved_ipv_delete(self, reserved_ipv6: str) -> Any:
        """
        [Public Preview] Delete a Reserved IPv6

        Args:
            reserved_ipv6 (string): reserved_ipv6

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            [Public Preview] Reserved IPv6
        """
        if reserved_ipv6 is None:
            raise ValueError("Missing required parameter 'reserved_ipv6'.")
        url = f"{self.base_url}/v2/reserved_ipv6/{reserved_ipv6}"
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

    def reserved_ipv_actions_post(
        self,
        reserved_ipv6: str,
        type: str | None = None,
        droplet_id: int | None = None,
    ) -> Any:
        """
        [Public Preview] Initiate a Reserved IPv6 Action

        Args:
            reserved_ipv6 (string): reserved_ipv6
            type (string): The type of action to initiate for the reserved IPv6.
            droplet_id (integer): The ID of the Droplet that the reserved IPv6 will be assigned to. Example: '758604968'.

        Returns:
            Any: The response will be an object with a key called `action`. The value of this will be an object that contains the standard reserved IP action attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            [Public Preview] Reserved IPv6 Actions
        """
        if reserved_ipv6 is None:
            raise ValueError("Missing required parameter 'reserved_ipv6'.")
        request_body_data = None
        request_body_data = {
            "type": type,
            "droplet_id": droplet_id,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/reserved_ipv6/{reserved_ipv6}/actions"
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

    def sizes_list(self, per_page: int | None = None, page: int | None = None) -> Any:
        """
        List All Droplet Sizes

        Args:
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: A JSON object with a key called `sizes`. The value of this will be an array of `size` objects each of which contain the standard size attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Sizes
        """
        url = f"{self.base_url}/v2/sizes"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def snapshots_list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        resource_type: str | None = None,
    ) -> Any:
        """
        List All Snapshots

        Args:
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.
            resource_type (string): Used to filter snapshots by a resource type. Example: 'droplet'.

        Returns:
            Any: A JSON object with a key of `snapshots`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Snapshots
        """
        url = f"{self.base_url}/v2/snapshots"
        query_params = {
            k: v
            for k, v in [
                ("per_page", per_page),
                ("page", page),
                ("resource_type", resource_type),
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

    def snapshots_get(self, snapshot_id: str) -> Any:
        """
        Retrieve an Existing Snapshot

        Args:
            snapshot_id (string): snapshot_id

        Returns:
            Any: A JSON object with a key called `snapshot`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Snapshots
        """
        if snapshot_id is None:
            raise ValueError("Missing required parameter 'snapshot_id'.")
        url = f"{self.base_url}/v2/snapshots/{snapshot_id}"
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

    def snapshots_delete(self, snapshot_id: str) -> Any:
        """
        Delete a Snapshot

        Args:
            snapshot_id (string): snapshot_id

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Snapshots
        """
        if snapshot_id is None:
            raise ValueError("Missing required parameter 'snapshot_id'.")
        url = f"{self.base_url}/v2/snapshots/{snapshot_id}"
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

    def spaces_key_list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        sort: str | None = None,
        sort_direction: str | None = None,
        name: str | None = None,
        bucket: str | None = None,
        permission: str | None = None,
    ) -> Any:
        """
        List Spaces Access Keys

        Args:
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.
            sort (string): The field to sort by. Example: 'created_at'.
            sort_direction (string): The direction to sort by. Possible values are `asc` or `desc`. Example: 'desc'.
            name (string): The access key's name. Example: 'my-access-key'.
            bucket (string): The bucket's name. Example: 'my-bucket'.
            permission (string): The permission of the access key. Possible values are `read`, `readwrite`, `fullaccess`, or an empty string. Example: 'read'.

        Returns:
            Any: A JSON response containing a list of keys.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Spaces Keys
        """
        url = f"{self.base_url}/v2/spaces/keys"
        query_params = {
            k: v
            for k, v in [
                ("per_page", per_page),
                ("page", page),
                ("sort", sort),
                ("sort_direction", sort_direction),
                ("name", name),
                ("bucket", bucket),
                ("permission", permission),
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

    def spaces_key_create(
        self,
        name: str | None = None,
        grants: list[dict[str, Any]] | None = None,
        access_key: str | None = None,
        created_at: str | None = None,
    ) -> Any:
        """
        Create a New Spaces Access Key

        Args:
            name (string): The access key's name. Example: 'my-access-key'.
            grants (array): The list of permissions for the access key. Example: [{'bucket': 'my-bucket', 'permission': 'read'}].
            access_key (string): The Access Key ID used to access a bucket. Example: 'DOACCESSKEYEXAMPLE'.
            created_at (string): The date and time the key was created. Example: '2018-07-19T15:04:16Z'.

        Returns:
            Any: A JSON response containing details about the new key.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Spaces Keys
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "grants": grants,
            "access_key": access_key,
            "created_at": created_at,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/spaces/keys"
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

    def spaces_key_get(self, access_key: str) -> Any:
        """
        Get a Spaces Access Key

        Args:
            access_key (string): access_key

        Returns:
            Any: A JSON response containing details about the key.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Spaces Keys
        """
        if access_key is None:
            raise ValueError("Missing required parameter 'access_key'.")
        url = f"{self.base_url}/v2/spaces/keys/{access_key}"
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

    def spaces_key_delete(self, access_key: str) -> Any:
        """
        Delete a Spaces Access Key

        Args:
            access_key (string): access_key

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Spaces Keys
        """
        if access_key is None:
            raise ValueError("Missing required parameter 'access_key'.")
        url = f"{self.base_url}/v2/spaces/keys/{access_key}"
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

    def spaces_key_update(
        self,
        access_key: str,
        name: str | None = None,
        grants: list[dict[str, Any]] | None = None,
        access_key_body: str | None = None,
        created_at: str | None = None,
    ) -> Any:
        """
        Update Spaces Access Keys

        Args:
            access_key (string): access_key
            name (string): The access key's name. Example: 'my-access-key'.
            grants (array): The list of permissions for the access key.
            access_key_body (string): The Access Key ID used to access a bucket. Example: 'DOACCESSKEYEXAMPLE'.
            created_at (string): The date and time the key was created. Example: '2018-07-19T15:04:16Z'.

        Returns:
            Any: The response will be a JSON object

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Spaces Keys
        """
        if access_key is None:
            raise ValueError("Missing required parameter 'access_key'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "grants": grants,
            "access_key": access_key_body,
            "created_at": created_at,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/spaces/keys/{access_key}"
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

    def spaces_key_patch(
        self,
        access_key: str,
        name: str | None = None,
        grants: list[dict[str, Any]] | None = None,
        access_key_body: str | None = None,
        created_at: str | None = None,
    ) -> Any:
        """
        Update Spaces Access Keys

        Args:
            access_key (string): access_key
            name (string): The access key's name. Example: 'my-access-key'.
            grants (array): The list of permissions for the access key.
            access_key_body (string): The Access Key ID used to access a bucket. Example: 'DOACCESSKEYEXAMPLE'.
            created_at (string): The date and time the key was created. Example: '2018-07-19T15:04:16Z'.

        Returns:
            Any: The response will be a JSON object

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Spaces Keys
        """
        if access_key is None:
            raise ValueError("Missing required parameter 'access_key'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "grants": grants,
            "access_key": access_key_body,
            "created_at": created_at,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/spaces/keys/{access_key}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def tags_list(self, per_page: int | None = None, page: int | None = None) -> Any:
        """
        List All Tags

        Args:
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: To list all of your tags, you can send a `GET` request to `/v2/tags`.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tags
        """
        url = f"{self.base_url}/v2/tags"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def tags_create(
        self, name: str | None = None, resources: dict[str, Any] | None = None
    ) -> Any:
        """
        Create a New Tag

        Args:
            name (string): The name of the tag. Tags may contain letters, numbers, colons, dashes, and underscores.
        There is a limit of 255 characters per tag.

        **Note:** Tag names are case stable, which means the capitalization you use when you first create a tag is canonical.

        When working with tags in the API, you must use the tag's canonical capitalization. For example, if you create a tag named "PROD", the URL to add that tag to a resource would be `https://api.digitalocean.com/v2/tags/PROD/resources` (not `/v2/tags/prod/resources`).

        Tagged resources in the control panel will always display the canonical capitalization. For example, if you create a tag named "PROD", you can tag resources in the control panel by entering "prod". The tag will still display with its canonical capitalization, "PROD".
         Example: 'extra-awesome'.
            resources (object): An embedded object containing key value pairs of resource type and resource statistics. It also includes a count of the total number of resources tagged with the current tag as well as a `last_tagged_uri` attribute set to the last resource tagged with the current tag. Example: "{'count': 5, 'last_tagged_uri': 'https://api.digitalocean.com/v2/images/7555620', 'droplets': {'count': 1, 'last_tagged_uri': 'https://api.digitalocean.com/v2/droplets/3164444'}, 'images': {'count': 1, 'last_tagged_uri': 'https://api.digitalocean.com/v2/images/7555620'}, 'volumes': {'count': 1, 'last_tagged_uri': 'https://api.digitalocean.com/v2/volumes/3d80cb72-342b-4aaa-b92e-4e4abb24a933'}, 'volume_snapshots': {'count': 1, 'last_tagged_uri': 'https://api.digitalocean.com/v2/snapshots/1f6f46e8-6b60-11e9-be4e-0a58ac144519'}, 'databases': {'count': 1, 'last_tagged_uri': 'https://api.digitalocean.com/v2/databases/b92438f6-ba03-416c-b642-e9236db91976'}}".

        Returns:
            Any: The response will be a JSON object with a key called tag.  The value of this will be a tag object containing the standard tag attributes

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tags
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "resources": resources,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/tags"
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

    def tags_get(self, tag_id: str) -> dict[str, Any]:
        """
        Retrieve a Tag

        Args:
            tag_id (string): tag_id

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `tag`.  The value of this will be a tag object containing the standard tag attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tags
        """
        if tag_id is None:
            raise ValueError("Missing required parameter 'tag_id'.")
        url = f"{self.base_url}/v2/tags/{tag_id}"
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

    def tags_delete(self, tag_id: str) -> Any:
        """
        Delete a Tag

        Args:
            tag_id (string): tag_id

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tags
        """
        if tag_id is None:
            raise ValueError("Missing required parameter 'tag_id'.")
        url = f"{self.base_url}/v2/tags/{tag_id}"
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

    def tags_assign_resources(self, tag_id: str, resources: list[Any]) -> Any:
        """
        Tag a Resource

        Args:
            tag_id (string): tag_id
            resources (array): An array of objects containing resource_id and resource_type  attributes. Example: "[{'resource_id': '9569411', 'resource_type': 'droplet'}, {'resource_id': '7555620', 'resource_type': 'image'}, {'resource_id': '3d80cb72-342b-4aaa-b92e-4e4abb24a933', 'resource_type': 'volume'}]".

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tags
        """
        if tag_id is None:
            raise ValueError("Missing required parameter 'tag_id'.")
        request_body_data = None
        request_body_data = {
            "resources": resources,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/tags/{tag_id}/resources"
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

    def tags_unassign_resources(self, tag_id: str, resources: list[Any]) -> Any:
        """
        Untag a Resource

        Args:
            tag_id (string): tag_id
            resources (array): An array of objects containing resource_id and resource_type  attributes. Example: "[{'resource_id': '9569411', 'resource_type': 'droplet'}, {'resource_id': '7555620', 'resource_type': 'image'}, {'resource_id': '3d80cb72-342b-4aaa-b92e-4e4abb24a933', 'resource_type': 'volume'}]".

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tags
        """
        if tag_id is None:
            raise ValueError("Missing required parameter 'tag_id'.")
        request_body_data = {
            "resources": resources,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/tags/{tag_id}/resources"
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

    def volumes_list(
        self,
        name: str | None = None,
        region: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> Any:
        """
        List All Block Storage Volumes

        Args:
            name (string): The block storage volume's name. Example: 'example'.
            region (string): The slug identifier for the region where the resource is available. Example: 'nyc3'.
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: The response will be a JSON object with a key called `volumes`. This will be set to an array of volume objects, each of which will contain the standard volume attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Block Storage, important
        """
        url = f"{self.base_url}/v2/volumes"
        query_params = {
            k: v
            for k, v in [
                ("name", name),
                ("region", region),
                ("per_page", per_page),
                ("page", page),
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

    def volumes_create(
        self,
        id: str | None = None,
        droplet_ids: list[int] | None = None,
        name: str | None = None,
        description: str | None = None,
        size_gigabytes: int | None = None,
        created_at: str | None = None,
        tags: list[str] | None = None,
        snapshot_id: str | None = None,
        filesystem_type: str | None = None,
        region: str | None = None,
        filesystem_label: Any | None = None,
    ) -> Any:
        """
        Create a New Block Storage Volume

        Args:
            id (string): The unique identifier for the block storage volume. Example: '506f78a4-e098-11e5-ad9f-000f53306ae1'.
            droplet_ids (array): An array containing the IDs of the Droplets the volume is attached to. Note that at this time, a volume can only be attached to a single Droplet. Example: '[]'.
            name (string): A human-readable name for the block storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters. The name must begin with a letter. Example: 'example'.
            description (string): An optional free-form text field to describe a block storage volume. Example: 'Block store for examples'.
            size_gigabytes (integer): The size of the block storage volume in GiB (1024^3). This field does not apply  when creating a volume from a snapshot. Example: '10'.
            created_at (string): A time value given in ISO8601 combined date and time format that represents when the block storage volume was created. Example: '2020-03-02T17:00:49Z'.
            tags (array): A flat array of tag names as strings to be applied to the resource. Tag names may be for either existing or new tags. Example: "['base-image', 'prod']".
            snapshot_id (string): The unique identifier for the volume snapshot from which to create the volume. Example: 'b0798135-fb76-11eb-946a-0a58ac146f33'.
            filesystem_type (string): The name of the filesystem type to be used on the volume. When provided, the volume will automatically be formatted to the specified filesystem type. Currently, the available options are `ext4` and `xfs`. Pre-formatted volumes are automatically mounted when attached to Ubuntu, Debian, Fedora, Fedora Atomic, and CentOS Droplets created on or after April 26, 2018. Attaching pre-formatted volumes to other Droplets is not recommended. Example: 'ext4'.
            region (string): The slug identifier for the region where the resource will initially be  available. Example: 'nyc3'.
            filesystem_label (string): filesystem_label Example: 'ext4_volume_01'.

        Returns:
            Any: The response will be a JSON object with a key called `volume`. The value will be an object containing the standard attributes associated with a volume.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Block Storage, important
        """
        request_body_data = None
        request_body_data = {
            "id": id,
            "droplet_ids": droplet_ids,
            "name": name,
            "description": description,
            "size_gigabytes": size_gigabytes,
            "created_at": created_at,
            "tags": tags,
            "snapshot_id": snapshot_id,
            "filesystem_type": filesystem_type,
            "region": region,
            "filesystem_label": filesystem_label,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/volumes"
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

    def volumes_delete_by_name(
        self, name: str | None = None, region: str | None = None
    ) -> Any:
        """
        Delete a Block Storage Volume by Name

        Args:
            name (string): The block storage volume's name. Example: 'example'.
            region (string): The slug identifier for the region where the resource is available. Example: 'nyc3'.

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Block Storage
        """
        url = f"{self.base_url}/v2/volumes"
        query_params = {
            k: v for k, v in [("name", name), ("region", region)] if v is not None
        }
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

    def volume_actions_post(
        self,
        per_page: int | None = None,
        page: int | None = None,
        type: str | None = None,
        region: str | None = None,
        droplet_id: int | None = None,
        tags: list[str] | None = None,
    ) -> Any:
        """
        Initiate A Block Storage Action By Volume Name

        Args:
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.
            type (string): The volume action to initiate. Example: 'attach'.
            region (string): The slug identifier for the region where the resource will initially be  available. Example: 'nyc3'.
            droplet_id (integer): The unique identifier for the Droplet the volume will be attached or detached from. Example: '11612190'.
            tags (array): A flat array of tag names as strings to be applied to the resource. Tag names may be for either existing or new tags. Example: "['base-image', 'prod']".

        Returns:
            Any: The response will be an object with a key called `action`. The value of this will be an object that contains the standard volume action attributes

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Block Storage Actions
        """
        request_body_data = None
        request_body_data = {
            "type": type,
            "region": region,
            "droplet_id": droplet_id,
            "tags": tags,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/volumes/actions"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def volume_snapshots_get_by_id(self, snapshot_id: str) -> Any:
        """
        Retrieve an Existing Volume Snapshot

        Args:
            snapshot_id (string): snapshot_id

        Returns:
            Any: You will get back a JSON object that has a `snapshot` key. This will contain the standard snapshot attributes

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Block Storage
        """
        if snapshot_id is None:
            raise ValueError("Missing required parameter 'snapshot_id'.")
        url = f"{self.base_url}/v2/volumes/snapshots/{snapshot_id}"
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

    def volume_snapshots_delete_by_id(self, snapshot_id: str) -> Any:
        """
        Delete a Volume Snapshot

        Args:
            snapshot_id (string): snapshot_id

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Block Storage
        """
        if snapshot_id is None:
            raise ValueError("Missing required parameter 'snapshot_id'.")
        url = f"{self.base_url}/v2/volumes/snapshots/{snapshot_id}"
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

    def volumes_get(self, volume_id: str) -> Any:
        """
        Retrieve an Existing Block Storage Volume

        Args:
            volume_id (string): volume_id

        Returns:
            Any: The response will be a JSON object with a key called `volume`. The value will be an object containing the standard attributes associated with a volume.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Block Storage
        """
        if volume_id is None:
            raise ValueError("Missing required parameter 'volume_id'.")
        url = f"{self.base_url}/v2/volumes/{volume_id}"
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

    def volumes_delete(self, volume_id: str) -> Any:
        """
        Delete a Block Storage Volume

        Args:
            volume_id (string): volume_id

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Block Storage
        """
        if volume_id is None:
            raise ValueError("Missing required parameter 'volume_id'.")
        url = f"{self.base_url}/v2/volumes/{volume_id}"
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

    def volume_actions_list(
        self, volume_id: str, per_page: int | None = None, page: int | None = None
    ) -> Any:
        """
        List All Actions for a Volume

        Args:
            volume_id (string): volume_id
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: The response will be an object with a key called `action`. The value of this will be an object that contains the standard volume action attributes.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Block Storage Actions
        """
        if volume_id is None:
            raise ValueError("Missing required parameter 'volume_id'.")
        url = f"{self.base_url}/v2/volumes/{volume_id}/actions"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def volume_actions_post_by_id(
        self,
        volume_id: str,
        per_page: int | None = None,
        page: int | None = None,
        type: str | None = None,
        region: str | None = None,
        droplet_id: int | None = None,
        tags: list[str] | None = None,
        size_gigabytes: int | None = None,
    ) -> Any:
        """
        Initiate A Block Storage Action By Volume Id

        Args:
            volume_id (string): volume_id
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.
            type (string): The volume action to initiate. Example: 'attach'.
            region (string): The slug identifier for the region where the resource will initially be  available. Example: 'nyc3'.
            droplet_id (integer): The unique identifier for the Droplet the volume will be attached or detached from. Example: '11612190'.
            tags (array): A flat array of tag names as strings to be applied to the resource. Tag names may be for either existing or new tags. Example: "['base-image', 'prod']".
            size_gigabytes (integer): The new size of the block storage volume in GiB (1024^3).

        Returns:
            Any: The response will be an object with a key called `action`. The value of this will be an object that contains the standard volume action attributes

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Block Storage Actions
        """
        if volume_id is None:
            raise ValueError("Missing required parameter 'volume_id'.")
        request_body_data = None
        request_body_data = {
            "type": type,
            "region": region,
            "droplet_id": droplet_id,
            "tags": tags,
            "size_gigabytes": size_gigabytes,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/volumes/{volume_id}/actions"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def volume_actions_get(
        self,
        volume_id: str,
        action_id: str,
        per_page: int | None = None,
        page: int | None = None,
    ) -> Any:
        """
        Retrieve an Existing Volume Action

        Args:
            volume_id (string): volume_id
            action_id (string): action_id
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: The response will be an object with a key called `action`. The value of this will be an object that contains the standard volume action attributes

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Block Storage Actions
        """
        if volume_id is None:
            raise ValueError("Missing required parameter 'volume_id'.")
        if action_id is None:
            raise ValueError("Missing required parameter 'action_id'.")
        url = f"{self.base_url}/v2/volumes/{volume_id}/actions/{action_id}"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def volume_snapshots_list(
        self, volume_id: str, per_page: int | None = None, page: int | None = None
    ) -> Any:
        """
        List Snapshots for a Volume

        Args:
            volume_id (string): volume_id
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: You will get back a JSON object that has a `snapshots` key. This will be set to an array of snapshot objects, each of which contain the standard snapshot attributes

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Block Storage
        """
        if volume_id is None:
            raise ValueError("Missing required parameter 'volume_id'.")
        url = f"{self.base_url}/v2/volumes/{volume_id}/snapshots"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def volume_snapshots_create(
        self, volume_id: str, name: str, tags: list[str] | None = None
    ) -> Any:
        """
        Create Snapshot from a Volume

        Args:
            volume_id (string): volume_id
            name (string): A human-readable name for the volume snapshot. Example: 'big-data-snapshot1475261774'.
            tags (array): A flat array of tag names as strings to be applied to the resource. Tag names may be for either existing or new tags. Example: "['base-image', 'prod']".

        Returns:
            Any: You will get back a JSON object that has a `snapshot` key. This will contain the standard snapshot attributes

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Block Storage
        """
        if volume_id is None:
            raise ValueError("Missing required parameter 'volume_id'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "tags": tags,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/volumes/{volume_id}/snapshots"
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

    def vpcs_list(self, per_page: int | None = None, page: int | None = None) -> Any:
        """
        List All VPCs

        Args:
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: The response will be a JSON object with a key called `vpcs`. This will be set to an array of objects, each of which will contain the standard attributes associated with a VPC

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            VPCs
        """
        url = f"{self.base_url}/v2/vpcs"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def vpcs_create(
        self,
        name: str,
        region: str,
        description: str | None = None,
        ip_range: str | None = None,
    ) -> dict[str, Any]:
        """
        Create a New VPC

        Args:
            name (string): The name of the VPC. Must be unique and may only contain alphanumeric characters, dashes, and periods. Example: 'env.prod-vpc'.
            region (string): The slug identifier for the region where the VPC will be created. Example: 'nyc1'.
            description (string): A free-form text field for describing the VPC's purpose. It may be a maximum of 255 characters. Example: 'VPC for production environment'.
            ip_range (string): The range of IP addresses in the VPC in CIDR notation. Network ranges cannot overlap with other networks in the same account and must be in range of private addresses as defined in RFC1918. It may not be smaller than `/28` nor larger than `/16`. If no IP range is specified, a `/20` network range is generated that won't conflict with other VPC networks in your account. Example: '10.10.10.0/24'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `vpc`. The value of this will be an object that contains the standard attributes associated with a VPC.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            VPCs
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "description": description,
            "region": region,
            "ip_range": ip_range,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/vpcs"
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

    def vpcs_get(self, vpc_id: str) -> dict[str, Any]:
        """
        Retrieve an Existing VPC

        Args:
            vpc_id (string): vpc_id

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `vpc`. The value of this will be an object that contains the standard attributes associated with a VPC.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            VPCs
        """
        if vpc_id is None:
            raise ValueError("Missing required parameter 'vpc_id'.")
        url = f"{self.base_url}/v2/vpcs/{vpc_id}"
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

    def vpcs_update(
        self,
        vpc_id: str,
        name: str,
        description: str | None = None,
        default: bool | None = None,
    ) -> dict[str, Any]:
        """
        Update a VPC

        Args:
            vpc_id (string): vpc_id
            name (string): The name of the VPC. Must be unique and may only contain alphanumeric characters, dashes, and periods. Example: 'env.prod-vpc'.
            description (string): A free-form text field for describing the VPC's purpose. It may be a maximum of 255 characters. Example: 'VPC for production environment'.
            default (boolean): A boolean value indicating whether or not the VPC is the default network for the region. All applicable resources are placed into the default VPC network unless otherwise specified during their creation. The `default` field cannot be unset from `true`. If you want to set a new default VPC network, update the `default` field of another VPC network in the same region. The previous network's `default` field will be set to `false` when a new default VPC has been defined. Example: 'True'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `vpc`. The value of this will be an object that contains the standard attributes associated with a VPC.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            VPCs
        """
        if vpc_id is None:
            raise ValueError("Missing required parameter 'vpc_id'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "description": description,
            "default": default,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/vpcs/{vpc_id}"
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

    def vpcs_patch(
        self,
        vpc_id: str,
        name: str | None = None,
        description: str | None = None,
        default: bool | None = None,
    ) -> dict[str, Any]:
        """
        Partially Update a VPC

        Args:
            vpc_id (string): vpc_id
            name (string): The name of the VPC. Must be unique and may only contain alphanumeric characters, dashes, and periods. Example: 'env.prod-vpc'.
            description (string): A free-form text field for describing the VPC's purpose. It may be a maximum of 255 characters. Example: 'VPC for production environment'.
            default (boolean): A boolean value indicating whether or not the VPC is the default network for the region. All applicable resources are placed into the default VPC network unless otherwise specified during their creation. The `default` field cannot be unset from `true`. If you want to set a new default VPC network, update the `default` field of another VPC network in the same region. The previous network's `default` field will be set to `false` when a new default VPC has been defined. Example: 'True'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `vpc`. The value of this will be an object that contains the standard attributes associated with a VPC.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            VPCs
        """
        if vpc_id is None:
            raise ValueError("Missing required parameter 'vpc_id'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "description": description,
            "default": default,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/vpcs/{vpc_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def vpcs_delete(self, vpc_id: str) -> Any:
        """
        Delete a VPC

        Args:
            vpc_id (string): vpc_id

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            VPCs
        """
        if vpc_id is None:
            raise ValueError("Missing required parameter 'vpc_id'.")
        url = f"{self.base_url}/v2/vpcs/{vpc_id}"
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

    def vpcs_list_members(
        self,
        vpc_id: str,
        resource_type: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> Any:
        """
        List the Member Resources of a VPC

        Args:
            vpc_id (string): vpc_id
            resource_type (string): Used to filter VPC members by a resource type. Example: 'droplet'.
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: The response will be a JSON object with a key called members. This will be set to an array of objects, each of which will contain the standard attributes associated with a VPC member.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            VPCs
        """
        if vpc_id is None:
            raise ValueError("Missing required parameter 'vpc_id'.")
        url = f"{self.base_url}/v2/vpcs/{vpc_id}/members"
        query_params = {
            k: v
            for k, v in [
                ("resource_type", resource_type),
                ("per_page", per_page),
                ("page", page),
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

    def vpcs_list_peerings(
        self, vpc_id: str, per_page: int | None = None, page: int | None = None
    ) -> Any:
        """
        List the Peerings of a VPC

        Args:
            vpc_id (string): vpc_id
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: The response will be a JSON object with a key called `peerings`. This  will be set to an array of objects, each of which will contain the standard  attributes associated with a VPC peering.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            VPCs
        """
        if vpc_id is None:
            raise ValueError("Missing required parameter 'vpc_id'.")
        url = f"{self.base_url}/v2/vpcs/{vpc_id}/peerings"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def vpcs_create_peerings(
        self, vpc_id: str, name: str, vpc_id_body: str
    ) -> dict[str, Any]:
        """
        Create a Peering with a VPC

        Args:
            vpc_id (string): vpc_id
            name (string): The name of the VPC peering. Must be unique and may only contain alphanumeric characters, dashes, and periods. Example: 'nyc1-blr1-peering'.
            vpc_id_body (string): The ID of the VPC to peer with. Example: 'c140286f-e6ce-4131-8b7b-df4590ce8d6a'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `peering`, containing  the standard attributes associated with a VPC peering.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            VPCs
        """
        if vpc_id is None:
            raise ValueError("Missing required parameter 'vpc_id'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "vpc_id": vpc_id_body,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/vpcs/{vpc_id}/peerings"
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

    def vpcs_patch_peerings(
        self, vpc_id: str, vpc_peering_id: str, name: str
    ) -> dict[str, Any]:
        """
        Update a VPC Peering

        Args:
            vpc_id (string): vpc_id
            vpc_peering_id (string): vpc_peering_id
            name (string): The name of the VPC peering. Must be unique within the team and may only contain alphanumeric characters and dashes. Example: 'nyc1-blr1-peering'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `peering`, containing  the standard attributes associated with a VPC peering.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            VPCs
        """
        if vpc_id is None:
            raise ValueError("Missing required parameter 'vpc_id'.")
        if vpc_peering_id is None:
            raise ValueError("Missing required parameter 'vpc_peering_id'.")
        request_body_data = None
        request_body_data = {
            "name": name,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/vpcs/{vpc_id}/peerings/{vpc_peering_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def vpc_peerings_list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        region: str | None = None,
    ) -> Any:
        """
        List All VPC Peerings

        Args:
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.
            region (string): The slug identifier for the region where the resource is available. Example: 'nyc3'.

        Returns:
            Any: The response will be a JSON object with a key called `vpc_peerings`. This  will be set to an array of objects, each of which will contain the standard  attributes associated with a VPC peering.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            VPC Peerings
        """
        url = f"{self.base_url}/v2/vpc_peerings"
        query_params = {
            k: v
            for k, v in [("per_page", per_page), ("page", page), ("region", region)]
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

    def vpc_peerings_create(self, name: str, vpc_ids: list[str]) -> dict[str, Any]:
        """
        Create a New VPC Peering

        Args:
            name (string): The name of the VPC peering. Must be unique within the team and may only contain alphanumeric characters and dashes. Example: 'nyc1-blr1-peering'.
            vpc_ids (array): An array of the two peered VPCs IDs. Example: "['c140286f-e6ce-4131-8b7b-df4590ce8d6a', '994a2735-dc84-11e8-80bc-3cfdfea9fba1']".

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `vpc_peering`. The value of this will be an object that contains the standard attributes associated with a VPC peering.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            VPC Peerings
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "vpc_ids": vpc_ids,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/vpc_peerings"
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

    def vpc_peerings_get(self, vpc_peering_id: str) -> dict[str, Any]:
        """
        Retrieve an Existing VPC Peering

        Args:
            vpc_peering_id (string): vpc_peering_id

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `vpc_peering`. The value of this will be an object that contains the standard attributes associated with a VPC peering.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            VPC Peerings
        """
        if vpc_peering_id is None:
            raise ValueError("Missing required parameter 'vpc_peering_id'.")
        url = f"{self.base_url}/v2/vpc_peerings/{vpc_peering_id}"
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

    def vpc_peerings_patch(self, vpc_peering_id: str, name: str) -> dict[str, Any]:
        """
        Update a VPC peering

        Args:
            vpc_peering_id (string): vpc_peering_id
            name (string): The name of the VPC peering. Must be unique within the team and may only contain alphanumeric characters and dashes. Example: 'nyc1-blr1-peering'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `vpc_peering`. The value of this will be an object that contains the standard attributes associated with a VPC peering.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            VPC Peerings
        """
        if vpc_peering_id is None:
            raise ValueError("Missing required parameter 'vpc_peering_id'.")
        request_body_data = None
        request_body_data = {
            "name": name,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/vpc_peerings/{vpc_peering_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        if (
            response.status_code == 204
            or not response.content
            or not response.text.strip()
        ):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def vpc_peerings_delete(self, vpc_peering_id: str) -> dict[str, Any]:
        """
        Delete a VPC peering

        Args:
            vpc_peering_id (string): vpc_peering_id

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `vpc_peering`. The value of this will be an object that contains the standard attributes associated with a VPC peering.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            VPC Peerings
        """
        if vpc_peering_id is None:
            raise ValueError("Missing required parameter 'vpc_peering_id'.")
        url = f"{self.base_url}/v2/vpc_peerings/{vpc_peering_id}"
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

    def uptime_list_checks(
        self, per_page: int | None = None, page: int | None = None
    ) -> Any:
        """
        List All Checks

        Args:
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: The response will be a JSON object with a key called `checks`. This will be set to an array of objects, each of which will contain the standard attributes associated with an uptime check

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Uptime
        """
        url = f"{self.base_url}/v2/uptime/checks"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def uptime_create_check(
        self, name: str, type: str, target: str, regions: list[str], enabled: bool
    ) -> dict[str, Any]:
        """
        Create a New Check

        Args:
            name (string): A human-friendly display name. Example: 'Landing page check'.
            type (string): The type of health check to perform. Example: 'https'.
            target (string): The endpoint to perform healthchecks on. Example: 'https://www.landingpage.com'.
            regions (array): An array containing the selected regions to perform healthchecks from. Example: "['us_east', 'eu_west']".
            enabled (boolean): A boolean value indicating whether the check is enabled/disabled. Example: 'True'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `check`. The value of this will be an object that contains the standard attributes associated with an uptime check.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Uptime
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "type": type,
            "target": target,
            "regions": regions,
            "enabled": enabled,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/uptime/checks"
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

    def uptime_get_check(self, check_id: str) -> dict[str, Any]:
        """
        Retrieve an Existing Check

        Args:
            check_id (string): check_id

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `check`. The value of this will be an object that contains the standard attributes associated with an uptime check.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Uptime
        """
        if check_id is None:
            raise ValueError("Missing required parameter 'check_id'.")
        url = f"{self.base_url}/v2/uptime/checks/{check_id}"
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

    def uptime_update_check(
        self,
        check_id: str,
        name: str | None = None,
        type: str | None = None,
        target: str | None = None,
        regions: list[str] | None = None,
        enabled: bool | None = None,
    ) -> dict[str, Any]:
        """
        Update a Check

        Args:
            check_id (string): check_id
            name (string): A human-friendly display name. Example: 'Landing page check'.
            type (string): The type of health check to perform. Example: 'https'.
            target (string): The endpoint to perform healthchecks on. Example: 'https://www.landingpage.com'.
            regions (array): An array containing the selected regions to perform healthchecks from. Example: "['us_east', 'eu_west']".
            enabled (boolean): A boolean value indicating whether the check is enabled/disabled. Example: 'True'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `check`. The value of this will be an object that contains the standard attributes associated with an uptime check.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Uptime
        """
        if check_id is None:
            raise ValueError("Missing required parameter 'check_id'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "type": type,
            "target": target,
            "regions": regions,
            "enabled": enabled,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/uptime/checks/{check_id}"
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

    def uptime_delete_check(self, check_id: str) -> Any:
        """
        Delete a Check

        Args:
            check_id (string): check_id

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Uptime
        """
        if check_id is None:
            raise ValueError("Missing required parameter 'check_id'.")
        url = f"{self.base_url}/v2/uptime/checks/{check_id}"
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

    def uptime_get_check_state(self, check_id: str) -> dict[str, Any]:
        """
        Retrieve Check State

        Args:
            check_id (string): check_id

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `state`. The value of this will be an object that contains the standard attributes associated with an uptime check's state.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Uptime
        """
        if check_id is None:
            raise ValueError("Missing required parameter 'check_id'.")
        url = f"{self.base_url}/v2/uptime/checks/{check_id}/state"
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

    def uptime_list_alerts(
        self, check_id: str, per_page: int | None = None, page: int | None = None
    ) -> Any:
        """
        List All Alerts

        Args:
            check_id (string): check_id
            per_page (integer): Number of items returned per page Example: '2'.
            page (integer): Which 'page' of paginated results to return. Example: '1'.

        Returns:
            Any: The response will be a JSON object with a key called `alerts`. This will be set to an array of objects, each of which will contain the standard attributes associated with an uptime alert.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Uptime
        """
        if check_id is None:
            raise ValueError("Missing required parameter 'check_id'.")
        url = f"{self.base_url}/v2/uptime/checks/{check_id}/alerts"
        query_params = {
            k: v for k, v in [("per_page", per_page), ("page", page)] if v is not None
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

    def uptime_create_alert(
        self,
        check_id: str,
        name: str,
        type: str,
        notifications: dict[str, Any],
        period: str,
        id: str | None = None,
        threshold: int | None = None,
        comparison: str | None = None,
    ) -> dict[str, Any]:
        """
        Create a New Alert

        Args:
            check_id (string): check_id
            name (string): A human-friendly display name. Example: 'Landing page degraded performance'.
            type (string): The type of alert. Example: 'latency'.
            notifications (object): The notification settings for a trigger alert.
            period (string): Period of time the threshold must be exceeded to trigger the alert. Example: '2m'.
            id (string): A unique ID that can be used to identify and reference the alert. Example: '5a4981aa-9653-4bd1-bef5-d6bff52042e4'.
            threshold (integer): The threshold at which the alert will enter a trigger state. The specific threshold is dependent on the alert type. Example: '300'.
            comparison (string): The comparison operator used against the alert's threshold. Example: 'greater_than'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `alert`. The value of this will be an object that contains the standard attributes associated with an uptime alert.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Uptime
        """
        if check_id is None:
            raise ValueError("Missing required parameter 'check_id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "name": name,
            "type": type,
            "threshold": threshold,
            "comparison": comparison,
            "notifications": notifications,
            "period": period,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/uptime/checks/{check_id}/alerts"
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

    def uptime_get_alert(self, check_id: str, alert_id: str) -> dict[str, Any]:
        """
        Retrieve an Existing Alert

        Args:
            check_id (string): check_id
            alert_id (string): alert_id

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `alert`. The value of this will be an object that contains the standard attributes associated with an uptime alert.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Uptime
        """
        if check_id is None:
            raise ValueError("Missing required parameter 'check_id'.")
        if alert_id is None:
            raise ValueError("Missing required parameter 'alert_id'.")
        url = f"{self.base_url}/v2/uptime/checks/{check_id}/alerts/{alert_id}"
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

    def uptime_update_alert(
        self,
        check_id: str,
        alert_id: str,
        name: str,
        type: str,
        notifications: dict[str, Any],
        period: str,
        threshold: int | None = None,
        comparison: str | None = None,
    ) -> dict[str, Any]:
        """
        Update an Alert

        Args:
            check_id (string): check_id
            alert_id (string): alert_id
            name (string): A human-friendly display name. Example: 'Landing page degraded performance'.
            type (string): The type of alert. Example: 'latency'.
            notifications (object): The notification settings for a trigger alert.
            period (string): Period of time the threshold must be exceeded to trigger the alert. Example: '2m'.
            threshold (integer): The threshold at which the alert will enter a trigger state. The specific threshold is dependent on the alert type. Example: '300'.
            comparison (string): The comparison operator used against the alert's threshold. Example: 'greater_than'.

        Returns:
            dict[str, Any]: The response will be a JSON object with a key called `alert`. The value of this will be an object that contains the standard attributes associated with an uptime alert.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Uptime
        """
        if check_id is None:
            raise ValueError("Missing required parameter 'check_id'.")
        if alert_id is None:
            raise ValueError("Missing required parameter 'alert_id'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "type": type,
            "threshold": threshold,
            "comparison": comparison,
            "notifications": notifications,
            "period": period,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/uptime/checks/{check_id}/alerts/{alert_id}"
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

    def uptime_delete_alert(self, check_id: str, alert_id: str) -> Any:
        """
        Delete an Alert

        Args:
            check_id (string): check_id
            alert_id (string): alert_id

        Returns:
            Any: The action was successful and the response body is empty.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Uptime
        """
        if check_id is None:
            raise ValueError("Missing required parameter 'check_id'.")
        if alert_id is None:
            raise ValueError("Missing required parameter 'alert_id'.")
        url = f"{self.base_url}/v2/uptime/checks/{check_id}/alerts/{alert_id}"
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

    def genai_list_agents(
        self,
        only_deployed: bool | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> dict[str, Any]:
        """
        List Agents

        Args:
            only_deployed (boolean): Only list agents that are deployed. Example: 'True'.
            page (integer): Page number. Example: '1'.
            per_page (integer): Items per page. Example: '1'.

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        url = f"{self.base_url}/v2/gen-ai/agents"
        query_params = {
            k: v
            for k, v in [
                ("only_deployed", only_deployed),
                ("page", page),
                ("per_page", per_page),
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

    def genai_create_agent(
        self,
        anthropic_key_uuid: str | None = None,
        description: str | None = None,
        instruction: str | None = None,
        knowledge_base_uuid: list[str] | None = None,
        model_uuid: str | None = None,
        name: str | None = None,
        open_ai_key_uuid: str | None = None,
        project_id: str | None = None,
        region: str | None = None,
        tags: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Create an Agent

        Args:
            anthropic_key_uuid (string): Optional Anthropic API key ID to use with Anthropic models Example: '"12345678-1234-1234-1234-123456789012"'.
            description (string): A text description of the agent, not used in inference Example: '"My Agent Description"'.
            instruction (string): Agent instruction. Instructions help your agent to perform its job effectively. See [Write Effective Agent Instructions](https://docs.digitalocean.com/products/genai-platform/concepts/best-practices/#agent-instructions) for best practices. Example: '"You are an agent who thinks deeply about the world"'.
            knowledge_base_uuid (array): Ids of the knowledge base(s) to attach to the agent Example: "['example string']".
            model_uuid (string): Identifier for the foundation model. Example: '"12345678-1234-1234-1234-123456789012"'.
            name (string): Agent name Example: '"My Agent"'.
            open_ai_key_uuid (string): Optional OpenAI API key ID to use with OpenAI models Example: '"12345678-1234-1234-1234-123456789012"'.
            project_id (string): The id of the DigitalOcean project this agent will belong to Example: '"12345678-1234-1234-1234-123456789012"'.
            region (string): The DigitalOcean region to deploy your agent in Example: '"tor1"'.
            tags (array): Agent tag to organize related resources Example: "['example string']".

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        request_body_data = None
        request_body_data = {
            "anthropic_key_uuid": anthropic_key_uuid,
            "description": description,
            "instruction": instruction,
            "knowledge_base_uuid": knowledge_base_uuid,
            "model_uuid": model_uuid,
            "name": name,
            "open_ai_key_uuid": open_ai_key_uuid,
            "project_id": project_id,
            "region": region,
            "tags": tags,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/gen-ai/agents"
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

    def genai_list_agent_api_keys(
        self,
        agent_uuid: str,
        page: int | None = None,
        per_page: int | None = None,
    ) -> dict[str, Any]:
        """
        List Agent API Keys

        Args:
            agent_uuid (string): agent_uuid
            page (integer): Page number. Example: '1'.
            per_page (integer): Items per page. Example: '1'.

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if agent_uuid is None:
            raise ValueError("Missing required parameter 'agent_uuid'.")
        url = f"{self.base_url}/v2/gen-ai/agents/{agent_uuid}/api_keys"
        query_params = {
            k: v for k, v in [("page", page), ("per_page", per_page)] if v is not None
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

    def genai_create_agent_api_key(
        self,
        agent_uuid: str,
        agent_uuid_body: str | None = None,
        name: str | None = None,
    ) -> dict[str, Any]:
        """
        Create an Agent API Key

        Args:
            agent_uuid (string): agent_uuid
            agent_uuid_body (string): Agent id Example: '"12345678-1234-1234-1234-123456789012"'.
            name (string): A human friendly name to identify the key Example: 'Production Key'.

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if agent_uuid is None:
            raise ValueError("Missing required parameter 'agent_uuid'.")
        request_body_data = None
        request_body_data = {
            "agent_uuid": agent_uuid_body,
            "name": name,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/gen-ai/agents/{agent_uuid}/api_keys"
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

    def genai_update_agent_api_key(
        self,
        agent_uuid: str,
        api_key_uuid: str,
        agent_uuid_body: str | None = None,
        api_key_uuid_body: str | None = None,
        name: str | None = None,
    ) -> dict[str, Any]:
        """
        Update API Key for an Agent

        Args:
            agent_uuid (string): agent_uuid
            api_key_uuid (string): api_key_uuid
            agent_uuid_body (string): Agent id Example: '"12345678-1234-1234-1234-123456789012"'.
            api_key_uuid_body (string): API key ID Example: '"12345678-1234-1234-1234-123456789012"'.
            name (string): Name Example: '"Production Key"'.

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if agent_uuid is None:
            raise ValueError("Missing required parameter 'agent_uuid'.")
        if api_key_uuid is None:
            raise ValueError("Missing required parameter 'api_key_uuid'.")
        request_body_data = None
        request_body_data = {
            "agent_uuid": agent_uuid_body,
            "api_key_uuid": api_key_uuid_body,
            "name": name,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/gen-ai/agents/{agent_uuid}/api_keys/{api_key_uuid}"
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

    def genai_delete_agent_api_key(
        self, agent_uuid: str, api_key_uuid: str
    ) -> dict[str, Any]:
        """
        Delete API Key for an Agent

        Args:
            agent_uuid (string): agent_uuid
            api_key_uuid (string): api_key_uuid

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if agent_uuid is None:
            raise ValueError("Missing required parameter 'agent_uuid'.")
        if api_key_uuid is None:
            raise ValueError("Missing required parameter 'api_key_uuid'.")
        url = f"{self.base_url}/v2/gen-ai/agents/{agent_uuid}/api_keys/{api_key_uuid}"
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

    def genai_regenerate_agent_api_key(
        self, agent_uuid: str, api_key_uuid: str
    ) -> dict[str, Any]:
        """
        Regenerate API Key for an Agent

        Args:
            agent_uuid (string): agent_uuid
            api_key_uuid (string): api_key_uuid

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if agent_uuid is None:
            raise ValueError("Missing required parameter 'agent_uuid'.")
        if api_key_uuid is None:
            raise ValueError("Missing required parameter 'api_key_uuid'.")
        request_body_data = None
        url = f"{self.base_url}/v2/gen-ai/agents/{agent_uuid}/api_keys/{api_key_uuid}/regenerate"
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

    def genai_attach_agent_function(
        self,
        agent_uuid: str,
        agent_uuid_body: str | None = None,
        description: str | None = None,
        faas_name: str | None = None,
        faas_namespace: str | None = None,
        function_name: str | None = None,
        input_schema: dict[str, Any] | None = None,
        output_schema: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Add Function Route to an Agent

        Args:
            agent_uuid (string): agent_uuid
            agent_uuid_body (string): Agent id Example: '"12345678-1234-1234-1234-123456789012"'.
            description (string): Function description Example: '"My Function Description"'.
            faas_name (string): The name of the function in the DigitalOcean functions platform Example: '"my-function"'.
            faas_namespace (string): The namespace of the function in the DigitalOcean functions platform Example: '"default"'.
            function_name (string): Function name Example: '"My Function"'.
            input_schema (object): Describe the input schema for the function so the agent may call it
            output_schema (object): Describe the output schema for the function so the agent handle its response

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if agent_uuid is None:
            raise ValueError("Missing required parameter 'agent_uuid'.")
        request_body_data = None
        request_body_data = {
            "agent_uuid": agent_uuid_body,
            "description": description,
            "faas_name": faas_name,
            "faas_namespace": faas_namespace,
            "function_name": function_name,
            "input_schema": input_schema,
            "output_schema": output_schema,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/gen-ai/agents/{agent_uuid}/functions"
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

    def genai_update_agent_function(
        self,
        agent_uuid: str,
        function_uuid: str,
        agent_uuid_body: str | None = None,
        description: str | None = None,
        faas_name: str | None = None,
        faas_namespace: str | None = None,
        function_name: str | None = None,
        function_uuid_body: str | None = None,
        input_schema: dict[str, Any] | None = None,
        output_schema: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Update Function Route for an Agent

        Args:
            agent_uuid (string): agent_uuid
            function_uuid (string): function_uuid
            agent_uuid_body (string): Agent id Example: '"12345678-1234-1234-1234-123456789012"'.
            description (string): Funciton description Example: '"My Function Description"'.
            faas_name (string): The name of the function in the DigitalOcean functions platform Example: '"my-function"'.
            faas_namespace (string): The namespace of the function in the DigitalOcean functions platform Example: '"default"'.
            function_name (string): Function name Example: '"My Function"'.
            function_uuid_body (string): Function id Example: '"12345678-1234-1234-1234-123456789012"'.
            input_schema (object): Describe the input schema for the function so the agent may call it
            output_schema (object): Describe the output schema for the function so the agent handle its response

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if agent_uuid is None:
            raise ValueError("Missing required parameter 'agent_uuid'.")
        if function_uuid is None:
            raise ValueError("Missing required parameter 'function_uuid'.")
        request_body_data = None
        request_body_data = {
            "agent_uuid": agent_uuid_body,
            "description": description,
            "faas_name": faas_name,
            "faas_namespace": faas_namespace,
            "function_name": function_name,
            "function_uuid": function_uuid_body,
            "input_schema": input_schema,
            "output_schema": output_schema,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/gen-ai/agents/{agent_uuid}/functions/{function_uuid}"
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

    def genai_detach_agent_function(
        self, agent_uuid: str, function_uuid: str
    ) -> dict[str, Any]:
        """
        Delete Function Route for an Agent

        Args:
            agent_uuid (string): agent_uuid
            function_uuid (string): function_uuid

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if agent_uuid is None:
            raise ValueError("Missing required parameter 'agent_uuid'.")
        if function_uuid is None:
            raise ValueError("Missing required parameter 'function_uuid'.")
        url = f"{self.base_url}/v2/gen-ai/agents/{agent_uuid}/functions/{function_uuid}"
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

    def genai_attach_knowledge_bases(self, agent_uuid: str) -> dict[str, Any]:
        """
        Attach Knowledge Bases to an Agent

        Args:
            agent_uuid (string): agent_uuid

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if agent_uuid is None:
            raise ValueError("Missing required parameter 'agent_uuid'.")
        request_body_data = None
        url = f"{self.base_url}/v2/gen-ai/agents/{agent_uuid}/knowledge_bases"
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

    def genai_attach_knowledge_base(
        self, agent_uuid: str, knowledge_base_uuid: str
    ) -> dict[str, Any]:
        """
        Attach Knowledge Base to an Agent

        Args:
            agent_uuid (string): agent_uuid
            knowledge_base_uuid (string): knowledge_base_uuid

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if agent_uuid is None:
            raise ValueError("Missing required parameter 'agent_uuid'.")
        if knowledge_base_uuid is None:
            raise ValueError("Missing required parameter 'knowledge_base_uuid'.")
        request_body_data = None
        url = f"{self.base_url}/v2/gen-ai/agents/{agent_uuid}/knowledge_bases/{knowledge_base_uuid}"
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

    def genai_detach_knowledge_base(
        self, agent_uuid: str, knowledge_base_uuid: str
    ) -> dict[str, Any]:
        """
        Detach Knowledge Base from an Agent

        Args:
            agent_uuid (string): agent_uuid
            knowledge_base_uuid (string): knowledge_base_uuid

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if agent_uuid is None:
            raise ValueError("Missing required parameter 'agent_uuid'.")
        if knowledge_base_uuid is None:
            raise ValueError("Missing required parameter 'knowledge_base_uuid'.")
        url = f"{self.base_url}/v2/gen-ai/agents/{agent_uuid}/knowledge_bases/{knowledge_base_uuid}"
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

    def genai_attach_agent(
        self,
        parent_agent_uuid: str,
        child_agent_uuid: str,
        child_agent_uuid_body: str | None = None,
        if_case: str | None = None,
        parent_agent_uuid_body: str | None = None,
        route_name: str | None = None,
    ) -> dict[str, Any]:
        """
        Add Agent Route to an Agent

        Args:
            parent_agent_uuid (string): parent_agent_uuid
            child_agent_uuid (string): child_agent_uuid
            child_agent_uuid_body (string): Routed agent id Example: '"12345678-1234-1234-1234-123456789012"'.
            if_case (string): if_case Example: '"use this to get weather information"'.
            parent_agent_uuid_body (string): A unique identifier for the parent agent. Example: '"12345678-1234-1234-1234-123456789012"'.
            route_name (string): Name of route Example: '"weather_route"'.

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if parent_agent_uuid is None:
            raise ValueError("Missing required parameter 'parent_agent_uuid'.")
        if child_agent_uuid is None:
            raise ValueError("Missing required parameter 'child_agent_uuid'.")
        request_body_data = None
        request_body_data = {
            "child_agent_uuid": child_agent_uuid_body,
            "if_case": if_case,
            "parent_agent_uuid": parent_agent_uuid_body,
            "route_name": route_name,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/gen-ai/agents/{parent_agent_uuid}/child_agents/{child_agent_uuid}"
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

    def genai_update_attached_agent(
        self,
        parent_agent_uuid: str,
        child_agent_uuid: str,
        child_agent_uuid_body: str | None = None,
        if_case: str | None = None,
        parent_agent_uuid_body: str | None = None,
        route_name: str | None = None,
        uuid: str | None = None,
    ) -> dict[str, Any]:
        """
        Update Agent Route for an Agent

        Args:
            parent_agent_uuid (string): parent_agent_uuid
            child_agent_uuid (string): child_agent_uuid
            child_agent_uuid_body (string): Routed agent id Example: '"12345678-1234-1234-1234-123456789012"'.
            if_case (string): Describes the case in which the child agent should be used Example: '"use this to get weather information"'.
            parent_agent_uuid_body (string): A unique identifier for the parent agent. Example: '"12345678-1234-1234-1234-123456789012"'.
            route_name (string): Route name Example: '"weather_route"'.
            uuid (string): Unique id of linkage Example: '"12345678-1234-1234-1234-123456789012"'.

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if parent_agent_uuid is None:
            raise ValueError("Missing required parameter 'parent_agent_uuid'.")
        if child_agent_uuid is None:
            raise ValueError("Missing required parameter 'child_agent_uuid'.")
        request_body_data = None
        request_body_data = {
            "child_agent_uuid": child_agent_uuid_body,
            "if_case": if_case,
            "parent_agent_uuid": parent_agent_uuid_body,
            "route_name": route_name,
            "uuid": uuid,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/gen-ai/agents/{parent_agent_uuid}/child_agents/{child_agent_uuid}"
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

    def genai_detach_agent(
        self, parent_agent_uuid: str, child_agent_uuid: str
    ) -> dict[str, Any]:
        """
        Delete Agent Route for an Agent

        Args:
            parent_agent_uuid (string): parent_agent_uuid
            child_agent_uuid (string): child_agent_uuid

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if parent_agent_uuid is None:
            raise ValueError("Missing required parameter 'parent_agent_uuid'.")
        if child_agent_uuid is None:
            raise ValueError("Missing required parameter 'child_agent_uuid'.")
        url = f"{self.base_url}/v2/gen-ai/agents/{parent_agent_uuid}/child_agents/{child_agent_uuid}"
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

    def genai_get_agent(self, uuid: str) -> dict[str, Any]:
        """
        Retrieve an Existing Agent

        Args:
            uuid (string): uuid

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'.")
        url = f"{self.base_url}/v2/gen-ai/agents/{uuid}"
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

    def genai_update_agent(
        self,
        uuid: str,
        anthropic_key_uuid: str | None = None,
        description: str | None = None,
        instruction: str | None = None,
        k: int | None = None,
        max_tokens: int | None = None,
        model_uuid: str | None = None,
        name: str | None = None,
        open_ai_key_uuid: str | None = None,
        project_id: str | None = None,
        provide_citations: bool | None = None,
        retrieval_method: str | None = None,
        tags: list[str] | None = None,
        temperature: float | None = None,
        top_p: float | None = None,
        uuid_body: str | None = None,
    ) -> dict[str, Any]:
        """
        Update an Agent

        Args:
            uuid (string): uuid
            anthropic_key_uuid (string): Optional anthropic key uuid for use with anthropic models Example: '"12345678-1234-1234-1234-123456789012"'.
            description (string): Agent description Example: '"My Agent Description"'.
            instruction (string): Agent instruction. Instructions help your agent to perform its job effectively. See [Write Effective Agent Instructions](https://docs.digitalocean.com/products/genai-platform/concepts/best-practices/#agent-instructions) for best practices. Example: '"You are an agent who thinks deeply about the world"'.
            k (integer): How many results should be considered from an attached knowledge base Example: '5'.
            max_tokens (integer): Specifies the maximum number of tokens the model can process in a single input or output, set as a number between 1 and 512. This determines the length of each response. Example: '100'.
            model_uuid (string): Identifier for the foundation model. Example: '"12345678-1234-1234-1234-123456789012"'.
            name (string): Agent name Example: '"My New Agent Name"'.
            open_ai_key_uuid (string): Optional OpenAI key uuid for use with OpenAI models Example: '"12345678-1234-1234-1234-123456789012"'.
            project_id (string): The id of the DigitalOcean project this agent will belong to Example: '"12345678-1234-1234-1234-123456789012"'.
            provide_citations (boolean): provide_citations Example: 'True'.
            retrieval_method (string): - RETRIEVAL_METHOD_UNKNOWN: The retrieval method is unknown
         - RETRIEVAL_METHOD_REWRITE: The retrieval method is rewrite
         - RETRIEVAL_METHOD_STEP_BACK: The retrieval method is step back
         - RETRIEVAL_METHOD_SUB_QUERIES: The retrieval method is sub queries
         - RETRIEVAL_METHOD_NONE: The retrieval method is none Example: 'RETRIEVAL_METHOD_UNKNOWN'.
            tags (array): A set of abitrary tags to organize your agent Example: "['example string']".
            temperature (number): Controls the model’s creativity, specified as a number between 0 and 1. Lower values produce more predictable and conservative responses, while higher values encourage creativity and variation. Example: '0.7'.
            top_p (number): Defines the cumulative probability threshold for word selection, specified as a number between 0 and 1. Higher values allow for more diverse outputs, while lower values ensure focused and coherent responses. Example: '0.9'.
            uuid_body (string): Unique agent id Example: '"12345678-1234-1234-1234-123456789012"'.

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'.")
        request_body_data = None
        request_body_data = {
            "anthropic_key_uuid": anthropic_key_uuid,
            "description": description,
            "instruction": instruction,
            "k": k,
            "max_tokens": max_tokens,
            "model_uuid": model_uuid,
            "name": name,
            "open_ai_key_uuid": open_ai_key_uuid,
            "project_id": project_id,
            "provide_citations": provide_citations,
            "retrieval_method": retrieval_method,
            "tags": tags,
            "temperature": temperature,
            "top_p": top_p,
            "uuid": uuid_body,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/gen-ai/agents/{uuid}"
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

    def genai_delete_agent(self, uuid: str) -> dict[str, Any]:
        """
        Delete an Agent

        Args:
            uuid (string): uuid

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'.")
        url = f"{self.base_url}/v2/gen-ai/agents/{uuid}"
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

    def genai_get_agent_children(self, uuid: str) -> dict[str, Any]:
        """
        View Agent Routes

        Args:
            uuid (string): uuid

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'.")
        url = f"{self.base_url}/v2/gen-ai/agents/{uuid}/child_agents"
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

    def update_deployment_visibility(
        self,
        uuid: str,
        uuid_body: str | None = None,
        visibility: str | None = None,
    ) -> dict[str, Any]:
        """
        Update Agent Status

        Args:
            uuid (string): uuid
            uuid_body (string): Unique id Example: '"12345678-1234-1234-1234-123456789012"'.
            visibility (string): - VISIBILITY_UNKNOWN: The status of the deployment is unknown
         - VISIBILITY_DISABLED: The deployment is disabled and will no longer service requests
         - VISIBILITY_PLAYGROUND: Deprecated: No longer a valid state
         - VISIBILITY_PUBLIC: The deployment is public and will service requests from the public internet
         - VISIBILITY_PRIVATE: The deployment is private and will only service requests from other agents, or through API keys Example: 'VISIBILITY_UNKNOWN'.

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'.")
        request_body_data = None
        request_body_data = {
            "uuid": uuid_body,
            "visibility": visibility,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/gen-ai/agents/{uuid}/deployment_visibility"
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

    def genai_list_agent_versions(
        self, uuid: str, page: int | None = None, per_page: int | None = None
    ) -> dict[str, Any]:
        """
        List Agent Versions

        Args:
            uuid (string): uuid
            page (integer): Page number. Example: '1'.
            per_page (integer): Items per page. Example: '1'.

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'.")
        url = f"{self.base_url}/v2/gen-ai/agents/{uuid}/versions"
        query_params = {
            k: v for k, v in [("page", page), ("per_page", per_page)] if v is not None
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

    def update_agent_version_by_uuid(
        self,
        uuid: str,
        uuid_body: str | None = None,
        version_hash: str | None = None,
    ) -> dict[str, Any]:
        """
        Rollback to Agent Version

        Args:
            uuid (string): uuid
            uuid_body (string): Agent unique identifier Example: '"12345678-1234-1234-1234-123456789012"'.
            version_hash (string): Unique identifier Example: 'c3658d8b5c05494cd03ce042926ef08157889ed54b1b74b5ee0b3d66dcee4b73'.

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'.")
        request_body_data = None
        request_body_data = {
            "uuid": uuid_body,
            "version_hash": version_hash,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/gen-ai/agents/{uuid}/versions"
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

    def genai_list_anthropic_api_keys(
        self, page: int | None = None, per_page: int | None = None
    ) -> dict[str, Any]:
        """
        List Anthropic API Keys

        Args:
            page (integer): Page number. Example: '1'.
            per_page (integer): Items per page. Example: '1'.

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        url = f"{self.base_url}/v2/gen-ai/anthropic/keys"
        query_params = {
            k: v for k, v in [("page", page), ("per_page", per_page)] if v is not None
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

    def genai_create_anthropic_api_key(
        self, api_key: str | None = None, name: str | None = None
    ) -> dict[str, Any]:
        """
        Create Anthropic API Key

        Args:
            api_key (string): Anthropic API key Example: '"sk-ant-12345678901234567890123456789012"'.
            name (string): Name of the key Example: '"Production Key"'.

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        request_body_data = None
        request_body_data = {
            "api_key": api_key,
            "name": name,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/gen-ai/anthropic/keys"
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

    def genai_get_anthropic_api_key(self, api_key_uuid: str) -> dict[str, Any]:
        """
        Get Anthropic API Key

        Args:
            api_key_uuid (string): api_key_uuid

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if api_key_uuid is None:
            raise ValueError("Missing required parameter 'api_key_uuid'.")
        url = f"{self.base_url}/v2/gen-ai/anthropic/keys/{api_key_uuid}"
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

    def genai_update_anthropic_api_key(
        self,
        api_key_uuid: str,
        api_key: str | None = None,
        api_key_uuid_body: str | None = None,
        name: str | None = None,
    ) -> dict[str, Any]:
        """
        Update Anthropic API Key

        Args:
            api_key_uuid (string): api_key_uuid
            api_key (string): Anthropic API key Example: '"sk-ant-12345678901234567890123456789012"'.
            api_key_uuid_body (string): API key ID Example: '"12345678-1234-1234-1234-123456789012"'.
            name (string): Name of the key Example: '"Production Key"'.

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if api_key_uuid is None:
            raise ValueError("Missing required parameter 'api_key_uuid'.")
        request_body_data = None
        request_body_data = {
            "api_key": api_key,
            "api_key_uuid": api_key_uuid_body,
            "name": name,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/gen-ai/anthropic/keys/{api_key_uuid}"
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

    def genai_delete_anthropic_api_key(self, api_key_uuid: str) -> dict[str, Any]:
        """
        Delete Anthropic API Key

        Args:
            api_key_uuid (string): api_key_uuid

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if api_key_uuid is None:
            raise ValueError("Missing required parameter 'api_key_uuid'.")
        url = f"{self.base_url}/v2/gen-ai/anthropic/keys/{api_key_uuid}"
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

    def list_agents_by_key_uuid(
        self, uuid: str, page: int | None = None, per_page: int | None = None
    ) -> dict[str, Any]:
        """
        List agents by Anthropic key

        Args:
            uuid (string): uuid
            page (integer): Page number. Example: '1'.
            per_page (integer): Items per page. Example: '1'.

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'.")
        url = f"{self.base_url}/v2/gen-ai/anthropic/keys/{uuid}/agents"
        query_params = {
            k: v for k, v in [("page", page), ("per_page", per_page)] if v is not None
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

    def genai_list_indexing_jobs(
        self, page: int | None = None, per_page: int | None = None
    ) -> dict[str, Any]:
        """
        List Indexing Jobs for a Knowledge Base

        Args:
            page (integer): Page number. Example: '1'.
            per_page (integer): Items per page. Example: '1'.

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        url = f"{self.base_url}/v2/gen-ai/indexing_jobs"
        query_params = {
            k: v for k, v in [("page", page), ("per_page", per_page)] if v is not None
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

    def genai_create_indexing_job(
        self,
        data_source_uuids: list[str] | None = None,
        knowledge_base_uuid: str | None = None,
    ) -> dict[str, Any]:
        """
        Start Indexing Job for a Knowledge Base

        Args:
            data_source_uuids (array): List of data source ids to index, if none are provided, all data sources will be indexed Example: "['example string']".
            knowledge_base_uuid (string): Knowledge base id Example: '"12345678-1234-1234-1234-123456789012"'.

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        request_body_data = None
        request_body_data = {
            "data_source_uuids": data_source_uuids,
            "knowledge_base_uuid": knowledge_base_uuid,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/gen-ai/indexing_jobs"
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

    def list_job_data_sources(self, indexing_job_uuid: str) -> dict[str, Any]:
        """
        List Data Sources for Indexing Job for a Knowledge Base

        Args:
            indexing_job_uuid (string): indexing_job_uuid

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if indexing_job_uuid is None:
            raise ValueError("Missing required parameter 'indexing_job_uuid'.")
        url = (
            f"{self.base_url}/v2/gen-ai/indexing_jobs/{indexing_job_uuid}/data_sources"
        )
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

    def genai_get_indexing_job(self, uuid: str) -> dict[str, Any]:
        """
        Retrieve Status of Indexing Job for a Knowledge Base

        Args:
            uuid (string): uuid

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'.")
        url = f"{self.base_url}/v2/gen-ai/indexing_jobs/{uuid}"
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

    def genai_cancel_indexing_job(
        self, uuid: str, uuid_body: str | None = None
    ) -> dict[str, Any]:
        """
        Cancel Indexing Job for a Knowledge Base

        Args:
            uuid (string): uuid
            uuid_body (string): A unique identifier for an indexing job. Example: '"12345678-1234-1234-1234-123456789012"'.

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'.")
        request_body_data = None
        request_body_data = {
            "uuid": uuid_body,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/gen-ai/indexing_jobs/{uuid}/cancel"
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

    def genai_list_knowledge_bases(
        self, page: int | None = None, per_page: int | None = None
    ) -> dict[str, Any]:
        """
        List Knowledge Bases

        Args:
            page (integer): Page number. Example: '1'.
            per_page (integer): Items per page. Example: '1'.

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        url = f"{self.base_url}/v2/gen-ai/knowledge_bases"
        query_params = {
            k: v for k, v in [("page", page), ("per_page", per_page)] if v is not None
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

    def genai_create_knowledge_base(
        self,
        database_id: str | None = None,
        datasources: list[dict[str, Any]] | None = None,
        embedding_model_uuid: str | None = None,
        name: str | None = None,
        project_id: str | None = None,
        region: str | None = None,
        tags: list[str] | None = None,
        vpc_uuid: str | None = None,
    ) -> dict[str, Any]:
        """
        Create a Knowledge Base

        Args:
            database_id (string): Identifier of the DigitalOcean OpenSearch database this knowledge base will use, optional.
        If not provided, we create a new database for the knowledge base in
        the same region as the knowledge base. Example: '"12345678-1234-1234-1234-123456789012"'.
            datasources (array): The data sources to use for this knowledge base. See [Organize Data Sources](https://docs.digitalocean.com/products/genai-platform/concepts/best-practices/#spaces-buckets) for more information on data sources best practices.
            embedding_model_uuid (string): Identifier for the [embedding model](https://docs.digitalocean.com/products/genai-platform/details/models/#embedding-models). Example: '"12345678-1234-1234-1234-123456789012"'.
            name (string): Name of the knowledge base. Example: '"My Knowledge Base"'.
            project_id (string): Identifier of the DigitalOcean project this knowledge base will belong to. Example: '"12345678-1234-1234-1234-123456789012"'.
            region (string): The datacenter region to deploy the knowledge base in. Example: '"tor1"'.
            tags (array): Tags to organize your knowledge base. Example: "['example string']".
            vpc_uuid (string): The VPC to deploy the knowledge base database in Example: '"12345678-1234-1234-1234-123456789012"'.

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        request_body_data = None
        request_body_data = {
            "database_id": database_id,
            "datasources": datasources,
            "embedding_model_uuid": embedding_model_uuid,
            "name": name,
            "project_id": project_id,
            "region": region,
            "tags": tags,
            "vpc_uuid": vpc_uuid,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/gen-ai/knowledge_bases"
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

    def list_data_source_by_knowledge_base(
        self,
        knowledge_base_uuid: str,
        page: int | None = None,
        per_page: int | None = None,
    ) -> dict[str, Any]:
        """
        List Data Sources for a Knowledge Base

        Args:
            knowledge_base_uuid (string): knowledge_base_uuid
            page (integer): Page number. Example: '1'.
            per_page (integer): Items per page. Example: '1'.

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if knowledge_base_uuid is None:
            raise ValueError("Missing required parameter 'knowledge_base_uuid'.")
        url = f"{self.base_url}/v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/data_sources"
        query_params = {
            k: v for k, v in [("page", page), ("per_page", per_page)] if v is not None
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

    def add_data_source(
        self,
        knowledge_base_uuid: str,
        knowledge_base_uuid_body: str | None = None,
        spaces_data_source: dict[str, Any] | None = None,
        web_crawler_data_source: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Add Data Source to a Knowledge Base

        Args:
            knowledge_base_uuid (string): knowledge_base_uuid
            knowledge_base_uuid_body (string): Knowledge base id Example: '"12345678-1234-1234-1234-123456789012"'.
            spaces_data_source (object): Spaces Bucket Data Source
            web_crawler_data_source (object): WebCrawlerDataSource

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if knowledge_base_uuid is None:
            raise ValueError("Missing required parameter 'knowledge_base_uuid'.")
        request_body_data = None
        request_body_data = {
            "knowledge_base_uuid": knowledge_base_uuid_body,
            "spaces_data_source": spaces_data_source,
            "web_crawler_data_source": web_crawler_data_source,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/data_sources"
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

    def delete_data_source_by_uuid(
        self, knowledge_base_uuid: str, data_source_uuid: str
    ) -> dict[str, Any]:
        """
        Delete a Data Source from a Knowledge Base

        Args:
            knowledge_base_uuid (string): knowledge_base_uuid
            data_source_uuid (string): data_source_uuid

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if knowledge_base_uuid is None:
            raise ValueError("Missing required parameter 'knowledge_base_uuid'.")
        if data_source_uuid is None:
            raise ValueError("Missing required parameter 'data_source_uuid'.")
        url = f"{self.base_url}/v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/data_sources/{data_source_uuid}"
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

    def genai_get_knowledge_base(self, uuid: str) -> dict[str, Any]:
        """
        Retrieve Information About an Existing Knowledge Base

        Args:
            uuid (string): uuid

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'.")
        url = f"{self.base_url}/v2/gen-ai/knowledge_bases/{uuid}"
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

    def genai_update_knowledge_base(
        self,
        uuid: str,
        database_id: str | None = None,
        embedding_model_uuid: str | None = None,
        name: str | None = None,
        project_id: str | None = None,
        tags: list[str] | None = None,
        uuid_body: str | None = None,
    ) -> dict[str, Any]:
        """
        Update a Knowledge Base

        Args:
            uuid (string): uuid
            database_id (string): The id of the DigitalOcean database this knowledge base will use, optiona. Example: '"12345678-1234-1234-1234-123456789012"'.
            embedding_model_uuid (string): Identifier for the foundation model. Example: '"12345678-1234-1234-1234-123456789012"'.
            name (string): Knowledge base name Example: '"My Knowledge Base"'.
            project_id (string): The id of the DigitalOcean project this knowledge base will belong to Example: '"12345678-1234-1234-1234-123456789012"'.
            tags (array): Tags to organize your knowledge base. Example: "['example string']".
            uuid_body (string): Knowledge base id Example: '"12345678-1234-1234-1234-123456789012"'.

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'.")
        request_body_data = None
        request_body_data = {
            "database_id": database_id,
            "embedding_model_uuid": embedding_model_uuid,
            "name": name,
            "project_id": project_id,
            "tags": tags,
            "uuid": uuid_body,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/gen-ai/knowledge_bases/{uuid}"
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

    def genai_delete_knowledge_base(self, uuid: str) -> dict[str, Any]:
        """
        Delete a Knowledge Base

        Args:
            uuid (string): uuid

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'.")
        url = f"{self.base_url}/v2/gen-ai/knowledge_bases/{uuid}"
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

    def genai_list_models(
        self,
        usecases: list[str] | None = None,
        public_only: bool | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> dict[str, Any]:
        """
        List Available Models

        Args:
            usecases (array): Include only models defined for the listed usecases.

         - MODEL_USECASE_UNKNOWN: The use case of the model is unknown
         - MODEL_USECASE_AGENT: The model maybe used in an agent
         - MODEL_USECASE_FINETUNED: The model maybe used for fine tuning
         - MODEL_USECASE_KNOWLEDGEBASE: The model maybe used for knowledge bases (embedding models)
         - MODEL_USECASE_GUARDRAIL: The model maybe used for guardrails
         - MODEL_USECASE_REASONING: The model usecase for reasoning
         - MODEL_USECASE_SERVERLESS: The model usecase for serverless inference Example: "['MODEL_USECASE_UNKNOWN']".
            public_only (boolean): Only include models that are publicly available. Example: 'True'.
            page (integer): Page number. Example: '1'.
            per_page (integer): Items per page. Example: '1'.

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        url = f"{self.base_url}/v2/gen-ai/models"
        query_params = {
            k: v
            for k, v in [
                ("usecases", usecases),
                ("public_only", public_only),
                ("page", page),
                ("per_page", per_page),
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

    def genai_list_model_api_keys(
        self, page: int | None = None, per_page: int | None = None
    ) -> dict[str, Any]:
        """
        List Model API Keys

        Args:
            page (integer): Page number. Example: '1'.
            per_page (integer): Items per page. Example: '1'.

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        url = f"{self.base_url}/v2/gen-ai/models/api_keys"
        query_params = {
            k: v for k, v in [("page", page), ("per_page", per_page)] if v is not None
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

    def genai_create_model_api_key(self, name: str | None = None) -> dict[str, Any]:
        """
        Create a Model API Key

        Args:
            name (string): A human friendly name to identify the key Example: 'Production Key'.

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        request_body_data = None
        request_body_data = {
            "name": name,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/gen-ai/models/api_keys"
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

    def genai_update_model_api_key(
        self,
        api_key_uuid: str,
        api_key_uuid_body: str | None = None,
        name: str | None = None,
    ) -> dict[str, Any]:
        """
        Update API Key for a Model

        Args:
            api_key_uuid (string): api_key_uuid
            api_key_uuid_body (string): API key ID Example: '"12345678-1234-1234-1234-123456789012"'.
            name (string): Name Example: '"Production Key"'.

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if api_key_uuid is None:
            raise ValueError("Missing required parameter 'api_key_uuid'.")
        request_body_data = None
        request_body_data = {
            "api_key_uuid": api_key_uuid_body,
            "name": name,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/gen-ai/models/api_keys/{api_key_uuid}"
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

    def genai_delete_model_api_key(self, api_key_uuid: str) -> dict[str, Any]:
        """
        Delete API Key for a Model

        Args:
            api_key_uuid (string): api_key_uuid

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if api_key_uuid is None:
            raise ValueError("Missing required parameter 'api_key_uuid'.")
        url = f"{self.base_url}/v2/gen-ai/models/api_keys/{api_key_uuid}"
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

    def genai_regenerate_model_api_key(self, api_key_uuid: str) -> dict[str, Any]:
        """
        Regenerate API Key for a Model

        Args:
            api_key_uuid (string): api_key_uuid

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if api_key_uuid is None:
            raise ValueError("Missing required parameter 'api_key_uuid'.")
        request_body_data = None
        url = f"{self.base_url}/v2/gen-ai/models/api_keys/{api_key_uuid}/regenerate"
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

    def genai_list_openai_api_keys(
        self, page: int | None = None, per_page: int | None = None
    ) -> dict[str, Any]:
        """
        List OpenAI API Keys

        Args:
            page (integer): Page number. Example: '1'.
            per_page (integer): Items per page. Example: '1'.

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        url = f"{self.base_url}/v2/gen-ai/openai/keys"
        query_params = {
            k: v for k, v in [("page", page), ("per_page", per_page)] if v is not None
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

    def genai_create_openai_api_key(
        self, api_key: str | None = None, name: str | None = None
    ) -> dict[str, Any]:
        """
        Create OpenAI API Key

        Args:
            api_key (string): OpenAI API key Example: '"sk-proj--123456789098765432123456789"'.
            name (string): Name of the key Example: '"Production Key"'.

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        request_body_data = None
        request_body_data = {
            "api_key": api_key,
            "name": name,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/gen-ai/openai/keys"
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

    def genai_get_openai_api_key(self, api_key_uuid: str) -> dict[str, Any]:
        """
        Get OpenAI API Key

        Args:
            api_key_uuid (string): api_key_uuid

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if api_key_uuid is None:
            raise ValueError("Missing required parameter 'api_key_uuid'.")
        url = f"{self.base_url}/v2/gen-ai/openai/keys/{api_key_uuid}"
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

    def genai_update_openai_api_key(
        self,
        api_key_uuid: str,
        api_key: str | None = None,
        api_key_uuid_body: str | None = None,
        name: str | None = None,
    ) -> dict[str, Any]:
        """
        Update OpenAI API Key

        Args:
            api_key_uuid (string): api_key_uuid
            api_key (string): OpenAI API key Example: '"sk-ant-12345678901234567890123456789012"'.
            api_key_uuid_body (string): API key ID Example: '"12345678-1234-1234-1234-123456789012"'.
            name (string): Name of the key Example: '"Production Key"'.

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if api_key_uuid is None:
            raise ValueError("Missing required parameter 'api_key_uuid'.")
        request_body_data = None
        request_body_data = {
            "api_key": api_key,
            "api_key_uuid": api_key_uuid_body,
            "name": name,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/gen-ai/openai/keys/{api_key_uuid}"
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

    def genai_delete_openai_api_key(self, api_key_uuid: str) -> dict[str, Any]:
        """
        Delete OpenAI API Key

        Args:
            api_key_uuid (string): api_key_uuid

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if api_key_uuid is None:
            raise ValueError("Missing required parameter 'api_key_uuid'.")
        url = f"{self.base_url}/v2/gen-ai/openai/keys/{api_key_uuid}"
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

    def get_agents_by_key_uuid(
        self, uuid: str, page: int | None = None, per_page: int | None = None
    ) -> dict[str, Any]:
        """
        List agents by OpenAI key

        Args:
            uuid (string): uuid
            page (integer): Page number. Example: '1'.
            per_page (integer): Items per page. Example: '1'.

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'.")
        url = f"{self.base_url}/v2/gen-ai/openai/keys/{uuid}/agents"
        query_params = {
            k: v for k, v in [("page", page), ("per_page", per_page)] if v is not None
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

    def genai_list_datacenter_regions(
        self,
        serves_inference: bool | None = None,
        serves_batch: bool | None = None,
    ) -> dict[str, Any]:
        """
        List Datacenter Regions

        Args:
            serves_inference (boolean): Include datacenters that serve inference. Example: 'True'.
            serves_batch (boolean): Include datacenters that are capable of running batch jobs. Example: 'True'.

        Returns:
            dict[str, Any]: A successful response.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            GenAI Platform (Public Preview)
        """
        url = f"{self.base_url}/v2/gen-ai/regions"
        query_params = {
            k: v
            for k, v in [
                ("serves_inference", serves_inference),
                ("serves_batch", serves_batch),
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
            self.one_clicks_list,
            self.one_clicks_install_kubernetes,
            self.account_get,
            self.ssh_keys_list,
            self.ssh_keys_create,
            self.ssh_keys_get,
            self.ssh_keys_update,
            self.ssh_keys_delete,
            self.actions_list,
            self.actions_get,
            self.apps_list,
            self.apps_create,
            self.apps_delete,
            self.apps_get,
            self.apps_update,
            self.apps_restart,
            self.get_app_component_logs,
            self.get_component_execution_details,
            self.apps_get_instances,
            self.apps_list_deployments,
            self.apps_create_deployment,
            self.apps_get_deployment,
            self.apps_cancel_deployment,
            self.apps_get_logs,
            self.apps_get_logs_aggregate,
            self.apps_get_exec,
            self.get_app_logs,
            self.apps_list_instance_sizes,
            self.apps_get_instance_size,
            self.apps_list_regions,
            self.apps_validate_app_spec,
            self.apps_list_alerts,
            self.apps_assign_alert_destinations,
            self.apps_create_rollback,
            self.apps_validate_rollback,
            self.apps_commit_rollback,
            self.apps_revert_rollback,
            self.get_app_bandwidth_daily,
            self.create_daily_bandwidth_metrics,
            self.apps_get_health,
            self.cdn_list_endpoints,
            self.cdn_create_endpoint,
            self.cdn_get_endpoint,
            self.cdn_update_endpoints,
            self.cdn_delete_endpoint,
            self.cdn_purge_cache,
            self.certificates_list,
            self.certificates_create,
            self.certificates_get,
            self.certificates_delete,
            self.balance_get,
            self.billing_history_list,
            self.invoices_list,
            self.invoices_get_by_uuid,
            self.invoices_get_csv_by_uuid,
            self.invoices_get_pdf_by_uuid,
            self.invoices_get_summary_by_uuid,
            self.databases_list_options,
            self.databases_list_clusters,
            self.databases_create_cluster,
            self.databases_get_cluster,
            self.databases_destroy_cluster,
            self.databases_get_config,
            self.databases_patch_config,
            self.databases_get_ca,
            self.databases_get_migration_status,
            self.start_online_migration,
            self.delete_online_migration_by_id,
            self.databases_update_region,
            self.databases_update_cluster_size,
            self.databases_list_firewall_rules,
            self.update_database_cluster_firewall,
            self.update_database_maintenance,
            self.databases_install_update,
            self.databases_list_backups,
            self.databases_list_replicas,
            self.databases_create_replica,
            self.databases_list_events_logs,
            self.databases_get_replica,
            self.databases_destroy_replica,
            self.databases_promote_replica,
            self.databases_list_users,
            self.databases_add_user,
            self.databases_get_user,
            self.databases_delete_user,
            self.databases_update_user,
            self.databases_reset_auth,
            self.databases_list,
            self.databases_add,
            self.databases_get,
            self.databases_delete,
            self.databases_list_connection_pools,
            self.databases_add_connection_pool,
            self.databases_get_connection_pool,
            self.update_database_pool,
            self.delete_pool,
            self.databases_get_eviction_policy,
            self.update_eviction_policy,
            self.databases_get_sql_mode,
            self.databases_update_sql_mode,
            self.databases_update_major_version,
            self.databases_list_kafka_topics,
            self.databases_create_kafka_topic,
            self.databases_get_kafka_topic,
            self.databases_update_kafka_topic,
            self.databases_delete_kafka_topic,
            self.databases_list_logsink,
            self.databases_create_logsink,
            self.databases_get_logsink,
            self.databases_update_logsink,
            self.databases_delete_logsink,
            self.get_database_metrics_credentials,
            self.update_database_credentials,
            self.list_database_indexes,
            self.delete_database_index_by_name,
            self.domains_list,
            self.domains_create,
            self.domains_get,
            self.domains_delete,
            self.domains_list_records,
            self.domains_create_record,
            self.domains_get_record,
            self.domains_patch_record,
            self.domains_update_record,
            self.domains_delete_record,
            self.droplets_list,
            self.droplets_create,
            self.droplets_destroy_by_tag,
            self.droplets_get,
            self.droplets_destroy,
            self.droplets_list_backups,
            self.droplets_get_backup_policy,
            self.droplets_list_backup_policies,
            self.list_supported_policies,
            self.droplets_list_snapshots,
            self.droplet_actions_list,
            self.droplet_actions_post,
            self.droplet_actions_post_by_tag,
            self.droplet_actions_get,
            self.droplets_list_kernels,
            self.droplets_list_firewalls,
            self.droplets_list_neighbors,
            self.destroy_droplet_with_resources,
            self.destroy_select,
            self.delete_droplet_resources,
            self.get_droplet_status,
            self.retry_droplet_with_resources,
            self.autoscalepools_list,
            self.autoscalepools_create,
            self.autoscalepools_get,
            self.autoscalepools_update,
            self.autoscalepools_delete,
            self.delete_autoscale_pool_dangerously,
            self.autoscalepools_list_members,
            self.autoscalepools_list_history,
            self.firewalls_list,
            self.firewalls_create,
            self.firewalls_get,
            self.firewalls_update,
            self.firewalls_delete,
            self.firewalls_assign_droplets,
            self.firewalls_delete_droplets,
            self.firewalls_add_tags,
            self.firewalls_delete_tags,
            self.firewalls_add_rules,
            self.firewalls_delete_rules,
            self.floating_ips_list,
            self.floating_ips_create,
            self.floating_ips_get,
            self.floating_ips_delete,
            self.floating_ips_action_list,
            self.floating_ips_action_post,
            self.floating_ips_action_get,
            self.functions_list_namespaces,
            self.functions_create_namespace,
            self.functions_get_namespace,
            self.functions_delete_namespace,
            self.functions_list_triggers,
            self.functions_create_trigger,
            self.functions_get_trigger,
            self.functions_update_trigger,
            self.functions_delete_trigger,
            self.images_list,
            self.images_create_custom,
            self.images_get,
            self.images_update,
            self.images_delete,
            self.image_actions_list,
            self.image_actions_post,
            self.image_actions_get,
            self.kubernetes_list_clusters,
            self.kubernetes_create_cluster,
            self.kubernetes_get_cluster,
            self.kubernetes_update_cluster,
            self.kubernetes_delete_cluster,
            self.destroy_cluster_resources,
            self.delete_cluster_resources,
            self.destroy_cluster_with_resources,
            self.kubernetes_get_kubeconfig,
            self.kubernetes_get_credentials,
            self.get_cluster_upgrades,
            self.kubernetes_upgrade_cluster,
            self.kubernetes_list_node_pools,
            self.kubernetes_add_node_pool,
            self.kubernetes_get_node_pool,
            self.kubernetes_update_node_pool,
            self.kubernetes_delete_node_pool,
            self.kubernetes_delete_node,
            self.kubernetes_recycle_node_pool,
            self.kubernetes_get_cluster_user,
            self.kubernetes_list_options,
            self.kubernetes_run_cluster_lint,
            self.get_cluster_lint,
            self.kubernetes_add_registry,
            self.kubernetes_remove_registry,
            self.kubernetes_get_status_messages,
            self.load_balancers_create,
            self.load_balancers_list,
            self.load_balancers_get,
            self.load_balancers_update,
            self.load_balancers_delete,
            self.load_balancers_delete_cache,
            self.load_balancers_add_droplets,
            self.load_balancers_remove_droplets,
            self.add_forwarding_rule,
            self.delete_lb_forwarding_rules,
            self.monitoring_list_alert_policy,
            self.monitoring_create_alert_policy,
            self.monitoring_get_alert_policy,
            self.monitoring_update_alert_policy,
            self.monitoring_delete_alert_policy,
            self.get_droplet_bandwidth_metrics,
            self.get_droplet_cpu_metrics,
            self.get_droplet_filesystem_free,
            self.get_droplet_filesystem_size,
            self.get_droplet_load_metrics,
            self.get_droplet_load5_metrics,
            self.get_droplet_load_metric,
            self.get_droplet_memory_cached,
            self.get_droplet_memory_free,
            self.get_droplet_memory_total,
            self.get_droplet_memory_available,
            self.get_app_memory_percentage,
            self.get_app_cpu_metrics,
            self.get_app_restart_count,
            self.get_frontend_connections,
            self.get_lb_frontend_connections_limit,
            self.get_frontend_cpu_utilization,
            self.get_frontend_firewall_bytes,
            self.get_lb_frontend_fw_dropped_pkts,
            self.get_load_balancer_responses,
            self.fetch_frontend_request_rate,
            self.get_frontend_network_throughput,
            self.get_frontend_udp_throughput,
            self.get_frontend_tcp_throughput,
            self.get_frontend_nlb_tcp_throughput,
            self.get_nlb_udp_throughput,
            self.get_frontend_tls_connections,
            self.get_frontend_tls_connections_limit,
            self.get_tls_exceeding_rate_limit,
            self.get_droplet_session_duration_avg,
            self.get_droplet_session_duration_50p,
            self.get_droplet_session_duration_95p,
            self.get_droplet_response_time,
            self.get_droplet_http_response_time,
            self.get_droplets_http_response_timep_95p,
            self.get_droplets_http_response_timep_99p,
            self.get_droplet_queue_size,
            self.get_droplet_responses,
            self.get_droplet_connections,
            self.get_droplet_health_checks,
            self.get_load_balancer_downtime,
            self.get_current_autoscale_instances,
            self.list_target_instances,
            self.get_droplet_cpu_utilization,
            self.get_droplet_target_cpu_utilization,
            self.get_droplet_memory_utilization,
            self.get_autoscale_memory_target,
            self.monitoring_create_destination,
            self.monitoring_list_destinations,
            self.monitoring_get_destination,
            self.monitoring_update_destination,
            self.monitoring_delete_destination,
            self.monitoring_create_sink,
            self.monitoring_list_sinks,
            self.monitoring_get_sink,
            self.monitoring_delete_sink,
            self.partner_attachments_list,
            self.partner_attachments_create,
            self.partner_attachments_get,
            self.partner_attachments_patch,
            self.partner_attachments_delete,
            self.get_bgp_auth_key_by_pa_id,
            self.get_partner_network_remote_routes,
            self.update_remote_routes,
            self.get_partner_service_key,
            self.create_service_key,
            self.projects_list,
            self.projects_create,
            self.projects_get_default,
            self.projects_update_default,
            self.projects_patch_default,
            self.projects_get,
            self.projects_update,
            self.projects_patch,
            self.projects_delete,
            self.projects_list_resources,
            self.projects_assign_resources,
            self.list_project_resources,
            self.create_default_project_resource,
            self.regions_list,
            self.registry_get,
            self.registry_create,
            self.registry_delete,
            self.registry_get_subscription,
            self.registry_update_subscription,
            self.registry_get_docker_credentials,
            self.registry_validate_name,
            self.registry_list_repositories,
            self.registry_list_repositories_v,
            self.registry_list_repository_tags,
            self.registry_delete_repository_tag,
            self.get_repository_digests,
            self.delete_manifest_digest,
            self.registry_run_garbage_collection,
            self.registry_get_garbage_collection,
            self.list_registry_garbage_collections,
            self.update_garbage_collection,
            self.registry_get_options,
            self.droplets_list_neighbors_ids,
            self.reserved_ips_list,
            self.reserved_ips_create,
            self.reserved_ips_get,
            self.reserved_ips_delete,
            self.reserved_ips_actions_list,
            self.reserved_ips_actions_post,
            self.reserved_ips_actions_get,
            self.reserved_ipv_list,
            self.reserved_ipv_create,
            self.reserved_ipv_get,
            self.reserved_ipv_delete,
            self.reserved_ipv_actions_post,
            self.sizes_list,
            self.snapshots_list,
            self.snapshots_get,
            self.snapshots_delete,
            self.spaces_key_list,
            self.spaces_key_create,
            self.spaces_key_get,
            self.spaces_key_delete,
            self.spaces_key_update,
            self.spaces_key_patch,
            self.tags_list,
            self.tags_create,
            self.tags_get,
            self.tags_delete,
            self.tags_assign_resources,
            self.tags_unassign_resources,
            self.volumes_list,
            self.volumes_create,
            self.volumes_delete_by_name,
            self.volume_actions_post,
            self.volume_snapshots_get_by_id,
            self.volume_snapshots_delete_by_id,
            self.volumes_get,
            self.volumes_delete,
            self.volume_actions_list,
            self.volume_actions_post_by_id,
            self.volume_actions_get,
            self.volume_snapshots_list,
            self.volume_snapshots_create,
            self.vpcs_list,
            self.vpcs_create,
            self.vpcs_get,
            self.vpcs_update,
            self.vpcs_patch,
            self.vpcs_delete,
            self.vpcs_list_members,
            self.vpcs_list_peerings,
            self.vpcs_create_peerings,
            self.vpcs_patch_peerings,
            self.vpc_peerings_list,
            self.vpc_peerings_create,
            self.vpc_peerings_get,
            self.vpc_peerings_patch,
            self.vpc_peerings_delete,
            self.uptime_list_checks,
            self.uptime_create_check,
            self.uptime_get_check,
            self.uptime_update_check,
            self.uptime_delete_check,
            self.uptime_get_check_state,
            self.uptime_list_alerts,
            self.uptime_create_alert,
            self.uptime_get_alert,
            self.uptime_update_alert,
            self.uptime_delete_alert,
            self.genai_list_agents,
            self.genai_create_agent,
            self.genai_list_agent_api_keys,
            self.genai_create_agent_api_key,
            self.genai_update_agent_api_key,
            self.genai_delete_agent_api_key,
            self.genai_regenerate_agent_api_key,
            self.genai_attach_agent_function,
            self.genai_update_agent_function,
            self.genai_detach_agent_function,
            self.genai_attach_knowledge_bases,
            self.genai_attach_knowledge_base,
            self.genai_detach_knowledge_base,
            self.genai_attach_agent,
            self.genai_update_attached_agent,
            self.genai_detach_agent,
            self.genai_get_agent,
            self.genai_update_agent,
            self.genai_delete_agent,
            self.genai_get_agent_children,
            self.update_deployment_visibility,
            self.genai_list_agent_versions,
            self.update_agent_version_by_uuid,
            self.genai_list_anthropic_api_keys,
            self.genai_create_anthropic_api_key,
            self.genai_get_anthropic_api_key,
            self.genai_update_anthropic_api_key,
            self.genai_delete_anthropic_api_key,
            self.list_agents_by_key_uuid,
            self.genai_list_indexing_jobs,
            self.genai_create_indexing_job,
            self.list_job_data_sources,
            self.genai_get_indexing_job,
            self.genai_cancel_indexing_job,
            self.genai_list_knowledge_bases,
            self.genai_create_knowledge_base,
            self.list_data_source_by_knowledge_base,
            self.add_data_source,
            self.delete_data_source_by_uuid,
            self.genai_get_knowledge_base,
            self.genai_update_knowledge_base,
            self.genai_delete_knowledge_base,
            self.genai_list_models,
            self.genai_list_model_api_keys,
            self.genai_create_model_api_key,
            self.genai_update_model_api_key,
            self.genai_delete_model_api_key,
            self.genai_regenerate_model_api_key,
            self.genai_list_openai_api_keys,
            self.genai_create_openai_api_key,
            self.genai_get_openai_api_key,
            self.genai_update_openai_api_key,
            self.genai_delete_openai_api_key,
            self.get_agents_by_key_uuid,
            self.genai_list_datacenter_regions,
        ]
