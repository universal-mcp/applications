from typing import Any

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class FigmaApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="figma", integration=integration, **kwargs)
        self.base_url = "https://api.figma.com"

    def get_file(
        self,
        file_key,
        version=None,
        ids=None,
        depth=None,
        geometry=None,
        plugin_data=None,
        branch_data=None,
    ) -> dict[str, Any]:
        """
        Retrieves a specified file's data (including versions, geometry, and plugin information) from the API using a unique file identifier.

        Args:
            file_key (string): file_key
            version (string): A specific version ID to get. Omitting this will get the current version of the file.
            ids (string): Comma separated list of nodes that you care about in the document. If specified, only a subset of the document will be returned corresponding to the nodes listed, their children, and everything between the root node and the listed nodes. Note: There may be other nodes included in the returned JSON that are outside the ancestor chains of the desired nodes. The response may also include dependencies of anything in the nodes' subtrees. For example, if a node subtree contains an instance of a local component that lives elsewhere in that file, that component and its ancestor chain will also be included. For historical reasons, top-level canvas nodes are always returned, regardless of whether they are listed in the `ids` parameter. This quirk may be removed in a future version of the API.
            depth (number): Positive integer representing how deep into the document tree to traverse. For example, setting this to 1 returns only Pages, setting it to 2 returns Pages and all top level objects on each page. Not setting this parameter returns all nodes.
            geometry (string): Set to "paths" to export vector data.
            plugin_data (string): A comma separated list of plugin IDs and/or the string "shared". Any data present in the document written by those plugins will be included in the result in the `pluginData` and `sharedPluginData` properties.
            branch_data (boolean): Returns branch metadata for the requested file. If the file is a branch, the main file's key will be included in the returned response. If the file has branches, their metadata will be included in the returned response. Default: false.

        Returns:
            dict[str, Any]: Response from the GET /v1/files/{file_key} endpoint.

        Tags:
            Files, important
        """
        if file_key is None:
            raise ValueError("Missing required parameter 'file_key'")
        url = f"{self.base_url}/v1/files/{file_key}"
        query_params = {
            k: v
            for k, v in [
                ("version", version),
                ("ids", ids),
                ("depth", depth),
                ("geometry", geometry),
                ("plugin_data", plugin_data),
                ("branch_data", branch_data),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_file_nodes(
        self, file_key, ids, version=None, depth=None, geometry=None, plugin_data=None
    ) -> dict[str, Any]:
        """
        Retrieves nodes related to a file identified by the "file_key" using the specified query parameters for filtering by "ids", "version", "depth", "geometry", and "plugin_data".

        Args:
            file_key (string): file_key
            ids (string): A comma separated list of node IDs to retrieve and convert.
            version (string): A specific version ID to get. Omitting this will get the current version of the file.
            depth (number): Positive integer representing how deep into the node tree to traverse. For example, setting this to 1 will return only the children directly underneath the desired nodes. Not setting this parameter returns all nodes. Note: this parameter behaves differently from the same parameter in the `GET /v1/files/:key` endpoint. In this endpoint, the depth will be counted starting from the desired node rather than the document root node.
            geometry (string): Set to "paths" to export vector data.
            plugin_data (string): A comma separated list of plugin IDs and/or the string "shared". Any data present in the document written by those plugins will be included in the result in the `pluginData` and `sharedPluginData` properties.

        Returns:
            dict[str, Any]: Response from the GET /v1/files/{file_key}/nodes endpoint.

        Tags:
            Files, important
        """
        if file_key is None:
            raise ValueError("Missing required parameter 'file_key'")
        url = f"{self.base_url}/v1/files/{file_key}/nodes"
        query_params = {
            k: v
            for k, v in [
                ("ids", ids),
                ("version", version),
                ("depth", depth),
                ("geometry", geometry),
                ("plugin_data", plugin_data),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_images(
        self,
        file_key,
        ids,
        version=None,
        scale=None,
        format=None,
        svg_outline_text=None,
        svg_include_id=None,
        svg_include_node_id=None,
        svg_simplify_stroke=None,
        contents_only=None,
        use_absolute_bounds=None,
    ) -> dict[str, Any]:
        """
        Retrieves an image specified by the `file_key` using the GET method, allowing optional query parameters for customization such as formatting, scaling, and SVG options.

        Args:
            file_key (string): file_key
            ids (string): A comma separated list of node IDs to render.
            version (string): A specific version ID to get. Omitting this will get the current version of the file.
            scale (number): A number between 0.01 and 4, the image scaling factor.
            format (string): A string enum for the image output format.
            svg_outline_text (boolean): Whether text elements are rendered as outlines (vector paths) or as `<text>` elements in SVGs. Rendering text elements as outlines guarantees that the text looks exactly the same in the SVG as it does in the browser/inside Figma. Exporting as `<text>` allows text to be selectable inside SVGs and generally makes the SVG easier to read. However, this relies on the browser's rendering engine which can vary between browsers and/or operating systems. As such, visual accuracy is not guaranteed as the result could look different than in Figma.
            svg_include_id (boolean): Whether to include id attributes for all SVG elements. Adds the layer name to the `id` attribute of an svg element.
            svg_include_node_id (boolean): Whether to include node id attributes for all SVG elements. Adds the node id to a `data-node-id` attribute of an svg element.
            svg_simplify_stroke (boolean): Whether to simplify inside/outside strokes and use stroke attribute if possible instead of `<mask>`.
            contents_only (boolean): Whether content that overlaps the node should be excluded from rendering. Passing false (i.e., rendering overlaps) may increase processing time, since more of the document must be included in rendering.
            use_absolute_bounds (boolean): Use the full dimensions of the node regardless of whether or not it is cropped or the space around it is empty. Use this to export text nodes without cropping.

        Returns:
            dict[str, Any]: Response from the GET /v1/images/{file_key} endpoint.

        Tags:
            Files, important
        """
        if file_key is None:
            raise ValueError("Missing required parameter 'file_key'")
        url = f"{self.base_url}/v1/images/{file_key}"
        query_params = {
            k: v
            for k, v in [
                ("ids", ids),
                ("version", version),
                ("scale", scale),
                ("format", format),
                ("svg_outline_text", svg_outline_text),
                ("svg_include_id", svg_include_id),
                ("svg_include_node_id", svg_include_node_id),
                ("svg_simplify_stroke", svg_simplify_stroke),
                ("contents_only", contents_only),
                ("use_absolute_bounds", use_absolute_bounds),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_image_fills(self, file_key) -> dict[str, Any]:
        """
        Retrieves images associated with a file identified by the `{file_key}` using the `/v1/files/{file_key}/images` API endpoint.

        Args:
            file_key (string): file_key

        Returns:
            dict[str, Any]: Response from the GET /v1/files/{file_key}/images endpoint.

        Tags:
            Files
        """
        if file_key is None:
            raise ValueError("Missing required parameter 'file_key'")
        url = f"{self.base_url}/v1/files/{file_key}/images"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_team_projects(self, team_id) -> dict[str, Any]:
        """
        Retrieves a list of projects associated with a specific team identified by the team_id parameter.

        Args:
            team_id (string): team_id

        Returns:
            dict[str, Any]: Response from the GET /v1/teams/{team_id}/projects endpoint.

        Tags:
            Projects
        """
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        url = f"{self.base_url}/v1/teams/{team_id}/projects"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_project_files(self, project_id, branch_data=None) -> dict[str, Any]:
        """
        Retrieves files from a specified project, optionally including branch data, using the provided project identifier.

        Args:
            project_id (string): project_id
            branch_data (boolean): Returns branch metadata in the response for each main file with a branch inside the project.

        Returns:
            dict[str, Any]: Response from the GET /v1/projects/{project_id}/files endpoint.

        Tags:
            Projects
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = f"{self.base_url}/v1/projects/{project_id}/files"
        query_params = {
            k: v for k, v in [("branch_data", branch_data)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_file_versions(
        self, file_key, page_size=None, before=None, after=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of file versions using the "GET" method, filtering by file key and optional query parameters for pagination and sorting.

        Args:
            file_key (string): file_key
            page_size (number): The number of items returned in a page of the response. If not included, `page_size` is `30`.
            before (number): A version ID for one of the versions in the history. Gets versions before this ID. Used for paginating. If the response is not paginated, this link returns the same data in the current response.
            after (number): A version ID for one of the versions in the history. Gets versions after this ID. Used for paginating. If the response is not paginated, this property is not included.

        Returns:
            dict[str, Any]: Response from the GET /v1/files/{file_key}/versions endpoint.

        Tags:
            Files
        """
        if file_key is None:
            raise ValueError("Missing required parameter 'file_key'")
        url = f"{self.base_url}/v1/files/{file_key}/versions"
        query_params = {
            k: v
            for k, v in [("page_size", page_size), ("before", before), ("after", after)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_comments(self, file_key, as_md=None) -> dict[str, Any]:
        """
        Retrieves comments associated with a specified file and optionally returns them in Markdown format based on the query parameter.

        Args:
            file_key (string): file_key
            as_md (boolean): If enabled, will return comments as their markdown equivalents when applicable.

        Returns:
            dict[str, Any]: Response from the GET /v1/files/{file_key}/comments endpoint.

        Tags:
            Comments
        """
        if file_key is None:
            raise ValueError("Missing required parameter 'file_key'")
        url = f"{self.base_url}/v1/files/{file_key}/comments"
        query_params = {k: v for k, v in [("as_md", as_md)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def post_comment(
        self, file_key, message, comment_id=None, client_meta=None
    ) -> dict[str, Any]:
        """
        Creates a new comment on a file specified by the file_key and returns an appropriate status code.

        Args:
            file_key (string): file_key
            message (string): The text contents of the comment to post.
            comment_id (string): The ID of the comment to reply to, if any. This must be a root comment. You cannot reply to other replies (a comment that has a parent_id).
            client_meta (string): The position where to place the comment.

        Returns:
            dict[str, Any]: Response from the POST /v1/files/{file_key}/comments endpoint.

        Tags:
            Comments
        """
        if file_key is None:
            raise ValueError("Missing required parameter 'file_key'")
        request_body = {
            "message": message,
            "comment_id": comment_id,
            "client_meta": client_meta,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v1/files/{file_key}/comments"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_comment(self, file_key, comment_id) -> dict[str, Any]:
        """
        Deletes a specified comment from a file identified by its file key and comment ID.

        Args:
            file_key (string): file_key
            comment_id (string): comment_id

        Returns:
            dict[str, Any]: Response from the DELETE /v1/files/{file_key}/comments/{comment_id} endpoint.

        Tags:
            Comments
        """
        if file_key is None:
            raise ValueError("Missing required parameter 'file_key'")
        if comment_id is None:
            raise ValueError("Missing required parameter 'comment_id'")
        url = f"{self.base_url}/v1/files/{file_key}/comments/{comment_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_comment_reactions(
        self, file_key, comment_id, cursor=None
    ) -> dict[str, Any]:
        """
        Retrieves reactions for a specific comment in a file using the provided file key and comment ID.

        Args:
            file_key (string): file_key
            comment_id (string): comment_id
            cursor (string): Cursor for pagination, retrieved from the response of the previous call.

        Returns:
            dict[str, Any]: Response from the GET /v1/files/{file_key}/comments/{comment_id}/reactions endpoint.

        Tags:
            Comment Reactions
        """
        if file_key is None:
            raise ValueError("Missing required parameter 'file_key'")
        if comment_id is None:
            raise ValueError("Missing required parameter 'comment_id'")
        url = f"{self.base_url}/v1/files/{file_key}/comments/{comment_id}/reactions"
        query_params = {k: v for k, v in [("cursor", cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def post_comment_reaction(self, file_key, comment_id, emoji) -> dict[str, Any]:
        """
        Adds a reaction to a specific comment on a file identified by the file key and comment ID using the "POST" method at the "/v1/files/{file_key}/comments/{comment_id}/reactions" endpoint.

        Args:
            file_key (string): file_key
            comment_id (string): comment_id
            emoji (string): The emoji type of reaction as shortcode (e.g. `:heart:`, `:+1::skin-tone-2:`). The list of accepted emoji shortcodes can be found in [this file](https://raw.githubusercontent.com/missive/emoji-mart/main/packages/emoji-mart-data/sets/14/native.json) under the top-level emojis and aliases fields, with optional skin tone modifiers when applicable.

        Returns:
            dict[str, Any]: Response from the POST /v1/files/{file_key}/comments/{comment_id}/reactions endpoint.

        Tags:
            Comment Reactions
        """
        if file_key is None:
            raise ValueError("Missing required parameter 'file_key'")
        if comment_id is None:
            raise ValueError("Missing required parameter 'comment_id'")
        request_body = {
            "emoji": emoji,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v1/files/{file_key}/comments/{comment_id}/reactions"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_comment_reaction(self, file_key, comment_id, emoji) -> dict[str, Any]:
        """
        Removes a reaction emoji from a comment on a file using the specified emoji parameter.

        Args:
            file_key (string): file_key
            comment_id (string): comment_id
            emoji (string): Specifies the emoji identifier to be removed from the comment reaction.

        Returns:
            dict[str, Any]: Response from the DELETE /v1/files/{file_key}/comments/{comment_id}/reactions endpoint.

        Tags:
            Comment Reactions
        """
        if file_key is None:
            raise ValueError("Missing required parameter 'file_key'")
        if comment_id is None:
            raise ValueError("Missing required parameter 'comment_id'")
        url = f"{self.base_url}/v1/files/{file_key}/comments/{comment_id}/reactions"
        query_params = {k: v for k, v in [("emoji", emoji)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_me(self) -> Any:
        """
        Retrieves the authenticated user's profile data.

        Returns:
            Any: Response from the GET /v1/me endpoint.

        Tags:
            Users, important
        """
        url = f"{self.base_url}/v1/me"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_team_components(
        self, team_id, page_size=None, after=None, before=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of components for a specified team with pagination support using page_size, after, and before parameters.

        Args:
            team_id (string): team_id
            page_size (number): Number of items to return in a paged list of results. Defaults to 30.
            after (number): Cursor indicating which id after which to start retrieving components for. Exclusive with before. The cursor value is an internally tracked integer that doesn't correspond to any Ids.
            before (number): Cursor indicating which id before which to start retrieving components for. Exclusive with after. The cursor value is an internally tracked integer that doesn't correspond to any Ids.

        Returns:
            dict[str, Any]: Response from the GET /v1/teams/{team_id}/components endpoint.

        Tags:
            Components
        """
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        url = f"{self.base_url}/v1/teams/{team_id}/components"
        query_params = {
            k: v
            for k, v in [("page_size", page_size), ("after", after), ("before", before)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_file_components(self, file_key) -> dict[str, Any]:
        """
        Retrieves a list of components associated with a file identified by the specified file key using the API endpoint "/v1/files/{file_key}/components".

        Args:
            file_key (string): file_key

        Returns:
            dict[str, Any]: Response from the GET /v1/files/{file_key}/components endpoint.

        Tags:
            Components
        """
        if file_key is None:
            raise ValueError("Missing required parameter 'file_key'")
        url = f"{self.base_url}/v1/files/{file_key}/components"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_component(self, key) -> dict[str, Any]:
        """
        Retrieves component information for a specific key using the API endpoint at "/v1/components/{key}" with the GET method.

        Args:
            key (string): key

        Returns:
            dict[str, Any]: Response from the GET /v1/components/{key} endpoint.

        Tags:
            Components
        """
        if key is None:
            raise ValueError("Missing required parameter 'key'")
        url = f"{self.base_url}/v1/components/{key}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_team_component_sets(
        self, team_id, page_size=None, after=None, before=None
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of component sets associated with a specific team ID, supporting pagination via page size, after, and before query parameters.

        Args:
            team_id (string): team_id
            page_size (number): Number of items to return in a paged list of results. Defaults to 30.
            after (number): Cursor indicating which id after which to start retrieving component sets for. Exclusive with before. The cursor value is an internally tracked integer that doesn't correspond to any Ids.
            before (number): Cursor indicating which id before which to start retrieving component sets for. Exclusive with after. The cursor value is an internally tracked integer that doesn't correspond to any Ids.

        Returns:
            dict[str, Any]: Response from the GET /v1/teams/{team_id}/component_sets endpoint.

        Tags:
            Component Sets
        """
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        url = f"{self.base_url}/v1/teams/{team_id}/component_sets"
        query_params = {
            k: v
            for k, v in [("page_size", page_size), ("after", after), ("before", before)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_file_component_sets(self, file_key) -> dict[str, Any]:
        """
        Retrieves the component sets associated with a file identified by a specific file key using the "GET" method at the "/v1/files/{file_key}/component_sets" endpoint.

        Args:
            file_key (string): file_key

        Returns:
            dict[str, Any]: Response from the GET /v1/files/{file_key}/component_sets endpoint.

        Tags:
            Component Sets
        """
        if file_key is None:
            raise ValueError("Missing required parameter 'file_key'")
        url = f"{self.base_url}/v1/files/{file_key}/component_sets"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_component_set(self, key) -> dict[str, Any]:
        """
        Retrieves a component set by its unique key identifier and returns the associated component data.

        Args:
            key (string): key

        Returns:
            dict[str, Any]: Response from the GET /v1/component_sets/{key} endpoint.

        Tags:
            Component Sets
        """
        if key is None:
            raise ValueError("Missing required parameter 'key'")
        url = f"{self.base_url}/v1/component_sets/{key}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_team_styles(
        self, team_id, page_size=None, after=None, before=None
    ) -> dict[str, Any]:
        """
        Retrieves paginated style resources associated with a specific team using query parameters for pagination control.

        Args:
            team_id (string): team_id
            page_size (number): Number of items to return in a paged list of results. Defaults to 30.
            after (number): Cursor indicating which id after which to start retrieving styles for. Exclusive with before. The cursor value is an internally tracked integer that doesn't correspond to any Ids.
            before (number): Cursor indicating which id before which to start retrieving styles for. Exclusive with after. The cursor value is an internally tracked integer that doesn't correspond to any Ids.

        Returns:
            dict[str, Any]: Response from the GET /v1/teams/{team_id}/styles endpoint.

        Tags:
            Styles
        """
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        url = f"{self.base_url}/v1/teams/{team_id}/styles"
        query_params = {
            k: v
            for k, v in [("page_size", page_size), ("after", after), ("before", before)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_file_styles(self, file_key) -> dict[str, Any]:
        """
        Retrieves styles information for a specific file identified by the file key using the API endpoint "/v1/files/{file_key}/styles" with the GET method.

        Args:
            file_key (string): file_key

        Returns:
            dict[str, Any]: Response from the GET /v1/files/{file_key}/styles endpoint.

        Tags:
            Styles
        """
        if file_key is None:
            raise ValueError("Missing required parameter 'file_key'")
        url = f"{self.base_url}/v1/files/{file_key}/styles"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_style(self, key) -> dict[str, Any]:
        """
        Retrieves a style object associated with the specified key using the "GET" method at the "/v1/styles/{key}" endpoint.

        Args:
            key (string): key

        Returns:
            dict[str, Any]: Response from the GET /v1/styles/{key} endpoint.

        Tags:
            Styles
        """
        if key is None:
            raise ValueError("Missing required parameter 'key'")
        url = f"{self.base_url}/v1/styles/{key}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def post_webhook(
        self, event_type, team_id, endpoint, passcode, status=None, description=None
    ) -> dict[str, Any]:
        """
        Registers a new webhook to receive HTTP callbacks for specified events, returning success or error status codes.

        Args:
            event_type (string): An enum representing the possible events that a webhook can subscribe to
            team_id (string): Team id to receive updates about
            endpoint (string): The HTTP endpoint that will receive a POST request when the event triggers. Max length 2048 characters.
            passcode (string): String that will be passed back to your webhook endpoint to verify that it is being called by Figma. Max length 100 characters.
            status (string): An enum representing the possible statuses you can set a webhook to:
        - `ACTIVE`: The webhook is healthy and receive all events
        - `PAUSED`: The webhook is paused and will not receive any events
            description (string): User provided description or name for the webhook. Max length 150 characters.

        Returns:
            dict[str, Any]: Response from the POST /v2/webhooks endpoint.

        Tags:
            Webhooks
        """
        request_body = {
            "event_type": event_type,
            "team_id": team_id,
            "endpoint": endpoint,
            "passcode": passcode,
            "status": status,
            "description": description,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/webhooks"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_webhook(self, webhook_id) -> dict[str, Any]:
        """
        Retrieves information about a specific webhook by its ID using the "GET" method at the path "/v2/webhooks/{webhook_id}".

        Args:
            webhook_id (string): webhook_id

        Returns:
            dict[str, Any]: Response from the GET /v2/webhooks/{webhook_id} endpoint.

        Tags:
            Webhooks
        """
        if webhook_id is None:
            raise ValueError("Missing required parameter 'webhook_id'")
        url = f"{self.base_url}/v2/webhooks/{webhook_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def put_webhook(
        self, webhook_id, event_type, endpoint, passcode, status=None, description=None
    ) -> dict[str, Any]:
        """
        Updates an existing webhook's configuration using the provided webhook ID and returns an HTTP status code indicating success or failure.

        Args:
            webhook_id (string): webhook_id
            event_type (string): An enum representing the possible events that a webhook can subscribe to
            endpoint (string): The HTTP endpoint that will receive a POST request when the event triggers. Max length 2048 characters.
            passcode (string): String that will be passed back to your webhook endpoint to verify that it is being called by Figma. Max length 100 characters.
            status (string): An enum representing the possible statuses you can set a webhook to:
        - `ACTIVE`: The webhook is healthy and receive all events
        - `PAUSED`: The webhook is paused and will not receive any events
            description (string): User provided description or name for the webhook. Max length 150 characters.

        Returns:
            dict[str, Any]: Response from the PUT /v2/webhooks/{webhook_id} endpoint.

        Tags:
            Webhooks
        """
        if webhook_id is None:
            raise ValueError("Missing required parameter 'webhook_id'")
        request_body = {
            "event_type": event_type,
            "endpoint": endpoint,
            "passcode": passcode,
            "status": status,
            "description": description,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v2/webhooks/{webhook_id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_webhook(self, webhook_id) -> dict[str, Any]:
        """
        Deletes a webhook identified by its `webhook_id`, permanently removing it to manage and optimize webhook configurations.

        Args:
            webhook_id (string): webhook_id

        Returns:
            dict[str, Any]: Response from the DELETE /v2/webhooks/{webhook_id} endpoint.

        Tags:
            Webhooks
        """
        if webhook_id is None:
            raise ValueError("Missing required parameter 'webhook_id'")
        url = f"{self.base_url}/v2/webhooks/{webhook_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_team_webhooks(self, team_id) -> dict[str, Any]:
        """
        Retrieves a list of webhooks for a specified team using the "GET" method, with the team identified by the `team_id` path parameter.

        Args:
            team_id (string): team_id

        Returns:
            dict[str, Any]: Response from the GET /v2/teams/{team_id}/webhooks endpoint.

        Tags:
            Webhooks
        """
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        url = f"{self.base_url}/v2/teams/{team_id}/webhooks"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_webhook_requests(self, webhook_id) -> dict[str, Any]:
        """
        Retrieves a list of requests for a specific webhook identified by `{webhook_id}` using the "GET" method.

        Args:
            webhook_id (string): webhook_id

        Returns:
            dict[str, Any]: Response from the GET /v2/webhooks/{webhook_id}/requests endpoint.

        Tags:
            Webhooks
        """
        if webhook_id is None:
            raise ValueError("Missing required parameter 'webhook_id'")
        url = f"{self.base_url}/v2/webhooks/{webhook_id}/requests"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_activity_logs(
        self, events=None, start_time=None, end_time=None, limit=None, order=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of activity logs filtered by specified events, time range, and other parameters, returning the results in a specified order with a limited number of entries.

        Args:
            events (string): Event type(s) to include in the response. Can have multiple values separated by comma. All events are returned by default.
            start_time (number): Unix timestamp of the least recent event to include. This param defaults to one year ago if unspecified. Events prior to one year ago are not available.
            end_time (number): Unix timestamp of the most recent event to include. This param defaults to the current timestamp if unspecified.
            limit (number): Maximum number of events to return. This param defaults to 1000 if unspecified.
            order (string): Event order by timestamp. This param can be either "asc" (default) or "desc".

        Returns:
            dict[str, Any]: Response from the GET /v1/activity_logs endpoint.

        Tags:
            Activity Logs
        """
        url = f"{self.base_url}/v1/activity_logs"
        query_params = {
            k: v
            for k, v in [
                ("events", events),
                ("start_time", start_time),
                ("end_time", end_time),
                ("limit", limit),
                ("order", order),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_payments(
        self,
        plugin_payment_token=None,
        user_id=None,
        community_file_id=None,
        plugin_id=None,
        widget_id=None,
    ) -> dict[str, Any]:
        """
        Retrieves payment information based on specified parameters, including plugin payment token, user ID, community file ID, plugin ID, and widget ID, using the "/v1/payments" API endpoint with a GET request.

        Args:
            plugin_payment_token (string): Short-lived token returned from "getPluginPaymentTokenAsync" in the plugin payments API and used to authenticate to this endpoint. Read more about generating this token through "Calling the Payments REST API from a plugin or widget" below.
            user_id (number): The ID of the user to query payment information about. You can get the user ID by having the user OAuth2 to the Figma REST API.
            community_file_id (number): The ID of the Community file to query a user's payment information on. You can get the Community file ID from the file's Community page (look for the number after "file/" in the URL). Provide exactly one of "community_file_id", "plugin_id", or "widget_id".
            plugin_id (number): The ID of the plugin to query a user's payment information on. You can get the plugin ID from the plugin's manifest, or from the plugin's Community page (look for the number after "plugin/" in the URL). Provide exactly one of "community_file_id", "plugin_id", or "widget_id".
            widget_id (number): The ID of the widget to query a user's payment information on. You can get the widget ID from the widget's manifest, or from the widget's Community page (look for the number after "widget/" in the URL). Provide exactly one of "community_file_id", "plugin_id", or "widget_id".

        Returns:
            dict[str, Any]: Response from the GET /v1/payments endpoint.

        Tags:
            Payments
        """
        url = f"{self.base_url}/v1/payments"
        query_params = {
            k: v
            for k, v in [
                ("plugin_payment_token", plugin_payment_token),
                ("user_id", user_id),
                ("community_file_id", community_file_id),
                ("plugin_id", plugin_id),
                ("widget_id", widget_id),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_local_variables(self, file_key) -> dict[str, Any]:
        """
        Retrieves local variables for a file specified by the "file_key" using the "GET" method.

        Args:
            file_key (string): file_key

        Returns:
            dict[str, Any]: Response from the GET /v1/files/{file_key}/variables/local endpoint.

        Tags:
            Variables
        """
        if file_key is None:
            raise ValueError("Missing required parameter 'file_key'")
        url = f"{self.base_url}/v1/files/{file_key}/variables/local"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_published_variables(self, file_key) -> dict[str, Any]:
        """
        Retrieves the published variables for a file identified by the `{file_key}` using the `GET` method.

        Args:
            file_key (string): file_key

        Returns:
            dict[str, Any]: Response from the GET /v1/files/{file_key}/variables/published endpoint.

        Tags:
            Variables
        """
        if file_key is None:
            raise ValueError("Missing required parameter 'file_key'")
        url = f"{self.base_url}/v1/files/{file_key}/variables/published"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def post_variables(
        self,
        file_key,
        variableCollections=None,
        variableModes=None,
        variables=None,
        variableModeValues=None,
    ) -> dict[str, Any]:
        """
        Creates variables for a specific file identified by its file_key and returns an appropriate status code based on the operation's outcome.

        Args:
            file_key (string): file_key
            variableCollections (array): For creating, updating, and deleting variable collections.
            variableModes (array): For creating, updating, and deleting modes within variable collections.
            variables (array): For creating, updating, and deleting variables.
            variableModeValues (array): For setting a specific value, given a variable and a mode.

        Returns:
            dict[str, Any]: Response from the POST /v1/files/{file_key}/variables endpoint.

        Tags:
            Variables
        """
        if file_key is None:
            raise ValueError("Missing required parameter 'file_key'")
        request_body = {
            "variableCollections": variableCollections,
            "variableModes": variableModes,
            "variables": variables,
            "variableModeValues": variableModeValues,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v1/files/{file_key}/variables"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_dev_resources(self, file_key, node_ids=None) -> dict[str, Any]:
        """
        Retrieves development resources associated with a specific file, identified by its file_key, with optional filtering by node IDs.

        Args:
            file_key (string): file_key
            node_ids (string): Comma separated list of nodes that you care about in the document. If specified, only dev resources attached to these nodes will be returned. If not specified, all dev resources in the file will be returned.

        Returns:
            dict[str, Any]: Response from the GET /v1/files/{file_key}/dev_resources endpoint.

        Tags:
            Dev Resources
        """
        if file_key is None:
            raise ValueError("Missing required parameter 'file_key'")
        url = f"{self.base_url}/v1/files/{file_key}/dev_resources"
        query_params = {k: v for k, v in [("node_ids", node_ids)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def post_dev_resources(self, dev_resources) -> dict[str, Any]:
        """
        Creates developer resources via the API and returns a status response.

        Args:
            dev_resources (array): An array of dev resources.

        Returns:
            dict[str, Any]: Response from the POST /v1/dev_resources endpoint.

        Tags:
            Dev Resources
        """
        request_body = {
            "dev_resources": dev_resources,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v1/dev_resources"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def put_dev_resources(self, dev_resources) -> dict[str, Any]:
        """
        Replaces a specific developer resource at the specified path with updated data, returning a status code for success or error conditions.

        Args:
            dev_resources (array): An array of dev resources.

        Returns:
            dict[str, Any]: Response from the PUT /v1/dev_resources endpoint.

        Tags:
            Dev Resources
        """
        request_body = {
            "dev_resources": dev_resources,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v1/dev_resources"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_dev_resource(self, file_key, dev_resource_id) -> Any:
        """
        Deletes a specific development resource associated with a file using the provided file key and development resource ID.

        Args:
            file_key (string): file_key
            dev_resource_id (string): dev_resource_id

        Returns:
            Any: Response from the DELETE /v1/files/{file_key}/dev_resources/{dev_resource_id} endpoint.

        Tags:
            Dev Resources
        """
        if file_key is None:
            raise ValueError("Missing required parameter 'file_key'")
        if dev_resource_id is None:
            raise ValueError("Missing required parameter 'dev_resource_id'")
        url = f"{self.base_url}/v1/files/{file_key}/dev_resources/{dev_resource_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [
            self.get_file,
            self.get_file_nodes,
            self.get_images,
            self.get_image_fills,
            self.get_team_projects,
            self.get_project_files,
            self.get_file_versions,
            self.get_comments,
            self.post_comment,
            self.delete_comment,
            self.get_comment_reactions,
            self.post_comment_reaction,
            self.delete_comment_reaction,
            self.get_me,
            self.get_team_components,
            self.get_file_components,
            self.get_component,
            self.get_team_component_sets,
            self.get_file_component_sets,
            self.get_component_set,
            self.get_team_styles,
            self.get_file_styles,
            self.get_style,
            self.post_webhook,
            self.get_webhook,
            self.put_webhook,
            self.delete_webhook,
            self.get_team_webhooks,
            self.get_webhook_requests,
            self.get_activity_logs,
            self.get_payments,
            self.get_local_variables,
            self.get_published_variables,
            self.post_variables,
            self.get_dev_resources,
            self.post_dev_resources,
            self.put_dev_resources,
            self.delete_dev_resource,
        ]
