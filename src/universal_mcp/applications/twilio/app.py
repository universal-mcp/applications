from collections.abc import Callable
from datetime import datetime
from typing import Any

from loguru import logger

try:
    from twilio.rest import Client as TwilioClient
except ImportError:
    TwilioClient = None
    logger.error(
        "Twilio SDK is not installed. Please install 'twilio' to use TwilioApp."
    )

from universal_mcp.applications.application import APIApplication
from universal_mcp.exceptions import NotAuthorizedError, ToolError
from universal_mcp.integrations import Integration


class TwilioApp(APIApplication):
    """
    Application for interacting with the Twilio Messaging API using the official Python SDK.
    """

    def __init__(self, integration: Integration, **kwargs: Any) -> None:
        super().__init__(name="twilio", integration=integration, **kwargs)
        self.base_url = "https://api.twilio.com/2010-04-01"
        self._twilio_client: Any | None = None
        self._account_sid: str | None = None
        self._auth_token: str | None = None
        if TwilioClient is None:
            logger.warning(
                "Twilio SDK is not available. Twilio tools will not function."
            )

    @property
    def account_sid(self) -> str:
        """
        Retrieves and caches the Twilio Account SID from the integration credentials.
        """
        if self._account_sid is None:
            if not self.integration:
                raise NotAuthorizedError("Integration not configured for Twilio App.")
            try:
                credentials = self.integration.get_credentials()
            except Exception as e:
                raise NotAuthorizedError(f"Failed to get Twilio credentials: {e}")

            sid = (
                credentials.get("account_sid")
                or credentials.get("ACCOUNT_SID")
                or credentials.get("TWILIO_ACCOUNT_SID")
            )
            if not sid:
                raise NotAuthorizedError(
                    "Twilio Account SID is missing. Please set it in the integration."
                )
            self._account_sid = sid
        return self._account_sid

    @property
    def auth_token(self) -> str:
        """
        Retrieves and caches the Twilio Auth Token from the integration credentials.
        """
        if self._auth_token is None:
            if not self.integration:
                raise NotAuthorizedError("Integration not configured for Twilio App.")
            try:
                credentials = self.integration.get_credentials()
            except Exception as e:
                raise NotAuthorizedError(f"Failed to get Twilio credentials: {e}")

            token = (
                credentials.get("auth_token")
                or credentials.get("AUTH_TOKEN")
                or credentials.get("TWILIO_AUTH_TOKEN")
            )
            if not token:
                raise NotAuthorizedError(
                    "Twilio Auth Token is missing. Please set it in the integration."
                )
            self._auth_token = token
        return self._auth_token

    @property
    def twilio_client(self) -> Any:
        """
        Returns a cached Twilio Client instance.
        """
        if self._twilio_client is None:
            if TwilioClient is None:
                raise ToolError("Twilio SDK is not installed.")
            self._twilio_client = TwilioClient(self.account_sid, self.auth_token)
        return self._twilio_client

    def create_message(self, from_: str, to: str, body: str) -> dict[str, Any]:
        """
        Sends a new SMS or MMS message using Twilio.

        Args:
            from_: The Twilio phone number (in E.164 format) to send the message from.
            to: The recipient's phone number (in E.164 format).
            body: The content of the message.

        Returns:
            A dictionary containing the Twilio message resource details.

        Raises:
            NotAuthorizedError: If credentials are missing or invalid.
            ToolError: If the SDK is not installed or sending fails.

        Tags:
            create, message, sms, mms, send, twilio, api, important
        """
        try:
            message = self.twilio_client.messages.create(
                from_=from_,
                to=to,
                body=body,
            )
            # Convert the Twilio MessageInstance to a dict
            return {
                "sid": message.sid,
                "status": message.status,
                "body": message.body,
                "from": message.from_,
                "to": message.to,
                "date_created": str(message.date_created),
                "date_sent": str(message.date_sent),
                "date_updated": str(message.date_updated),
                "error_code": message.error_code,
                "error_message": message.error_message,
            }
        except Exception as e:
            if "Authenticate" in str(e) or "401" in str(e):
                raise NotAuthorizedError(f"Twilio authentication failed: {e}")
            raise ToolError(f"Failed to send message: {e}")

    def fetch_message(self, message_sid: str) -> dict[str, Any]:
        """
        Fetches the details of a specific message by its SID.

        Args:
            message_sid: The unique SID of the message (starts with 'SM').

        Returns:
            A dictionary containing the message details.

        Raises:
            NotAuthorizedError: If credentials are missing or invalid.
            ToolError: If the SDK is not installed or fetch fails.

        Tags:
            fetch, message, sms, mms, read, twilio, api, important
        """
        try:
            message = self.twilio_client.messages(message_sid).fetch()
            return {
                "sid": message.sid,
                "status": message.status,
                "body": message.body,
                "from": message.from_,
                "to": message.to,
                "date_created": str(message.date_created),
                "date_sent": str(message.date_sent),
                "date_updated": str(message.date_updated),
                "error_code": message.error_code,
                "error_message": message.error_message,
            }
        except Exception as e:
            if "Authenticate" in str(e) or "401" in str(e):
                raise NotAuthorizedError(f"Twilio authentication failed: {e}")
            raise ToolError(f"Failed to fetch message: {e}")

    def list_messages(
        self,
        limit: int = 20,
        date_sent_before: datetime | None = None,
        date_sent_after: datetime | None = None,
    ) -> list[dict[str, Any]]:
        """
        Lists messages from your Twilio account, optionally filtered by date.

        Args:
            limit: The maximum number of messages to return (default: 20).
            date_sent_before: Only include messages sent before this datetime (optional).
            date_sent_after: Only include messages sent after this datetime (optional).

        Returns:
            A list of dictionaries, each representing a message.

        Raises:
            NotAuthorizedError: If credentials are missing or invalid.
            ToolError: If the SDK is not installed or listing fails.

        Tags:
            list, message, sms, mms, read, twilio, api, important
        """
        try:
            params = {
                "limit": limit,
            }
            if date_sent_before:
                params["date_sent_before"] = date_sent_before
            if date_sent_after:
                params["date_sent_after"] = date_sent_after

            messages = self.twilio_client.messages.list(**params)
            result = []
            for msg in messages:
                result.append(
                    {
                        "sid": msg.sid,
                        "status": msg.status,
                        "body": msg.body,
                        "from": msg.from_,
                        "to": msg.to,
                        "date_created": str(msg.date_created),
                        "date_sent": str(msg.date_sent),
                        "date_updated": str(msg.date_updated),
                        "error_code": msg.error_code,
                        "error_message": msg.error_message,
                    }
                )
            return result
        except Exception as e:
            if "Authenticate" in str(e) or "401" in str(e):
                raise NotAuthorizedError(f"Twilio authentication failed: {e}")
            raise ToolError(f"Failed to list messages: {e}")

    def delete_message(self, message_sid: str) -> bool:
        """
        Deletes a specific message from your Twilio account.

        Args:
            message_sid: The unique SID of the message to delete (starts with 'SM').

        Returns:
            True if the message was deleted successfully, False otherwise.

        Raises:
            NotAuthorizedError: If credentials are missing or invalid.
            ToolError: If the SDK is not installed or deletion fails.

        Tags:
            delete, message, sms, mms, remove, twilio, api, important
        """
        try:
            result = self.twilio_client.messages(message_sid).delete()
            return bool(result)
        except Exception as e:
            if "Authenticate" in str(e) or "401" in str(e):
                raise NotAuthorizedError(f"Twilio authentication failed: {e}")
            raise ToolError(f"Failed to delete message: {e}")

    def list_tools(self) -> list[Callable]:
        """
        Lists all public tools provided by the TwilioApp.

        Returns:
            A list of callable tool methods.
        """
        return [
            self.create_message,
            self.fetch_message,
            self.list_messages,
            self.delete_message,
        ]
