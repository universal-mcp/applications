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
        files: Any = None,
        params: dict = None,
        content_type: str = None,
        **kwargs,
    ):
        return self.main_app_client._post(
            url,
            data=data,
            files=files,
            params=params,
            content_type=content_type,
            **kwargs,
        )

    def _put(
        self,
        url: str,
        data: Any = None,
        files: Any = None,
        params: dict = None,
        content_type: str = None,
        **kwargs,
    ):
        return self.main_app_client._put(
            url,
            data=data,
            files=files,
            params=params,
            content_type=content_type,
            **kwargs,
        )

    def _patch(self, url: str, data: Any = None, params: dict = None, **kwargs):
        return self.main_app_client._patch(url, data=data, params=params, **kwargs)

    def _delete(self, url: str, params: dict = None, **kwargs):
        return self.main_app_client._delete(url, params=params, **kwargs)
