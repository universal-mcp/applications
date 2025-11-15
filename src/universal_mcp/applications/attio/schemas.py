from typing import Any, Optional, List
from pydantic import BaseModel, Field

# Generated Response Models


class GetobjectsresponseDataItem(BaseModel):
    id: dict[str, Any]
    api_slug: Any
    singular_noun: Any
    plural_noun: Any
    created_at: str


class Getobjectsresponse(BaseModel):
    data: List[GetobjectsresponseDataItem]


class Postobjectsresponse(BaseModel):
    data: dict[str, Any]


class GetattributesresponseDataItem(BaseModel):
    id: dict[str, Any]
    title: str
    description: Any
    api_slug: str
    type: str
    is_system_attribute: bool
    is_writable: bool
    is_required: bool
    is_unique: bool
    is_multiselect: bool
    is_default_value_enabled: bool
    is_archived: bool
    default_value: Any
    relationship: Any
    created_at: str
    config: dict[str, Any]


class Getattributesresponse(BaseModel):
    data: List[GetattributesresponseDataItem]


class Postattributesresponse(BaseModel):
    data: dict[str, Any]


class GetoptionsresponseDataItem(BaseModel):
    id: dict[str, Any]
    title: str
    is_archived: bool


class Getoptionsresponse(BaseModel):
    data: List[GetoptionsresponseDataItem]


class Postoptionsresponse(BaseModel):
    data: dict[str, Any]


class GetstatusesresponseDataItem(BaseModel):
    id: dict[str, Any]
    title: str
    is_archived: bool
    celebration_enabled: bool
    target_time_in_status: Any


class Getstatusesresponse(BaseModel):
    data: List[GetstatusesresponseDataItem]


class Poststatusesresponse(BaseModel):
    data: dict[str, Any]


class PostqueryresponseDataItem(BaseModel):
    id: dict[str, Any]
    created_at: str
    web_url: str
    values: dict[str, List[Any]]


class Postqueryresponse(BaseModel):
    data: List[PostqueryresponseDataItem]


class Postrecordsresponse(BaseModel):
    data: dict[str, Any]


class Deleterecordsresponse(BaseModel):
    pass


class Getvaluesresponse(BaseModel):
    data: List[Any]


class GetentriesresponseDataItem(BaseModel):
    list_id: str
    list_api_slug: str
    entry_id: str
    created_at: str


class Getentriesresponse(BaseModel):
    data: List[GetentriesresponseDataItem]


class Postsearchresponse(BaseModel):
    data: List[Any]


class GetlistsresponseDataItemWorkspace_member_accessItem(BaseModel):
    workspace_member_id: str
    level: str


class GetlistsresponseDataItem(BaseModel):
    id: dict[str, Any]
    api_slug: str
    name: str
    parent_object: List[str]
    workspace_access: Any
    workspace_member_access: List[GetlistsresponseDataItemWorkspace_member_accessItem]
    created_by_actor: dict[str, Any]
    created_at: str


class Getlistsresponse(BaseModel):
    data: List[GetlistsresponseDataItem]


class Postlistsresponse(BaseModel):
    data: dict[str, Any]


class Postqueryresponse1DataItem(BaseModel):
    id: dict[str, Any]
    parent_record_id: str
    parent_object: str
    created_at: str
    entry_values: dict[str, List[Any]]


class Postqueryresponse1(BaseModel):
    data: List[Postqueryresponse1DataItem]


class Postentriesresponse(BaseModel):
    data: dict[str, Any]


class GetworkspaceMembersresponseDataItem(BaseModel):
    id: dict[str, Any]
    first_name: str
    last_name: str
    avatar_url: Any
    email_address: str
    created_at: str
    access_level: str


class GetworkspaceMembersresponse(BaseModel):
    data: List[GetworkspaceMembersresponseDataItem]


class GetworkspaceMembersresponse1(BaseModel):
    data: dict[str, Any]


class GetnotesresponseDataItem(BaseModel):
    id: dict[str, Any]
    parent_object: str
    parent_record_id: str
    title: str
    meeting_id: Any
    content_plaintext: str
    content_markdown: str
    tags: List[Any]
    created_by_actor: dict[str, Any]
    created_at: str


class Getnotesresponse(BaseModel):
    data: List[GetnotesresponseDataItem]


class Postnotesresponse(BaseModel):
    data: dict[str, Any]


class Gettasksresponse(BaseModel):
    data: dict[str, Any]


class GetthreadsresponseDataItemCommentsItem(BaseModel):
    id: dict[str, Any]
    thread_id: str
    content_plaintext: str
    entry: Any
    record: dict[str, Any]
    resolved_at: Any
    resolved_by: dict[str, Any]
    created_at: str
    author: dict[str, Any]


class GetthreadsresponseDataItem(BaseModel):
    id: dict[str, Any]
    comments: List[GetthreadsresponseDataItemCommentsItem]
    created_at: str


class Getthreadsresponse(BaseModel):
    data: List[GetthreadsresponseDataItem]


class Getthreadsresponse1(BaseModel):
    data: dict[str, Any]


class Postcommentsresponse(BaseModel):
    data: dict[str, Any]


class Getmeetingsresponse(BaseModel):
    data: dict[str, Any]


class GetcallRecordingsresponseDataItem(BaseModel):
    id: dict[str, Any]
    status: str
    web_url: str
    created_by_actor: dict[str, Any]
    created_at: str


class GetcallRecordingsresponse(BaseModel):
    data: List[GetcallRecordingsresponseDataItem]
    pagination: dict[str, Any]


class GetcallRecordingsresponse1(BaseModel):
    data: dict[str, Any]


class Gettranscriptresponse(BaseModel):
    data: dict[str, Any]
    pagination: dict[str, Any]


class GetwebhooksresponseDataItemSubscriptionsItem(BaseModel):
    event_type: str
    filter: Any


class GetwebhooksresponseDataItem(BaseModel):
    target_url: str
    subscriptions: List[GetwebhooksresponseDataItemSubscriptionsItem]
    id: dict[str, Any]
    status: str
    created_at: str


class Getwebhooksresponse(BaseModel):
    data: List[GetwebhooksresponseDataItem]


class Postwebhooksresponse(BaseModel):
    data: dict[str, Any]


class Getwebhooksresponse1(BaseModel):
    data: dict[str, Any]
