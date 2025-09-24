from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration

from universal_mcp.applications.twitter.api_segments.compliance_api import ComplianceApi
from universal_mcp.applications.twitter.api_segments.dm_conversations_api import (
    DmConversationsApi,
)
from universal_mcp.applications.twitter.api_segments.dm_events_api import DmEventsApi
from universal_mcp.applications.twitter.api_segments.likes_api import LikesApi
from universal_mcp.applications.twitter.api_segments.lists_api import ListsApi
from universal_mcp.applications.twitter.api_segments.openapi_json_api import (
    OpenapiJsonApi,
)
from universal_mcp.applications.twitter.api_segments.spaces_api import SpacesApi
from universal_mcp.applications.twitter.api_segments.trends_api import TrendsApi
from universal_mcp.applications.twitter.api_segments.tweets_api import TweetsApi
from universal_mcp.applications.twitter.api_segments.usage_api import UsageApi
from universal_mcp.applications.twitter.api_segments.users_api import UsersApi


class TwitterApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="twitter", integration=integration, **kwargs)
        self.base_url = "https://api.twitter.com"
        self.compliance = ComplianceApi(self)
        self.dm_conversations = DmConversationsApi(self)
        self.dm_events = DmEventsApi(self)
        self.likes = LikesApi(self)
        self.lists = ListsApi(self)
        self.openapi_json = OpenapiJsonApi(self)
        self.spaces = SpacesApi(self)
        self.trends = TrendsApi(self)
        self.tweets = TweetsApi(self)
        self.usage = UsageApi(self)
        self.users = UsersApi(self)

    def list_tools(self):
        all_tools = []
        all_tools.extend(self.compliance.list_tools())
        all_tools.extend(self.dm_conversations.list_tools())
        all_tools.extend(self.dm_events.list_tools())
        all_tools.extend(self.likes.list_tools())
        all_tools.extend(self.lists.list_tools())
        all_tools.extend(self.openapi_json.list_tools())
        all_tools.extend(self.spaces.list_tools())
        all_tools.extend(self.trends.list_tools())
        all_tools.extend(self.tweets.list_tools())
        all_tools.extend(self.usage.list_tools())
        all_tools.extend(self.users.list_tools())
        return all_tools
