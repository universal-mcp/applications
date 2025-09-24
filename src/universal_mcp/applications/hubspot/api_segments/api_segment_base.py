from typing import Any


class APISegmentBase:
    def __init__(self, main_app_client: Any):
        self.main_app_client = main_app_client

    def _get(self, url: str, params: dict = None, **kwargs):
        return self.main_app_client._get(url, params=params, **kwargs)

    def _post(
        self,
        url: str,
        data: Any = None,
        params: dict = None,
        content_type: str = None,
        files: Any = None,
        **kwargs,
    ):
        return self.main_app_client._post(
            url,
            data=data,
            params=params,
            content_type=content_type,
            files=files,
            **kwargs,
        )

    def _put(
        self,
        url: str,
        data: Any = None,
        params: dict = None,
        content_type: str = None,
        files: Any = None,
        **kwargs,
    ):
        return self.main_app_client._put(
            url,
            data=data,
            params=params,
            content_type=content_type,
            files=files,
            **kwargs,
        )

    def _patch(self, url: str, data: Any = None, params: dict = None, **kwargs):
        return self.main_app_client._patch(url, data=data, params=params, **kwargs)

    def _delete(self, url: str, params: dict = None, **kwargs):
        return self.main_app_client._delete(url, params=params, **kwargs)

    def _handle_response(self, response):
        return self.main_app_client._handle_response(response)
