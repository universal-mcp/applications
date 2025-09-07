import requests
import json
from datetime import datetime
from dataclasses import dataclass
from typing import Optional, List, Tuple
import os.path
from . import audio
from dotenv import load_dotenv

load_dotenv()

WHATSAPP_API_BASE_URL = os.getenv('WHATSAPP_API_BASE_URL', "http://134.209.144.43:8080")

@dataclass
class Message:
    timestamp: datetime
    sender: str
    content: str
    is_from_me: bool
    chat_jid: str
    id: str
    chat_name: Optional[str] = None
    media_type: Optional[str] = None

@dataclass
class Chat:
    jid: str
    name: Optional[str]
    last_message_time: Optional[datetime]
    last_message: Optional[str] = None
    last_sender: Optional[str] = None
    last_is_from_me: Optional[bool] = None

    @property
    def is_group(self) -> bool:
        """Determine if chat is a group based on JID pattern."""
        return self.jid.endswith("@g.us")

@dataclass
class Contact:
    phone_number: str
    name: Optional[str]
    jid: str

@dataclass
class MessageContext:
    message: Message
    before: List[Message]
    after: List[Message]

def _make_api_request(endpoint: str, method: str = "GET", data: dict = None, user_id: str = "default_user") -> dict:
    """Make HTTP request to WhatsApp Bridge API."""
    url = f"{WHATSAPP_API_BASE_URL}/api/{endpoint}"
    
    # Add user_id to query parameters for GET requests
    if method.upper() == "GET" and data:
        data["user_id"] = user_id
    elif method.upper() == "GET":
        data = {"user_id": user_id}
    
    try:
        if method.upper() == "GET":
            response = requests.get(url, params=data, timeout=30)
        elif method.upper() == "POST":
            response = requests.post(url, json=data, timeout=30)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"HTTP {response.status_code}: {response.text}"}
            
    except requests.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except json.JSONDecodeError:
        return {"error": f"Invalid JSON response: {response.text}"}

def get_sender_name(sender_jid: str, user_id: str = "default_user") -> str:
    """Get sender name via API call."""
    result = _make_api_request("sender_name", data={"sender_jid": sender_jid}, user_id=user_id)
    
    if "error" in result:
        return sender_jid
    
    return result.get("name", sender_jid)

def format_message(message: Message, show_chat_info: bool = True, user_id: str = "default_user") -> str:
    """Print a single message with consistent formatting."""
    output = ""
    
    if show_chat_info and message.chat_name:
        output += f"[{message.timestamp:%Y-%m-%d %H:%M:%S}] Chat: {message.chat_name} "
    else:
        output += f"[{message.timestamp:%Y-%m-%d %H:%M:%S}] "
        
    content_prefix = ""
    if hasattr(message, 'media_type') and message.media_type:
        content_prefix = f"[{message.media_type} - Message ID: {message.id} - Chat JID: {message.chat_jid}] "
    
    try:
        sender_name = get_sender_name(message.sender, user_id) if not message.is_from_me else "Me"
        output += f"From: {sender_name}: {content_prefix}{message.content}\n"
    except Exception as e:
        print(f"Error formatting message: {e}")
    return output

def format_messages_list(messages: List[Message], show_chat_info: bool = True, user_id: str = "default_user") -> str:
    output = ""
    if not messages:
        output += "No messages to display."
        return output
    
    for message in messages:
        output += format_message(message, show_chat_info, user_id)
    return output

def list_messages(
    after: Optional[str] = None,
    before: Optional[str] = None,
    sender_phone_number: Optional[str] = None,
    chat_jid: Optional[str] = None,
    query: Optional[str] = None,
    limit: int = 20,
    page: int = 0,
    include_context: bool = True,
    context_before: int = 1,
    context_after: int = 1,
    user_id: str = "default_user"
) -> str:
    """Get messages matching the specified criteria with optional context via API."""
    params = {
        "after": after,
        "before": before,
        "sender_phone_number": sender_phone_number,
        "chat_jid": chat_jid,
        "query": query,
        "limit": limit,
        "page": page,
        "include_context": include_context,
        "context_before": context_before,
        "context_after": context_after
    }
    
    # Remove None values
    params = {k: v for k, v in params.items() if v is not None}
    
    result = _make_api_request("messages", data=params, user_id=user_id)
    
    if "error" in result:
        return f"Error retrieving messages: {result['error']}"
    
    return result.get("messages", "No messages found")

def get_message_context(
    message_id: str,
    before: int = 5,
    after: int = 5,
    user_id: str = "default_user"
) -> MessageContext:
    """Get context around a specific message via API."""
    params = {
        "message_id": message_id,
        "before": before,
        "after": after
    }
    
    result = _make_api_request("message_context", data=params, user_id=user_id)
    
    if "error" in result:
        raise ValueError(f"Error getting message context: {result['error']}")
    
    # Parse the response into MessageContext object
    # This would need to be implemented based on the API response structure
    # For now, returning a simple error message
    raise NotImplementedError("Message context API not yet implemented in bridge")

def list_chats(
    query: Optional[str] = None,
    limit: int = 20,
    page: int = 0,
    include_last_message: bool = True,
    sort_by: str = "last_active",
    user_id: str = "default_user"
) -> List[Chat]:
    """Get chats matching the specified criteria via API."""
    params = {
        "query": query,
        "limit": limit,
        "page": page,
        "include_last_message": include_last_message,
        "sort_by": sort_by
    }
    
    # Remove None values
    params = {k: v for k, v in params.items() if v is not None}
    
    result = _make_api_request("chats", data=params, user_id=user_id)
    
    if "error" in result:
        print(f"Error retrieving chats: {result['error']}")
        return []
    
    chats_data = result.get("chats", [])
    chats = []
    
    for chat_data in chats_data:
        chat = Chat(
            jid=chat_data["jid"],
            name=chat_data.get("name"),
            last_message_time=datetime.fromisoformat(chat_data["last_message_time"]) if chat_data.get("last_message_time") else None,
            last_message=chat_data.get("last_message"),
            last_sender=chat_data.get("last_sender"),
            last_is_from_me=chat_data.get("last_is_from_me")
        )
        chats.append(chat)
    
    return chats

def search_contacts(query: str, user_id: str = "default_user") -> List[Contact]:
    """Search contacts by name or phone number via API."""
    result = _make_api_request("contacts", data={"query": query}, user_id=user_id)
    
    if "error" in result:
        print(f"Error searching contacts: {result['error']}")
        return []
    
    contacts_data = result.get("contacts", [])
    contacts = []
    
    for contact_data in contacts_data:
        contact = Contact(
            phone_number=contact_data["phone_number"],
            name=contact_data.get("name"),
            jid=contact_data["jid"]
        )
        contacts.append(contact)
    
    return contacts

def get_contact_chats(jid: str, limit: int = 20, page: int = 0, user_id: str = "default_user") -> List[Chat]:
    """Get all chats involving the contact via API."""
    params = {
        "jid": jid,
        "limit": limit,
        "page": page
    }
    
    result = _make_api_request("contact_chats", data=params, user_id=user_id)
    
    if "error" in result:
        print(f"Error getting contact chats: {result['error']}")
        return []
    
    chats_data = result.get("chats", [])
    chats = []
    
    for chat_data in chats_data:
        chat = Chat(
            jid=chat_data["jid"],
            name=chat_data.get("name"),
            last_message_time=datetime.fromisoformat(chat_data["last_message_time"]) if chat_data.get("last_message_time") else None,
            last_message=chat_data.get("last_message"),
            last_sender=chat_data.get("last_sender"),
            last_is_from_me=chat_data.get("last_is_from_me")
        )
        chats.append(chat)
    
    return chats

def get_last_interaction(jid: str, user_id: str = "default_user") -> str:
    """Get most recent message involving the contact via API."""
    result = _make_api_request("last_interaction", data={"jid": jid}, user_id=user_id)
    
    if "error" in result:
        return f"Error getting last interaction: {result['error']}"
    
    return result.get("message", "No interaction found")

def get_chat(chat_jid: str, include_last_message: bool = True, user_id: str = "default_user") -> Optional[Chat]:
    """Get chat metadata by JID via API."""
    params = {
        "chat_jid": chat_jid,
        "include_last_message": include_last_message
    }
    
    result = _make_api_request("chat", data=params, user_id=user_id)
    
    if "error" in result:
        print(f"Error getting chat: {result['error']}")
        return None
    
    chat_data = result.get("chat")
    if not chat_data:
        return None
    
    return Chat(
        jid=chat_data["jid"],
        name=chat_data.get("name"),
        last_message_time=datetime.fromisoformat(chat_data["last_message_time"]) if chat_data.get("last_message_time") else None,
        last_message=chat_data.get("last_message"),
        last_sender=chat_data.get("last_sender"),
        last_is_from_me=chat_data.get("last_is_from_me")
    )

def get_direct_chat_by_contact(sender_phone_number: str, user_id: str = "default_user") -> Optional[Chat]:
    """Get chat metadata by sender phone number via API."""
    result = _make_api_request("direct_chat", data={"sender_phone_number": sender_phone_number}, user_id=user_id)
    
    if "error" in result:
        print(f"Error getting direct chat: {result['error']}")
        return None
    
    chat_data = result.get("chat")
    if not chat_data:
        return None
    
    return Chat(
        jid=chat_data["jid"],
        name=chat_data.get("name"),
        last_message_time=datetime.fromisoformat(chat_data["last_message_time"]) if chat_data.get("last_message_time") else None,
        last_message=chat_data.get("last_message"),
        last_sender=chat_data.get("last_sender"),
        last_is_from_me=chat_data.get("last_is_from_me")
    )

def send_message(recipient: str, message: str, user_id: str = "default_user") -> Tuple[bool, str]:
    """Send message via API."""
    payload = {
        "user_id": user_id,
        "recipient": recipient,
        "message": message
    }
    
    result = _make_api_request("send", method="POST", data=payload, user_id=user_id)
    
    if "error" in result:
        return False, result["error"]
    
    return result.get("success", False), result.get("message", "Unknown response")

def send_file(recipient: str, media_path: str, user_id: str = "default_user") -> Tuple[bool, str]:
    """Send file via API."""
    payload = {
        "user_id": user_id,
        "recipient": recipient,
        "media_path": media_path
    }
    
    result = _make_api_request("send", method="POST", data=payload, user_id=user_id)
    
    if "error" in result:
        return False, result["error"]
    
    return result.get("success", False), result.get("message", "Unknown response")

def send_audio_message(recipient: str, media_path: str, user_id: str = "default_user") -> Tuple[bool, str]:
    """Send audio message via API."""
    if not media_path.endswith(".ogg"):
        try:
            media_path = audio.convert_to_opus_ogg_temp(media_path)
        except Exception as e:
            return False, f"Error converting file to opus ogg. You likely need to install ffmpeg: {str(e)}"
    
    payload = {
        "user_id": user_id,
        "recipient": recipient,
        "media_path": media_path
    }
    
    result = _make_api_request("send", method="POST", data=payload, user_id=user_id)
    
    if "error" in result:
        return False, result["error"]
    
    return result.get("success", False), result.get("message", "Unknown response")

def download_media(message_id: str, chat_jid: str, user_id: str = "default_user") -> Optional[str]:
    """Download media from a message via API."""
    payload = {
        "user_id": user_id,
        "message_id": message_id,
        "chat_jid": chat_jid
    }
    
    result = _make_api_request("download", method="POST", data=payload, user_id=user_id)
    
    if "error" in result:
        print(f"Download failed: {result['error']}")
        return None
    
    if result.get("success", False):
        path = result.get("path")
        print(f"Media downloaded successfully: {path}")
        return path
    else:
        print(f"Download failed: {result.get('message', 'Unknown error')}")
        return None
