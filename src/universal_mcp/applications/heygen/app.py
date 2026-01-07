from typing import Any, Literal, Optional, Dict, Union
from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class HeygenApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="heygen", integration=integration, **kwargs)
        self.base_url = "https://api.heygen.com"

    async def _aget_headers(self) -> dict[str, Any]:
        credentials = await self.integration.get_credentials_async()
        api_key = credentials.get("api_key") or credentials.get("API_KEY") or credentials.get("apiKey")
        return {"x-api-key": f"{api_key}", "Content-Type": "application/json", "Accept": "application/json"}

    async def get_v2_avatars(self) -> Any:
        """
        Retrieves a list of avatar objects from the /v2/avatars API endpoint.

        Returns:
            A JSON-decoded object containing the paginated list of avatars.

        Raises:
            requests.exceptions.HTTPError: If the HTTP request to the /v2/avatars endpoint returns an unsuccessful status code.

        Tags:
            get, list, avatars, api
        """
        url = f"{self.base_url}/v2/avatars"
        response = await self._aget(url=url)
        return self._handle_response(response)

    async def list_avatar_groups(self, include_public: bool = False) -> Any:
        """
        Retrieves a list of avatar groups from the /v2/avatar_group.list API endpoint.

        Args:
            include_public: Whether to include public avatar groups in the response. Defaults to False.

        Returns:
            A JSON-decoded object containing the list of avatar groups.

        Raises:
            requests.exceptions.HTTPError: If the HTTP request returns an unsuccessful status code.

        Tags:
            list, avatar_groups, api
        """
        url = f"{self.base_url}/v2/avatar_group.list"
        params = {"include_public": str(include_public).lower()}    
        response = await self._aget(url=url, params=params)
        return self._handle_response(response)

    async def list_avatars_in_group(self, group_id: str) -> Any:
        """
        Retrieves a list of avatars from a specific avatar group.

        Args:
            group_id: The unique identifier of the avatar group.

        Returns:
            A JSON-decoded object containing the list of avatars in the group.

        Raises:
            requests.exceptions.HTTPError: If the HTTP request returns an unsuccessful status code.

        Tags:
            list, avatars, avatar_group, api
        """
        url = f"{self.base_url}/v2/avatar_group/{group_id}/avatars"
        response = await self._aget(url=url)
        return self._handle_response(response)

    async def get_avatar_details(self, avatar_id: str) -> Any:
        """
        Retrieves detailed information about a specific avatar by its ID.

        Args:
            avatar_id: The unique identifier of the avatar.

        Returns:
            A JSON-decoded object containing the avatar details.

        Raises:
            requests.exceptions.HTTPError: If the HTTP request returns an unsuccessful status code.

        Tags:
            get, avatar, details, api
        """
        url = f"{self.base_url}/v2/avatar/{avatar_id}/details"
        response = await self._aget(url=url)
        return self._handle_response(response)


    async def create_avatar_video(
        self,
        # --- Character ---
        avatar_id: str = None,
        talking_photo_id: str = None,
        avatar_style: str = "normal",
        talking_style: str = "stable",
        talking_photo_style: str = "circle",
        
        # --- Voice ---
        input_text: str = None,
        voice_id: str = None,
        voice_type: Literal["text", "audio", "silence"] = "text",
        silence_duration: float = 1, 
        voice_speed: float = 1.0, 
        voice_pitch: int = 0,    
        voice_emotion: Optional[Literal["Excited", "Friendly", "Serious", "Soothing", "Broadcaster"]] = None,
        audio_asset_id: str = None,
        audio_url: str = None,
        
        # --- Background ---
        background_type: Literal["color", "image", "video"] = "color",
        background_value: str = "#008000", 
        background_play_style: Literal["freeze", "loop", "fit_to_scene", "once"] = "freeze",
        background_fit: Literal["crop", "cover", "contain", "none"] = "cover",
        background_url: str = None,
        background_image_asset_id: str = None,
        background_video_asset_id: str = None,
        
        # --- Text Overlay ---
        overlay_text: str = None,
        overlay_font_size: float = None,
        overlay_font_weight: Optional[Literal["bold"]] = None,
        overlay_color: str = None, 
        overlay_position: Dict[str, Any] = None, 
        overlay_text_align: Optional[Literal["left", "center", "right"]] = None,
        line_height: float = 1.0, 
        
        # --- Top Level ---
        title: str = None,
        caption: bool = False,
        callback_id: str = None,
        width: int = 1280,
        height: int = 720,
        folder_id: str = None,
        callback_url: str = None,
    ) -> Any:
        """
        Creates a new avatar video using the /v2/video/generate API endpoint.

        Args:
            avatar_id: The unique identifier of the avatar to use.
            talking_photo_id: The unique identifier of the talking photo to use.
            avatar_style: Style of the avatar (e.g., "normal", "casual"). Defaults to "normal".
            talking_style: Speaking style for talking photo (e.g., "stable"). Defaults to "stable".
            talking_photo_style: Visual style for talking photo (e.g., "circle", "square"). Defaults to "circle".
            input_text: The text script for the avatar/voice to speak.
            voice_id: Unique identifier for the voice.
            voice_type: Type of voice input ("text", "audio", "silence"). Defaults to "text".
            silence_duration: Duration of silence in seconds (if voice_type is "silence").
            voice_speed: Speed of the voice (0.5 to 2.0). Defaults to 1.0.
            voice_pitch: Pitch of the voice (-20 to 20). Defaults to 0.
            voice_emotion: Emotion of the voice (e.g., "Excited", "Friendly").
            audio_asset_id: ID of an uploaded audio asset (if voice_type is "audio").
            audio_url: URL of an audio file (if voice_type is "audio").
            background_type: Type of background ("color", "image", "video"). Defaults to "color".
            background_value: Hex color code (if background_type is "color"). Defaults to "#008000".
            background_play_style: Play style for image/video backgrounds ("freeze", "loop", etc.). Defaults to "freeze".
            background_fit: How the background fits ("cover", "contain", etc.). Defaults to "cover".
            background_url: URL for background image/video.
            background_image_asset_id: Asset ID for background image.
            background_video_asset_id: Asset ID for background video.
            overlay_text: Text to display on the video.
            overlay_font_size: Font size for overlay text.
            overlay_font_weight: Font weight (e.g., "bold").
            overlay_color: Hex color for overlay text.
            overlay_position: Dictionary for position (e.g., {"x": 10, "y": 10}).
            overlay_text_align: Text alignment ("left", "center", "right").
            line_height: Line height for overlay text. Defaults to 1.0.
            title: Title of the video.
            caption: Whether to include captions. Defaults to False.
            callback_id: Custom ID for callback tracking.
            width: Video width. Defaults to 1280.
            height: Video height. Defaults to 720.
            folder_id: ID of the folder to save the video in.
            callback_url: Webhook URL for status updates.

        Returns:
            A JSON-decoded object containing the generated video details (e.g., video_id).

        Raises:
            requests.exceptions.HTTPError: If the HTTP request returns an unsuccessful status code.

        Tags:
            create, video, avatar, api, important
        """
        url = f"{self.base_url}/v2/video/generate"

        # 1. Character construction
        character = {}
        if avatar_id:
            character["type"] = "avatar"
            character["avatar_id"] = avatar_id
            character["avatar_style"] = avatar_style
        elif talking_photo_id:
            character["type"] = "talking_photo"
            character["talking_photo_id"] = talking_photo_id
            character["talking_style"] = talking_style
            if talking_photo_style:
                character["talking_photo_style"] = talking_photo_style

        # 2. Voice construction
        voice = {"type": voice_type}
        
        if voice_type == "text":
            if input_text: voice["input_text"] = input_text
            if voice_id: voice["voice_id"] = voice_id
            
            # Optional attributes for text voice
            if voice_speed != 1.0: voice["speed"] = voice_speed
            if voice_pitch != 0: voice["pitch"] = voice_pitch
            if voice_emotion: voice["emotion"] = voice_emotion
            
        elif voice_type == "silence":
            if silence_duration:
                # Docs specify this must be a string
                voice["duration"] = str(silence_duration)
                
        elif voice_type == "audio":
            if audio_asset_id: voice["audio_asset_id"] = audio_asset_id
            if audio_url: voice["audio_url"] = audio_url

        # 3. Background construction
        background = {"type": background_type}
        if background_type == "color":
            background["value"] = background_value
        elif background_type in ["image", "video"]:
            background["play_style"] = background_play_style
            background["fit"] = background_fit
            if background_url:
                background["url"] = background_url
            if background_image_asset_id:
                background["image_asset_id"] = background_image_asset_id
            if background_video_asset_id:
                background["video_asset_id"] = background_video_asset_id

        # 4. Video Input Assembly
        video_input = {
            "character": character,
            "voice": voice,
            "background": background,
            "dimension": {
                "width": width,
                "height": height
            }
        }

        # 5. Text Overlay construction (Optional)
        if overlay_text:
            text_obj = {
                "type": "text", # Allowed: text (hardcoded as it is the only option)
                "text": overlay_text,
                "line_height": line_height
            }
            if overlay_font_size: text_obj["font_size"] = overlay_font_size
            if overlay_font_weight: text_obj["font_weight"] = overlay_font_weight
            if overlay_color: text_obj["color"] = overlay_color
            if overlay_position: text_obj["position"] = overlay_position
            if overlay_text_align: text_obj["text_align"] = overlay_text_align
            
            video_input["text"] = text_obj

        # 6. Final Payload
        payload = {
            "video_inputs": [video_input],
            "caption": caption
        }

        if title: payload["title"] = title
        if callback_id: payload["callback_id"] = callback_id
        if folder_id: payload["folder_id"] = folder_id
        if callback_url: payload["callback_url"] = callback_url

        response = await self._apost(url=url, data=payload)
        return self._handle_response(response)

    async def get_video_status(
        self,
        video_id: str
    ) -> Any:
        """
        Retrieves the status and details of a specific video by ID using the /v1/video_status.get endpoint.

        Args:
            video_id: The unique identifier of the video.

        Returns:
            A JSON-decoded object containing the video status and details (e.g., status, video_url).

        Raises:
            requests.exceptions.HTTPError: If the HTTP request returns an unsuccessful status code.

        Tags:
            get, video, status, api
        """
        url = f"{self.base_url}/v1/video_status.get"
        
        params = {
            "video_id": video_id
        }
        
        response = await self._aget(url=url, params=params)
        return self._handle_response(response)

    async def create_folder(
        self,
        name: str,
        # Allowed values from screenshot: video_translate, instant_avatar, video, asset, brand_kit, mixed
        project_type: Literal[
            "video_translate", 
            "instant_avatar", 
            "video", 
            "asset", 
            "brand_kit", 
            "mixed"
        ] = "mixed",
        parent_id: Optional[str] = None
    ) -> Any:
        """
        Creates a new folder under your account using the /v1/folders/create endpoint.

        Args:
            name: The name of the folder.
            project_type: The type of projects the folder will contain. Defaults to "mixed".
                          Allowed values: "video_translate", "instant_avatar", "video", "asset", "brand_kit", "mixed".
            parent_id: Optional ID of the parent folder.

        Returns:
            A JSON-decoded object containing the created folder details.

        Raises:
            requests.exceptions.HTTPError: If the HTTP request returns an unsuccessful status code.

        Tags:
            create, folder, api
        """
        url = f"{self.base_url}/v1/folders/create"
        
        payload = {
            "name": name,
            "project_type": project_type
        }
        
        if parent_id:
            payload["parent_id"] = parent_id
            
        response = await self._apost(url=url, data=payload)
        return self._handle_response(response)

    async def list_folders(
        self,
        limit: Optional[int] = None, # Accepts values from 0 to 100
        parent_id: Optional[str] = None,
        name_filter: Optional[str] = None,
        is_trash: bool = False,
        token: Optional[str] = None
    ) -> Any:
        """
        Retrieves a paginated list of folders created under your account using the /v1/folders endpoint.

        Args:
            limit: The maximum number of folders to return (0 to 100).
            parent_id: Optional ID of the parent folder to list children of.
            name_filter: Optional string to filter folders by name.
            is_trash: Whether to list folders in the trash. Defaults to False.
            token: Pagination token for retrieving the next page of results.

        Returns:
            A JSON-decoded object containing the list of folders and pagination info.

        Raises:
            requests.exceptions.HTTPError: If the HTTP request returns an unsuccessful status code.

        Tags:
            list, folders, api
        """
        url = f"{self.base_url}/v1/folders"
        
        params = {}
        
        if limit is not None:
            params["limit"] = limit
        if parent_id:
            params["parent_id"] = parent_id
        if name_filter:
            params["name_filter"] = name_filter
        if is_trash:
            params["is_trash"] = "true"
        if token:
            params["token"] = token
            
        response = await self._aget(url=url, params=params)
        return self._handle_response(response)

    async def update_folder(
        self,
        folder_id: str,
        name: str
    ) -> Any:
        """
        Updates the name of an existing folder using the /v1/folders/{folder_id} endpoint.

        Args:
            folder_id: The unique identifier of the folder to update.
            name: The new name for the folder.

        Returns:
            A JSON-decoded object containing the updated folder details.

        Raises:
            requests.exceptions.HTTPError: If the HTTP request returns an unsuccessful status code.

        Tags:
            update, folder, api
        """
        url = f"{self.base_url}/v1/folders/{folder_id}"
        payload = {
            "name": name
        }
        
        response = await self._apost(url=url, data=payload)
        return self._handle_response(response)

    async def trash_folder(
        self,
        folder_id: str
    ) -> Any:
        """
        Deletes (trashes) a specific folder by its unique folder ID using the /v1/folders/{folder_id}/trash endpoint.

        Args:
            folder_id: The unique identifier of the folder to move to trash.

        Returns:
            A JSON-decoded object confirming the action.

        Raises:
            requests.exceptions.HTTPError: If the HTTP request returns an unsuccessful status code.

        Tags:
            delete, trash, folder, api
        """
        url = f"{self.base_url}/v1/folders/{folder_id}/trash"
        response = await self._apost(url=url)
        return self._handle_response(response)

    async def restore_folder(
        self,
        folder_id: str
    ) -> Any:
        """
        Restores a previously deleted folder using the /v1/folders/{folder_id}/restore endpoint.

        Args:
            folder_id: The unique identifier of the folder to restore.

        Returns:
            A JSON-decoded object confirming the action.

        Raises:
            requests.exceptions.HTTPError: If the HTTP request returns an unsuccessful status code.

        Tags:
            restore, folder, api
        """
        url = f"{self.base_url}/v1/folders/{folder_id}/restore"        
        response = await self._apost(url=url)
        return self._handle_response(response)

    def list_tools(self):
        return [
            self.get_v2_avatars,
            self.list_avatar_groups,
            self.list_avatars_in_group,
            self.get_avatar_details,
            self.create_avatar_video,
            self.get_video_status,
            self.create_folder,
            self.list_folders,
            self.update_folder,
            self.trash_folder,
            self.restore_folder,
        ]
