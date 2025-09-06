from typing import Any

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class KlaviyoApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="klaviyo", integration=integration, **kwargs)
        self.base_url = "https://a.klaviyo.com"

    def _get_headers(self):
        if not self.integration:
            raise ValueError("Integration not configured for KlaviyoApp")
        credentials = self.integration.get_credentials()
        if "headers" in credentials:
            return credentials["headers"]
        if "access_token" not in credentials:
            raise ValueError("Access token not found in KlaviyoApp credentials")
        return {
            "Authorization": f"Bearer {credentials['access_token']}",
            "Accept": "application/json",
            "revision": "2024-07-15",
        }

    def create_client_review(self, company_id=None, data=None) -> Any:
        """
        Creates a new client review, requiring a company ID as a query parameter and a revision in the request header.

        Args:
            company_id (string): (Required) Your Public API Key / Site ID. See [this article]( for more details. Example: '<string>'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "author": "<string>",
                      "content": "<string>",
                      "custom_questions": [
                        {
                          "answers": [
                            "<string>",
                            "<string>"
                          ],
                          "id": "<string>"
                        },
                        {
                          "answers": [
                            "<string>",
                            "<string>"
                          ],
                          "id": "<string>"
                        }
                      ],
                      "email": "<string>",
                      "images": [
                        "<string>",
                        "<string>"
                      ],
                      "incentive_type": "free_product",
                      "product": {
                        "external_id": "<string>",
                        "integration_key": "woocommerce"
                      },
                      "rating": 2,
                      "review_type": "rating",
                      "title": "<string>"
                    },
                    "relationships": {
                      "order": {
                        "data": {
                          "id": "<string>",
                          "type": "order"
                        }
                      }
                    },
                    "type": "review"
                  }
                }
                ```

        Returns:
            Any: Success

        Tags:
            Beta APIs
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/client/reviews"
        query_params = {k: v for k, v in [("company_id", company_id)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_accounts(self, fields_account=None) -> dict[str, Any]:
        """
        Retrieves account information using the GET method, allowing optional filtering by specific account fields and requiring a revision header, returning a successful response with the requested data if available.

        Args:
            fields_account (string): For more information please visit Example: 'contact_information.street_address.address1,contact_information.street_address.city'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Accounts, important
        """
        url = f"{self.base_url}/api/accounts"
        query_params = {
            k: v for k, v in [("fields[account]", fields_account)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_account(self, id, fields_account=None) -> dict[str, Any]:
        """
        Retrieves detailed information about a specific account identified by `{id}` with optional filtering by `fields[account]` and version control via the `revision` header.

        Args:
            id (string): id
            fields_account (string): For more information please visit Example: 'contact_information.street_address.address1,contact_information.street_address.city'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Accounts
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/accounts/{id}"
        query_params = {
            k: v for k, v in [("fields[account]", fields_account)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaigns(
        self,
        fields_campaign_message=None,
        fields_campaign=None,
        fields_tag=None,
        filter=None,
        include=None,
        page_cursor=None,
        sort=None,
    ) -> dict[str, Any]:
        """
        Retrieve a list of campaigns using optional filtering, sorting, and inclusion parameters, with the option to specify fields for campaign messages, campaigns, and tags.

        Args:
            fields_campaign_message (string): For more information please visit Example: 'definition.content.subject,created_at'.
            fields_campaign (string): For more information please visit Example: 'send_time,send_options.use_smart_sending'.
            fields_tag (string): For more information please visit Example: 'name,name'.
            filter (string): (Required) For more information please visit field(s)/operator(s):<br>`messages.channel`: `equals`<br>`name`: `contains`<br>`status`: `any`, `equals`<br>`archived`: `equals`<br>`created_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`scheduled_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`updated_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than` Example: '<string>'.
            include (string): For more information please visit Example: 'tags,tags'.
            page_cursor (string): For more information please visit Example: '<string>'.
            sort (string): For more information please visit Example: '-updated_at'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Campaigns, important
        """
        url = f"{self.base_url}/api/campaigns"
        query_params = {
            k: v
            for k, v in [
                ("fields[campaign-message]", fields_campaign_message),
                ("fields[campaign]", fields_campaign),
                ("fields[tag]", fields_tag),
                ("filter", filter),
                ("include", include),
                ("page[cursor]", page_cursor),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_campaign(self, data=None) -> dict[str, Any]:
        """
        Creates a new campaign using specified parameters, returning appropriate status codes for success (201), client errors (400), or server issues (500).

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "audiences": {
                        "excluded": [
                          "<string>",
                          "<string>"
                        ],
                        "included": [
                          "<string>",
                          "<string>"
                        ]
                      },
                      "campaign-messages": {
                        "data": [
                          {
                            "attributes": {
                              "definition": {
                                "channel": "email",
                                "content": {
                                  "bcc_email": "<string>",
                                  "cc_email": "<string>",
                                  "from_email": "<string>",
                                  "from_label": "<string>",
                                  "preview_text": "<string>",
                                  "reply_to_email": "<string>",
                                  "subject": "<string>"
                                },
                                "label": "<string>"
                              }
                            },
                            "relationships": {
                              "image": {
                                "data": {
                                  "id": "<string>",
                                  "type": "image"
                                }
                              }
                            },
                            "type": "campaign-message"
                          },
                          {
                            "attributes": {
                              "definition": {
                                "channel": "email",
                                "content": {
                                  "bcc_email": "<string>",
                                  "cc_email": "<string>",
                                  "from_email": "<string>",
                                  "from_label": "<string>",
                                  "preview_text": "<string>",
                                  "reply_to_email": "<string>",
                                  "subject": "<string>"
                                },
                                "label": "<string>"
                              }
                            },
                            "relationships": {
                              "image": {
                                "data": {
                                  "id": "<string>",
                                  "type": "image"
                                }
                              }
                            },
                            "type": "campaign-message"
                          }
                        ]
                      },
                      "name": "<string>",
                      "send_options": {
                        "use_smart_sending": true
                      },
                      "send_strategy": {
                        "datetime": "<dateTime>",
                        "method": "static",
                        "options": {
                          "is_local": true,
                          "send_past_recipients_immediately": false
                        }
                      },
                      "tracking_options": {
                        "add_utm": "<boolean>",
                        "is_tracking_clicks": "<boolean>",
                        "is_tracking_opens": "<boolean>",
                        "utm_params": [
                          {
                            "name": "<string>",
                            "value": "<string>"
                          },
                          {
                            "name": "<string>",
                            "value": "<string>"
                          }
                        ]
                      }
                    },
                    "type": "campaign"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Campaigns, important
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/campaigns"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaign(
        self,
        id,
        fields_campaign_message=None,
        fields_campaign=None,
        fields_tag=None,
        include=None,
    ) -> dict[str, Any]:
        """
        Retrieves detailed information about a campaign by its ID, allowing for selective field inclusion and revision specification through query parameters and headers.

        Args:
            id (string): id
            fields_campaign_message (string): For more information please visit Example: 'definition.content.subject,created_at'.
            fields_campaign (string): For more information please visit Example: 'send_time,send_options.use_smart_sending'.
            fields_tag (string): For more information please visit Example: 'name,name'.
            include (string): For more information please visit Example: 'tags,tags'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Campaigns, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaigns/{id}"
        query_params = {
            k: v
            for k, v in [
                ("fields[campaign-message]", fields_campaign_message),
                ("fields[campaign]", fields_campaign),
                ("fields[tag]", fields_tag),
                ("include", include),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_campaign(self, id) -> Any:
        """
        Deletes a specific campaign by its ID, requiring a revision header and returning 204 No Content on success, with 400 and 500 for client and server errors, respectively.

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            Campaigns, Campaigns1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaigns/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_campaign(self, id, data=None) -> dict[str, Any]:
        """
        The **PATCH** operation at **"/api/campaigns/{id}"** partially updates a campaign resource identified by `{id}`, with the revision specified in the header, returning a successful response if the update is applied correctly.

        Args:
            id (string): id
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "audiences": {
                        "excluded": [
                          "<string>",
                          "<string>"
                        ],
                        "included": [
                          "<string>",
                          "<string>"
                        ]
                      },
                      "name": "<string>",
                      "send_options": {
                        "use_smart_sending": true
                      },
                      "send_strategy": {
                        "datetime": "<dateTime>",
                        "method": "static",
                        "options": {
                          "is_local": true,
                          "send_past_recipients_immediately": false
                        }
                      },
                      "tracking_options": {
                        "add_utm": "<boolean>",
                        "is_tracking_clicks": "<boolean>",
                        "is_tracking_opens": "<boolean>",
                        "utm_params": [
                          {
                            "name": "<string>",
                            "value": "<string>"
                          },
                          {
                            "name": "<string>",
                            "value": "<string>"
                          }
                        ]
                      }
                    },
                    "id": "<string>",
                    "type": "campaign"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Campaigns, Campaigns1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/campaigns/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaign_recipient_estimation(
        self, id, fields_campaign_recipient_estimation=None
    ) -> dict[str, Any]:
        """
        Retrieves a campaign recipient estimation by ID with optional fields filtering via query parameters and revision tracking through headers.

        Args:
            id (string): id
            fields_campaign_recipient_estimation (string): For more information please visit Example: 'estimated_recipient_count,estimated_recipient_count'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Campaigns, Campaigns1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaign-recipient-estimations/{id}"
        query_params = {
            k: v
            for k, v in [
                (
                    "fields[campaign-recipient-estimation]",
                    fields_campaign_recipient_estimation,
                )
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_campaign_clone(self, data=None) -> dict[str, Any]:
        """
        Clones a campaign, accepting a revision header and returning appropriate status codes (201 Created, 400 Bad Request, 500 Internal Server Error).

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "new_name": "<string>"
                    },
                    "id": "<string>",
                    "type": "campaign"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Campaigns, Campaigns1
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/campaign-clone"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tags_for_campaign(self, id, fields_tag=None) -> dict[str, Any]:
        """
        This API operation retrieves tags for a campaign by ID using the GET method, allowing optional filtering by specific fields and versioning through a revision header.

        Args:
            id (string): id
            fields_tag (string): For more information please visit Example: 'name,name'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Campaigns, Campaigns1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaigns/{id}/tags"
        query_params = {k: v for k, v in [("fields[tag]", fields_tag)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag_ids_for_campaign(self, id) -> dict[str, Any]:
        """
        This API operation retrieves the relationships between a campaign, identified by its ID, and associated tags, returning the relevant tag information.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Campaigns, Campaigns1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaigns/{id}/relationships/tags"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_messages_for_campaign(
        self,
        id,
        fields_campaign_message=None,
        fields_campaign=None,
        fields_image=None,
        fields_template=None,
        include=None,
    ) -> dict[str, Any]:
        """
        Retrieves campaign messages associated with a specific campaign ID, allowing optional field selection and resource inclusion via query parameters, with support for header-based versioning.

        Args:
            id (string): id
            fields_campaign_message (string): For more information please visit Example: 'definition.content.subject,created_at'.
            fields_campaign (string): For more information please visit Example: 'send_time,send_options.use_smart_sending'.
            fields_image (string): For more information please visit Example: 'image_url,name'.
            fields_template (string): For more information please visit Example: 'name,text'.
            include (string): For more information please visit Example: 'campaign,template'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Campaigns, Campaigns1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaigns/{id}/campaign-messages"
        query_params = {
            k: v
            for k, v in [
                ("fields[campaign-message]", fields_campaign_message),
                ("fields[campaign]", fields_campaign),
                ("fields[image]", fields_image),
                ("fields[template]", fields_template),
                ("include", include),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_message_ids_for_campaign(self, id) -> dict[str, Any]:
        """
        Retrieves the relationships between the specified campaign and its associated messages using the "revision" header parameter for versioning.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Campaigns, Campaigns1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaigns/{id}/relationships/campaign-messages"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaign_message(
        self,
        id,
        fields_campaign_message=None,
        fields_campaign=None,
        fields_image=None,
        fields_template=None,
        include=None,
    ) -> dict[str, Any]:
        """
        This API operation uses the "GET" method to retrieve a campaign message by its ID, allowing for customizable field selection via query parameters and revision specification in the header.

        Args:
            id (string): id
            fields_campaign_message (string): For more information please visit Example: 'definition.content.subject,created_at'.
            fields_campaign (string): For more information please visit Example: 'send_time,send_options.use_smart_sending'.
            fields_image (string): For more information please visit Example: 'image_url,name'.
            fields_template (string): For more information please visit Example: 'name,text'.
            include (string): For more information please visit Example: 'campaign,template'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Campaigns, Messages
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaign-messages/{id}"
        query_params = {
            k: v
            for k, v in [
                ("fields[campaign-message]", fields_campaign_message),
                ("fields[campaign]", fields_campaign),
                ("fields[image]", fields_image),
                ("fields[template]", fields_template),
                ("include", include),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_campaign_message(self, id, data=None) -> dict[str, Any]:
        """
        The **PATCH** operation at "/api/campaign-messages/{id}" partially updates a campaign message by applying specified changes, using a revision header to ensure data consistency.

        Args:
            id (string): id
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "definition": {
                        "channel": "email",
                        "content": {
                          "bcc_email": "<string>",
                          "cc_email": "<string>",
                          "from_email": "<string>",
                          "from_label": "<string>",
                          "preview_text": "<string>",
                          "reply_to_email": "<string>",
                          "subject": "<string>"
                        },
                        "label": "<string>"
                      }
                    },
                    "id": "<string>",
                    "relationships": {
                      "image": {
                        "data": {
                          "id": "<string>",
                          "type": "image"
                        }
                      }
                    },
                    "type": "campaign-message"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Campaigns, Messages
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/campaign-messages/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def assign_template_to_campaign_message(self, data=None) -> dict[str, Any]:
        """
        Creates a new campaign message template assignment, requiring a revision header parameter, returning HTTP 201 on success or 400/500 for client/server errors.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "id": "<string>",
                    "relationships": {
                      "template": {
                        "data": {
                          "id": "<string>",
                          "type": "template"
                        }
                      }
                    },
                    "type": "campaign-message"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Campaigns, Messages
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/campaign-message-assign-template"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaign_for_campaign_message(
        self, id, fields_campaign=None
    ) -> dict[str, Any]:
        """
        Retrieves the campaign associated with a specific campaign message ID, optionally filtering returned campaign fields via query parameter and supporting revision tracking via header.

        Args:
            id (string): id
            fields_campaign (string): For more information please visit Example: 'send_time,send_options.use_smart_sending'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Campaigns, Messages
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaign-messages/{id}/campaign"
        query_params = {
            k: v for k, v in [("fields[campaign]", fields_campaign)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaign_id_for_campaign_message(self, id) -> dict[str, Any]:
        """
        Retrieves the relationship between a campaign message and its associated campaign by making a GET request to the "/api/campaign-messages/{id}/relationships/campaign" endpoint, optionally specifying a revision in the header.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Campaigns, Messages
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaign-messages/{id}/relationships/campaign"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_template_for_campaign_message(
        self, id, fields_template=None
    ) -> dict[str, Any]:
        """
        Retrieves the template details for a campaign message specified by the provided ID, allowing optional filtering of response fields and specifying a revision via the header.

        Args:
            id (string): id
            fields_template (string): For more information please visit Example: 'name,text'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Campaigns, Messages
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaign-messages/{id}/template"
        query_params = {
            k: v for k, v in [("fields[template]", fields_template)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_template_id_for_campaign_message(self, id) -> dict[str, Any]:
        """
        Retrieves the template relationship associated with a specific campaign message, identified by its ID, with an optional revision header parameter for version control.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Campaigns, Messages
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaign-messages/{id}/relationships/template"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_image_for_campaign_message(self, id, fields_image=None) -> dict[str, Any]:
        """
        Retrieves the image associated with a campaign message by ID, allowing optional filtering by image fields and specifying a revision in the request header.

        Args:
            id (string): id
            fields_image (string): For more information please visit Example: 'image_url,name'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Campaigns, Messages
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaign-messages/{id}/image"
        query_params = {
            k: v for k, v in [("fields[image]", fields_image)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_image_id_for_campaign_message(self, id) -> dict[str, Any]:
        """
        Retrieves the image relationship for a campaign message with the specified ID, optionally filtered by a header revision parameter.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Campaigns, Messages
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaign-messages/{id}/relationships/image"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_image_for_campaign_message(self, id, data=None) -> Any:
        """
        Updates the image relationship for a campaign message by replacing the existing related image with a new one using the provided revision for concurrency control.

        Args:
            id (string): id
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "id": "<string>",
                    "type": "image"
                  }
                }
                ```

        Returns:
            Any: Success

        Tags:
            Campaigns, Messages
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/campaign-messages/{id}/relationships/image"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaign_send_job(
        self, id, fields_campaign_send_job=None
    ) -> dict[str, Any]:
        """
        Retrieves a specific campaign send job by ID, supporting optional query parameters for field selection and header-based revision control.

        Args:
            id (string): id
            fields_campaign_send_job (string): For more information please visit Example: 'status,status'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Campaigns, Jobs
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaign-send-jobs/{id}"
        query_params = {
            k: v
            for k, v in [("fields[campaign-send-job]", fields_campaign_send_job)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def cancel_campaign_send(self, id, data=None) -> Any:
        """
        The **PATCH** operation at path "/api/campaign-send-jobs/{id}" partially updates a campaign send job by applying specific changes, requiring a revision in the header, and returns a successful response without content if modified successfully (204), or error codes for invalid requests (400) or server errors (500).

        Args:
            id (string): id
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "action": "cancel"
                    },
                    "id": "<string>",
                    "type": "campaign-send-job"
                  }
                }
                ```

        Returns:
            Any: Success

        Tags:
            Campaigns, Jobs
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/campaign-send-jobs/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaign_recipient_estimation_job(
        self, id, fields_campaign_recipient_estimation_job=None
    ) -> dict[str, Any]:
        """
        Retrieves details of a specific campaign recipient estimation job by its ID with optional field selection and revision header.

        Args:
            id (string): id
            fields_campaign_recipient_estimation_job (string): For more information please visit Example: 'status,status'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Campaigns, Jobs
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaign-recipient-estimation-jobs/{id}"
        query_params = {
            k: v
            for k, v in [
                (
                    "fields[campaign-recipient-estimation-job]",
                    fields_campaign_recipient_estimation_job,
                )
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def send_campaign(self, data=None) -> dict[str, Any]:
        """
        Submits a campaign send job for asynchronous processing of a message dispatch, with a required API version header parameter.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "id": "<string>",
                    "type": "campaign-send-job"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Campaigns, Jobs
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/campaign-send-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def refresh_campaign_recipient_estimation(self, data=None) -> dict[str, Any]:
        """
        Submits a request to create and initiate a campaign recipient estimation job, requiring a revision header and returning 202 Accepted, 400 Bad Request, or 500 Internal Server Error responses.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "id": "<string>",
                    "type": "campaign-recipient-estimation-job"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Campaigns, Jobs
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/campaign-recipient-estimation-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_catalog_items(
        self,
        fields_catalog_item=None,
        fields_catalog_variant=None,
        filter=None,
        include=None,
        page_cursor=None,
        sort=None,
    ) -> dict[str, Any]:
        """
        This API operation retrieves a list of catalog items, allowing for customizable fields, filtering, sorting, and pagination, with optional inclusion of related resources and version control through a revision header.

        Args:
            fields_catalog_item (string): For more information please visit Example: 'images,external_id'.
            fields_catalog_variant (string): For more information please visit Example: 'title,price'.
            filter (string): For more information please visit field(s)/operator(s):<br>`ids`: `any`<br>`category.id`: `equals`<br>`title`: `contains`<br>`published`: `equals` Example: '<string>'.
            include (string): For more information please visit Example: 'variants,variants'.
            page_cursor (string): For more information please visit Example: '<string>'.
            sort (string): For more information please visit Example: 'created'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Items
        """
        url = f"{self.base_url}/api/catalog-items"
        query_params = {
            k: v
            for k, v in [
                ("fields[catalog-item]", fields_catalog_item),
                ("fields[catalog-variant]", fields_catalog_variant),
                ("filter", filter),
                ("include", include),
                ("page[cursor]", page_cursor),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_catalog_item(self, data=None) -> dict[str, Any]:
        """
        Creates a new catalog item entry with optional revision control through header parameters, returning success (201), client error (400), or server error (500) status codes.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "catalog_type": "$default",
                      "custom_metadata": {},
                      "description": "<string>",
                      "external_id": "<string>",
                      "image_full_url": "<string>",
                      "image_thumbnail_url": "<string>",
                      "images": [
                        "<string>",
                        "<string>"
                      ],
                      "integration_type": "$custom",
                      "price": "<number>",
                      "published": true,
                      "title": "<string>",
                      "url": "<string>"
                    },
                    "relationships": {
                      "categories": {
                        "data": [
                          {
                            "id": "<string>",
                            "type": "catalog-category"
                          },
                          {
                            "id": "<string>",
                            "type": "catalog-category"
                          }
                        ]
                      }
                    },
                    "type": "catalog-item"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Items
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-items"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_catalog_item(
        self, id, fields_catalog_item=None, fields_catalog_variant=None, include=None
    ) -> dict[str, Any]:
        """
        The **GET /api/catalog-items/{id}** operation retrieves a specific catalog item by its ID, allowing for customizable field selection via query parameters and inclusion of additional resources, while requiring revision information in the header.

        Args:
            id (string): id
            fields_catalog_item (string): For more information please visit Example: 'images,external_id'.
            fields_catalog_variant (string): For more information please visit Example: 'title,price'.
            include (string): For more information please visit Example: 'variants,variants'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Items
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-items/{id}"
        query_params = {
            k: v
            for k, v in [
                ("fields[catalog-item]", fields_catalog_item),
                ("fields[catalog-variant]", fields_catalog_variant),
                ("include", include),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_catalog_item(self, id) -> Any:
        """
        Deletes a catalog item by its ID, requiring a revision parameter in the header, and returns a successful response with a 204 status if the operation is completed without issues.

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            Catalogs, Items
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-items/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_catalog_item(self, id, data=None) -> dict[str, Any]:
        """
        Updates a catalog item by its ID with partial modifications, requiring a revision header and returning success (200), bad request (400), or server error (500) status codes.

        Args:
            id (string): id
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "custom_metadata": {},
                      "description": "<string>",
                      "image_full_url": "<string>",
                      "image_thumbnail_url": "<string>",
                      "images": [
                        "<string>",
                        "<string>"
                      ],
                      "price": "<number>",
                      "published": "<boolean>",
                      "title": "<string>",
                      "url": "<string>"
                    },
                    "id": "<string>",
                    "relationships": {
                      "categories": {
                        "data": [
                          {
                            "id": "<string>",
                            "type": "catalog-category"
                          },
                          {
                            "id": "<string>",
                            "type": "catalog-category"
                          }
                        ]
                      }
                    },
                    "type": "catalog-item"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Items
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-items/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_create_catalog_items_jobs(
        self, fields_catalog_item_bulk_create_job=None, filter=None, page_cursor=None
    ) -> dict[str, Any]:
        """
        The "/api/catalog-item-bulk-create-jobs" API operation using the "GET" method retrieves a list of catalog item bulk create jobs, allowing for filtering, pagination, and customization of returned fields based on provided parameters.

        Args:
            fields_catalog_item_bulk_create_job (string): For more information please visit Example: 'errors,failed_count'.
            filter (string): For more information please visit field(s)/operator(s):<br>`status`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Items
        """
        url = f"{self.base_url}/api/catalog-item-bulk-create-jobs"
        query_params = {
            k: v
            for k, v in [
                (
                    "fields[catalog-item-bulk-create-job]",
                    fields_catalog_item_bulk_create_job,
                ),
                ("filter", filter),
                ("page[cursor]", page_cursor),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_create_catalog_items(self, data=None) -> dict[str, Any]:
        """
        Submits a request to create multiple catalog items asynchronously via bulk processing.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "items": {
                        "data": [
                          {
                            "attributes": {
                              "catalog_type": "$default",
                              "custom_metadata": {},
                              "description": "<string>",
                              "external_id": "<string>",
                              "image_full_url": "<string>",
                              "image_thumbnail_url": "<string>",
                              "images": [
                                "<string>",
                                "<string>"
                              ],
                              "integration_type": "$custom",
                              "price": "<number>",
                              "published": true,
                              "title": "<string>",
                              "url": "<string>"
                            },
                            "relationships": {
                              "categories": {
                                "data": [
                                  {
                                    "id": "<string>",
                                    "type": "catalog-category"
                                  },
                                  {
                                    "id": "<string>",
                                    "type": "catalog-category"
                                  }
                                ]
                              }
                            },
                            "type": "catalog-item"
                          },
                          {
                            "attributes": {
                              "catalog_type": "$default",
                              "custom_metadata": {},
                              "description": "<string>",
                              "external_id": "<string>",
                              "image_full_url": "<string>",
                              "image_thumbnail_url": "<string>",
                              "images": [
                                "<string>",
                                "<string>"
                              ],
                              "integration_type": "$custom",
                              "price": "<number>",
                              "published": true,
                              "title": "<string>",
                              "url": "<string>"
                            },
                            "relationships": {
                              "categories": {
                                "data": [
                                  {
                                    "id": "<string>",
                                    "type": "catalog-category"
                                  },
                                  {
                                    "id": "<string>",
                                    "type": "catalog-category"
                                  }
                                ]
                              }
                            },
                            "type": "catalog-item"
                          }
                        ]
                      }
                    },
                    "type": "catalog-item-bulk-create-job"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Items
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-item-bulk-create-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_create_catalog_items_job(
        self,
        job_id,
        fields_catalog_item_bulk_create_job=None,
        fields_catalog_item=None,
        include=None,
    ) -> dict[str, Any]:
        """
        This API operation retrieves a catalog item bulk creation job by its ID, allowing optional fields and included resources to be specified for detailed job information.

        Args:
            job_id (string): job_id
            fields_catalog_item_bulk_create_job (string): For more information please visit Example: 'errors,failed_count'.
            fields_catalog_item (string): For more information please visit Example: 'images,external_id'.
            include (string): For more information please visit Example: 'items,items'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Items
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/catalog-item-bulk-create-jobs/{job_id}"
        query_params = {
            k: v
            for k, v in [
                (
                    "fields[catalog-item-bulk-create-job]",
                    fields_catalog_item_bulk_create_job,
                ),
                ("fields[catalog-item]", fields_catalog_item),
                ("include", include),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_update_catalog_items_jobs(
        self, fields_catalog_item_bulk_update_job=None, filter=None, page_cursor=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of catalog item bulk update jobs with optional filtering, cursor-based pagination, and field selection.

        Args:
            fields_catalog_item_bulk_update_job (string): For more information please visit Example: 'errors,failed_count'.
            filter (string): For more information please visit field(s)/operator(s):<br>`status`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Items
        """
        url = f"{self.base_url}/api/catalog-item-bulk-update-jobs"
        query_params = {
            k: v
            for k, v in [
                (
                    "fields[catalog-item-bulk-update-job]",
                    fields_catalog_item_bulk_update_job,
                ),
                ("filter", filter),
                ("page[cursor]", page_cursor),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_update_catalog_items(self, data=None) -> dict[str, Any]:
        """
        Creates a bulk update job for catalog items, accepting header-based revision control and returning asynchronous responses including 202 Accepted, 400 Bad Request, and 500 Internal Server Error status codes.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "items": {
                        "data": [
                          {
                            "attributes": {
                              "custom_metadata": {},
                              "description": "<string>",
                              "image_full_url": "<string>",
                              "image_thumbnail_url": "<string>",
                              "images": [
                                "<string>",
                                "<string>"
                              ],
                              "price": "<number>",
                              "published": "<boolean>",
                              "title": "<string>",
                              "url": "<string>"
                            },
                            "id": "<string>",
                            "relationships": {
                              "categories": {
                                "data": [
                                  {
                                    "id": "<string>",
                                    "type": "catalog-category"
                                  },
                                  {
                                    "id": "<string>",
                                    "type": "catalog-category"
                                  }
                                ]
                              }
                            },
                            "type": "catalog-item"
                          },
                          {
                            "attributes": {
                              "custom_metadata": {},
                              "description": "<string>",
                              "image_full_url": "<string>",
                              "image_thumbnail_url": "<string>",
                              "images": [
                                "<string>",
                                "<string>"
                              ],
                              "price": "<number>",
                              "published": "<boolean>",
                              "title": "<string>",
                              "url": "<string>"
                            },
                            "id": "<string>",
                            "relationships": {
                              "categories": {
                                "data": [
                                  {
                                    "id": "<string>",
                                    "type": "catalog-category"
                                  },
                                  {
                                    "id": "<string>",
                                    "type": "catalog-category"
                                  }
                                ]
                              }
                            },
                            "type": "catalog-item"
                          }
                        ]
                      }
                    },
                    "type": "catalog-item-bulk-update-job"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Items
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-item-bulk-update-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_update_catalog_items_job(
        self,
        job_id,
        fields_catalog_item_bulk_update_job=None,
        fields_catalog_item=None,
        include=None,
    ) -> dict[str, Any]:
        """
        Retrieves the status and details of a specific catalog item bulk update job, including optional related items and field filtering via query parameters.

        Args:
            job_id (string): job_id
            fields_catalog_item_bulk_update_job (string): For more information please visit Example: 'errors,failed_count'.
            fields_catalog_item (string): For more information please visit Example: 'images,external_id'.
            include (string): For more information please visit Example: 'items,items'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Items
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/catalog-item-bulk-update-jobs/{job_id}"
        query_params = {
            k: v
            for k, v in [
                (
                    "fields[catalog-item-bulk-update-job]",
                    fields_catalog_item_bulk_update_job,
                ),
                ("fields[catalog-item]", fields_catalog_item),
                ("include", include),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_delete_catalog_items_jobs(
        self, fields_catalog_item_bulk_delete_job=None, filter=None, page_cursor=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of catalog item bulk delete jobs with optional field filtering, pagination, and revision header support.

        Args:
            fields_catalog_item_bulk_delete_job (string): For more information please visit Example: 'errors,failed_count'.
            filter (string): For more information please visit field(s)/operator(s):<br>`status`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Items
        """
        url = f"{self.base_url}/api/catalog-item-bulk-delete-jobs"
        query_params = {
            k: v
            for k, v in [
                (
                    "fields[catalog-item-bulk-delete-job]",
                    fields_catalog_item_bulk_delete_job,
                ),
                ("filter", filter),
                ("page[cursor]", page_cursor),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_delete_catalog_items(self, data=None) -> dict[str, Any]:
        """
        Creates a bulk delete job for catalog items with a specified revision header, returning 202 on success, 400 for bad requests, or 500 for server errors.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "items": {
                        "data": [
                          {
                            "id": "<string>",
                            "type": "catalog-item"
                          },
                          {
                            "id": "<string>",
                            "type": "catalog-item"
                          }
                        ]
                      }
                    },
                    "type": "catalog-item-bulk-delete-job"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Items
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-item-bulk-delete-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_delete_catalog_items_job(
        self, job_id, fields_catalog_item_bulk_delete_job=None
    ) -> dict[str, Any]:
        """
        Retrieve a catalog item bulk delete job by its job ID, allowing for the inspection of job details such as status and progress, with optional filtering of returned fields and specification of a revision.

        Args:
            job_id (string): job_id
            fields_catalog_item_bulk_delete_job (string): For more information please visit Example: 'errors,failed_count'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Items
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/catalog-item-bulk-delete-jobs/{job_id}"
        query_params = {
            k: v
            for k, v in [
                (
                    "fields[catalog-item-bulk-delete-job]",
                    fields_catalog_item_bulk_delete_job,
                )
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_items_for_catalog_category(
        self,
        id,
        fields_catalog_item=None,
        fields_catalog_variant=None,
        filter=None,
        include=None,
        page_cursor=None,
        sort=None,
    ) -> dict[str, Any]:
        """
        Retrieve a list of items within a specified catalog category by ID, allowing optional filtering, sorting, and inclusion of additional details.

        Args:
            id (string): id
            fields_catalog_item (string): For more information please visit Example: 'images,external_id'.
            fields_catalog_variant (string): For more information please visit Example: 'title,price'.
            filter (string): For more information please visit field(s)/operator(s):<br>`ids`: `any`<br>`category.id`: `equals`<br>`title`: `contains`<br>`published`: `equals` Example: '<string>'.
            include (string): For more information please visit Example: 'variants,variants'.
            page_cursor (string): For more information please visit Example: '<string>'.
            sort (string): For more information please visit Example: 'created'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Items
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-categories/{id}/items"
        query_params = {
            k: v
            for k, v in [
                ("fields[catalog-item]", fields_catalog_item),
                ("fields[catalog-variant]", fields_catalog_variant),
                ("filter", filter),
                ("include", include),
                ("page[cursor]", page_cursor),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_category_ids_for_catalog_item(
        self, id, filter=None, page_cursor=None, sort=None
    ) -> dict[str, Any]:
        """
        The API operation at path "/api/catalog-items/{id}/relationships/categories" using the "GET" method retrieves the category relationships for a specific catalog item identified by its ID, allowing filtering, pagination, and sorting of the results, with optional revision specification in the header.

        Args:
            id (string): id
            filter (string): For more information please visit field(s)/operator(s):<br>`ids`: `any`<br>`item.id`: `equals`<br>`name`: `contains` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.
            sort (string): For more information please visit Example: 'created'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Items
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-items/{id}/relationships/categories"
        query_params = {
            k: v
            for k, v in [
                ("filter", filter),
                ("page[cursor]", page_cursor),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_categories_to_catalog_item(self, id, data=None) -> Any:
        """
        Adds a relationship between the specified catalog item and one or more categories using the provided revision header.

        Args:
            id (string): id
            data (array): data
                Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "catalog-category"
                    },
                    {
                      "id": "<string>",
                      "type": "catalog-category"
                    }
                  ]
                }
                ```

        Returns:
            Any: Success

        Tags:
            Catalogs, Items
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-items/{id}/relationships/categories"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_categories_from_catalog_item(self, id, data=None) -> Any:
        """
        Deletes a relationship between a catalog item, identified by `{id}`, and its categories, requiring a revision provided in the header for validation.

        Args:
            id (string): id
            data (array): data
                Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "catalog-category"
                    },
                    {
                      "id": "<string>",
                      "type": "catalog-category"
                    }
                  ]
                }
                ```

        Returns:
            Any: Success

        Tags:
            Catalogs, Items
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-items/{id}/relationships/categories"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_categories_for_catalog_item(self, id, data=None) -> Any:
        """
        This API operation updates the categories relationship for a catalog item by applying partial modifications using the PATCH method, requiring a revision header to ensure data consistency.

        Args:
            id (string): id
            data (array): data
                Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "catalog-category"
                    },
                    {
                      "id": "<string>",
                      "type": "catalog-category"
                    }
                  ]
                }
                ```

        Returns:
            Any: Success

        Tags:
            Catalogs, Items
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-items/{id}/relationships/categories"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_catalog_variants(
        self, fields_catalog_variant=None, filter=None, page_cursor=None, sort=None
    ) -> dict[str, Any]:
        """
        Retrieves all catalog variants with optional filtering, sorting, pagination, and field selection parameters.

        Args:
            fields_catalog_variant (string): For more information please visit Example: 'title,price'.
            filter (string): For more information please visit field(s)/operator(s):<br>`ids`: `any`<br>`item.id`: `equals`<br>`sku`: `equals`<br>`title`: `contains`<br>`published`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.
            sort (string): For more information please visit Example: 'created'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Variants
        """
        url = f"{self.base_url}/api/catalog-variants"
        query_params = {
            k: v
            for k, v in [
                ("fields[catalog-variant]", fields_catalog_variant),
                ("filter", filter),
                ("page[cursor]", page_cursor),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_catalog_variant(self, data=None) -> dict[str, Any]:
        """
        Creates a new catalog variant with the provided data, requiring a revision header and returning status codes for success (201), client errors (400), and server errors (500).

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "catalog_type": "$default",
                      "custom_metadata": {},
                      "description": "<string>",
                      "external_id": "<string>",
                      "image_full_url": "<string>",
                      "image_thumbnail_url": "<string>",
                      "images": [
                        "<string>",
                        "<string>"
                      ],
                      "integration_type": "$custom",
                      "inventory_policy": 0,
                      "inventory_quantity": "<number>",
                      "price": "<number>",
                      "published": true,
                      "sku": "<string>",
                      "title": "<string>",
                      "url": "<string>"
                    },
                    "relationships": {
                      "item": {
                        "data": {
                          "id": "<string>",
                          "type": "catalog-item"
                        }
                      }
                    },
                    "type": "catalog-variant"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Variants
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-variants"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_catalog_variant(self, id, fields_catalog_variant=None) -> dict[str, Any]:
        """
        Retrieves a catalog variant by ID with optional field filtering and revision header support.

        Args:
            id (string): id
            fields_catalog_variant (string): For more information please visit Example: 'title,price'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Variants
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-variants/{id}"
        query_params = {
            k: v
            for k, v in [("fields[catalog-variant]", fields_catalog_variant)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_catalog_variant(self, id) -> Any:
        """
        Deletes a catalog variant by its ID using a specified header revision, returning status codes for success (204), client error (400), or server error (500).

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            Catalogs, Variants
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-variants/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_catalog_variant(self, id, data=None) -> dict[str, Any]:
        """
        Updates a catalog variant's partial data using a revision header and returns the updated result upon success.

        Args:
            id (string): id
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "custom_metadata": {},
                      "description": "<string>",
                      "image_full_url": "<string>",
                      "image_thumbnail_url": "<string>",
                      "images": [
                        "<string>",
                        "<string>"
                      ],
                      "inventory_policy": 0,
                      "inventory_quantity": "<number>",
                      "price": "<number>",
                      "published": "<boolean>",
                      "sku": "<string>",
                      "title": "<string>",
                      "url": "<string>"
                    },
                    "id": "<string>",
                    "type": "catalog-variant"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Variants
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-variants/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_create_variants_jobs(
        self, fields_catalog_variant_bulk_create_job=None, filter=None, page_cursor=None
    ) -> dict[str, Any]:
        """
        Retrieves a catalog variant bulk create job by ID, supporting optional filtering, pagination, and field selection in the response.

        Args:
            fields_catalog_variant_bulk_create_job (string): For more information please visit Example: 'errors,failed_count'.
            filter (string): For more information please visit field(s)/operator(s):<br>`status`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Variants
        """
        url = f"{self.base_url}/api/catalog-variant-bulk-create-jobs"
        query_params = {
            k: v
            for k, v in [
                (
                    "fields[catalog-variant-bulk-create-job]",
                    fields_catalog_variant_bulk_create_job,
                ),
                ("filter", filter),
                ("page[cursor]", page_cursor),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_create_catalog_variants(self, data=None) -> dict[str, Any]:
        """
        The **POST /api/catalog-variant-bulk-create-jobs** operation creates a job to bulk create catalog variants, accepting up to 100 variants per request, with a required "revision" header for versioning.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "variants": {
                        "data": [
                          {
                            "attributes": {
                              "catalog_type": "$default",
                              "custom_metadata": {},
                              "description": "<string>",
                              "external_id": "<string>",
                              "image_full_url": "<string>",
                              "image_thumbnail_url": "<string>",
                              "images": [
                                "<string>",
                                "<string>"
                              ],
                              "integration_type": "$custom",
                              "inventory_policy": 0,
                              "inventory_quantity": "<number>",
                              "price": "<number>",
                              "published": true,
                              "sku": "<string>",
                              "title": "<string>",
                              "url": "<string>"
                            },
                            "relationships": {
                              "item": {
                                "data": {
                                  "id": "<string>",
                                  "type": "catalog-item"
                                }
                              }
                            },
                            "type": "catalog-variant"
                          },
                          {
                            "attributes": {
                              "catalog_type": "$default",
                              "custom_metadata": {},
                              "description": "<string>",
                              "external_id": "<string>",
                              "image_full_url": "<string>",
                              "image_thumbnail_url": "<string>",
                              "images": [
                                "<string>",
                                "<string>"
                              ],
                              "integration_type": "$custom",
                              "inventory_policy": 0,
                              "inventory_quantity": "<number>",
                              "price": "<number>",
                              "published": true,
                              "sku": "<string>",
                              "title": "<string>",
                              "url": "<string>"
                            },
                            "relationships": {
                              "item": {
                                "data": {
                                  "id": "<string>",
                                  "type": "catalog-item"
                                }
                              }
                            },
                            "type": "catalog-variant"
                          }
                        ]
                      }
                    },
                    "type": "catalog-variant-bulk-create-job"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Variants
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-variant-bulk-create-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_create_variants_job(
        self,
        job_id,
        fields_catalog_variant_bulk_create_job=None,
        fields_catalog_variant=None,
        include=None,
    ) -> dict[str, Any]:
        """
        Retrieve details of a specific catalog variant bulk creation job by its ID, supporting optional field selection, inclusion of related resources, and requiring a revision header.

        Args:
            job_id (string): job_id
            fields_catalog_variant_bulk_create_job (string): For more information please visit Example: 'errors,failed_count'.
            fields_catalog_variant (string): For more information please visit Example: 'title,price'.
            include (string): For more information please visit Example: 'variants,variants'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Variants
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/catalog-variant-bulk-create-jobs/{job_id}"
        query_params = {
            k: v
            for k, v in [
                (
                    "fields[catalog-variant-bulk-create-job]",
                    fields_catalog_variant_bulk_create_job,
                ),
                ("fields[catalog-variant]", fields_catalog_variant),
                ("include", include),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_update_variants_jobs(
        self, fields_catalog_variant_bulk_update_job=None, filter=None, page_cursor=None
    ) -> dict[str, Any]:
        """
        The **GET** operation at "/api/catalog-variant-bulk-update-jobs" retrieves a list of catalog variant bulk update jobs, allowing users to filter results by specific fields and pagination options.

        Args:
            fields_catalog_variant_bulk_update_job (string): For more information please visit Example: 'errors,failed_count'.
            filter (string): For more information please visit field(s)/operator(s):<br>`status`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Variants
        """
        url = f"{self.base_url}/api/catalog-variant-bulk-update-jobs"
        query_params = {
            k: v
            for k, v in [
                (
                    "fields[catalog-variant-bulk-update-job]",
                    fields_catalog_variant_bulk_update_job,
                ),
                ("filter", filter),
                ("page[cursor]", page_cursor),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_update_catalog_variants(self, data=None) -> dict[str, Any]:
        """
        Creates a catalog variant bulk update job to process batch updates for multiple product variants.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "variants": {
                        "data": [
                          {
                            "attributes": {
                              "custom_metadata": {},
                              "description": "<string>",
                              "image_full_url": "<string>",
                              "image_thumbnail_url": "<string>",
                              "images": [
                                "<string>",
                                "<string>"
                              ],
                              "inventory_policy": 2,
                              "inventory_quantity": "<number>",
                              "price": "<number>",
                              "published": "<boolean>",
                              "sku": "<string>",
                              "title": "<string>",
                              "url": "<string>"
                            },
                            "id": "<string>",
                            "type": "catalog-variant"
                          },
                          {
                            "attributes": {
                              "custom_metadata": {},
                              "description": "<string>",
                              "image_full_url": "<string>",
                              "image_thumbnail_url": "<string>",
                              "images": [
                                "<string>",
                                "<string>"
                              ],
                              "inventory_policy": 0,
                              "inventory_quantity": "<number>",
                              "price": "<number>",
                              "published": "<boolean>",
                              "sku": "<string>",
                              "title": "<string>",
                              "url": "<string>"
                            },
                            "id": "<string>",
                            "type": "catalog-variant"
                          }
                        ]
                      }
                    },
                    "type": "catalog-variant-bulk-update-job"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Variants
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-variant-bulk-update-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_update_variants_job(
        self,
        job_id,
        fields_catalog_variant_bulk_update_job=None,
        fields_catalog_variant=None,
        include=None,
    ) -> dict[str, Any]:
        """
        The API operation defined at path "/api/catalog-variant-bulk-update-jobs/{job_id}" using the "GET" method retrieves details about a specific catalog variant bulk update job, allowing optional specification of fields to include and related objects.

        Args:
            job_id (string): job_id
            fields_catalog_variant_bulk_update_job (string): For more information please visit Example: 'errors,failed_count'.
            fields_catalog_variant (string): For more information please visit Example: 'title,price'.
            include (string): For more information please visit Example: 'variants,variants'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Variants
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/catalog-variant-bulk-update-jobs/{job_id}"
        query_params = {
            k: v
            for k, v in [
                (
                    "fields[catalog-variant-bulk-update-job]",
                    fields_catalog_variant_bulk_update_job,
                ),
                ("fields[catalog-variant]", fields_catalog_variant),
                ("include", include),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_delete_variants_jobs(
        self, fields_catalog_variant_bulk_delete_job=None, filter=None, page_cursor=None
    ) -> dict[str, Any]:
        """
        The API operation at path "/api/catalog-variant-bulk-delete-jobs" using the "GET" method retrieves information about catalog variant bulk delete jobs, allowing filtering and pagination, and providing specific fields of the job based on query parameters.

        Args:
            fields_catalog_variant_bulk_delete_job (string): For more information please visit Example: 'errors,failed_count'.
            filter (string): For more information please visit field(s)/operator(s):<br>`status`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Variants
        """
        url = f"{self.base_url}/api/catalog-variant-bulk-delete-jobs"
        query_params = {
            k: v
            for k, v in [
                (
                    "fields[catalog-variant-bulk-delete-job]",
                    fields_catalog_variant_bulk_delete_job,
                ),
                ("filter", filter),
                ("page[cursor]", page_cursor),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_delete_catalog_variants(self, data=None) -> dict[str, Any]:
        """
        Creates a bulk delete job for catalog variants, accepting up to 100 variants per request, with header parameter "revision" and returning 202, 400, or 500 status codes.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "variants": {
                        "data": [
                          {
                            "id": "<string>",
                            "type": "catalog-variant"
                          },
                          {
                            "id": "<string>",
                            "type": "catalog-variant"
                          }
                        ]
                      }
                    },
                    "type": "catalog-variant-bulk-delete-job"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Variants
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-variant-bulk-delete-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_delete_variants_job(
        self, job_id, fields_catalog_variant_bulk_delete_job=None
    ) -> dict[str, Any]:
        """
        Retrieve a specific catalog variant bulk delete job's status and details by its job ID, supporting optional field filtering via query parameters and API version control through headers.

        Args:
            job_id (string): job_id
            fields_catalog_variant_bulk_delete_job (string): For more information please visit Example: 'errors,failed_count'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Variants
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/catalog-variant-bulk-delete-jobs/{job_id}"
        query_params = {
            k: v
            for k, v in [
                (
                    "fields[catalog-variant-bulk-delete-job]",
                    fields_catalog_variant_bulk_delete_job,
                )
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_variants_for_catalog_item(
        self, id, fields_catalog_variant=None, filter=None, page_cursor=None, sort=None
    ) -> dict[str, Any]:
        """
        Retrieves a catalog item's variants with optional filtering, sorting, pagination, and field selection.

        Args:
            id (string): id
            fields_catalog_variant (string): For more information please visit Example: 'title,price'.
            filter (string): For more information please visit field(s)/operator(s):<br>`ids`: `any`<br>`item.id`: `equals`<br>`sku`: `equals`<br>`title`: `contains`<br>`published`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.
            sort (string): For more information please visit Example: 'created'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Variants
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-items/{id}/variants"
        query_params = {
            k: v
            for k, v in [
                ("fields[catalog-variant]", fields_catalog_variant),
                ("filter", filter),
                ("page[cursor]", page_cursor),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_variant_ids_for_catalog_item(
        self, id, filter=None, page_cursor=None, sort=None
    ) -> dict[str, Any]:
        """
        Retrieves variant relationships for a catalog item with optional filtering, pagination, and sorting parameters.

        Args:
            id (string): id
            filter (string): For more information please visit field(s)/operator(s):<br>`ids`: `any`<br>`item.id`: `equals`<br>`sku`: `equals`<br>`title`: `contains`<br>`published`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.
            sort (string): For more information please visit Example: 'created'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Variants
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-items/{id}/relationships/variants"
        query_params = {
            k: v
            for k, v in [
                ("filter", filter),
                ("page[cursor]", page_cursor),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_catalog_categories(
        self, fields_catalog_category=None, filter=None, page_cursor=None, sort=None
    ) -> dict[str, Any]:
        """
        The "/api/catalog-categories" API operation using the "GET" method retrieves a list of catalog categories, allowing filtering, sorting, and pagination through query parameters, while also supporting revision specification via a header.

        Args:
            fields_catalog_category (string): For more information please visit Example: 'external_id,external_id'.
            filter (string): For more information please visit field(s)/operator(s):<br>`ids`: `any`<br>`item.id`: `equals`<br>`name`: `contains` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.
            sort (string): For more information please visit Example: 'created'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Categories
        """
        url = f"{self.base_url}/api/catalog-categories"
        query_params = {
            k: v
            for k, v in [
                ("fields[catalog-category]", fields_catalog_category),
                ("filter", filter),
                ("page[cursor]", page_cursor),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_catalog_category(self, data=None) -> dict[str, Any]:
        """
        Creates a new catalog category using specified parameters, returning a 201 status code on successful creation.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "catalog_type": "$default",
                      "external_id": "<string>",
                      "integration_type": "$custom",
                      "name": "<string>"
                    },
                    "relationships": {
                      "items": {
                        "data": [
                          {
                            "id": "<string>",
                            "type": "catalog-item"
                          },
                          {
                            "id": "<string>",
                            "type": "catalog-item"
                          }
                        ]
                      }
                    },
                    "type": "catalog-category"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Categories
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-categories"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_catalog_category(self, id, fields_catalog_category=None) -> dict[str, Any]:
        """
        Retrieves a specific catalog category by ID with optional field selection and revision header.

        Args:
            id (string): id
            fields_catalog_category (string): For more information please visit Example: 'external_id,external_id'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Categories
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-categories/{id}"
        query_params = {
            k: v
            for k, v in [("fields[catalog-category]", fields_catalog_category)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_catalog_category(self, id) -> Any:
        """
        Deletes a catalog category identified by its ID, accepting an optional revision header, and returns a successful response with a 204 status code if executed correctly.

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            Catalogs, Categories
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-categories/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_catalog_category(self, id, data=None) -> dict[str, Any]:
        """
        Patches a catalog category with the specified ID, allowing partial updates while requiring a revision header for version control.

        Args:
            id (string): id
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "name": "<string>"
                    },
                    "id": "<string>",
                    "relationships": {
                      "items": {
                        "data": [
                          {
                            "id": "<string>",
                            "type": "catalog-item"
                          },
                          {
                            "id": "<string>",
                            "type": "catalog-item"
                          }
                        ]
                      }
                    },
                    "type": "catalog-category"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Categories
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-categories/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_create_categories_jobs(
        self,
        fields_catalog_category_bulk_create_job=None,
        filter=None,
        page_cursor=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of catalog category bulk creation jobs with support for filtering, field selection, pagination via cursor, and revision headers.

        Args:
            fields_catalog_category_bulk_create_job (string): For more information please visit Example: 'errors,failed_count'.
            filter (string): For more information please visit field(s)/operator(s):<br>`status`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Categories
        """
        url = f"{self.base_url}/api/catalog-category-bulk-create-jobs"
        query_params = {
            k: v
            for k, v in [
                (
                    "fields[catalog-category-bulk-create-job]",
                    fields_catalog_category_bulk_create_job,
                ),
                ("filter", filter),
                ("page[cursor]", page_cursor),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_create_catalog_categories(self, data=None) -> dict[str, Any]:
        """
        Create bulk jobs for catalog category creation, tracking progress via asynchronous processing.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "categories": {
                        "data": [
                          {
                            "attributes": {
                              "catalog_type": "$default",
                              "external_id": "<string>",
                              "integration_type": "$custom",
                              "name": "<string>"
                            },
                            "relationships": {
                              "items": {
                                "data": [
                                  {
                                    "id": "<string>",
                                    "type": "catalog-item"
                                  },
                                  {
                                    "id": "<string>",
                                    "type": "catalog-item"
                                  }
                                ]
                              }
                            },
                            "type": "catalog-category"
                          },
                          {
                            "attributes": {
                              "catalog_type": "$default",
                              "external_id": "<string>",
                              "integration_type": "$custom",
                              "name": "<string>"
                            },
                            "relationships": {
                              "items": {
                                "data": [
                                  {
                                    "id": "<string>",
                                    "type": "catalog-item"
                                  },
                                  {
                                    "id": "<string>",
                                    "type": "catalog-item"
                                  }
                                ]
                              }
                            },
                            "type": "catalog-category"
                          }
                        ]
                      }
                    },
                    "type": "catalog-category-bulk-create-job"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Categories
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-category-bulk-create-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_create_categories_job(
        self,
        job_id,
        fields_catalog_category_bulk_create_job=None,
        fields_catalog_category=None,
        include=None,
    ) -> dict[str, Any]:
        """
        The **`GET /api/catalog-category-bulk-create-jobs/{job_id}`** operation retrieves a specific catalog category bulk create job by its job ID, optionally including related resources such as categories based on the provided query parameters.

        Args:
            job_id (string): job_id
            fields_catalog_category_bulk_create_job (string): For more information please visit Example: 'errors,failed_count'.
            fields_catalog_category (string): For more information please visit Example: 'external_id,external_id'.
            include (string): For more information please visit Example: 'categories,categories'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Categories
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/catalog-category-bulk-create-jobs/{job_id}"
        query_params = {
            k: v
            for k, v in [
                (
                    "fields[catalog-category-bulk-create-job]",
                    fields_catalog_category_bulk_create_job,
                ),
                ("fields[catalog-category]", fields_catalog_category),
                ("include", include),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_update_categories_jobs(
        self,
        fields_catalog_category_bulk_update_job=None,
        filter=None,
        page_cursor=None,
    ) -> dict[str, Any]:
        """
        The API operation at "/api/catalog-category-bulk-update-jobs" using the "GET" method retrieves details of catalog category bulk update jobs, allowing for customization through query parameters such as fields, filters, and pagination, while also accepting a revision header.

        Args:
            fields_catalog_category_bulk_update_job (string): For more information please visit Example: 'errors,failed_count'.
            filter (string): For more information please visit field(s)/operator(s):<br>`status`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Categories
        """
        url = f"{self.base_url}/api/catalog-category-bulk-update-jobs"
        query_params = {
            k: v
            for k, v in [
                (
                    "fields[catalog-category-bulk-update-job]",
                    fields_catalog_category_bulk_update_job,
                ),
                ("filter", filter),
                ("page[cursor]", page_cursor),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_update_catalog_categories(self, data=None) -> dict[str, Any]:
        """
        This API operation initiates a bulk update job for catalog categories, allowing for the modification of multiple categories simultaneously, with an optional revision header for version control.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "categories": {
                        "data": [
                          {
                            "attributes": {
                              "name": "<string>"
                            },
                            "id": "<string>",
                            "relationships": {
                              "items": {
                                "data": [
                                  {
                                    "id": "<string>",
                                    "type": "catalog-item"
                                  },
                                  {
                                    "id": "<string>",
                                    "type": "catalog-item"
                                  }
                                ]
                              }
                            },
                            "type": "catalog-category"
                          },
                          {
                            "attributes": {
                              "name": "<string>"
                            },
                            "id": "<string>",
                            "relationships": {
                              "items": {
                                "data": [
                                  {
                                    "id": "<string>",
                                    "type": "catalog-item"
                                  },
                                  {
                                    "id": "<string>",
                                    "type": "catalog-item"
                                  }
                                ]
                              }
                            },
                            "type": "catalog-category"
                          }
                        ]
                      }
                    },
                    "type": "catalog-category-bulk-update-job"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Categories
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-category-bulk-update-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_update_categories_job(
        self,
        job_id,
        fields_catalog_category_bulk_update_job=None,
        fields_catalog_category=None,
        include=None,
    ) -> dict[str, Any]:
        """
        Retrieve the status and details of a specific catalog category bulk update job by its ID, supporting optional inclusion of related resources and field filtering.

        Args:
            job_id (string): job_id
            fields_catalog_category_bulk_update_job (string): For more information please visit Example: 'errors,failed_count'.
            fields_catalog_category (string): For more information please visit Example: 'external_id,external_id'.
            include (string): For more information please visit Example: 'categories,categories'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Categories
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/catalog-category-bulk-update-jobs/{job_id}"
        query_params = {
            k: v
            for k, v in [
                (
                    "fields[catalog-category-bulk-update-job]",
                    fields_catalog_category_bulk_update_job,
                ),
                ("fields[catalog-category]", fields_catalog_category),
                ("include", include),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_delete_categories_jobs(
        self,
        fields_catalog_category_bulk_delete_job=None,
        filter=None,
        page_cursor=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of catalog category bulk delete jobs based on specified fields, filters, and pagination, with an optional revision header.

        Args:
            fields_catalog_category_bulk_delete_job (string): For more information please visit Example: 'errors,failed_count'.
            filter (string): For more information please visit field(s)/operator(s):<br>`status`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Categories
        """
        url = f"{self.base_url}/api/catalog-category-bulk-delete-jobs"
        query_params = {
            k: v
            for k, v in [
                (
                    "fields[catalog-category-bulk-delete-job]",
                    fields_catalog_category_bulk_delete_job,
                ),
                ("filter", filter),
                ("page[cursor]", page_cursor),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_delete_catalog_categories(self, data=None) -> dict[str, Any]:
        """
        Creates a catalog category bulk delete job to delete a batch of categories, accepting up to 100 per request and requiring a revision header.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "categories": {
                        "data": [
                          {
                            "id": "<string>",
                            "type": "catalog-category"
                          },
                          {
                            "id": "<string>",
                            "type": "catalog-category"
                          }
                        ]
                      }
                    },
                    "type": "catalog-category-bulk-delete-job"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Categories
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-category-bulk-delete-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_delete_categories_job(
        self, job_id, fields_catalog_category_bulk_delete_job=None
    ) -> dict[str, Any]:
        """
        Retrieves the status and details of a specific catalog category bulk delete job using the provided job ID, with optional field filtering and API version control.

        Args:
            job_id (string): job_id
            fields_catalog_category_bulk_delete_job (string): For more information please visit Example: 'errors,failed_count'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Categories
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/catalog-category-bulk-delete-jobs/{job_id}"
        query_params = {
            k: v
            for k, v in [
                (
                    "fields[catalog-category-bulk-delete-job]",
                    fields_catalog_category_bulk_delete_job,
                )
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_item_ids_for_catalog_category(
        self, id, filter=None, page_cursor=None, sort=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of items related to a specific catalog category with options to filter, sort, and paginate the results.

        Args:
            id (string): id
            filter (string): For more information please visit field(s)/operator(s):<br>`ids`: `any`<br>`category.id`: `equals`<br>`title`: `contains`<br>`published`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.
            sort (string): For more information please visit Example: 'created'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Categories
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-categories/{id}/relationships/items"
        query_params = {
            k: v
            for k, v in [
                ("filter", filter),
                ("page[cursor]", page_cursor),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_items_to_catalog_category(self, id, data=None) -> Any:
        """
        This API operation creates a new relationship between a specified catalog category and items using the POST method, requiring a revision header, and returns a 204 No Content response upon success.

        Args:
            id (string): id
            data (array): data
                Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "catalog-item"
                    },
                    {
                      "id": "<string>",
                      "type": "catalog-item"
                    }
                  ]
                }
                ```

        Returns:
            Any: Success

        Tags:
            Catalogs, Categories
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-categories/{id}/relationships/items"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_items_from_catalog_category(self, id, data=None) -> Any:
        """
        Deletes the relationship between a catalog category and its associated items, identified by the category ID provided in the path, and returns a successful response with no content upon completion.

        Args:
            id (string): id
            data (array): data
                Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "catalog-item"
                    },
                    {
                      "id": "<string>",
                      "type": "catalog-item"
                    }
                  ]
                }
                ```

        Returns:
            Any: Success

        Tags:
            Catalogs, Categories
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-categories/{id}/relationships/items"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_items_for_catalog_category(self, id, data=None) -> Any:
        """
        This API operation updates the items relationship of a catalog category with the specified ID using the PATCH method, requiring a revision header to ensure atomic updates, and returns a 204 No Content response upon success.

        Args:
            id (string): id
            data (array): data
                Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "catalog-item"
                    },
                    {
                      "id": "<string>",
                      "type": "catalog-item"
                    }
                  ]
                }
                ```

        Returns:
            Any: Success

        Tags:
            Catalogs, Categories
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-categories/{id}/relationships/items"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_categories_for_catalog_item(
        self, id, fields_catalog_category=None, filter=None, page_cursor=None, sort=None
    ) -> dict[str, Any]:
        """
        Retrieves categories associated with a catalog item by ID, allowing for query customization via fields, filters, pagination, sorting, and revision specification.

        Args:
            id (string): id
            fields_catalog_category (string): For more information please visit Example: 'external_id,external_id'.
            filter (string): For more information please visit field(s)/operator(s):<br>`ids`: `any`<br>`item.id`: `equals`<br>`name`: `contains` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.
            sort (string): For more information please visit Example: 'created'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Catalogs, Categories
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-items/{id}/categories"
        query_params = {
            k: v
            for k, v in [
                ("fields[catalog-category]", fields_catalog_category),
                ("filter", filter),
                ("page[cursor]", page_cursor),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_back_in_stock_subscription(self, data=None) -> Any:
        """
        The POST operation at the "/api/back-in-stock-subscriptions" path creates a new back-in-stock subscription, requiring a "revision" header, and returns a 202 response upon success or error responses for bad requests or internal server errors.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "channels": [
                        "PUSH",
                        "SMS"
                      ],
                      "profile": {
                        "data": {
                          "attributes": {
                            "anonymous_id": "<string>",
                            "email": "<string>",
                            "external_id": "<string>",
                            "phone_number": "<string>"
                          },
                          "id": "<string>",
                          "type": "profile"
                        }
                      }
                    },
                    "relationships": {
                      "variant": {
                        "data": {
                          "id": "<string>",
                          "type": "catalog-variant"
                        }
                      }
                    },
                    "type": "back-in-stock-subscription"
                  }
                }
                ```

        Returns:
            Any: Success

        Tags:
            Catalogs, Back In Stock
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/back-in-stock-subscriptions"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_client_subscription(self, company_id=None, data=None) -> Any:
        """
        Creates a subscription for a client, requiring a company_id query parameter and revision header while returning a 202 Accepted status upon successful request.

        Args:
            company_id (string): (Required) Your Public API Key / Site ID. See [this article]( for more details. Example: '{{companyId}}'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "custom_source": "<string>",
                      "profile": {
                        "data": {
                          "attributes": {
                            "_kx": "<string>",
                            "anonymous_id": "<string>",
                            "email": "<string>",
                            "external_id": "<string>",
                            "first_name": "<string>",
                            "image": "<string>",
                            "last_name": "<string>",
                            "locale": "<string>",
                            "location": {
                              "address1": "<string>",
                              "address2": "<string>",
                              "city": "<string>",
                              "country": "<string>",
                              "ip": "<string>",
                              "latitude": "<string>",
                              "longitude": "<string>",
                              "region": "<string>",
                              "timezone": "<string>",
                              "zip": "<string>"
                            },
                            "meta": {
                              "patch_properties": {
                                "append": {},
                                "unappend": {},
                                "unset": "<string>"
                              }
                            },
                            "organization": "<string>",
                            "phone_number": "<string>",
                            "properties": {},
                            "subscriptions": {
                              "email": {
                                "marketing": {
                                  "consent": "SUBSCRIBED",
                                  "consented_at": "<dateTime>"
                                }
                              },
                              "sms": {
                                "marketing": {
                                  "consent": "SUBSCRIBED",
                                  "consented_at": "<dateTime>"
                                },
                                "transactional": {
                                  "consent": "SUBSCRIBED",
                                  "consented_at": "<dateTime>"
                                }
                              }
                            },
                            "title": "<string>"
                          },
                          "id": "<string>",
                          "type": "profile"
                        }
                      }
                    },
                    "relationships": {
                      "list": {
                        "data": {
                          "id": "<string>",
                          "type": "list"
                        }
                      }
                    },
                    "type": "subscription"
                  }
                }
                ```

        Returns:
            Any: Success

        Tags:
            Client
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/client/subscriptions"
        query_params = {k: v for k, v in [("company_id", company_id)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_or_update_client_push_token(self, company_id=None, data=None) -> Any:
        """
        Registers a push token for a client by sending a POST request to "/client/push-tokens," which requires a "company_id" query parameter and a "revision" header, returning a 202 status on success.

        Args:
            company_id (string): (Required) Your Public API Key / Site ID. See [this article]( for more details. Example: '{{companyId}}'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "background": "AVAILABLE",
                      "device_metadata": {
                        "app_build": "<string>",
                        "app_id": "<string>",
                        "app_name": "<string>",
                        "app_version": "<string>",
                        "device_id": "<string>",
                        "device_model": "<string>",
                        "environment": "debug",
                        "klaviyo_sdk": "android",
                        "manufacturer": "<string>",
                        "os_name": "ipados",
                        "os_version": "<string>",
                        "sdk_version": "<string>"
                      },
                      "enablement_status": "AUTHORIZED",
                      "platform": "android",
                      "profile": {
                        "data": {
                          "attributes": {
                            "_kx": "<string>",
                            "anonymous_id": "<string>",
                            "email": "<string>",
                            "external_id": "<string>",
                            "first_name": "<string>",
                            "image": "<string>",
                            "last_name": "<string>",
                            "locale": "<string>",
                            "location": {
                              "address1": "<string>",
                              "address2": "<string>",
                              "city": "<string>",
                              "country": "<string>",
                              "ip": "<string>",
                              "latitude": "<string>",
                              "longitude": "<string>",
                              "region": "<string>",
                              "timezone": "<string>",
                              "zip": "<string>"
                            },
                            "meta": {
                              "patch_properties": {
                                "append": {},
                                "unappend": {},
                                "unset": "<string>"
                              }
                            },
                            "organization": "<string>",
                            "phone_number": "<string>",
                            "properties": {},
                            "title": "<string>"
                          },
                          "id": "<string>",
                          "type": "profile"
                        }
                      },
                      "token": "<string>",
                      "vendor": "apns"
                    },
                    "type": "push-token"
                  }
                }
                ```

        Returns:
            Any: Success

        Tags:
            Client
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/client/push-tokens"
        query_params = {k: v for k, v in [("company_id", company_id)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def unregister_client_push_token(self, company_id=None, data=None) -> Any:
        """
        Unregisters a client's push token by accepting a company ID as a query parameter and requiring a revision header, returning status codes for successful acceptance (202), client errors (400), or server errors (500).

        Args:
            company_id (string): (Required) Your Public API Key / Site ID. See [this article]( for more details. Example: '{{companyId}}'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "platform": "android",
                      "profile": {
                        "data": {
                          "attributes": {
                            "_kx": "<string>",
                            "anonymous_id": "<string>",
                            "email": "<string>",
                            "external_id": "<string>",
                            "first_name": "<string>",
                            "image": "<string>",
                            "last_name": "<string>",
                            "locale": "<string>",
                            "location": {
                              "address1": "<string>",
                              "address2": "<string>",
                              "city": "<string>",
                              "country": "<string>",
                              "ip": "<string>",
                              "latitude": "<string>",
                              "longitude": "<string>",
                              "region": "<string>",
                              "timezone": "<string>",
                              "zip": "<string>"
                            },
                            "organization": "<string>",
                            "phone_number": "<string>",
                            "properties": {},
                            "title": "<string>"
                          },
                          "id": "<string>",
                          "meta": {
                            "patch_properties": {
                              "append": {},
                              "unappend": {},
                              "unset": "<string>"
                            }
                          },
                          "type": "profile"
                        }
                      },
                      "token": "<string>",
                      "vendor": "fcm"
                    },
                    "type": "push-token-unregister"
                  }
                }
                ```

        Returns:
            Any: Success

        Tags:
            Client
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/client/push-token-unregister"
        query_params = {k: v for k, v in [("company_id", company_id)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_client_event(self, company_id=None, data=None) -> Any:
        """
        Creates an event for a client by submitting the event details via the POST method, requiring a `company_id` query parameter and a `revision` header.

        Args:
            company_id (string): (Required) Your Public API Key / Site ID. See [this article]( for more details. Example: '{{companyId}}'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "metric": {
                        "data": {
                          "attributes": {
                            "name": "<string>",
                            "service": "<string>"
                          },
                          "type": "metric"
                        }
                      },
                      "profile": {
                        "data": {
                          "attributes": {
                            "_kx": "<string>",
                            "anonymous_id": "<string>",
                            "email": "<string>",
                            "external_id": "<string>",
                            "first_name": "<string>",
                            "image": "<string>",
                            "last_name": "<string>",
                            "locale": "<string>",
                            "location": {
                              "address1": "<string>",
                              "address2": "<string>",
                              "city": "<string>",
                              "country": "<string>",
                              "ip": "<string>",
                              "latitude": "<string>",
                              "longitude": "<string>",
                              "region": "<string>",
                              "timezone": "<string>",
                              "zip": "<string>"
                            },
                            "meta": {
                              "patch_properties": {
                                "append": {},
                                "unappend": {},
                                "unset": "<string>"
                              }
                            },
                            "organization": "<string>",
                            "phone_number": "<string>",
                            "properties": {},
                            "title": "<string>"
                          },
                          "id": "<string>",
                          "type": "profile"
                        }
                      },
                      "properties": {},
                      "time": "<dateTime>",
                      "unique_id": "<string>",
                      "value": "<number>",
                      "value_currency": "<string>"
                    },
                    "type": "event"
                  }
                }
                ```

        Returns:
            Any: Success

        Tags:
            Client
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/client/events"
        query_params = {k: v for k, v in [("company_id", company_id)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_or_update_client_profile(self, company_id=None, data=None) -> Any:
        """
        Creates client profiles with required company_id in query parameters and revision header, returning status codes for accepted (202), bad request (400), and server error (500).

        Args:
            company_id (string): (Required) Your Public API Key / Site ID. See [this article]( for more details. Example: '{{companyId}}'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "_kx": "<string>",
                      "anonymous_id": "<string>",
                      "email": "<string>",
                      "external_id": "<string>",
                      "first_name": "<string>",
                      "image": "<string>",
                      "last_name": "<string>",
                      "locale": "<string>",
                      "location": {
                        "address1": "<string>",
                        "address2": "<string>",
                        "city": "<string>",
                        "country": "<string>",
                        "ip": "<string>",
                        "latitude": "<string>",
                        "longitude": "<string>",
                        "region": "<string>",
                        "timezone": "<string>",
                        "zip": "<string>"
                      },
                      "organization": "<string>",
                      "phone_number": "<string>",
                      "properties": {},
                      "title": "<string>"
                    },
                    "id": "<string>",
                    "meta": {
                      "patch_properties": {
                        "append": {},
                        "unappend": {},
                        "unset": "<string>"
                      }
                    },
                    "type": "profile"
                  }
                }
                ```

        Returns:
            Any: Success

        Tags:
            Client
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/client/profiles"
        query_params = {k: v for k, v in [("company_id", company_id)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_create_client_events(self, company_id=None, data=None) -> Any:
        """
        Creates multiple client events in bulk using a POST request, requiring a company ID as a query parameter and a revision in the request header.

        Args:
            company_id (string): (Required) Your Public API Key / Site ID. See [this article]( for more details. Example: '{{companyId}}'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "events": {
                        "data": [
                          {
                            "attributes": {
                              "metric": {
                                "data": {
                                  "attributes": {
                                    "name": "<string>",
                                    "service": "<string>"
                                  },
                                  "type": "metric"
                                }
                              },
                              "properties": {},
                              "time": "<dateTime>",
                              "unique_id": "<string>",
                              "value": "<number>",
                              "value_currency": "<string>"
                            },
                            "type": "event"
                          },
                          {
                            "attributes": {
                              "metric": {
                                "data": {
                                  "attributes": {
                                    "name": "<string>",
                                    "service": "<string>"
                                  },
                                  "type": "metric"
                                }
                              },
                              "properties": {},
                              "time": "<dateTime>",
                              "unique_id": "<string>",
                              "value": "<number>",
                              "value_currency": "<string>"
                            },
                            "type": "event"
                          }
                        ]
                      },
                      "profile": {
                        "data": {
                          "attributes": {
                            "_kx": "<string>",
                            "anonymous_id": "<string>",
                            "email": "<string>",
                            "external_id": "<string>",
                            "first_name": "<string>",
                            "image": "<string>",
                            "last_name": "<string>",
                            "locale": "<string>",
                            "location": {
                              "address1": "<string>",
                              "address2": "<string>",
                              "city": "<string>",
                              "country": "<string>",
                              "ip": "<string>",
                              "latitude": "<string>",
                              "longitude": "<string>",
                              "region": "<string>",
                              "timezone": "<string>",
                              "zip": "<string>"
                            },
                            "organization": "<string>",
                            "phone_number": "<string>",
                            "properties": {},
                            "title": "<string>"
                          },
                          "id": "<string>",
                          "meta": {
                            "patch_properties": {
                              "append": {},
                              "unappend": {},
                              "unset": "<string>"
                            }
                          },
                          "type": "profile"
                        }
                      }
                    },
                    "type": "event-bulk-create"
                  }
                }
                ```

        Returns:
            Any: Success

        Tags:
            Client
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/client/event-bulk-create"
        query_params = {k: v for k, v in [("company_id", company_id)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_client_back_in_stock_subscription(
        self, company_id=None, data=None
    ) -> Any:
        """
        Subscribe a customer to receive back-in-stock notifications for a product via POST request, requiring company ID and revision header, with responses indicating acceptance (202), invalid parameters (400), or server errors (500).

        Args:
            company_id (string): (Required) Your Public API Key / Site ID. See [this article]( for more details. Example: '{{companyId}}'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "channels": [
                        "SMS",
                        "PUSH"
                      ],
                      "profile": {
                        "data": {
                          "attributes": {
                            "anonymous_id": "<string>",
                            "email": "<string>",
                            "external_id": "<string>",
                            "phone_number": "<string>"
                          },
                          "id": "<string>",
                          "type": "profile"
                        }
                      }
                    },
                    "relationships": {
                      "variant": {
                        "data": {
                          "id": "<string>",
                          "type": "catalog-variant"
                        }
                      }
                    },
                    "type": "back-in-stock-subscription"
                  }
                }
                ```

        Returns:
            Any: Success

        Tags:
            Client
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/client/back-in-stock-subscriptions"
        query_params = {k: v for k, v in [("company_id", company_id)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_coupons(self, fields_coupon=None, page_cursor=None) -> dict[str, Any]:
        """
        The API operation at "/api/coupons" using the "GET" method retrieves coupon data based on optional query parameters for selecting fields and pagination, with an additional header option for specifying the revision.

        Args:
            fields_coupon (string): For more information please visit Example: 'external_id,external_id'.
            page_cursor (string): For more information please visit Example: '<string>'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Coupons
        """
        url = f"{self.base_url}/api/coupons"
        query_params = {
            k: v
            for k, v in [
                ("fields[coupon]", fields_coupon),
                ("page[cursor]", page_cursor),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_coupon(self, data=None) -> dict[str, Any]:
        """
        Creates a new coupon with a specified revision, returning a successful creation response or error messages for invalid requests or internal server errors.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "description": "<string>",
                      "external_id": "<string>"
                    },
                    "type": "coupon"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Coupons
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/coupons"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_coupon(self, id, fields_coupon=None) -> dict[str, Any]:
        """
        This API operation, located at `/api/coupons/{id}`, uses the GET method to retrieve details of a specific coupon based on its ID, allowing optional filtering by specifying coupon fields in the query and providing a revision in the headers.

        Args:
            id (string): id
            fields_coupon (string): For more information please visit Example: 'external_id,external_id'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Coupons
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/coupons/{id}"
        query_params = {
            k: v for k, v in [("fields[coupon]", fields_coupon)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_coupon(self, id) -> Any:
        """
        Deletes a coupon by ID, returning a 204 status code on success, and requires a revision header; error responses include 400 for invalid requests and 500 for server errors.

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            Coupons
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/coupons/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_coupon(self, id, data=None) -> dict[str, Any]:
        """
        Updates partial coupon data using the specified revision header, returning 200 for success, 400 for invalid requests, or 500 for errors.

        Args:
            id (string): id
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "description": "<string>"
                    },
                    "id": "<string>",
                    "type": "coupon"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Coupons
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/coupons/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_coupon_codes(
        self,
        fields_coupon_code=None,
        fields_coupon=None,
        filter=None,
        include=None,
        page_cursor=None,
    ) -> dict[str, Any]:
        """
        This API operation retrieves a list of coupon codes using the GET method at the "/api/coupon-codes" path, supporting filters and pagination through query parameters such as fields, filter, include, and page cursor, with a required revision header.

        Args:
            fields_coupon_code (string): For more information please visit Example: 'status,unique_code'.
            fields_coupon (string): For more information please visit Example: 'external_id,external_id'.
            filter (string): For more information please visit field(s)/operator(s):<br>`expires_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`status`: `equals`<br>`coupon.id`: `any`, `equals`<br>`profile.id`: `any`, `equals` Example: '<string>'.
            include (string): For more information please visit Example: 'coupon,coupon'.
            page_cursor (string): For more information please visit Example: '<string>'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Coupons
        """
        url = f"{self.base_url}/api/coupon-codes"
        query_params = {
            k: v
            for k, v in [
                ("fields[coupon-code]", fields_coupon_code),
                ("fields[coupon]", fields_coupon),
                ("filter", filter),
                ("include", include),
                ("page[cursor]", page_cursor),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_coupon_code(self, data=None) -> dict[str, Any]:
        """
        Create a new coupon code by sending a POST request to "/api/coupon-codes", optionally specifying a revision in the request headers.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "expires_at": "<dateTime>",
                      "unique_code": "<string>"
                    },
                    "relationships": {
                      "coupon": {
                        "data": {
                          "id": "<string>",
                          "type": "coupon"
                        }
                      }
                    },
                    "type": "coupon-code"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Coupons
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/coupon-codes"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_coupon_code(
        self, id, fields_coupon_code=None, fields_coupon=None, include=None
    ) -> dict[str, Any]:
        """
        Retrieves details of a coupon code by ID, allowing optional specification of fields to include and related resources via query parameters.

        Args:
            id (string): id
            fields_coupon_code (string): For more information please visit Example: 'status,unique_code'.
            fields_coupon (string): For more information please visit Example: 'external_id,external_id'.
            include (string): For more information please visit Example: 'coupon,coupon'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Coupons
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/coupon-codes/{id}"
        query_params = {
            k: v
            for k, v in [
                ("fields[coupon-code]", fields_coupon_code),
                ("fields[coupon]", fields_coupon),
                ("include", include),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_coupon_code(self, id) -> Any:
        """
        Deletes a coupon code with the specified ID, returning a 204 No Content response upon successful deletion, with optional revision information provided in the request headers.

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            Coupons
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/coupon-codes/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_coupon_code(self, id, data=None) -> dict[str, Any]:
        """
        Updates a coupon code's properties using a partial modification request, supporting conditional updates via the revision header.

        Args:
            id (string): id
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "expires_at": "<dateTime>",
                      "status": "USED"
                    },
                    "id": "<string>",
                    "type": "coupon-code"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Coupons
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/coupon-codes/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_create_coupon_code_jobs(
        self, fields_coupon_code_bulk_create_job=None, filter=None, page_cursor=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of bulk coupon code creation jobs, allowing for filtering, pagination, and specification of fields to include in the response.

        Args:
            fields_coupon_code_bulk_create_job (string): For more information please visit Example: 'errors,failed_count'.
            filter (string): For more information please visit field(s)/operator(s):<br>`status`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Coupons
        """
        url = f"{self.base_url}/api/coupon-code-bulk-create-jobs"
        query_params = {
            k: v
            for k, v in [
                (
                    "fields[coupon-code-bulk-create-job]",
                    fields_coupon_code_bulk_create_job,
                ),
                ("filter", filter),
                ("page[cursor]", page_cursor),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_create_coupon_codes(self, data=None) -> dict[str, Any]:
        """
        This API operation creates bulk jobs for coupon code creation via a POST request to the "/api/coupon-code-bulk-create-jobs" endpoint, requiring a revision header, and returns success with a 202 status code or error responses for bad requests (400) and internal server errors (500).

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "coupon-codes": {
                        "data": [
                          {
                            "attributes": {
                              "expires_at": "<dateTime>",
                              "unique_code": "<string>"
                            },
                            "relationships": {
                              "coupon": {
                                "data": {
                                  "id": "<string>",
                                  "type": "coupon"
                                }
                              }
                            },
                            "type": "coupon-code"
                          },
                          {
                            "attributes": {
                              "expires_at": "<dateTime>",
                              "unique_code": "<string>"
                            },
                            "relationships": {
                              "coupon": {
                                "data": {
                                  "id": "<string>",
                                  "type": "coupon"
                                }
                              }
                            },
                            "type": "coupon-code"
                          }
                        ]
                      }
                    },
                    "type": "coupon-code-bulk-create-job"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Coupons
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/coupon-code-bulk-create-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_create_coupon_codes_job(
        self,
        job_id,
        fields_coupon_code_bulk_create_job=None,
        fields_coupon_code=None,
        include=None,
    ) -> dict[str, Any]:
        """
        Retrieves information about a specific coupon code bulk create job by ID, allowing optional filtering of fields and inclusion of related data.

        Args:
            job_id (string): job_id
            fields_coupon_code_bulk_create_job (string): For more information please visit Example: 'errors,failed_count'.
            fields_coupon_code (string): For more information please visit Example: 'status,unique_code'.
            include (string): For more information please visit Example: 'coupon-codes,coupon-codes'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Coupons
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/coupon-code-bulk-create-jobs/{job_id}"
        query_params = {
            k: v
            for k, v in [
                (
                    "fields[coupon-code-bulk-create-job]",
                    fields_coupon_code_bulk_create_job,
                ),
                ("fields[coupon-code]", fields_coupon_code),
                ("include", include),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_coupon_for_coupon_code(self, id, fields_coupon=None) -> dict[str, Any]:
        """
        This API operation retrieves a coupon associated with a specific coupon code by its ID, allowing optional filtering of coupon fields and specifying a revision via header.

        Args:
            id (string): id
            fields_coupon (string): For more information please visit Example: 'external_id,external_id'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Coupons
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/coupon-codes/{id}/coupon"
        query_params = {
            k: v for k, v in [("fields[coupon]", fields_coupon)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_coupon_id_for_coupon_code(self, id) -> dict[str, Any]:
        """
        Retrieves the relationship details of a specific coupon code identified by its ID.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Coupons
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/coupon-codes/{id}/relationships/coupon"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_coupon_codes_for_coupon(
        self, id, fields_coupon_code=None, filter=None, page_cursor=None
    ) -> dict[str, Any]:
        """
        Retrieves coupon codes associated with a specific coupon ID, supporting optional filtering, field selection, and pagination via cursor-based navigation.

        Args:
            id (string): id
            fields_coupon_code (string): For more information please visit Example: 'status,unique_code'.
            filter (string): For more information please visit field(s)/operator(s):<br>`expires_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`status`: `equals`<br>`coupon.id`: `any`, `equals`<br>`profile.id`: `any`, `equals` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Coupons
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/coupons/{id}/coupon-codes"
        query_params = {
            k: v
            for k, v in [
                ("fields[coupon-code]", fields_coupon_code),
                ("filter", filter),
                ("page[cursor]", page_cursor),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_coupon_code_ids_for_coupon(
        self, id, filter=None, page_cursor=None
    ) -> dict[str, Any]:
        """
        This API operation retrieves the relationships between a coupon and its associated coupon codes, allowing for filtering and pagination with optional revision information provided in the request header.

        Args:
            id (string): id
            filter (string): For more information please visit field(s)/operator(s):<br>`expires_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`status`: `equals`<br>`coupon.id`: `any`, `equals`<br>`profile.id`: `any`, `equals` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Coupons
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/coupons/{id}/relationships/coupon-codes"
        query_params = {
            k: v
            for k, v in [("filter", filter), ("page[cursor]", page_cursor)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def request_profile_deletion(self, data=None) -> Any:
        """
        Initiates an asynchronous data privacy deletion job with optional revision control via header parameter.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "profile": {
                        "data": {
                          "attributes": {
                            "email": "<string>",
                            "phone_number": "<string>"
                          },
                          "id": "<string>",
                          "type": "profile"
                        }
                      }
                    },
                    "type": "data-privacy-deletion-job"
                  }
                }
                ```

        Returns:
            Any: Success

        Tags:
            Data Privacy
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/data-privacy-deletion-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_events(
        self,
        fields_event=None,
        fields_metric=None,
        fields_profile=None,
        filter=None,
        include=None,
        page_cursor=None,
        sort=None,
    ) -> dict[str, Any]:
        """
        Retrieves a filtered list of events with customizable fields, pagination, sorting, and related resources.

        Args:
            fields_event (string): For more information please visit Example: 'uuid,datetime'.
            fields_metric (string): For more information please visit Example: 'integration,created'.
            fields_profile (string): For more information please visit Example: 'location.country,location.zip'.
            filter (string): For more information please visit field(s)/operator(s):<br>`metric_id`: `equals`<br>`profile_id`: `equals`<br>`profile`: `has`<br>`datetime`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`timestamp`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than` Example: '<string>'.
            include (string): For more information please visit Example: 'attributions,metric'.
            page_cursor (string): For more information please visit Example: '<string>'.
            sort (string): For more information please visit Example: 'datetime'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Events
        """
        url = f"{self.base_url}/api/events"
        query_params = {
            k: v
            for k, v in [
                ("fields[event]", fields_event),
                ("fields[metric]", fields_metric),
                ("fields[profile]", fields_profile),
                ("filter", filter),
                ("include", include),
                ("page[cursor]", page_cursor),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_event(self, data=None) -> Any:
        """
        Create a new event by sending a POST request to the `/api/events` endpoint, which includes a `revision` header and returns success with a 202 status code, or error responses for bad requests (400) or internal server errors (500).

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "metric": {
                        "data": {
                          "attributes": {
                            "name": "<string>",
                            "service": "<string>"
                          },
                          "type": "metric"
                        }
                      },
                      "profile": {
                        "data": {
                          "attributes": {
                            "_kx": "<string>",
                            "anonymous_id": "<string>",
                            "email": "<string>",
                            "external_id": "<string>",
                            "first_name": "<string>",
                            "image": "<string>",
                            "last_name": "<string>",
                            "locale": "<string>",
                            "location": {
                              "address1": "<string>",
                              "address2": "<string>",
                              "city": "<string>",
                              "country": "<string>",
                              "ip": "<string>",
                              "latitude": "<string>",
                              "longitude": "<string>",
                              "region": "<string>",
                              "timezone": "<string>",
                              "zip": "<string>"
                            },
                            "meta": {
                              "patch_properties": {
                                "append": {},
                                "unappend": {},
                                "unset": "<string>"
                              }
                            },
                            "organization": "<string>",
                            "phone_number": "<string>",
                            "properties": {},
                            "title": "<string>"
                          },
                          "id": "<string>",
                          "type": "profile"
                        }
                      },
                      "properties": {},
                      "time": "<dateTime>",
                      "unique_id": "<string>",
                      "value": "<number>",
                      "value_currency": "<string>"
                    },
                    "type": "event"
                  }
                }
                ```

        Returns:
            Any: Success

        Tags:
            Events
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/events"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_event(
        self,
        id,
        fields_event=None,
        fields_metric=None,
        fields_profile=None,
        include=None,
    ) -> dict[str, Any]:
        """
        Retrieves a specific event by its ID, with optional filtering for fields and inclusion of related data.

        Args:
            id (string): id
            fields_event (string): For more information please visit Example: 'uuid,datetime'.
            fields_metric (string): For more information please visit Example: 'integration,created'.
            fields_profile (string): For more information please visit Example: 'location.country,location.zip'.
            include (string): For more information please visit Example: 'attributions,metric'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Events
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/events/{id}"
        query_params = {
            k: v
            for k, v in [
                ("fields[event]", fields_event),
                ("fields[metric]", fields_metric),
                ("fields[profile]", fields_profile),
                ("include", include),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_create_events(self, data=None) -> Any:
        """
        Creates a batch of events asynchronously via a bulk job with a version-controlled header (revision) and returns status codes for acceptance (202), invalid requests (400), or server errors (500).

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "events-bulk-create": {
                        "data": [
                          {
                            "attributes": {
                              "events": {
                                "data": [
                                  {
                                    "attributes": {
                                      "metric": {
                                        "data": {
                                          "attributes": {
                                            "name": "<string>",
                                            "service": "<string>"
                                          },
                                          "type": "metric"
                                        }
                                      },
                                      "properties": {},
                                      "time": "<dateTime>",
                                      "unique_id": "<string>",
                                      "value": "<number>",
                                      "value_currency": "<string>"
                                    },
                                    "type": "event"
                                  },
                                  {
                                    "attributes": {
                                      "metric": {
                                        "data": {
                                          "attributes": {
                                            "name": "<string>",
                                            "service": "<string>"
                                          },
                                          "type": "metric"
                                        }
                                      },
                                      "properties": {},
                                      "time": "<dateTime>",
                                      "unique_id": "<string>",
                                      "value": "<number>",
                                      "value_currency": "<string>"
                                    },
                                    "type": "event"
                                  }
                                ]
                              },
                              "profile": {
                                "data": {
                                  "attributes": {
                                    "_kx": "<string>",
                                    "anonymous_id": "<string>",
                                    "email": "<string>",
                                    "external_id": "<string>",
                                    "first_name": "<string>",
                                    "image": "<string>",
                                    "last_name": "<string>",
                                    "locale": "<string>",
                                    "location": {
                                      "address1": "<string>",
                                      "address2": "<string>",
                                      "city": "<string>",
                                      "country": "<string>",
                                      "ip": "<string>",
                                      "latitude": "<string>",
                                      "longitude": "<string>",
                                      "region": "<string>",
                                      "timezone": "<string>",
                                      "zip": "<string>"
                                    },
                                    "organization": "<string>",
                                    "phone_number": "<string>",
                                    "properties": {},
                                    "title": "<string>"
                                  },
                                  "id": "<string>",
                                  "meta": {
                                    "patch_properties": {
                                      "append": {},
                                      "unappend": {},
                                      "unset": "<string>"
                                    }
                                  },
                                  "type": "profile"
                                }
                              }
                            },
                            "type": "event-bulk-create"
                          },
                          {
                            "attributes": {
                              "events": {
                                "data": [
                                  {
                                    "attributes": {
                                      "metric": {
                                        "data": {
                                          "attributes": {
                                            "name": "<string>",
                                            "service": "<string>"
                                          },
                                          "type": "metric"
                                        }
                                      },
                                      "properties": {},
                                      "time": "<dateTime>",
                                      "unique_id": "<string>",
                                      "value": "<number>",
                                      "value_currency": "<string>"
                                    },
                                    "type": "event"
                                  },
                                  {
                                    "attributes": {
                                      "metric": {
                                        "data": {
                                          "attributes": {
                                            "name": "<string>",
                                            "service": "<string>"
                                          },
                                          "type": "metric"
                                        }
                                      },
                                      "properties": {},
                                      "time": "<dateTime>",
                                      "unique_id": "<string>",
                                      "value": "<number>",
                                      "value_currency": "<string>"
                                    },
                                    "type": "event"
                                  }
                                ]
                              },
                              "profile": {
                                "data": {
                                  "attributes": {
                                    "_kx": "<string>",
                                    "anonymous_id": "<string>",
                                    "email": "<string>",
                                    "external_id": "<string>",
                                    "first_name": "<string>",
                                    "image": "<string>",
                                    "last_name": "<string>",
                                    "locale": "<string>",
                                    "location": {
                                      "address1": "<string>",
                                      "address2": "<string>",
                                      "city": "<string>",
                                      "country": "<string>",
                                      "ip": "<string>",
                                      "latitude": "<string>",
                                      "longitude": "<string>",
                                      "region": "<string>",
                                      "timezone": "<string>",
                                      "zip": "<string>"
                                    },
                                    "organization": "<string>",
                                    "phone_number": "<string>",
                                    "properties": {},
                                    "title": "<string>"
                                  },
                                  "id": "<string>",
                                  "meta": {
                                    "patch_properties": {
                                      "append": {},
                                      "unappend": {},
                                      "unset": "<string>"
                                    }
                                  },
                                  "type": "profile"
                                }
                              }
                            },
                            "type": "event-bulk-create"
                          }
                        ]
                      }
                    },
                    "type": "event-bulk-create-job"
                  }
                }
                ```

        Returns:
            Any: Success

        Tags:
            Events
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/event-bulk-create-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_metric_for_event(self, id, fields_metric=None) -> dict[str, Any]:
        """
        This API operation retrieves event metric details by ID using a GET request to "/api/events/{id}/metric," allowing specification of metric fields via query parameters and requiring a revision header.

        Args:
            id (string): id
            fields_metric (string): For more information please visit Example: 'integration,created'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Events
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/events/{id}/metric"
        query_params = {
            k: v for k, v in [("fields[metric]", fields_metric)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_metric_id_for_event(self, id) -> dict[str, Any]:
        """
        This API operation retrieves a specific relationship between an event and a metric by ID using a GET request to the "/api/events/{id}/relationships/metric" path, with the ability to specify a revision via a header parameter.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Events
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/events/{id}/relationships/metric"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_profile_for_event(
        self, id, additional_fields_profile=None, fields_profile=None
    ) -> dict[str, Any]:
        """
        This API operation retrieves a profile associated with a specific event by its ID, allowing optional specification of additional fields and profile fields, while also accepting a revision header.

        Args:
            id (string): id
            additional_fields_profile (string): Request additional fields not included by default in the response. Supported values: 'subscriptions', 'predictive_analytics' Example: 'subscriptions,subscriptions'.
            fields_profile (string): For more information please visit Example: 'location.address2,subscriptions.sms.marketing.last_updated'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Events
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/events/{id}/profile"
        query_params = {
            k: v
            for k, v in [
                ("additional-fields[profile]", additional_fields_profile),
                ("fields[profile]", fields_profile),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_profile_id_for_event(self, id) -> dict[str, Any]:
        """
        Retrieves the profile relationship data for the specified event ID.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Events
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/events/{id}/relationships/profile"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flows(
        self,
        fields_flow_action=None,
        fields_flow=None,
        fields_tag=None,
        filter=None,
        include=None,
        page_cursor=None,
        page_size=None,
        sort=None,
    ) -> dict[str, Any]:
        """
        Retrieves flows with optional query parameters for field filtering, pagination, sorting, and inclusion of related resources, supporting cursor-based pagination and custom header-based revision tracking.

        Args:
            fields_flow_action (string): For more information please visit Example: 'render_options.add_org_prefix,send_options.is_transactional'.
            fields_flow (string): For more information please visit Example: 'created,status'.
            fields_tag (string): For more information please visit Example: 'name,name'.
            filter (string): For more information please visit field(s)/operator(s):<br>`id`: `any`<br>`name`: `contains`, `ends-with`, `equals`, `starts-with`<br>`status`: `equals`<br>`archived`: `equals`<br>`created`: `equals`, `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`updated`: `equals`, `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`trigger_type`: `equals` Example: '<string>'.
            include (string): For more information please visit Example: 'tags,flow-actions'.
            page_cursor (string): For more information please visit Example: '<string>'.
            page_size (string): Default: 50. Min: 1. Max: 50. Example: '50'.
            sort (string): For more information please visit Example: '-created'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Flows
        """
        url = f"{self.base_url}/api/flows"
        query_params = {
            k: v
            for k, v in [
                ("fields[flow-action]", fields_flow_action),
                ("fields[flow]", fields_flow),
                ("fields[tag]", fields_tag),
                ("filter", filter),
                ("include", include),
                ("page[cursor]", page_cursor),
                ("page[size]", page_size),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_flow(self, additional_fields_flow=None, data=None) -> dict[str, Any]:
        """
        Creates a new flow resource, supporting optional query parameters for additional flow fields and header-based revision tracking, returning HTTP 201 on success.

        Args:
            additional_fields_flow (string): Request additional fields not included by default in the response. Supported values: 'definition' Example: 'definition,definition'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "definition": {
                        "actions": [
                          {
                            "id": "<string>",
                            "links": {
                              "next": "<string>"
                            },
                            "temporary_id": "<string>",
                            "type": "back-in-stock-delay"
                          },
                          {
                            "id": "<string>",
                            "links": {
                              "next": "<string>"
                            },
                            "temporary_id": "<string>",
                            "type": "back-in-stock-delay"
                          }
                        ],
                        "entry_action_id": "<string>",
                        "profile_filter": {
                          "condition_groups": [
                            {
                              "conditions": [
                                {
                                  "filter": {
                                    "operator": "not-starts-with",
                                    "type": "string",
                                    "value": "<string>"
                                  },
                                  "property": "<string>",
                                  "type": "profile-property"
                                },
                                {
                                  "filter": {
                                    "operator": "not-equals",
                                    "type": "string",
                                    "value": "<string>"
                                  },
                                  "property": "<string>",
                                  "type": "profile-property"
                                }
                              ]
                            },
                            {
                              "conditions": [
                                {
                                  "filter": {
                                    "operator": "equals",
                                    "type": "string",
                                    "value": "<string>"
                                  },
                                  "property": "<string>",
                                  "type": "profile-property"
                                },
                                {
                                  "filter": {
                                    "operator": "not-starts-with",
                                    "type": "string",
                                    "value": "<string>"
                                  },
                                  "property": "<string>",
                                  "type": "profile-property"
                                }
                              ]
                            }
                          ]
                        },
                        "triggers": [
                          {
                            "id": "<string>",
                            "type": "list"
                          },
                          {
                            "id": "<string>",
                            "type": "list"
                          }
                        ]
                      },
                      "name": "<string>"
                    },
                    "type": "flow"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Flows
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/flows"
        query_params = {
            k: v
            for k, v in [("additional-fields[flow]", additional_fields_flow)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flow(
        self,
        id,
        additional_fields_flow=None,
        fields_flow_action=None,
        fields_flow=None,
        fields_tag=None,
        include=None,
    ) -> dict[str, Any]:
        """
        Retrieves a flow by ID with optional filtering by additional fields, flow actions, flow details, tags, and includes, using a specified revision from the header.

        Args:
            id (string): id
            additional_fields_flow (string): Request additional fields not included by default in the response. Supported values: 'definition' Example: 'definition,definition'.
            fields_flow_action (string): For more information please visit Example: 'render_options.add_org_prefix,send_options.is_transactional'.
            fields_flow (string): For more information please visit Example: 'status,definition.triggers'.
            fields_tag (string): For more information please visit Example: 'name,name'.
            include (string): For more information please visit Example: 'tags,flow-actions'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Flows
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flows/{id}"
        query_params = {
            k: v
            for k, v in [
                ("additional-fields[flow]", additional_fields_flow),
                ("fields[flow-action]", fields_flow_action),
                ("fields[flow]", fields_flow),
                ("fields[tag]", fields_tag),
                ("include", include),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_flow(self, id) -> Any:
        """
        Deletes the flow with the specified ID, requiring a revision header, and returns a 204 (No Content) on success, with 400 and 500 codes for client errors and server failures.

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            Flows
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flows/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_flow_status(self, id, data=None) -> dict[str, Any]:
        """
        Updates a specific flow by ID using partial modifications, requiring a revision header.

        Args:
            id (string): id
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "status": "<string>"
                    },
                    "id": "<string>",
                    "type": "flow"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Flows
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/flows/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flow_action(
        self,
        id,
        fields_flow_action=None,
        fields_flow_message=None,
        fields_flow=None,
        include=None,
    ) -> dict[str, Any]:
        """
        Retrieves a specific flow action by ID, optionally including additional fields and related resources, with support for revision tracking via a header.

        Args:
            id (string): id
            fields_flow_action (string): For more information please visit Example: 'render_options.add_org_prefix,send_options.is_transactional'.
            fields_flow_message (string): For more information please visit Example: 'content.cc_email,content.reply_to_email'.
            fields_flow (string): For more information please visit Example: 'created,status'.
            include (string): For more information please visit Example: 'flow-messages,flow-messages'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Flows
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flow-actions/{id}"
        query_params = {
            k: v
            for k, v in [
                ("fields[flow-action]", fields_flow_action),
                ("fields[flow-message]", fields_flow_message),
                ("fields[flow]", fields_flow),
                ("include", include),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flow_message(
        self,
        id,
        fields_flow_action=None,
        fields_flow_message=None,
        fields_template=None,
        include=None,
    ) -> dict[str, Any]:
        """
        Retrieves a specific flow message by ID with optional filtering (fields selection) and related resource inclusion (include parameter).

        Args:
            id (string): id
            fields_flow_action (string): For more information please visit Example: 'render_options.add_org_prefix,send_options.is_transactional'.
            fields_flow_message (string): For more information please visit Example: 'content.cc_email,content.reply_to_email'.
            fields_template (string): For more information please visit Example: 'name,text'.
            include (string): For more information please visit Example: 'template,template'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Flows
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flow-messages/{id}"
        query_params = {
            k: v
            for k, v in [
                ("fields[flow-action]", fields_flow_action),
                ("fields[flow-message]", fields_flow_message),
                ("fields[template]", fields_template),
                ("include", include),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_actions_for_flow(
        self,
        id,
        fields_flow_action=None,
        filter=None,
        page_cursor=None,
        page_size=None,
        sort=None,
    ) -> dict[str, Any]:
        """
        Retrieves flow actions for a specific flow with filtering, pagination, and field selection capabilities.

        Args:
            id (string): id
            fields_flow_action (string): For more information please visit Example: 'render_options.add_org_prefix,send_options.is_transactional'.
            filter (string): For more information please visit field(s)/operator(s):<br>`id`: `any`<br>`action_type`: `any`, `equals`<br>`status`: `equals`<br>`created`: `equals`, `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`updated`: `equals`, `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.
            page_size (string): Default: 50. Min: 1. Max: 50. Example: '50'.
            sort (string): For more information please visit Example: 'action_type'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Flows
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flows/{id}/flow-actions"
        query_params = {
            k: v
            for k, v in [
                ("fields[flow-action]", fields_flow_action),
                ("filter", filter),
                ("page[cursor]", page_cursor),
                ("page[size]", page_size),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_action_ids_for_flow(
        self, id, filter=None, page_cursor=None, page_size=None, sort=None
    ) -> dict[str, Any]:
        """
        The API operation at "/api/flows/{id}/relationships/flow-actions" using the "GET" method retrieves relationships associated with flow actions for a specific flow ID, allowing filtering, pagination, and sorting of results.

        Args:
            id (string): id
            filter (string): For more information please visit field(s)/operator(s):<br>`id`: `any`<br>`action_type`: `any`, `equals`<br>`status`: `equals`<br>`created`: `equals`, `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`updated`: `equals`, `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.
            page_size (string): Default: 50. Min: 1. Max: 50. Example: '50'.
            sort (string): For more information please visit Example: 'action_type'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Flows
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flows/{id}/relationships/flow-actions"
        query_params = {
            k: v
            for k, v in [
                ("filter", filter),
                ("page[cursor]", page_cursor),
                ("page[size]", page_size),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tags_for_flow(self, id, fields_tag=None) -> dict[str, Any]:
        """
        Retrieves the tags associated with a specific flow identified by its ID, allowing optional filtering of tag fields and requiring a revision header.

        Args:
            id (string): id
            fields_tag (string): For more information please visit Example: 'name,name'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Flows
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flows/{id}/tags"
        query_params = {k: v for k, v in [("fields[tag]", fields_tag)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag_ids_for_flow(self, id) -> dict[str, Any]:
        """
        Retrieves the tag relationships associated with a specific flow ID, requiring a revision header parameter, and returns success (200), client error (400), or server error (500) responses.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Flows
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flows/{id}/relationships/tags"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flow_for_flow_action(self, id, fields_flow=None) -> dict[str, Any]:
        """
        Retrieves the flow details associated with a specific flow action by ID, allowing optional filtering of flow fields and specifying a revision via headers.

        Args:
            id (string): id
            fields_flow (string): For more information please visit Example: 'created,status'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Flows
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flow-actions/{id}/flow"
        query_params = {
            k: v for k, v in [("fields[flow]", fields_flow)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flow_id_for_flow_action(self, id) -> dict[str, Any]:
        """
        Retrieves relationships for a specific flow action identified by `{id}`, requiring a `revision` header and returning responses for successful retrieval, bad requests, or server errors.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Flows
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flow-actions/{id}/relationships/flow"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_messages_for_flow_action(
        self,
        id,
        fields_flow_message=None,
        filter=None,
        page_cursor=None,
        page_size=None,
        sort=None,
    ) -> dict[str, Any]:
        """
        This API operation, accessible via GET method at the "/api/flow-actions/{id}/flow-messages" path, retrieves flow messages associated with a specific flow action identified by "id," allowing customization through query parameters for fields, filtering, pagination, and sorting, with additional revision details provided in the header.

        Args:
            id (string): id
            fields_flow_message (string): For more information please visit Example: 'content.cc_email,content.reply_to_email'.
            filter (string): For more information please visit field(s)/operator(s):<br>`id`: `any`<br>`name`: `contains`, `ends-with`, `equals`, `starts-with`<br>`created`: `equals`, `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`updated`: `equals`, `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.
            page_size (string): Default: 50. Min: 1. Max: 50. Example: '50'.
            sort (string): For more information please visit Example: '-updated'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Flows
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flow-actions/{id}/flow-messages"
        query_params = {
            k: v
            for k, v in [
                ("fields[flow-message]", fields_flow_message),
                ("filter", filter),
                ("page[cursor]", page_cursor),
                ("page[size]", page_size),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_message_ids_for_flow_action(
        self, id, filter=None, page_cursor=None, page_size=None, sort=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of flow messages associated with the specified flow action, supporting pagination, filtering, sorting, and optional revision header.

        Args:
            id (string): id
            filter (string): For more information please visit field(s)/operator(s):<br>`name`: `contains`, `ends-with`, `equals`, `starts-with`<br>`created`: `equals`, `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`updated`: `equals`, `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.
            page_size (string): Default: 50. Min: 1. Max: 50. Example: '50'.
            sort (string): For more information please visit Example: '-updated'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Flows
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flow-actions/{id}/relationships/flow-messages"
        query_params = {
            k: v
            for k, v in [
                ("filter", filter),
                ("page[cursor]", page_cursor),
                ("page[size]", page_size),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_action_for_flow_message(
        self, id, fields_flow_action=None
    ) -> dict[str, Any]:
        """
        Retrieves a flow action for a specific flow message by ID, allowing optional filtering by fields and revision, returning a successful response or error codes for bad requests or server errors.

        Args:
            id (string): id
            fields_flow_action (string): For more information please visit Example: 'render_options.add_org_prefix,send_options.is_transactional'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Flows
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flow-messages/{id}/flow-action"
        query_params = {
            k: v
            for k, v in [("fields[flow-action]", fields_flow_action)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_action_id_for_flow_message(self, id) -> dict[str, Any]:
        """
        Retrieves the relationships between a flow message, identified by `{id}`, and a flow action, allowing for the inspection of how flow messages are associated with actions, with optional revision filtering via the `revision` header.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Flows
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flow-messages/{id}/relationships/flow-action"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_template_for_flow_message(self, id, fields_template=None) -> dict[str, Any]:
        """
        The `/api/flow-messages/{id}/template` operation retrieves a template for a flow message by its ID using the GET method, allowing optional filtering of template fields via query parameters and specifying revisions through headers.

        Args:
            id (string): id
            fields_template (string): For more information please visit Example: 'name,text'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Flows
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flow-messages/{id}/template"
        query_params = {
            k: v for k, v in [("fields[template]", fields_template)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_template_id_for_flow_message(self, id) -> dict[str, Any]:
        """
        Retrieves the relationship details associated with a template for a specific flow message, identified by `{id}`, with optional filtering by revision specified in the header.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Flows
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flow-messages/{id}/relationships/template"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_forms(
        self, fields_form=None, filter=None, page_cursor=None, page_size=None, sort=None
    ) -> dict[str, Any]:
        """
        The "GET /api/forms" operation retrieves a list of forms based on provided query parameters such as fields, filters, pagination, and sorting, with an optional revision header, returning a successful response with a 200 status code.

        Args:
            fields_form (string): For more information please visit Example: 'name,ab_test'.
            filter (string): For more information please visit field(s)/operator(s):<br>`id`: `any`, `equals`<br>`name`: `any`, `contains`, `equals`<br>`ab_test`: `equals`<br>`updated_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`created_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`status`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.
            page_size (string): Default: 20. Min: 1. Max: 100. Example: '20'.
            sort (string): For more information please visit Example: '-created_at'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Forms
        """
        url = f"{self.base_url}/api/forms"
        query_params = {
            k: v
            for k, v in [
                ("fields[form]", fields_form),
                ("filter", filter),
                ("page[cursor]", page_cursor),
                ("page[size]", page_size),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_form(
        self, id, fields_form_version=None, fields_form=None, include=None
    ) -> dict[str, Any]:
        """
        Retrieves a specific form using its ID, supporting optional query parameters for field filtering, includes, and a revision header.

        Args:
            id (string): id
            fields_form_version (string): For more information please visit Example: 'updated_at,form_type'.
            fields_form (string): For more information please visit Example: 'name,ab_test'.
            include (string): For more information please visit Example: 'form-versions,form-versions'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Forms
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/forms/{id}"
        query_params = {
            k: v
            for k, v in [
                ("fields[form-version]", fields_form_version),
                ("fields[form]", fields_form),
                ("include", include),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_form_version(self, id, fields_form_version=None) -> dict[str, Any]:
        """
        Retrieves a specific form version by ID using the GET method, allowing optional filtering by form-version fields and revision headers.

        Args:
            id (string): id
            fields_form_version (string): For more information please visit Example: 'updated_at,form_type'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Forms
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/form-versions/{id}"
        query_params = {
            k: v
            for k, v in [("fields[form-version]", fields_form_version)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_versions_for_form(
        self,
        id,
        fields_form_version=None,
        filter=None,
        page_cursor=None,
        page_size=None,
        sort=None,
    ) -> dict[str, Any]:
        """
        Retrieves paginated form versions for a specific form with filtering, sorting, field selection, and pagination options.

        Args:
            id (string): id
            fields_form_version (string): For more information please visit Example: 'updated_at,form_type'.
            filter (string): For more information please visit field(s)/operator(s):<br>`form_type`: `any`, `equals`<br>`status`: `equals`<br>`updated_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`created_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.
            page_size (string): Default: 20. Min: 1. Max: 100. Example: '20'.
            sort (string): For more information please visit Example: '-created_at'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Forms
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/forms/{id}/form-versions"
        query_params = {
            k: v
            for k, v in [
                ("fields[form-version]", fields_form_version),
                ("filter", filter),
                ("page[cursor]", page_cursor),
                ("page[size]", page_size),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_version_ids_for_form(
        self, id, filter=None, page_cursor=None, page_size=None, sort=None
    ) -> dict[str, Any]:
        """
        This API operation retrieves the relationships between a form and its versions via a GET request to "/api/forms/{id}/relationships/form-versions," allowing filtering, pagination, and sorting of results.

        Args:
            id (string): id
            filter (string): For more information please visit field(s)/operator(s):<br>`form_type`: `any`, `equals`<br>`status`: `equals`<br>`updated_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`created_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.
            page_size (string): Default: 20. Min: 1. Max: 100. Example: '20'.
            sort (string): For more information please visit Example: '-created_at'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Forms
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/forms/{id}/relationships/form-versions"
        query_params = {
            k: v
            for k, v in [
                ("filter", filter),
                ("page[cursor]", page_cursor),
                ("page[size]", page_size),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_form_for_form_version(self, id, fields_form=None) -> dict[str, Any]:
        """
        Retrieves the specified form version's form details, with optional field filtering via `fields[form]` query parameter and revision tracking via `revision` header.

        Args:
            id (string): id
            fields_form (string): For more information please visit Example: 'name,ab_test'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Forms
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/form-versions/{id}/form"
        query_params = {
            k: v for k, v in [("fields[form]", fields_form)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_form_id_for_form_version(self, id) -> dict[str, Any]:
        """
        Retrieves the relationship details of a specified form version by its ID using the provided revision header.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Forms
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/form-versions/{id}/relationships/form"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_images(
        self,
        fields_image=None,
        filter=None,
        page_cursor=None,
        page_size=None,
        sort=None,
    ) -> dict[str, Any]:
        """
        The **GET /api/images** operation retrieves image resources based on optional query parameters for filtering, pagination, sorting, and specific fields, with the option to include a revision header.

        Args:
            fields_image (string): For more information please visit Example: 'image_url,name'.
            filter (string): For more information please visit field(s)/operator(s):<br>`id`: `any`, `equals`<br>`updated_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`format`: `any`, `equals`<br>`name`: `any`, `contains`, `ends-with`, `equals`, `starts-with`<br>`size`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`hidden`: `any`, `equals` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.
            page_size (string): Default: 20. Min: 1. Max: 100. Example: '20'.
            sort (string): For more information please visit Example: '-format'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Images
        """
        url = f"{self.base_url}/api/images"
        query_params = {
            k: v
            for k, v in [
                ("fields[image]", fields_image),
                ("filter", filter),
                ("page[cursor]", page_cursor),
                ("page[size]", page_size),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def upload_image_from_url(self, data=None) -> dict[str, Any]:
        """
        Creates a new image resource with the specified revision, returning a successful creation response if valid, or error responses for invalid requests or server issues.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "hidden": false,
                      "import_from_url": "<string>",
                      "name": "<string>"
                    },
                    "type": "image"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Images
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/images"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_image(self, id, fields_image=None) -> dict[str, Any]:
        """
        Retrieves a specific image by ID, allowing optional query parameter "fields[image]" and a required revision header, returning data if successful or error responses for bad requests or internal server errors.

        Args:
            id (string): id
            fields_image (string): For more information please visit Example: 'image_url,name'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Images
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/images/{id}"
        query_params = {
            k: v for k, v in [("fields[image]", fields_image)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_image(self, id, data=None) -> dict[str, Any]:
        """
        The PATCH method at "/api/images/{id}" allows for partial updates of an image resource by specifying changes in the request body, with the revision tracked via a header parameter.

        Args:
            id (string): id
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "hidden": "<boolean>",
                      "name": "<string>"
                    },
                    "id": "<string>",
                    "type": "image"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Images
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/images/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_lists(
        self,
        fields_flow=None,
        fields_list=None,
        fields_tag=None,
        filter=None,
        include=None,
        page_cursor=None,
        sort=None,
    ) -> dict[str, Any]:
        """
        The API operation at "/api/lists" using the "GET" method retrieves a list of items based on specified query parameters for fields, filters, sorting, and pagination, with optional headers for revision control.

        Args:
            fields_flow (string): For more information please visit Example: 'created,status'.
            fields_list (string): For more information please visit Example: 'updated,opt_in_process'.
            fields_tag (string): For more information please visit Example: 'name,name'.
            filter (string): For more information please visit field(s)/operator(s):<br>`name`: `any`, `equals`<br>`id`: `any`, `equals`<br>`created`: `greater-than`<br>`updated`: `greater-than` Example: '<string>'.
            include (string): For more information please visit Example: 'flow-triggers,tags'.
            page_cursor (string): For more information please visit Example: '<string>'.
            sort (string): For more information please visit Example: '-updated'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Lists
        """
        url = f"{self.base_url}/api/lists"
        query_params = {
            k: v
            for k, v in [
                ("fields[flow]", fields_flow),
                ("fields[list]", fields_list),
                ("fields[tag]", fields_tag),
                ("filter", filter),
                ("include", include),
                ("page[cursor]", page_cursor),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_list(self, data=None) -> dict[str, Any]:
        """
        The POST operation at "/api/lists" creates a new list resource, returning a 201 status upon success, and accepts a `revision` parameter in the request header.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "name": "<string>"
                    },
                    "type": "list"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Lists
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/lists"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_list(
        self,
        id,
        additional_fields_list=None,
        fields_flow=None,
        fields_list=None,
        fields_tag=None,
        include=None,
    ) -> dict[str, Any]:
        """
        Retrieves a specific list by ID with customizable response fields, optional related resources to include, and support for specifying data revisions via headers.

        Args:
            id (string): id
            additional_fields_list (string): Request additional fields not included by default in the response. Supported values: 'profile_count' Example: 'profile_count,profile_count'.
            fields_flow (string): For more information please visit Example: 'created,status'.
            fields_list (string): For more information please visit Example: 'updated,opt_in_process'.
            fields_tag (string): For more information please visit Example: 'name,name'.
            include (string): For more information please visit Example: 'flow-triggers,tags'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Lists
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/lists/{id}"
        query_params = {
            k: v
            for k, v in [
                ("additional-fields[list]", additional_fields_list),
                ("fields[flow]", fields_flow),
                ("fields[list]", fields_list),
                ("fields[tag]", fields_tag),
                ("include", include),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_list(self, id) -> Any:
        """
        Deletes the specified list by ID when the correct revision header is provided, returning HTTP 204 for successful deletion, or 400/500 for invalid requests or server errors.

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            Lists
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/lists/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_list(self, id, data=None) -> dict[str, Any]:
        """
        Updates a list resource partially by applying modifications to the specified fields at the path "/api/lists/{id}", requiring a revision header for concurrent version control.

        Args:
            id (string): id
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "name": "<string>"
                    },
                    "id": "<string>",
                    "type": "list"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Lists
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/lists/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tags_for_list(self, id, fields_tag=None) -> dict[str, Any]:
        """
        This API operation retrieves the tags associated with a list specified by its ID, allowing optional filtering of specific fields and revision information via query and header parameters, respectively.

        Args:
            id (string): id
            fields_tag (string): For more information please visit Example: 'name,name'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Lists
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/lists/{id}/tags"
        query_params = {k: v for k, v in [("fields[tag]", fields_tag)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag_ids_for_list(self, id) -> dict[str, Any]:
        """
        Retrieves the relationships between a specified list and its associated tags.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Lists
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/lists/{id}/relationships/tags"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_profiles_for_list(
        self,
        id,
        additional_fields_profile=None,
        fields_profile=None,
        filter=None,
        page_cursor=None,
        page_size=None,
        sort=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of profiles associated with the specified list ID, allowing optional filtering, sorting, and pagination, with customizable fields and revision tracking.

        Args:
            id (string): id
            additional_fields_profile (string): Request additional fields not included by default in the response. Supported values: 'subscriptions', 'predictive_analytics' Example: 'subscriptions,subscriptions'.
            fields_profile (string): For more information please visit Example: 'location.address1,first_name'.
            filter (string): For more information please visit field(s)/operator(s):<br>`email`: `any`, `equals`<br>`phone_number`: `any`, `equals`<br>`push_token`: `any`, `equals`<br>`_kx`: `equals`<br>`joined_group_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.
            page_size (string): Default: 20. Min: 1. Max: 100. Example: '20'.
            sort (string): For more information please visit Example: '-joined_group_at'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Lists
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/lists/{id}/profiles"
        query_params = {
            k: v
            for k, v in [
                ("additional-fields[profile]", additional_fields_profile),
                ("fields[profile]", fields_profile),
                ("filter", filter),
                ("page[cursor]", page_cursor),
                ("page[size]", page_size),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_profile_ids_for_list(
        self, id, filter=None, page_cursor=None, page_size=None, sort=None
    ) -> dict[str, Any]:
        """
        This API operation retrieves the profiles related to a list identified by `{id}`, allowing for filtering, pagination, sorting, and revision specification via query parameters and headers.

        Args:
            id (string): id
            filter (string): For more information please visit field(s)/operator(s):<br>`email`: `any`, `equals`<br>`phone_number`: `any`, `equals`<br>`push_token`: `any`, `equals`<br>`_kx`: `equals`<br>`joined_group_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.
            page_size (string): Default: 20. Min: 1. Max: 100. Example: '20'.
            sort (string): For more information please visit Example: '-joined_group_at'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Lists
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/lists/{id}/relationships/profiles"
        query_params = {
            k: v
            for k, v in [
                ("filter", filter),
                ("page[cursor]", page_cursor),
                ("page[size]", page_size),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_profiles_to_list(self, id, data=None) -> Any:
        """
        Creates a relationship between a specified list and one or more profiles using a POST request with an optional revision header, returning a 204 on success, 400 for client errors, and 500 for server errors.

        Args:
            id (string): id
            data (array): data
                Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "profile"
                    },
                    {
                      "id": "<string>",
                      "type": "profile"
                    }
                  ]
                }
                ```

        Returns:
            Any: Success

        Tags:
            Lists
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/lists/{id}/relationships/profiles"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_profiles_from_list(self, id, data=None) -> Any:
        """
        Deletes the relationship between the specified list and associated profiles using a revision header, returning status codes for success, bad request, and server errors.

        Args:
            id (string): id
            data (array): data
                Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "profile"
                    },
                    {
                      "id": "<string>",
                      "type": "profile"
                    }
                  ]
                }
                ```

        Returns:
            Any: Success

        Tags:
            Lists
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/lists/{id}/relationships/profiles"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flows_triggered_by_list(self, id, fields_flow=None) -> dict[str, Any]:
        """
        Retrieves flow triggers for a specific list by ID, supporting optional filtering by flow fields and specifying a revision in the request header.

        Args:
            id (string): id
            fields_flow (string): For more information please visit Example: 'created,status'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Lists
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/lists/{id}/flow-triggers"
        query_params = {
            k: v for k, v in [("fields[flow]", fields_flow)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_ids_for_flows_triggered_by_list(self, id) -> dict[str, Any]:
        """
        Retrieves the flow triggers associated with a specific list using the provided ID, including revision header parameter, and returns status codes for success (200), client errors (400), or server issues (500).

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Lists
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/lists/{id}/relationships/flow-triggers"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_metrics(
        self,
        fields_flow=None,
        fields_metric=None,
        filter=None,
        include=None,
        page_cursor=None,
    ) -> dict[str, Any]:
        """
        Retrieves paginated metrics data with optional field filtering, resource inclusion, and cursor-based pagination, requiring a revision header.

        Args:
            fields_flow (string): For more information please visit Example: 'created,status'.
            fields_metric (string): For more information please visit Example: 'integration,created'.
            filter (string): For more information please visit field(s)/operator(s):<br>`integration.name`: `equals`<br>`integration.category`: `equals` Example: '<string>'.
            include (string): For more information please visit Example: 'flow-triggers,flow-triggers'.
            page_cursor (string): For more information please visit Example: '<string>'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Metrics
        """
        url = f"{self.base_url}/api/metrics"
        query_params = {
            k: v
            for k, v in [
                ("fields[flow]", fields_flow),
                ("fields[metric]", fields_metric),
                ("filter", filter),
                ("include", include),
                ("page[cursor]", page_cursor),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_metric(
        self, id, fields_flow=None, fields_metric=None, include=None
    ) -> dict[str, Any]:
        """
        Retrieves specific metric data by ID, allowing optional filtering by flow and metric fields, inclusion of additional data, and specification of a revision via a header.

        Args:
            id (string): id
            fields_flow (string): For more information please visit Example: 'created,status'.
            fields_metric (string): For more information please visit Example: 'integration,created'.
            include (string): For more information please visit Example: 'flow-triggers,flow-triggers'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Metrics
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/metrics/{id}"
        query_params = {
            k: v
            for k, v in [
                ("fields[flow]", fields_flow),
                ("fields[metric]", fields_metric),
                ("include", include),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_metric_property(
        self,
        id,
        additional_fields_metric_property=None,
        fields_metric_property=None,
        fields_metric=None,
        include=None,
    ) -> dict[str, Any]:
        """
        Retrieves a metric property by ID, allowing optional filtering of fields and inclusion of additional data through query parameters, with support for revision specification via a header.

        Args:
            id (string): id
            additional_fields_metric_property (string): Request additional fields not included by default in the response. Supported values: 'sample_values' Example: 'sample_values,sample_values'.
            fields_metric_property (string): For more information please visit Example: 'sample_values,property'.
            fields_metric (string): For more information please visit Example: 'integration,created'.
            include (string): For more information please visit Example: 'metric,metric'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Metrics
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/metric-properties/{id}"
        query_params = {
            k: v
            for k, v in [
                (
                    "additional-fields[metric-property]",
                    additional_fields_metric_property,
                ),
                ("fields[metric-property]", fields_metric_property),
                ("fields[metric]", fields_metric),
                ("include", include),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def query_metric_aggregates(self, data=None) -> dict[str, Any]:
        """
        Posts a request to the "/api/metric-aggregates" endpoint, requiring a "revision" header, to aggregate metrics, returning a successful response if valid or error responses for bad requests or server errors.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "by": [
                        "$attributed_channel",
                        "Client Type"
                      ],
                      "filter": [
                        "<string>",
                        "<string>"
                      ],
                      "interval": "day",
                      "measurements": [
                        "unique",
                        "unique"
                      ],
                      "metric_id": "<string>",
                      "page_cursor": "<string>",
                      "page_size": 500,
                      "return_fields": [
                        "<string>",
                        "<string>"
                      ],
                      "sort": "-URL",
                      "timezone": "UTC"
                    },
                    "type": "metric-aggregate"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Metrics
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/metric-aggregates"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flows_triggered_by_metric(self, id, fields_flow=None) -> dict[str, Any]:
        """
        Retrieves flow trigger details for a specified metric ID, supporting filtering via query parameters and optional header-based versioning.

        Args:
            id (string): id
            fields_flow (string): For more information please visit Example: 'created,status'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Metrics
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/metrics/{id}/flow-triggers"
        query_params = {
            k: v for k, v in [("fields[flow]", fields_flow)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_ids_for_flows_triggered_by_metric(self, id) -> dict[str, Any]:
        """
        This API operation retrieves the flow triggers associated with a specific metric identified by `{id}`, allowing for the inspection of triggers configured for that metric.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Metrics
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/metrics/{id}/relationships/flow-triggers"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_properties_for_metric(
        self, id, additional_fields_metric_property=None, fields_metric_property=None
    ) -> dict[str, Any]:
        """
        Retrieves properties of a specific metric by ID, supporting query-based field filtering and custom headers for revision management.

        Args:
            id (string): id
            additional_fields_metric_property (string): Request additional fields not included by default in the response. Supported values: 'sample_values' Example: 'sample_values,sample_values'.
            fields_metric_property (string): For more information please visit Example: 'sample_values,property'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Metrics
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/metrics/{id}/metric-properties"
        query_params = {
            k: v
            for k, v in [
                (
                    "additional-fields[metric-property]",
                    additional_fields_metric_property,
                ),
                ("fields[metric-property]", fields_metric_property),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_property_ids_for_metric(self, id) -> dict[str, Any]:
        """
        Retrieves the relationships of metric properties associated with a specific metric by ID, with the option to specify a revision via the request header.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Metrics
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/metrics/{id}/relationships/metric-properties"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_metric_for_metric_property(self, id, fields_metric=None) -> dict[str, Any]:
        """
        Retrieves a specific metric property by ID, allowing filtering via query parameters and supporting revision headers for conditional requests.

        Args:
            id (string): id
            fields_metric (string): For more information please visit Example: 'integration,created'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Metrics
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/metric-properties/{id}/metric"
        query_params = {
            k: v for k, v in [("fields[metric]", fields_metric)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_metric_id_for_metric_property(self, id) -> dict[str, Any]:
        """
        Retrieves the relationships of a metric property identified by {id} through the "GET" method, supporting a "revision" header parameter with response codes indicating success (200), client errors (400), and server errors (500).

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Metrics
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/metric-properties/{id}/relationships/metric"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_profiles(
        self,
        additional_fields_profile=None,
        fields_profile=None,
        filter=None,
        page_cursor=None,
        page_size=None,
        sort=None,
    ) -> dict[str, Any]:
        """
        Retrieves profiles with support for field filtering, pagination, sorting, and custom filtering via query parameters.

        Args:
            additional_fields_profile (string): Request additional fields not included by default in the response. Supported values: 'subscriptions', 'predictive_analytics' Example: 'subscriptions,subscriptions'.
            fields_profile (string): For more information please visit Example: 'location.address2,subscriptions.sms.marketing.last_updated'.
            filter (string): For more information please visit field(s)/operator(s):<br>`id`: `any`, `equals`<br>`email`: `any`, `equals`<br>`phone_number`: `any`, `equals`<br>`external_id`: `any`, `equals`<br>`_kx`: `equals`<br>`created`: `greater-than`, `less-than`<br>`updated`: `greater-than`, `less-than`<br>`subscriptions.email.marketing.list_suppressions.reason`: `equals`<br>`subscriptions.email.marketing.list_suppressions.timestamp`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`subscriptions.email.marketing.list_suppressions.list_id`: `equals`<br>`subscriptions.email.marketing.suppression.reason`: `equals`<br>`subscriptions.email.marketing.suppression.timestamp`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.
            page_size (string): Default: 20. Min: 1. Max: 100. Example: '20'.
            sort (string): For more information please visit Example: '-subscriptions.email.marketing.suppression.timestamp'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Profiles, Profiles1
        """
        url = f"{self.base_url}/api/profiles"
        query_params = {
            k: v
            for k, v in [
                ("additional-fields[profile]", additional_fields_profile),
                ("fields[profile]", fields_profile),
                ("filter", filter),
                ("page[cursor]", page_cursor),
                ("page[size]", page_size),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_profile(
        self, additional_fields_profile=None, data=None
    ) -> dict[str, Any]:
        """
        Creates a new profile with additional fields passed via query parameters and custom header for revision control, returning success (201), client error (400), or server error (500) status codes.

        Args:
            additional_fields_profile (string): Request additional fields not included by default in the response. Supported values: 'subscriptions', 'predictive_analytics' Example: 'subscriptions,subscriptions'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "email": "<string>",
                      "external_id": "<string>",
                      "first_name": "<string>",
                      "image": "<string>",
                      "last_name": "<string>",
                      "locale": "<string>",
                      "location": {
                        "address1": "<string>",
                        "address2": "<string>",
                        "city": "<string>",
                        "country": "<string>",
                        "ip": "<string>",
                        "latitude": "<string>",
                        "longitude": "<string>",
                        "region": "<string>",
                        "timezone": "<string>",
                        "zip": "<string>"
                      },
                      "organization": "<string>",
                      "phone_number": "<string>",
                      "properties": {},
                      "title": "<string>"
                    },
                    "type": "profile"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Profiles, Profiles1
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/profiles"
        query_params = {
            k: v
            for k, v in [("additional-fields[profile]", additional_fields_profile)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_profile(
        self,
        id,
        additional_fields_profile=None,
        fields_list=None,
        fields_profile=None,
        fields_segment=None,
        include=None,
    ) -> dict[str, Any]:
        """
        Retrieves a specific profile by ID with customizable field selection through query parameters for enhanced data filtering.

        Args:
            id (string): id
            additional_fields_profile (string): Request additional fields not included by default in the response. Supported values: 'subscriptions', 'predictive_analytics' Example: 'subscriptions,subscriptions'.
            fields_list (string): For more information please visit Example: 'updated,opt_in_process'.
            fields_profile (string): For more information please visit Example: 'location.address2,subscriptions.sms.marketing.last_updated'.
            fields_segment (string): For more information please visit Example: 'is_processing,is_processing'.
            include (string): For more information please visit Example: 'lists,segments'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Profiles, Profiles1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/profiles/{id}"
        query_params = {
            k: v
            for k, v in [
                ("additional-fields[profile]", additional_fields_profile),
                ("fields[list]", fields_list),
                ("fields[profile]", fields_profile),
                ("fields[segment]", fields_segment),
                ("include", include),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_profile(
        self, id, additional_fields_profile=None, data=None
    ) -> dict[str, Any]:
        """
        Updates specific fields of a profile identified by {id} using a partial payload, with optional query parameters for additional fields and a revision header for concurrency control.

        Args:
            id (string): id
            additional_fields_profile (string): Request additional fields not included by default in the response. Supported values: 'subscriptions', 'predictive_analytics' Example: 'subscriptions,subscriptions'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "anonymous_id": "<string>",
                      "email": "<string>",
                      "external_id": "<string>",
                      "first_name": "<string>",
                      "image": "<string>",
                      "last_name": "<string>",
                      "locale": "<string>",
                      "location": {
                        "address1": "<string>",
                        "address2": "<string>",
                        "city": "<string>",
                        "country": "<string>",
                        "ip": "<string>",
                        "latitude": "<string>",
                        "longitude": "<string>",
                        "region": "<string>",
                        "timezone": "<string>",
                        "zip": "<string>"
                      },
                      "organization": "<string>",
                      "phone_number": "<string>",
                      "properties": {},
                      "title": "<string>"
                    },
                    "id": "<string>",
                    "meta": {
                      "patch_properties": {
                        "append": {},
                        "unappend": {},
                        "unset": "<string>"
                      }
                    },
                    "type": "profile"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Profiles, Profiles1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/profiles/{id}"
        query_params = {
            k: v
            for k, v in [("additional-fields[profile]", additional_fields_profile)]
            if v is not None
        }
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_suppress_profiles_jobs(
        self,
        fields_profile_suppression_bulk_create_job=None,
        filter=None,
        page_cursor=None,
        sort=None,
    ) -> dict[str, Any]:
        """
        The GET operation at the "/api/profile-suppression-bulk-create-jobs" path retrieves a list of bulk profile suppression jobs, allowing for filtering, sorting, and pagination of the results through query parameters.

        Args:
            fields_profile_suppression_bulk_create_job (string): For more information please visit Example: 'completed_at,completed_count'.
            filter (string): For more information please visit field(s)/operator(s):<br>`status`: `equals`<br>`list_id`: `equals`<br>`segment_id`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.
            sort (string): For more information please visit Example: 'created'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Profiles, Profiles1
        """
        url = f"{self.base_url}/api/profile-suppression-bulk-create-jobs"
        query_params = {
            k: v
            for k, v in [
                (
                    "fields[profile-suppression-bulk-create-job]",
                    fields_profile_suppression_bulk_create_job,
                ),
                ("filter", filter),
                ("page[cursor]", page_cursor),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_suppress_profiles(self, data=None) -> dict[str, Any]:
        """
        Creates a bulk suppression job for profiles to prevent email communication via the Klaviyo API.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "profiles": {
                        "data": [
                          {
                            "attributes": {
                              "email": "<string>"
                            },
                            "type": "profile"
                          },
                          {
                            "attributes": {
                              "email": "<string>"
                            },
                            "type": "profile"
                          }
                        ]
                      }
                    },
                    "relationships": {
                      "list": {
                        "data": {
                          "id": "<string>",
                          "type": "list"
                        }
                      },
                      "segment": {
                        "data": {
                          "id": "<string>",
                          "type": "segment"
                        }
                      }
                    },
                    "type": "profile-suppression-bulk-create-job"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Profiles, Consent
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/profile-suppression-bulk-create-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_suppress_profiles_job(
        self, job_id, fields_profile_suppression_bulk_create_job=None
    ) -> dict[str, Any]:
        """
        Retrieve the status and details of a bulk profile suppression job by its ID, including optional field filtering and revision header support.

        Args:
            job_id (string): job_id
            fields_profile_suppression_bulk_create_job (string): For more information please visit Example: 'completed_at,completed_count'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Profiles, Profiles1
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/profile-suppression-bulk-create-jobs/{job_id}"
        query_params = {
            k: v
            for k, v in [
                (
                    "fields[profile-suppression-bulk-create-job]",
                    fields_profile_suppression_bulk_create_job,
                )
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_unsuppress_profiles_jobs(
        self,
        fields_profile_suppression_bulk_delete_job=None,
        filter=None,
        page_cursor=None,
        sort=None,
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of bulk profile suppression deletion jobs with optional filtering, sorting, and field selection.

        Args:
            fields_profile_suppression_bulk_delete_job (string): For more information please visit Example: 'completed_at,completed_count'.
            filter (string): For more information please visit field(s)/operator(s):<br>`status`: `equals`<br>`list_id`: `equals`<br>`segment_id`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.
            sort (string): For more information please visit Example: 'created'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Profiles, Profiles1
        """
        url = f"{self.base_url}/api/profile-suppression-bulk-delete-jobs"
        query_params = {
            k: v
            for k, v in [
                (
                    "fields[profile-suppression-bulk-delete-job]",
                    fields_profile_suppression_bulk_delete_job,
                ),
                ("filter", filter),
                ("page[cursor]", page_cursor),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_unsuppress_profiles(self, data=None) -> dict[str, Any]:
        """
        Creates a bulk job to suppress and/or delete profiles asynchronously, returning a 202 Accepted status upon successful initiation.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "profiles": {
                        "data": [
                          {
                            "attributes": {
                              "email": "<string>"
                            },
                            "type": "profile"
                          },
                          {
                            "attributes": {
                              "email": "<string>"
                            },
                            "type": "profile"
                          }
                        ]
                      }
                    },
                    "relationships": {
                      "list": {
                        "data": {
                          "id": "<string>",
                          "type": "list"
                        }
                      },
                      "segment": {
                        "data": {
                          "id": "<string>",
                          "type": "segment"
                        }
                      }
                    },
                    "type": "profile-suppression-bulk-delete-job"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Profiles, Consent
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/profile-suppression-bulk-delete-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_unsuppress_profiles_job(
        self, job_id, fields_profile_suppression_bulk_delete_job=None
    ) -> dict[str, Any]:
        """
        Retrieves the status and details of a bulk profile suppression deletion job using specified query fields and header revision.

        Args:
            job_id (string): job_id
            fields_profile_suppression_bulk_delete_job (string): For more information please visit Example: 'completed_at,completed_count'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Profiles, Profiles1
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/profile-suppression-bulk-delete-jobs/{job_id}"
        query_params = {
            k: v
            for k, v in [
                (
                    "fields[profile-suppression-bulk-delete-job]",
                    fields_profile_suppression_bulk_delete_job,
                )
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_or_update_profile(
        self, additional_fields_profile=None, data=None
    ) -> dict[str, Any]:
        """
        The "POST /api/profile-import" operation imports profiles, accepting optional query parameters like "additional-fields[profile]" and requiring a "revision" header, with responses indicating success (200 or 201), bad requests (400), or internal server errors (500).

        Args:
            additional_fields_profile (string): Request additional fields not included by default in the response. Supported values: 'subscriptions', 'predictive_analytics' Example: 'subscriptions,subscriptions'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "_kx": "<string>",
                      "anonymous_id": "<string>",
                      "email": "<string>",
                      "external_id": "<string>",
                      "first_name": "<string>",
                      "image": "<string>",
                      "last_name": "<string>",
                      "locale": "<string>",
                      "location": {
                        "address1": "<string>",
                        "address2": "<string>",
                        "city": "<string>",
                        "country": "<string>",
                        "ip": "<string>",
                        "latitude": "<string>",
                        "longitude": "<string>",
                        "region": "<string>",
                        "timezone": "<string>",
                        "zip": "<string>"
                      },
                      "organization": "<string>",
                      "phone_number": "<string>",
                      "properties": {},
                      "title": "<string>"
                    },
                    "id": "<string>",
                    "meta": {
                      "patch_properties": {
                        "append": {},
                        "unappend": {},
                        "unset": "<string>"
                      }
                    },
                    "type": "profile"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Profile Updated Successfully

        Tags:
            Profiles, Profiles1
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/profile-import"
        query_params = {
            k: v
            for k, v in [("additional-fields[profile]", additional_fields_profile)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def merge_profiles(self, data=None) -> dict[str, Any]:
        """
        The API operation at "/api/profile-merge" using the "POST" method merges user profiles, integrating data from a source profile into a destination profile, with the source profile being deleted upon successful completion, and requires a revision header for version control.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "id": "<string>",
                    "relationships": {
                      "profiles": {
                        "data": [
                          {
                            "id": "<string>",
                            "type": "profile"
                          },
                          {
                            "id": "<string>",
                            "type": "profile"
                          }
                        ]
                      }
                    },
                    "type": "profile-merge"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Profiles, Profiles1
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/profile-merge"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_or_update_push_token(self, data=None) -> Any:
        """
        This API operation creates a new resource by posting to the "/api/push-tokens" endpoint, accepting a revision parameter in the request header, and returns a 202 response upon successful creation, with error responses for invalid requests or server errors.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "background": "AVAILABLE",
                      "device_metadata": {
                        "app_build": "<string>",
                        "app_id": "<string>",
                        "app_name": "<string>",
                        "app_version": "<string>",
                        "device_id": "<string>",
                        "device_model": "<string>",
                        "environment": "debug",
                        "klaviyo_sdk": "android",
                        "manufacturer": "<string>",
                        "os_name": "ipados",
                        "os_version": "<string>",
                        "sdk_version": "<string>"
                      },
                      "enablement_status": "AUTHORIZED",
                      "platform": "android",
                      "profile": {
                        "data": {
                          "attributes": {
                            "_kx": "<string>",
                            "anonymous_id": "<string>",
                            "email": "<string>",
                            "external_id": "<string>",
                            "first_name": "<string>",
                            "image": "<string>",
                            "last_name": "<string>",
                            "locale": "<string>",
                            "location": {
                              "address1": "<string>",
                              "address2": "<string>",
                              "city": "<string>",
                              "country": "<string>",
                              "ip": "<string>",
                              "latitude": "<string>",
                              "longitude": "<string>",
                              "region": "<string>",
                              "timezone": "<string>",
                              "zip": "<string>"
                            },
                            "meta": {
                              "patch_properties": {
                                "append": {},
                                "unappend": {},
                                "unset": "<string>"
                              }
                            },
                            "organization": "<string>",
                            "phone_number": "<string>",
                            "properties": {},
                            "title": "<string>"
                          },
                          "id": "<string>",
                          "type": "profile"
                        }
                      },
                      "token": "<string>",
                      "vendor": "apns"
                    },
                    "type": "push-token"
                  }
                }
                ```

        Returns:
            Any: Success

        Tags:
            Profiles, Profiles1
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/push-tokens"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_lists_for_profile(self, id, fields_list=None) -> dict[str, Any]:
        """
        This API operation retrieves a list associated with a specific profile identified by `{id}`, allowing optional filtering of fields via the `fields[list]` query parameter and specifying a revision via the `revision` header.

        Args:
            id (string): id
            fields_list (string): For more information please visit Example: 'updated,opt_in_process'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Profiles, Profiles1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/profiles/{id}/lists"
        query_params = {
            k: v for k, v in [("fields[list]", fields_list)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_list_ids_for_profile(self, id) -> dict[str, Any]:
        """
        Retrieves the lists associated with a specified profile ID via header-based version control.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Profiles, Profiles1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/profiles/{id}/relationships/lists"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_segments_for_profile(self, id, fields_segment=None) -> dict[str, Any]:
        """
        This API operation retrieves profile segment information for a specified profile ID, allowing for the selection of specific segment fields via query parameters and the specification of a revision in the request header.

        Args:
            id (string): id
            fields_segment (string): For more information please visit Example: 'is_processing,is_processing'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Profiles, Profiles1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/profiles/{id}/segments"
        query_params = {
            k: v for k, v in [("fields[segment]", fields_segment)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_segment_ids_for_profile(self, id) -> dict[str, Any]:
        """
        Retrieves the associated segments of a specific profile, requiring a revision header, and returns a 200 status on success with potential 400 or 500 error responses.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Profiles, Profiles1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/profiles/{id}/relationships/segments"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_import_profiles_jobs(
        self,
        fields_profile_bulk_import_job=None,
        filter=None,
        page_cursor=None,
        page_size=None,
        sort=None,
    ) -> dict[str, Any]:
        """
        The GET operation on `/api/profile-bulk-import-jobs` retrieves and filters paginated bulk profile import job records with customizable sorting, field selection, and cursor-based pagination.

        Args:
            fields_profile_bulk_import_job (string): For more information please visit Example: 'started_at,completed_at'.
            filter (string): For more information please visit field(s)/operator(s):<br>`status`: `any`, `equals` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.
            page_size (string): Default: 20. Min: 1. Max: 100. Example: '20'.
            sort (string): For more information please visit Example: 'created_at'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Profiles, Bulk Import Profiles
        """
        url = f"{self.base_url}/api/profile-bulk-import-jobs"
        query_params = {
            k: v
            for k, v in [
                ("fields[profile-bulk-import-job]", fields_profile_bulk_import_job),
                ("filter", filter),
                ("page[cursor]", page_cursor),
                ("page[size]", page_size),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_import_profiles(self, data=None) -> dict[str, Any]:
        """
        The POST operation at "/api/profile-bulk-import-jobs" creates a new bulk profile import job, allowing for the creation or update of multiple profiles, with a revision specified in the header.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "profiles": {
                        "data": [
                          {
                            "attributes": {
                              "_kx": "<string>",
                              "anonymous_id": "<string>",
                              "email": "<string>",
                              "external_id": "<string>",
                              "first_name": "<string>",
                              "image": "<string>",
                              "last_name": "<string>",
                              "locale": "<string>",
                              "location": {
                                "address1": "<string>",
                                "address2": "<string>",
                                "city": "<string>",
                                "country": "<string>",
                                "ip": "<string>",
                                "latitude": "<string>",
                                "longitude": "<string>",
                                "region": "<string>",
                                "timezone": "<string>",
                                "zip": "<string>"
                              },
                              "organization": "<string>",
                              "phone_number": "<string>",
                              "properties": {},
                              "title": "<string>"
                            },
                            "id": "<string>",
                            "meta": {
                              "patch_properties": {
                                "append": {},
                                "unappend": {},
                                "unset": "<string>"
                              }
                            },
                            "type": "profile"
                          },
                          {
                            "attributes": {
                              "_kx": "<string>",
                              "anonymous_id": "<string>",
                              "email": "<string>",
                              "external_id": "<string>",
                              "first_name": "<string>",
                              "image": "<string>",
                              "last_name": "<string>",
                              "locale": "<string>",
                              "location": {
                                "address1": "<string>",
                                "address2": "<string>",
                                "city": "<string>",
                                "country": "<string>",
                                "ip": "<string>",
                                "latitude": "<string>",
                                "longitude": "<string>",
                                "region": "<string>",
                                "timezone": "<string>",
                                "zip": "<string>"
                              },
                              "organization": "<string>",
                              "phone_number": "<string>",
                              "properties": {},
                              "title": "<string>"
                            },
                            "id": "<string>",
                            "meta": {
                              "patch_properties": {
                                "append": {},
                                "unappend": {},
                                "unset": "<string>"
                              }
                            },
                            "type": "profile"
                          }
                        ]
                      }
                    },
                    "relationships": {
                      "lists": {
                        "data": [
                          {
                            "id": "<string>",
                            "type": "list"
                          },
                          {
                            "id": "<string>",
                            "type": "list"
                          }
                        ]
                      }
                    },
                    "type": "profile-bulk-import-job"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Profiles, Bulk Import Profiles
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/profile-bulk-import-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_import_profiles_job(
        self,
        job_id,
        fields_list=None,
        fields_profile_bulk_import_job=None,
        include=None,
    ) -> dict[str, Any]:
        """
        Retrieves the status and details of a specific bulk profile import job, including optional field selection and resource inclusion via query parameters.

        Args:
            job_id (string): job_id
            fields_list (string): For more information please visit Example: 'updated,opt_in_process'.
            fields_profile_bulk_import_job (string): For more information please visit Example: 'started_at,completed_at'.
            include (string): For more information please visit Example: 'lists,lists'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Profiles, Bulk Import Profiles
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/profile-bulk-import-jobs/{job_id}"
        query_params = {
            k: v
            for k, v in [
                ("fields[list]", fields_list),
                ("fields[profile-bulk-import-job]", fields_profile_bulk_import_job),
                ("include", include),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_list_for_bulk_import_profiles_job(
        self, id, fields_list=None
    ) -> dict[str, Any]:
        """
        Retrieves profile lists associated with a specific bulk import job ID, allowing field filtering via query parameters and including a revision header.

        Args:
            id (string): id
            fields_list (string): For more information please visit Example: 'updated,opt_in_process'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Profiles, Bulk Import Profiles
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/profile-bulk-import-jobs/{id}/lists"
        query_params = {
            k: v for k, v in [("fields[list]", fields_list)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_list_ids_for_bulk_import_profiles_job(self, id) -> dict[str, Any]:
        """
        This API operation retrieves the relationships between a specific bulk profile import job and its associated lists, allowing the caller to fetch related list data using a GET request on the "/api/profile-bulk-import-jobs/{id}/relationships/lists" endpoint.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Profiles, Bulk Import Profiles
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/profile-bulk-import-jobs/{id}/relationships/lists"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_profiles_for_bulk_import_profiles_job(
        self,
        id,
        additional_fields_profile=None,
        fields_profile=None,
        page_cursor=None,
        page_size=None,
    ) -> dict[str, Any]:
        """
        The API operation defined at path "/api/profile-bulk-import-jobs/{id}/profiles" using the "GET" method retrieves a list of profiles associated with a specific bulk import job, allowing for pagination and customization of returned fields.

        Args:
            id (string): id
            additional_fields_profile (string): Request additional fields not included by default in the response. Supported values: 'subscriptions', 'predictive_analytics' Example: 'subscriptions,subscriptions'.
            fields_profile (string): For more information please visit Example: 'location.address2,subscriptions.sms.marketing.last_updated'.
            page_cursor (string): For more information please visit Example: '<string>'.
            page_size (string): Default: 20. Min: 1. Max: 100. Example: '20'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Profiles, Bulk Import Profiles
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/profile-bulk-import-jobs/{id}/profiles"
        query_params = {
            k: v
            for k, v in [
                ("additional-fields[profile]", additional_fields_profile),
                ("fields[profile]", fields_profile),
                ("page[cursor]", page_cursor),
                ("page[size]", page_size),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_profile_ids_for_bulk_import_profiles_job(
        self, id, page_cursor=None, page_size=None
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of profile relationships associated with a specific bulk import job using cursor-based pagination query parameters.

        Args:
            id (string): id
            page_cursor (string): For more information please visit Example: '<string>'.
            page_size (string): Default: 20. Min: 1. Max: 100. Example: '20'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Profiles, Bulk Import Profiles
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = (
            f"{self.base_url}/api/profile-bulk-import-jobs/{id}/relationships/profiles"
        )
        query_params = {
            k: v
            for k, v in [("page[cursor]", page_cursor), ("page[size]", page_size)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_errors_for_bulk_import_profiles_job(
        self, id, fields_import_error=None, page_cursor=None, page_size=None
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of import errors for a specific bulk import job, supporting optional filtering and pagination parameters.

        Args:
            id (string): id
            fields_import_error (string): For more information please visit Example: 'code,original_payload'.
            page_cursor (string): For more information please visit Example: '<string>'.
            page_size (string): Default: 20. Min: 1. Max: 100. Example: '20'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Profiles, Bulk Import Profiles
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/profile-bulk-import-jobs/{id}/import-errors"
        query_params = {
            k: v
            for k, v in [
                ("fields[import-error]", fields_import_error),
                ("page[cursor]", page_cursor),
                ("page[size]", page_size),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_subscribe_profiles(self, data=None) -> Any:
        """
        Subscribes one or more profiles to email/SMS marketing lists in bulk, handling consent and double opt-in where applicable.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "custom_source": "<string>",
                      "historical_import": false,
                      "profiles": {
                        "data": [
                          {
                            "attributes": {
                              "age_gated_date_of_birth": "<date>",
                              "email": "<string>",
                              "phone_number": "<string>",
                              "subscriptions": {
                                "email": {
                                  "marketing": {
                                    "consent": "SUBSCRIBED",
                                    "consented_at": "<dateTime>"
                                  }
                                },
                                "sms": {
                                  "marketing": {
                                    "consent": "SUBSCRIBED",
                                    "consented_at": "<dateTime>"
                                  },
                                  "transactional": {
                                    "consent": "SUBSCRIBED",
                                    "consented_at": "<dateTime>"
                                  }
                                }
                              }
                            },
                            "id": "<string>",
                            "type": "profile"
                          },
                          {
                            "attributes": {
                              "age_gated_date_of_birth": "<date>",
                              "email": "<string>",
                              "phone_number": "<string>",
                              "subscriptions": {
                                "email": {
                                  "marketing": {
                                    "consent": "SUBSCRIBED",
                                    "consented_at": "<dateTime>"
                                  }
                                },
                                "sms": {
                                  "marketing": {
                                    "consent": "SUBSCRIBED",
                                    "consented_at": "<dateTime>"
                                  },
                                  "transactional": {
                                    "consent": "SUBSCRIBED",
                                    "consented_at": "<dateTime>"
                                  }
                                }
                              }
                            },
                            "id": "<string>",
                            "type": "profile"
                          }
                        ]
                      }
                    },
                    "relationships": {
                      "list": {
                        "data": {
                          "id": "<string>",
                          "type": "list"
                        }
                      }
                    },
                    "type": "profile-subscription-bulk-create-job"
                  }
                }
                ```

        Returns:
            Any: Success

        Tags:
            Profiles, Consent
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/profile-subscription-bulk-create-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_unsubscribe_profiles(self, data=None) -> Any:
        """
        Initiates a bulk unsubscribe job to remove multiple profiles from email subscriptions asynchronously.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "profiles": {
                        "data": [
                          {
                            "attributes": {
                              "email": "<string>",
                              "phone_number": "<string>",
                              "subscriptions": {
                                "email": {
                                  "marketing": {
                                    "consent": "UNSUBSCRIBED"
                                  }
                                },
                                "sms": {
                                  "marketing": {
                                    "consent": "UNSUBSCRIBED"
                                  },
                                  "transactional": {
                                    "consent": "UNSUBSCRIBED"
                                  }
                                }
                              }
                            },
                            "type": "profile"
                          },
                          {
                            "attributes": {
                              "email": "<string>",
                              "phone_number": "<string>",
                              "subscriptions": {
                                "email": {
                                  "marketing": {
                                    "consent": "UNSUBSCRIBED"
                                  }
                                },
                                "sms": {
                                  "marketing": {
                                    "consent": "UNSUBSCRIBED"
                                  },
                                  "transactional": {
                                    "consent": "UNSUBSCRIBED"
                                  }
                                }
                              }
                            },
                            "type": "profile"
                          }
                        ]
                      }
                    },
                    "relationships": {
                      "list": {
                        "data": {
                          "id": "<string>",
                          "type": "list"
                        }
                      }
                    },
                    "type": "profile-subscription-bulk-delete-job"
                  }
                }
                ```

        Returns:
            Any: Success

        Tags:
            Profiles, Consent
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/profile-subscription-bulk-delete-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def query_campaign_values(self, page_cursor=None, data=None) -> dict[str, Any]:
        """
        Creates a campaign values report, accepting a page cursor as a query parameter and a revision in the request header, returning data if successful.

        Args:
            page_cursor (string): For more information please visit Example: '<string>'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "conversion_metric_id": "<string>",
                      "filter": "<string>",
                      "statistics": [
                        "unsubscribe_rate",
                        "spam_complaint_rate"
                      ],
                      "timeframe": {
                        "key": "last_3_months"
                      }
                    },
                    "type": "campaign-values-report"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Reporting
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/campaign-values-reports"
        query_params = {
            k: v for k, v in [("page_cursor", page_cursor)] if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def query_flow_values(self, page_cursor=None, data=None) -> dict[str, Any]:
        """
        This API operation, using the POST method at "/api/flow-values-reports", allows users to generate reports by providing a page cursor in the query and a revision in the header, with potential responses indicating success (200) or error conditions (400, 500).

        Args:
            page_cursor (string): For more information please visit Example: '<string>'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "conversion_metric_id": "<string>",
                      "filter": "<string>",
                      "statistics": [
                        "open_rate",
                        "conversion_value"
                      ],
                      "timeframe": {
                        "key": "this_week"
                      }
                    },
                    "type": "flow-values-report"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Reporting
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/flow-values-reports"
        query_params = {
            k: v for k, v in [("page_cursor", page_cursor)] if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def query_flow_series(self, page_cursor=None, data=None) -> dict[str, Any]:
        """
        This API operation at "/api/flow-series-reports" utilizes the POST method to create a flow series report, allowing clients to specify pagination with the "page_cursor" query parameter and specify a revision via the "revision" header, with responses for successful execution (200), bad request (400), and internal server error (500).

        Args:
            page_cursor (string): For more information please visit Example: '<string>'.
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "conversion_metric_id": "<string>",
                      "filter": "<string>",
                      "interval": "hourly",
                      "statistics": [
                        "clicks_unique",
                        "conversion_rate"
                      ],
                      "timeframe": {
                        "key": "last_365_days"
                      }
                    },
                    "type": "flow-series-report"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Reporting
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/flow-series-reports"
        query_params = {
            k: v for k, v in [("page_cursor", page_cursor)] if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def query_form_values(self, data=None) -> dict[str, Any]:
        """
        Submits form values report data with a specified revision header.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "filter": "<string>",
                      "group_by": [
                        "form_version_id",
                        "form_version_id"
                      ],
                      "statistics": [
                        "viewed_form_step",
                        "viewed_form"
                      ],
                      "timeframe": {
                        "key": "last_3_months"
                      }
                    },
                    "type": "form-values-report"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Reporting
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/form-values-reports"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def query_form_series(self, data=None) -> dict[str, Any]:
        """
        This API operation, exposed at the "/api/form-series-reports" path using the "POST" method, allows users to generate or submit form series reports, specifying a revision via a header parameter, and returns responses indicating success, bad request, or internal server error.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "filter": "<string>",
                      "group_by": [
                        "form_id",
                        "form_id"
                      ],
                      "interval": "weekly",
                      "statistics": [
                        "viewed_form_step_uniques",
                        "closed_form_uniques"
                      ],
                      "timeframe": {
                        "key": "last_week"
                      }
                    },
                    "type": "form-series-report"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Reporting
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/form-series-reports"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def query_segment_values(self, data=None) -> dict[str, Any]:
        """
        Creates a report on segment values using a POST request to the "/api/segment-values-reports" endpoint, which requires a revision header and returns a report upon successful execution.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "filter": "<string>",
                      "statistics": [
                        "members_added",
                        "net_members_changed"
                      ],
                      "timeframe": {
                        "key": "this_week"
                      }
                    },
                    "type": "segment-values-report"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Reporting
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/segment-values-reports"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def query_segment_series(self, data=None) -> dict[str, Any]:
        """
        The POST operation at the "/api/segment-series-reports" path generates segment series reports, requiring a revision number provided in the header, and returns successful reports with a 200 status code or error messages for invalid requests (400) or server issues (500).

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "filter": "<string>",
                      "interval": "daily",
                      "statistics": [
                        "members_removed",
                        "members_added"
                      ],
                      "timeframe": {
                        "key": "last_week"
                      }
                    },
                    "type": "segment-series-report"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Reporting
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/segment-series-reports"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_reviews(
        self,
        fields_event=None,
        fields_review=None,
        filter=None,
        include=None,
        page_cursor=None,
        page_size=None,
        sort=None,
    ) -> dict[str, Any]:
        """
        Retrieves review data with optional filtering, pagination, sorting, and field selection parameters for events and reviews.

        Args:
            fields_event (string): For more information please visit Example: 'uuid,datetime'.
            fields_review (string): For more information please visit Example: 'author,images'.
            filter (string): For more information please visit field(s)/operator(s):<br>`created`: `greater-or-equal`, `less-or-equal`<br>`rating`: `any`, `equals`, `greater-or-equal`, `less-or-equal`<br>`id`: `any`, `equals`<br>`item.id`: `any`, `equals`<br>`content`: `contains`<br>`status`: `equals`<br>`review_type`: `equals`<br>`verified`: `equals` Example: '<string>'.
            include (string): For more information please visit Example: 'events,events'.
            page_cursor (string): For more information please visit Example: '<string>'.
            page_size (string): Default: 20. Min: 1. Max: 100. Example: '20'.
            sort (string): For more information please visit Example: '-updated'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Reviews
        """
        url = f"{self.base_url}/api/reviews"
        query_params = {
            k: v
            for k, v in [
                ("fields[event]", fields_event),
                ("fields[review]", fields_review),
                ("filter", filter),
                ("include", include),
                ("page[cursor]", page_cursor),
                ("page[size]", page_size),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_review(
        self, id, fields_event=None, fields_review=None, include=None
    ) -> dict[str, Any]:
        """
        The "/api/reviews/{id}" API endpoint uses the GET method to retrieve a specific review by its ID, allowing optional query parameters for selecting fields and specifying additional data to include, with support for a revision header.

        Args:
            id (string): id
            fields_event (string): For more information please visit Example: 'uuid,datetime'.
            fields_review (string): For more information please visit Example: 'author,images'.
            include (string): For more information please visit Example: 'events,events'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Reviews
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/reviews/{id}"
        query_params = {
            k: v
            for k, v in [
                ("fields[event]", fields_event),
                ("fields[review]", fields_review),
                ("include", include),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_review(self, id, data=None) -> dict[str, Any]:
        """
        This API operation uses the PATCH method at the "/api/reviews/{id}" path to partially update a review by applying specific changes while maintaining the integrity of unchanged fields, requiring a revision header for processing.

        Args:
            id (string): id
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "status": {
                        "rejection_reason": {
                          "reason": "other",
                          "status_explanation": "<string>"
                        },
                        "value": "rejected"
                      }
                    },
                    "id": "<string>",
                    "type": "review"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Reviews
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/reviews/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_segments(
        self,
        fields_flow=None,
        fields_segment=None,
        fields_tag=None,
        filter=None,
        include=None,
        page_cursor=None,
        sort=None,
    ) -> dict[str, Any]:
        """
        Use this API endpoint to retrieve a list of segments, allowing you to filter the results by various criteria and customize the output with specific fields and sorting options.

        Args:
            fields_flow (string): For more information please visit Example: 'created,status'.
            fields_segment (string): For more information please visit Example: 'is_processing,is_processing'.
            fields_tag (string): For more information please visit Example: 'name,name'.
            filter (string): For more information please visit field(s)/operator(s):<br>`name`: `any`, `equals`<br>`id`: `any`, `equals`<br>`created`: `greater-than`<br>`updated`: `greater-than`<br>`is_active`: `any`, `equals`<br>`is_starred`: `equals` Example: '<string>'.
            include (string): For more information please visit Example: 'flow-triggers,tags'.
            page_cursor (string): For more information please visit Example: '<string>'.
            sort (string): For more information please visit Example: '-updated'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Segments
        """
        url = f"{self.base_url}/api/segments"
        query_params = {
            k: v
            for k, v in [
                ("fields[flow]", fields_flow),
                ("fields[segment]", fields_segment),
                ("fields[tag]", fields_tag),
                ("filter", filter),
                ("include", include),
                ("page[cursor]", page_cursor),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_segment(self, data=None) -> dict[str, Any]:
        """
        Creates a new segment with the specified configuration, returning the created resource upon success.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "definition": {
                        "condition_groups": [
                          {
                            "conditions": [
                              {
                                "group_ids": [
                                  "<string>",
                                  "<string>"
                                ],
                                "is_member": true,
                                "timeframe_filter": {
                                  "date": "<dateTime>",
                                  "operator": "before",
                                  "type": "date"
                                },
                                "type": "profile-group-membership"
                              },
                              {
                                "group_ids": [
                                  "<string>",
                                  "<string>"
                                ],
                                "is_member": true,
                                "timeframe_filter": {
                                  "date": "<dateTime>",
                                  "operator": "before",
                                  "type": "date"
                                },
                                "type": "profile-group-membership"
                              }
                            ]
                          },
                          {
                            "conditions": [
                              {
                                "group_ids": [
                                  "<string>",
                                  "<string>"
                                ],
                                "is_member": true,
                                "timeframe_filter": {
                                  "date": "<dateTime>",
                                  "operator": "before",
                                  "type": "date"
                                },
                                "type": "profile-group-membership"
                              },
                              {
                                "group_ids": [
                                  "<string>",
                                  "<string>"
                                ],
                                "is_member": true,
                                "timeframe_filter": {
                                  "date": "<dateTime>",
                                  "operator": "before",
                                  "type": "date"
                                },
                                "type": "profile-group-membership"
                              }
                            ]
                          }
                        ]
                      },
                      "is_starred": false,
                      "name": "<string>"
                    },
                    "type": "segment"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Segments
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/segments"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_segment(
        self,
        id,
        additional_fields_segment=None,
        fields_flow=None,
        fields_segment=None,
        fields_tag=None,
        include=None,
    ) -> dict[str, Any]:
        """
        Retrieve a segment by its ID, optionally including additional fields, flows, segment details, tags, and related data, with support for specifying a revision in the request header.

        Args:
            id (string): id
            additional_fields_segment (string): Request additional fields not included by default in the response. Supported values: 'profile_count' Example: 'profile_count,profile_count'.
            fields_flow (string): For more information please visit Example: 'created,status'.
            fields_segment (string): For more information please visit Example: 'updated,is_active'.
            fields_tag (string): For more information please visit Example: 'name,name'.
            include (string): For more information please visit Example: 'flow-triggers,tags'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Segments
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/segments/{id}"
        query_params = {
            k: v
            for k, v in [
                ("additional-fields[segment]", additional_fields_segment),
                ("fields[flow]", fields_flow),
                ("fields[segment]", fields_segment),
                ("fields[tag]", fields_tag),
                ("include", include),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_segment(self, id) -> Any:
        """
        Deletes the specified segment by ID, requiring a revision header, and returns a 204 for success, 400 for invalid requests, or 500 for server errors.

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            Segments
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/segments/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_segment(self, id, data=None) -> dict[str, Any]:
        """
        The PATCH method at "/api/segments/{id}" allows partial updates to a segment resource, enabling modifications of specific fields while leaving others unchanged, with an optional revision header for version control.

        Args:
            id (string): id
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "definition": {
                        "condition_groups": [
                          {
                            "conditions": [
                              {
                                "group_ids": [
                                  "<string>",
                                  "<string>"
                                ],
                                "is_member": true,
                                "timeframe_filter": {
                                  "date": "<dateTime>",
                                  "operator": "before",
                                  "type": "date"
                                },
                                "type": "profile-group-membership"
                              },
                              {
                                "group_ids": [
                                  "<string>",
                                  "<string>"
                                ],
                                "is_member": true,
                                "timeframe_filter": {
                                  "date": "<dateTime>",
                                  "operator": "before",
                                  "type": "date"
                                },
                                "type": "profile-group-membership"
                              }
                            ]
                          },
                          {
                            "conditions": [
                              {
                                "group_ids": [
                                  "<string>",
                                  "<string>"
                                ],
                                "is_member": true,
                                "timeframe_filter": {
                                  "date": "<dateTime>",
                                  "operator": "before",
                                  "type": "date"
                                },
                                "type": "profile-group-membership"
                              },
                              {
                                "group_ids": [
                                  "<string>",
                                  "<string>"
                                ],
                                "is_member": true,
                                "timeframe_filter": {
                                  "date": "<dateTime>",
                                  "operator": "before",
                                  "type": "date"
                                },
                                "type": "profile-group-membership"
                              }
                            ]
                          }
                        ]
                      },
                      "is_starred": "<boolean>",
                      "name": "<string>"
                    },
                    "id": "<string>",
                    "type": "segment"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Segments
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/segments/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tags_for_segment(self, id, fields_tag=None) -> dict[str, Any]:
        """
        Retrieves tags for a segment by ID, allowing optional filtering by specific tag fields and accepting a revision in the request header.

        Args:
            id (string): id
            fields_tag (string): For more information please visit Example: 'name,name'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Segments
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/segments/{id}/tags"
        query_params = {k: v for k, v in [("fields[tag]", fields_tag)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag_ids_for_segment(self, id) -> dict[str, Any]:
        """
        Retrieves the relationships and associated tags for a specific segment identified by its ID, including any revision header information.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Segments
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/segments/{id}/relationships/tags"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_profiles_for_segment(
        self,
        id,
        additional_fields_profile=None,
        fields_profile=None,
        filter=None,
        page_cursor=None,
        page_size=None,
        sort=None,
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of profiles associated with a specific segment, supporting filtering, sorting, and field selection.

        Args:
            id (string): id
            additional_fields_profile (string): Request additional fields not included by default in the response. Supported values: 'subscriptions', 'predictive_analytics' Example: 'subscriptions,subscriptions'.
            fields_profile (string): For more information please visit Example: 'location.address1,first_name'.
            filter (string): For more information please visit field(s)/operator(s):<br>`email`: `any`, `equals`<br>`phone_number`: `any`, `equals`<br>`push_token`: `any`, `equals`<br>`_kx`: `equals`<br>`joined_group_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.
            page_size (string): Default: 20. Min: 1. Max: 100. Example: '20'.
            sort (string): For more information please visit Example: '-joined_group_at'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Segments
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/segments/{id}/profiles"
        query_params = {
            k: v
            for k, v in [
                ("additional-fields[profile]", additional_fields_profile),
                ("fields[profile]", fields_profile),
                ("filter", filter),
                ("page[cursor]", page_cursor),
                ("page[size]", page_size),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_profile_ids_for_segment(
        self, id, filter=None, page_cursor=None, page_size=None, sort=None
    ) -> dict[str, Any]:
        """
        This API operation retrieves the profiles related to a segment with the specified ID using a GET method, allowing for filtering, pagination, sorting, and revision specification through query and header parameters.

        Args:
            id (string): id
            filter (string): For more information please visit field(s)/operator(s):<br>`email`: `any`, `equals`<br>`phone_number`: `any`, `equals`<br>`push_token`: `any`, `equals`<br>`_kx`: `equals`<br>`joined_group_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.
            page_size (string): Default: 20. Min: 1. Max: 100. Example: '20'.
            sort (string): For more information please visit Example: '-joined_group_at'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Segments
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/segments/{id}/relationships/profiles"
        query_params = {
            k: v
            for k, v in [
                ("filter", filter),
                ("page[cursor]", page_cursor),
                ("page[size]", page_size),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flows_triggered_by_segment(self, id, fields_flow=None) -> dict[str, Any]:
        """
        Retrieves flow triggers for a segment by ID, optionally filtering by specific flow fields and providing a revision in the header.

        Args:
            id (string): id
            fields_flow (string): For more information please visit Example: 'created,status'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Segments
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/segments/{id}/flow-triggers"
        query_params = {
            k: v for k, v in [("fields[flow]", fields_flow)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_ids_for_flows_triggered_by_segment(self, id) -> dict[str, Any]:
        """
        Retrieves the associated flow triggers linked to a specific segment by its ID, supporting a custom revision header for version control.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Segments
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/segments/{id}/relationships/flow-triggers"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tags(
        self,
        fields_tag_group=None,
        fields_tag=None,
        filter=None,
        include=None,
        page_cursor=None,
        sort=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of tags filtered, sorted, and paginated via query parameters while supporting selective field inclusion and specific API revisions via headers.

        Args:
            fields_tag_group (string): For more information please visit Example: 'name,exclusive'.
            fields_tag (string): For more information please visit Example: 'name,name'.
            filter (string): For more information please visit field(s)/operator(s):<br>`name`: `contains`, `ends-with`, `equals`, `starts-with` Example: '<string>'.
            include (string): For more information please visit Example: 'tag-group,tag-group'.
            page_cursor (string): For more information please visit Example: '<string>'.
            sort (string): For more information please visit Example: 'name'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Tags, Tags1
        """
        url = f"{self.base_url}/api/tags"
        query_params = {
            k: v
            for k, v in [
                ("fields[tag-group]", fields_tag_group),
                ("fields[tag]", fields_tag),
                ("filter", filter),
                ("include", include),
                ("page[cursor]", page_cursor),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_tag(self, data=None) -> dict[str, Any]:
        """
        Creates a new tag resource using the provided data, requiring a revision header and returning HTTP status codes for success (201), client errors (400), or server issues (500).

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "name": "<string>"
                    },
                    "relationships": {
                      "tag-group": {
                        "data": {
                          "id": "<string>",
                          "type": "tag-group"
                        }
                      }
                    },
                    "type": "tag"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Tags, Tags1
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tags"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag(
        self, id, fields_tag_group=None, fields_tag=None, include=None
    ) -> dict[str, Any]:
        """
        Retrieves a specific tag by ID with optional query parameters for field selection, included resources, and a header for revision control.

        Args:
            id (string): id
            fields_tag_group (string): For more information please visit Example: 'name,exclusive'.
            fields_tag (string): For more information please visit Example: 'name,name'.
            include (string): For more information please visit Example: 'tag-group,tag-group'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Tags, Tags1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tags/{id}"
        query_params = {
            k: v
            for k, v in [
                ("fields[tag-group]", fields_tag_group),
                ("fields[tag]", fields_tag),
                ("include", include),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_tag(self, id) -> Any:
        """
        Deletes the specified tag by ID, requiring a revision header, with responses indicating success (204 No Content), bad request (400), or server error (500).

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            Tags, Tags1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tags/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_tag(self, id, data=None) -> Any:
        """
        Updates the specified tag (ID: {id}) with partial modifications using the revision header for conflict detection, returning 204 on success.

        Args:
            id (string): id
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "name": "<string>"
                    },
                    "id": "<string>",
                    "type": "tag"
                  }
                }
                ```

        Returns:
            Any: Success

        Tags:
            Tags, Tags1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tags/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flow_ids_for_tag(self, id) -> dict[str, Any]:
        """
        Retrieves the associated flow resources linked to the specified tag ID, using the provided revision header for version control.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Tags, Tags1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tags/{id}/relationships/flows"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def tag_flows(self, id, data=None) -> Any:
        """
        The API operation at path "/api/tags/{id}/relationships/flows" using the "POST" method creates a new relationship between a tag and a flow, optionally specifying a revision in the header.

        Args:
            id (string): id
            data (array): data
                Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "flow"
                    },
                    {
                      "id": "<string>",
                      "type": "flow"
                    }
                  ]
                }
                ```

        Returns:
            Any: Success

        Tags:
            Tags, Tags1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tags/{id}/relationships/flows"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_tag_from_flows(self, id, data=None) -> Any:
        """
        Deletes the relationship between the specified tag and associated flows, returning a 204 No Content response upon successful deletion.

        Args:
            id (string): id
            data (array): data
                Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "flow"
                    },
                    {
                      "id": "<string>",
                      "type": "flow"
                    }
                  ]
                }
                ```

        Returns:
            Any: Success

        Tags:
            Tags, Tags1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tags/{id}/relationships/flows"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaign_ids_for_tag(self, id) -> dict[str, Any]:
        """
        This API operation retrieves relationships between a tag with the specified ID and campaigns, using the GET method at the path "/api/tags/{id}/relationships/campaigns".

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Tags, Tags1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tags/{id}/relationships/campaigns"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def tag_campaigns(self, id, data=None) -> Any:
        """
        Creates a relationship between the specified tag and campaign(s) using the "revision" header for concurrency control.

        Args:
            id (string): id
            data (array): data
                Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "campaign"
                    },
                    {
                      "id": "<string>",
                      "type": "campaign"
                    }
                  ]
                }
                ```

        Returns:
            Any: Success

        Tags:
            Tags, Tags1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tags/{id}/relationships/campaigns"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_tag_from_campaigns(self, id, data=None) -> Any:
        """
        The API operation defined at `/api/tags/{id}/relationships/campaigns` using the `DELETE` method removes the relationship between a tag with the specified ID and associated campaigns, requiring a `revision` header and returning a successful response with a 204 status code if completed correctly.

        Args:
            id (string): id
            data (array): data
                Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "campaign"
                    },
                    {
                      "id": "<string>",
                      "type": "campaign"
                    }
                  ]
                }
                ```

        Returns:
            Any: Success

        Tags:
            Tags, Tags1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tags/{id}/relationships/campaigns"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_list_ids_for_tag(self, id) -> dict[str, Any]:
        """
        Retrieves the relationship details for lists associated with a specified tag ID, requiring a revision header parameter.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Tags, Tags1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tags/{id}/relationships/lists"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def tag_lists(self, id, data=None) -> Any:
        """
        Creates a new relationship between a specified tag and lists using the provided header revision.

        Args:
            id (string): id
            data (array): data
                Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "list"
                    },
                    {
                      "id": "<string>",
                      "type": "list"
                    }
                  ]
                }
                ```

        Returns:
            Any: Success

        Tags:
            Tags, Tags1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tags/{id}/relationships/lists"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_tag_from_lists(self, id, data=None) -> Any:
        """
        Deletes the relationship between a tag with the specified ID and its associated lists, requiring a revision header.

        Args:
            id (string): id
            data (array): data
                Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "list"
                    },
                    {
                      "id": "<string>",
                      "type": "list"
                    }
                  ]
                }
                ```

        Returns:
            Any: Success

        Tags:
            Tags, Tags1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tags/{id}/relationships/lists"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_segment_ids_for_tag(self, id) -> dict[str, Any]:
        """
        Retrieves a list of relationships between a tag identified by `{id}` and segments, with the option to specify a revision in the request header.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Tags, Tags1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tags/{id}/relationships/segments"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def tag_segments(self, id, data=None) -> Any:
        """
        Creates a relationship between a tag identified by `{id}` and one or more segments, using the specified revision from the request header.

        Args:
            id (string): id
            data (array): data
                Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "segment"
                    },
                    {
                      "id": "<string>",
                      "type": "segment"
                    }
                  ]
                }
                ```

        Returns:
            Any: Success

        Tags:
            Tags, Tags1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tags/{id}/relationships/segments"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_tag_from_segments(self, id, data=None) -> Any:
        """
        Removes tag associations with one or more segments by specifying the tag ID in the path and segment relationships in the request body.

        Args:
            id (string): id
            data (array): data
                Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "segment"
                    },
                    {
                      "id": "<string>",
                      "type": "segment"
                    }
                  ]
                }
                ```

        Returns:
            Any: Success

        Tags:
            Tags, Tags1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tags/{id}/relationships/segments"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag_group_for_tag(self, id, fields_tag_group=None) -> dict[str, Any]:
        """
        Retrieves the details of a tag group associated with the specified tag ID, allowing field selection via query parameters and revision specification via headers.

        Args:
            id (string): id
            fields_tag_group (string): For more information please visit Example: 'name,exclusive'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Tags, Tags1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tags/{id}/tag-group"
        query_params = {
            k: v for k, v in [("fields[tag-group]", fields_tag_group)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag_group_id_for_tag(self, id) -> dict[str, Any]:
        """
        Retrieves the tag-group relationship details for the specified tag ID, including optional revision header parameters.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Tags, Tags1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tags/{id}/relationships/tag-group"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag_groups(
        self, fields_tag_group=None, filter=None, page_cursor=None, sort=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of tag groups with optional filtering, sorting, pagination via cursor, field selection, and revision headers, returning appropriate status responses.

        Args:
            fields_tag_group (string): For more information please visit Example: 'name,exclusive'.
            filter (string): For more information please visit field(s)/operator(s):<br>`name`: `contains`, `ends-with`, `equals`, `starts-with`<br>`exclusive`: `equals`<br>`default`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.
            sort (string): For more information please visit Example: 'name'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Tags, Tag Groups
        """
        url = f"{self.base_url}/api/tag-groups"
        query_params = {
            k: v
            for k, v in [
                ("fields[tag-group]", fields_tag_group),
                ("filter", filter),
                ("page[cursor]", page_cursor),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_tag_group(self, data=None) -> dict[str, Any]:
        """
        Creates a new tag group with the specified revision header, returning a 201 response on successful creation or appropriate error codes (400/500) for failures.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "exclusive": false,
                      "name": "<string>"
                    },
                    "type": "tag-group"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Tags, Tag Groups
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tag-groups"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag_group(self, id, fields_tag_group=None) -> dict[str, Any]:
        """
        Retrieves a tag group by ID, allowing optional filtering by specific fields and including a revision header, returning a successful response with a 200 status code.

        Args:
            id (string): id
            fields_tag_group (string): For more information please visit Example: 'name,exclusive'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Tags, Tag Groups
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tag-groups/{id}"
        query_params = {
            k: v for k, v in [("fields[tag-group]", fields_tag_group)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_tag_group(self, id) -> dict[str, Any]:
        """
        Deletes a tag group by its ID, with the revision specified in the request header, returning success if the operation completes without errors.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Tags, Tag Groups
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tag-groups/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_tag_group(self, id, data=None) -> dict[str, Any]:
        """
        Updates the specified tag group by ID using partial modifications, requiring a revision header and returning 200, 400, or 500 status codes.

        Args:
            id (string): id
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "name": "<string>",
                      "return_fields": [
                        "<string>",
                        "<string>"
                      ]
                    },
                    "id": "<string>",
                    "type": "tag-group"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Tags, Tag Groups
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tag-groups/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tags_for_tag_group(self, id, fields_tag=None) -> dict[str, Any]:
        """
        This API operation retrieves a list of tags associated with a specific tag group, identified by `{id}`, allowing optional filtering by specific tag fields via the `fields[tag]` query parameter, with support for specifying a revision in the request header.

        Args:
            id (string): id
            fields_tag (string): For more information please visit Example: 'name,name'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Tags, Tag Groups
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tag-groups/{id}/tags"
        query_params = {k: v for k, v in [("fields[tag]", fields_tag)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag_ids_for_tag_group(self, id) -> dict[str, Any]:
        """
        This GET operation retrieves the relationships between a specific tag group and its associated tags, identified by the provided `{id}` in the path, with an optional `revision` header for additional context.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Tags, Tag Groups
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tag-groups/{id}/relationships/tags"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_templates(
        self, fields_template=None, filter=None, page_cursor=None, sort=None
    ) -> dict[str, Any]:
        """
        Retrieves template resources with optional filtering, sorting, pagination, and field selection.

        Args:
            fields_template (string): For more information please visit Example: 'name,text'.
            filter (string): For more information please visit field(s)/operator(s):<br>`id`: `any`, `equals`<br>`name`: `any`, `equals`<br>`created`: `equals`, `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`updated`: `equals`, `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.
            sort (string): For more information please visit Example: '-updated'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Templates, Templates1
        """
        url = f"{self.base_url}/api/templates"
        query_params = {
            k: v
            for k, v in [
                ("fields[template]", fields_template),
                ("filter", filter),
                ("page[cursor]", page_cursor),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_template(self, data=None) -> dict[str, Any]:
        """
        Creates a new template with the specified revision, returning a successful response if created or error responses for bad requests or server failures.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "editor_type": "<string>",
                      "html": "<string>",
                      "name": "<string>",
                      "text": "<string>"
                    },
                    "type": "template"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Templates, Templates1
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/templates"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_template(self, id, fields_template=None) -> dict[str, Any]:
        """
        The API operation defined at the path "/api/templates/{id}" using the "GET" method retrieves a specific template by its ID, optionally specifying fields to include and a revision in the headers, returning a successful response with HTTP status 200.

        Args:
            id (string): id
            fields_template (string): For more information please visit Example: 'name,text'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Templates, Templates1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/templates/{id}"
        query_params = {
            k: v for k, v in [("fields[template]", fields_template)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_template(self, id) -> Any:
        """
        Deletes a template by ID with optional revision header, returning 204 on success or 400/500 for client/server errors.

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            Templates, Templates1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/templates/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_template(self, id, data=None) -> dict[str, Any]:
        """
        Updates a template's properties using partial modifications with a specified revision header, returning 200 on success.

        Args:
            id (string): id
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "html": "<string>",
                      "name": "<string>",
                      "text": "<string>"
                    },
                    "id": "<string>",
                    "type": "template"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Templates, Templates1
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/templates/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def render_template(self, data=None) -> dict[str, Any]:
        """
        Renders a template using the specified revision header, returning success (201) or error status (400/500).

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "context": {}
                    },
                    "id": "<string>",
                    "type": "template"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Templates, Templates1
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/template-render"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def clone_template(self, data=None) -> dict[str, Any]:
        """
        Creates a new template by cloning an existing one, requiring a revision header parameter and returning success (201), bad request (400), or server error (500) responses.

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "name": "<string>"
                    },
                    "id": "<string>",
                    "type": "template"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Templates, Templates1
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/template-clone"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_all_universal_content(
        self,
        fields_template_universal_content=None,
        filter=None,
        page_cursor=None,
        page_size=None,
        sort=None,
    ) -> dict[str, Any]:
        """
        This API operation uses the GET method at the "/api/template-universal-content" path to retrieve template universal content data, allowing filtering and sorting with optional parameters for fields, filter, pagination, and sorting, while requiring a revision in the header.

        Args:
            fields_template_universal_content (string): For more information please visit Example: 'definition.data.content,definition.data.styles.color'.
            filter (string): For more information please visit field(s)/operator(s):<br>`id`: `any`, `equals`<br>`name`: `any`, `equals`<br>`created`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`updated`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`definition.content_type`: `equals`<br>`definition.type`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit Example: '<string>'.
            page_size (string): Default: 20. Min: 1. Max: 100. Example: '20'.
            sort (string): For more information please visit Example: '-updated'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Templates, Universal Content
        """
        url = f"{self.base_url}/api/template-universal-content"
        query_params = {
            k: v
            for k, v in [
                (
                    "fields[template-universal-content]",
                    fields_template_universal_content,
                ),
                ("filter", filter),
                ("page[cursor]", page_cursor),
                ("page[size]", page_size),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_universal_content(self, data=None) -> dict[str, Any]:
        """
        Generates universal content templates with optional revision control in headers, returning success (201) or error codes (400, 500).

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "definition": {
                        "content_type": "block",
                        "data": {
                          "content": "<string>",
                          "display_options": {
                            "content_repeat": {
                              "item_alias": "<string>",
                              "repeat_for": "<string>"
                            },
                            "show_on": "all",
                            "visible_check": "<string>"
                          }
                        },
                        "type": "html"
                      },
                      "name": "<string>"
                    },
                    "type": "template-universal-content"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Templates, Universal Content
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/template-universal-content"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_universal_content(
        self, id, fields_template_universal_content=None
    ) -> dict[str, Any]:
        """
        This API operation retrieves a template with universal content specified by the `{id}` using the GET method, allowing optional filtering by specific fields and specifying a revision in the header.

        Args:
            id (string): id
            fields_template_universal_content (string): For more information please visit Example: 'definition.data.content,definition.data.styles.color'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Templates, Universal Content
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/template-universal-content/{id}"
        query_params = {
            k: v
            for k, v in [
                (
                    "fields[template-universal-content]",
                    fields_template_universal_content,
                )
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_universal_content(self, id) -> Any:
        """
        Deletes the specified universal content item by ID, requiring a revision header, and returns 204 No Content upon successful deletion.

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            Templates, Universal Content
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/template-universal-content/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_universal_content(self, id, data=None) -> dict[str, Any]:
        """
        The PATCH operation at "/api/template-universal-content/{id}" partially updates a template's content by specifying specific changes in the request body, with the revision specified in the header, returning a successful response or error based on the request's validity.

        Args:
            id (string): id
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "definition": {
                        "content_type": "block",
                        "data": {
                          "content": "<string>",
                          "display_options": {
                            "content_repeat": {
                              "item_alias": "<string>",
                              "repeat_for": "<string>"
                            },
                            "show_on": "desktop",
                            "visible_check": "<string>"
                          }
                        },
                        "type": "html"
                      },
                      "name": "<string>"
                    },
                    "id": "<string>",
                    "type": "template-universal-content"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Templates, Universal Content
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/template-universal-content/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tracking_settings(
        self, fields_tracking_setting=None, page_cursor=None, page_size=None
    ) -> dict[str, Any]:
        """
        Retrieves all tracking settings in an account with optional pagination and field filtering support.

        Args:
            fields_tracking_setting (string): For more information please visit Example: 'utm_term.campaign.value,utm_medium.flow.type'.
            page_cursor (string): For more information please visit Example: '<string>'.
            page_size (string): Default: 1. Min: 1. Max: 1. Example: '1'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Tracking Settings
        """
        url = f"{self.base_url}/api/tracking-settings"
        query_params = {
            k: v
            for k, v in [
                ("fields[tracking-setting]", fields_tracking_setting),
                ("page[cursor]", page_cursor),
                ("page[size]", page_size),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tracking_setting(self, id, fields_tracking_setting=None) -> dict[str, Any]:
        """
        Retrieves tracking settings by ID with optional field selection and revision header support.

        Args:
            id (string): id
            fields_tracking_setting (string): For more information please visit Example: 'utm_term.campaign.value,utm_medium.flow.type'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Tracking Settings
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tracking-settings/{id}"
        query_params = {
            k: v
            for k, v in [("fields[tracking-setting]", fields_tracking_setting)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_tracking_setting(self, id, data=None) -> dict[str, Any]:
        """
        PATCH /api/tracking-settings/{id} partially updates a specific tracking setting by ID, requiring a revision in the header, and may return a successful response or error codes based on input validity and server status.

        Args:
            id (string): id
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "auto_add_parameters": "<boolean>",
                      "custom_parameters": [
                        {
                          "campaign": {
                            "type": "dynamic",
                            "value": "campaign_name_id"
                          },
                          "flow": {
                            "type": "dynamic",
                            "value": "flow_id"
                          },
                          "name": "<string>"
                        },
                        {
                          "campaign": {
                            "type": "dynamic",
                            "value": "campaign_name"
                          },
                          "flow": {
                            "type": "dynamic",
                            "value": "message_type"
                          },
                          "name": "<string>"
                        }
                      ],
                      "utm_campaign": {
                        "campaign": {
                          "type": "dynamic",
                          "value": "profile_external_id"
                        },
                        "flow": {
                          "type": "dynamic",
                          "value": "profile_external_id"
                        }
                      },
                      "utm_id": {
                        "campaign": {
                          "type": "dynamic",
                          "value": "group_id"
                        },
                        "flow": {
                          "type": "dynamic",
                          "value": "flow_id"
                        }
                      },
                      "utm_medium": {
                        "campaign": {
                          "type": "dynamic",
                          "value": "campaign_name_id"
                        },
                        "flow": {
                          "type": "dynamic",
                          "value": "message_name_id"
                        }
                      },
                      "utm_source": {
                        "campaign": {
                          "type": "dynamic",
                          "value": "email_subject"
                        },
                        "flow": {
                          "type": "dynamic",
                          "value": "flow_id"
                        }
                      },
                      "utm_term": {
                        "campaign": {
                          "type": "dynamic",
                          "value": "link_alt_text"
                        },
                        "flow": {
                          "type": "dynamic",
                          "value": "flow_name"
                        }
                      }
                    },
                    "id": "<string>",
                    "type": "tracking-setting"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Tracking Settings
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tracking-settings/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_webhooks(self, fields_webhook=None, include=None) -> dict[str, Any]:
        """
        Retrieves webhooks with optional field selection, included resources, and revision headers.

        Args:
            fields_webhook (string): For more information please visit Example: 'description,updated_at'.
            include (string): For more information please visit Example: 'webhook-topics,webhook-topics'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Webhooks
        """
        url = f"{self.base_url}/api/webhooks"
        query_params = {
            k: v
            for k, v in [("fields[webhook]", fields_webhook), ("include", include)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_webhook(self, data=None) -> dict[str, Any]:
        """
        The "/api/webhooks" endpoint supports the "POST" method to create a new webhook, requiring a revision header, and returns a successful creation response with a 201 status code, or error responses for bad requests (400) or internal server errors (500).

        Args:
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "description": "<string>",
                      "endpoint_url": "<string>",
                      "name": "<string>",
                      "secret_key": "<string>"
                    },
                    "relationships": {
                      "webhook-topics": {
                        "data": [
                          {
                            "id": "<string>",
                            "type": "webhook-topic"
                          },
                          {
                            "id": "<string>",
                            "type": "webhook-topic"
                          }
                        ]
                      }
                    },
                    "type": "webhook"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Webhooks
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/webhooks"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_webhook(self, id, fields_webhook=None, include=None) -> dict[str, Any]:
        """
        Retrieves a webhook by its ID using a GET request, allowing optional filtering by specifying fields and includes, with support for revision tracking via a header.

        Args:
            id (string): id
            fields_webhook (string): For more information please visit Example: 'description,updated_at'.
            include (string): For more information please visit Example: 'webhook-topics,webhook-topics'.

        Returns:
            dict[str, Any]: Success

        Tags:
            Webhooks
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/webhooks/{id}"
        query_params = {
            k: v
            for k, v in [("fields[webhook]", fields_webhook), ("include", include)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_webhook(self, id) -> Any:
        """
        Deletes a webhook resource identified by its ID, returning a 204 No Content response upon successful deletion, with optional revision information provided in the headers, and error responses for invalid requests or server errors.

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            Webhooks
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/webhooks/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_webhook(self, id, data=None) -> dict[str, Any]:
        """
        Updates the webhook resource identified by {id} using partial modifications, requiring a revision header and returning appropriate status codes for success (200), client errors (400), or server errors (500).

        Args:
            id (string): id
            data (object): data
                Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "description": "<string>",
                      "enabled": "<boolean>",
                      "endpoint_url": "<string>",
                      "name": "<string>",
                      "secret_key": "<string>"
                    },
                    "id": "<string>",
                    "relationships": {
                      "webhook-topics": {
                        "data": [
                          {
                            "id": "<string>",
                            "type": "webhook-topic"
                          },
                          {
                            "id": "<string>",
                            "type": "webhook-topic"
                          }
                        ]
                      }
                    },
                    "type": "webhook"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Webhooks
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/webhooks/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_webhook_topics(self) -> dict[str, Any]:
        """
        Retrieves webhook topics with an optional revision header parameter, returning 200, 400, or 500 status codes.

        Returns:
            dict[str, Any]: Success

        Tags:
            Webhooks
        """
        url = f"{self.base_url}/api/webhook-topics"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_webhook_topic(self, id) -> dict[str, Any]:
        """
        Retrieves a webhook topic by its ID using the GET method, supporting revision information via a header parameter, and returns responses for successful retrieval (200), bad requests (400), and internal server errors (500).

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Webhooks
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/webhook-topics/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [
            self.create_client_review,
            self.get_accounts,
            self.get_account,
            self.get_campaigns,
            self.create_campaign,
            self.get_campaign,
            self.delete_campaign,
            self.update_campaign,
            self.get_campaign_recipient_estimation,
            self.create_campaign_clone,
            self.get_tags_for_campaign,
            self.get_tag_ids_for_campaign,
            self.get_messages_for_campaign,
            self.get_message_ids_for_campaign,
            self.get_campaign_message,
            self.update_campaign_message,
            self.assign_template_to_campaign_message,
            self.get_campaign_for_campaign_message,
            self.get_campaign_id_for_campaign_message,
            self.get_template_for_campaign_message,
            self.get_template_id_for_campaign_message,
            self.get_image_for_campaign_message,
            self.get_image_id_for_campaign_message,
            self.update_image_for_campaign_message,
            self.get_campaign_send_job,
            self.cancel_campaign_send,
            self.get_campaign_recipient_estimation_job,
            self.send_campaign,
            self.refresh_campaign_recipient_estimation,
            self.get_catalog_items,
            self.create_catalog_item,
            self.get_catalog_item,
            self.delete_catalog_item,
            self.update_catalog_item,
            self.get_bulk_create_catalog_items_jobs,
            self.bulk_create_catalog_items,
            self.get_bulk_create_catalog_items_job,
            self.get_bulk_update_catalog_items_jobs,
            self.bulk_update_catalog_items,
            self.get_bulk_update_catalog_items_job,
            self.get_bulk_delete_catalog_items_jobs,
            self.bulk_delete_catalog_items,
            self.get_bulk_delete_catalog_items_job,
            self.get_items_for_catalog_category,
            self.get_category_ids_for_catalog_item,
            self.add_categories_to_catalog_item,
            self.remove_categories_from_catalog_item,
            self.update_categories_for_catalog_item,
            self.get_catalog_variants,
            self.create_catalog_variant,
            self.get_catalog_variant,
            self.delete_catalog_variant,
            self.update_catalog_variant,
            self.get_create_variants_jobs,
            self.bulk_create_catalog_variants,
            self.get_create_variants_job,
            self.get_update_variants_jobs,
            self.bulk_update_catalog_variants,
            self.get_update_variants_job,
            self.get_delete_variants_jobs,
            self.bulk_delete_catalog_variants,
            self.get_delete_variants_job,
            self.get_variants_for_catalog_item,
            self.get_variant_ids_for_catalog_item,
            self.get_catalog_categories,
            self.create_catalog_category,
            self.get_catalog_category,
            self.delete_catalog_category,
            self.update_catalog_category,
            self.get_create_categories_jobs,
            self.bulk_create_catalog_categories,
            self.get_create_categories_job,
            self.get_update_categories_jobs,
            self.bulk_update_catalog_categories,
            self.get_update_categories_job,
            self.get_delete_categories_jobs,
            self.bulk_delete_catalog_categories,
            self.get_delete_categories_job,
            self.get_item_ids_for_catalog_category,
            self.add_items_to_catalog_category,
            self.remove_items_from_catalog_category,
            self.update_items_for_catalog_category,
            self.get_categories_for_catalog_item,
            self.create_back_in_stock_subscription,
            self.create_client_subscription,
            self.create_or_update_client_push_token,
            self.unregister_client_push_token,
            self.create_client_event,
            self.create_or_update_client_profile,
            self.bulk_create_client_events,
            self.create_client_back_in_stock_subscription,
            self.get_coupons,
            self.create_coupon,
            self.get_coupon,
            self.delete_coupon,
            self.update_coupon,
            self.get_coupon_codes,
            self.create_coupon_code,
            self.get_coupon_code,
            self.delete_coupon_code,
            self.update_coupon_code,
            self.get_bulk_create_coupon_code_jobs,
            self.bulk_create_coupon_codes,
            self.get_bulk_create_coupon_codes_job,
            self.get_coupon_for_coupon_code,
            self.get_coupon_id_for_coupon_code,
            self.get_coupon_codes_for_coupon,
            self.get_coupon_code_ids_for_coupon,
            self.request_profile_deletion,
            self.get_events,
            self.create_event,
            self.get_event,
            self.bulk_create_events,
            self.get_metric_for_event,
            self.get_metric_id_for_event,
            self.get_profile_for_event,
            self.get_profile_id_for_event,
            self.get_flows,
            self.create_flow,
            self.get_flow,
            self.delete_flow,
            self.update_flow_status,
            self.get_flow_action,
            self.get_flow_message,
            self.get_actions_for_flow,
            self.get_action_ids_for_flow,
            self.get_tags_for_flow,
            self.get_tag_ids_for_flow,
            self.get_flow_for_flow_action,
            self.get_flow_id_for_flow_action,
            self.get_messages_for_flow_action,
            self.get_message_ids_for_flow_action,
            self.get_action_for_flow_message,
            self.get_action_id_for_flow_message,
            self.get_template_for_flow_message,
            self.get_template_id_for_flow_message,
            self.get_forms,
            self.get_form,
            self.get_form_version,
            self.get_versions_for_form,
            self.get_version_ids_for_form,
            self.get_form_for_form_version,
            self.get_form_id_for_form_version,
            self.get_images,
            self.upload_image_from_url,
            self.get_image,
            self.update_image,
            self.get_lists,
            self.create_list,
            self.get_list,
            self.delete_list,
            self.update_list,
            self.get_tags_for_list,
            self.get_tag_ids_for_list,
            self.get_profiles_for_list,
            self.get_profile_ids_for_list,
            self.add_profiles_to_list,
            self.remove_profiles_from_list,
            self.get_flows_triggered_by_list,
            self.get_ids_for_flows_triggered_by_list,
            self.get_metrics,
            self.get_metric,
            self.get_metric_property,
            self.query_metric_aggregates,
            self.get_flows_triggered_by_metric,
            self.get_ids_for_flows_triggered_by_metric,
            self.get_properties_for_metric,
            self.get_property_ids_for_metric,
            self.get_metric_for_metric_property,
            self.get_metric_id_for_metric_property,
            self.get_profiles,
            self.create_profile,
            self.get_profile,
            self.update_profile,
            self.get_bulk_suppress_profiles_jobs,
            self.bulk_suppress_profiles,
            self.get_bulk_suppress_profiles_job,
            self.get_bulk_unsuppress_profiles_jobs,
            self.bulk_unsuppress_profiles,
            self.get_bulk_unsuppress_profiles_job,
            self.create_or_update_profile,
            self.merge_profiles,
            self.create_or_update_push_token,
            self.get_lists_for_profile,
            self.get_list_ids_for_profile,
            self.get_segments_for_profile,
            self.get_segment_ids_for_profile,
            self.get_bulk_import_profiles_jobs,
            self.bulk_import_profiles,
            self.get_bulk_import_profiles_job,
            self.get_list_for_bulk_import_profiles_job,
            self.get_list_ids_for_bulk_import_profiles_job,
            self.get_profiles_for_bulk_import_profiles_job,
            self.get_profile_ids_for_bulk_import_profiles_job,
            self.get_errors_for_bulk_import_profiles_job,
            self.bulk_subscribe_profiles,
            self.bulk_unsubscribe_profiles,
            self.query_campaign_values,
            self.query_flow_values,
            self.query_flow_series,
            self.query_form_values,
            self.query_form_series,
            self.query_segment_values,
            self.query_segment_series,
            self.get_reviews,
            self.get_review,
            self.update_review,
            self.get_segments,
            self.create_segment,
            self.get_segment,
            self.delete_segment,
            self.update_segment,
            self.get_tags_for_segment,
            self.get_tag_ids_for_segment,
            self.get_profiles_for_segment,
            self.get_profile_ids_for_segment,
            self.get_flows_triggered_by_segment,
            self.get_ids_for_flows_triggered_by_segment,
            self.get_tags,
            self.create_tag,
            self.get_tag,
            self.delete_tag,
            self.update_tag,
            self.get_flow_ids_for_tag,
            self.tag_flows,
            self.remove_tag_from_flows,
            self.get_campaign_ids_for_tag,
            self.tag_campaigns,
            self.remove_tag_from_campaigns,
            self.get_list_ids_for_tag,
            self.tag_lists,
            self.remove_tag_from_lists,
            self.get_segment_ids_for_tag,
            self.tag_segments,
            self.remove_tag_from_segments,
            self.get_tag_group_for_tag,
            self.get_tag_group_id_for_tag,
            self.get_tag_groups,
            self.create_tag_group,
            self.get_tag_group,
            self.delete_tag_group,
            self.update_tag_group,
            self.get_tags_for_tag_group,
            self.get_tag_ids_for_tag_group,
            self.get_templates,
            self.create_template,
            self.get_template,
            self.delete_template,
            self.update_template,
            self.render_template,
            self.clone_template,
            self.get_all_universal_content,
            self.create_universal_content,
            self.get_universal_content,
            self.delete_universal_content,
            self.update_universal_content,
            self.get_tracking_settings,
            self.get_tracking_setting,
            self.update_tracking_setting,
            self.get_webhooks,
            self.create_webhook,
            self.get_webhook,
            self.delete_webhook,
            self.update_webhook,
            self.get_webhook_topics,
            self.get_webhook_topic,
        ]
