from typing import Any

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class WhatsappBusinessApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="whatsapp_business", integration=integration, **kwargs)
        self.base_url = "https://graph.facebook.com"

    def get_whatsapp_business_account(
        self, api_version: str, waba_id: str, fields: str | None = None
    ) -> dict[str, Any]:
        """
        Fetches customizable data, primarily analytics, for a specific WhatsApp Business Account (WABA) using its ID. The `fields` parameter allows detailed queries, including date ranges and granularity for metrics like message volume, to refine the returned data.

        Args:
            api_version (string): api-version
            waba_id (string): waba-id
            fields (string): Specifies which fields to include/exclude in the response for the WhatsApp Business Account resource. Example: 'analytics.start(1680503760).end(1680564980).granularity(DAY).phone_numbers([]).country_codes(["US", "BR"])'.

        Returns:
            dict[str, Any]: Example reponse / Example response / Example response / Example response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            WhatsApp Business Accounts (WABA)
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'.")
        if waba_id is None:
            raise ValueError("Missing required parameter 'waba-id'.")
        url = f"{self.base_url}/{api_version}/{waba_id}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
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

    def get_business_account_credit_lines(
        self, api_version: str, business_account_id: str
    ) -> dict[str, Any]:
        """
        Retrieves the extended credit lines for a specified business account ID. This function fetches billing information by querying the `/extendedcredits` endpoint, returning financial details such as available credit for platform services.

        Args:
            api_version (string): api-version
            business_account_id (string): business-account-id

        Returns:
            dict[str, Any]: Example response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Billing
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'.")
        if business_account_id is None:
            raise ValueError("Missing required parameter 'business-account-id'.")
        url = f"{self.base_url}/{api_version}/{business_account_id}/extendedcredits"
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

    def get_business_account(
        self, api_version: str, business_account_id: str, fields: str | None = None
    ) -> dict[str, Any]:
        """
        Fetches details for a specific Meta Business Account using its ID. This function retrieves the core account object, unlike others that get associated resources like owned/shared WhatsApp Business Accounts (WABAs) or credit lines for the same ID. The response payload can be customized using the 'fields' parameter.

        Args:
            api_version (string): api-version
            business_account_id (string): business-account-id
            fields (string): Specifies the fields to include in the response, reducing payload size by returning only the requested data. Example: 'id,name,timezone_id'.

        Returns:
            dict[str, Any]: Example response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Business accounts, important
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'.")
        if business_account_id is None:
            raise ValueError("Missing required parameter 'business-account-id'.")
        url = f"{self.base_url}/{api_version}/{business_account_id}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
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

    def get_commerce_settings(
        self, api_version: str, business_phone_number_id: str
    ) -> dict[str, Any]:
        """
        Retrieves the commerce settings, such as cart availability and catalog visibility, for a specific WhatsApp Business phone number. This function reads the current configuration, contrasting with `set_or_update_commerce_settings` which modifies them.

        Args:
            api_version (string): api-version
            business_phone_number_id (string): business-phone-number-id

        Returns:
            dict[str, Any]: Example response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Commerce, important
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'.")
        if business_phone_number_id is None:
            raise ValueError("Missing required parameter 'business-phone-number-id'.")
        url = f"{self.base_url}/{api_version}/{business_phone_number_id}/whatsapp_commerce_settings"
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

    def update_commerce_settings(
        self,
        api_version: str,
        business_phone_number_id: str,
        is_cart_enabled: str | None = None,
        is_catalog_visible: str | None = None,
    ) -> dict[str, Any]:
        """
        Updates the commerce settings for a specific business phone number by enabling or disabling cart functionality and catalog visibility. This function differentiates from `get_commerce_settings` by using a POST request to modify data, rather than retrieving it.

        Args:
            api_version (string): api-version
            business_phone_number_id (string): business-phone-number-id
            is_cart_enabled (string): Indicates whether the shopping cart is enabled or disabled for the specified WhatsApp commerce settings. Example: 'true'.
            is_catalog_visible (string): Determines whether the business's product catalog is visible to customers in WhatsApp conversations. Example: 'true'.

        Returns:
            dict[str, Any]: Example response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Commerce
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'.")
        if business_phone_number_id is None:
            raise ValueError("Missing required parameter 'business-phone-number-id'.")
        request_body_data = None
        url = f"{self.base_url}/{api_version}/{business_phone_number_id}/whatsapp_commerce_settings"
        query_params = {
            k: v
            for k, v in [
                ("is_cart_enabled", is_cart_enabled),
                ("is_catalog_visible", is_catalog_visible),
            ]
            if v is not None
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

    def create_upload_session(
        self,
        api_version: str,
        app_id: str,
        file_length: str | None = None,
        file_type: str | None = None,
    ) -> dict[str, Any]:
        """
        Initiates a resumable upload session by providing file metadata (size, type). This function creates an upload session ID and is the first of a two-step process for uploading media, preceding the actual data transfer performed by `resume_session`.

        Args:
            api_version (string): api-version
            app_id (string): app-id
            file_length (string): File size, in bytes Example: '<FILE_SIZE>'.
            file_type (string): File MIME type (e.g. image/jpg) Example: '<MIME_TYPE>'.

        Returns:
            dict[str, Any]: Step 1 example response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Media
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'.")
        if app_id is None:
            raise ValueError("Missing required parameter 'app-id'.")
        request_body_data = None
        url = f"{self.base_url}/{api_version}/{app_id}/uploads"
        query_params = {
            k: v
            for k, v in [("file_length", file_length), ("file_type", file_type)]
            if v is not None
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

    def upload_file_to_session(self, api_version: str) -> dict[str, Any]:
        """
        Continues a media file upload by sending file data to an existing session. This function is the second step in the upload process, following `upload_file`, which creates the session and provides the required session ID.

        Args:
            api_version (string): api-version

        Returns:
            dict[str, Any]: Step 2 example response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Media
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'.")
        request_body_data = None
        url = f"{self.base_url}/{api_version}/<SESSION_ID>"
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

    def get_business_phone_number(
        self,
        api_version: str,
        business_phone_number_id: str,
        fields: str | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves details for a specific WhatsApp Business phone number by its unique ID. The optional `fields` parameter allows for customizing the response to include only desired data, differentiating it from `get_all_business_phone_numbers`, which retrieves a list of all numbers for a WABA.

        Args:
            api_version (string): api-version
            business_phone_number_id (string): business-phone-number-id
            fields (string): Specifies which fields to include in the response for the business phone number. Example: 'id,display_phone_number,name_status'.

        Returns:
            dict[str, Any]: Example response / Example response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Phone numbers, important
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'.")
        if business_phone_number_id is None:
            raise ValueError("Missing required parameter 'business-phone-number-id'.")
        url = f"{self.base_url}/{api_version}/{business_phone_number_id}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
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

    def list_waba_phone_numbers(
        self,
        api_version: str,
        waba_id: str,
        fields: str | None = None,
        filtering: str | None = None,
    ) -> list[Any]:
        """
        Fetches a list of phone numbers for a specified WhatsApp Business Account (WABA). This function allows for result filtering and customizable field selection, distinguishing it from `get_business_phone_number` which retrieves a single number by its unique ID.

        Args:
            api_version (string): api-version
            waba_id (string): waba-id
            fields (string): Optional parameter to specify which fields should be included in the response for phone numbers associated with a WABA, allowing customization of the returned data. Example: 'id,is_official_business_account,display_phone_number,verified_name'.
            filtering (string): Specifies query parameters to filter phone numbers based on specific criteria for the GET operation. Example: "[{'field':'account_mode','operator':'EQUAL','value':'SANDBOX'}]".

        Returns:
            list[Any]: Example response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Phone numbers, important
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'.")
        if waba_id is None:
            raise ValueError("Missing required parameter 'waba-id'.")
        url = f"{self.base_url}/{api_version}/{waba_id}/phone_numbers"
        query_params = {
            k: v
            for k, v in [("fields", fields), ("filtering", filtering)]
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

    def get_qr_code_by_id(
        self, api_version: str, business_phone_number_id: str
    ) -> dict[str, Any]:
        """
        Retrieves the details of a single QR code, such as its pre-filled message, by its unique ID for a specific business phone number. It fetches a specific code, distinguishing it from `get_all_qr_codes_default_fields` which retrieves a list of codes.

        Args:
            api_version (string): api-version
            business_phone_number_id (string): business-phone-number-id

        Returns:
            dict[str, Any]: Example Response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            QR codes
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'.")
        if business_phone_number_id is None:
            raise ValueError("Missing required parameter 'business-phone-number-id'.")
        url = f"{self.base_url}/{api_version}/{business_phone_number_id}/message_qrdls/<QR_CODE_ID>"
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

    def delete_qr_code_by_id(
        self, api_version: str, business_phone_number_id: str
    ) -> dict[str, Any]:
        """
        Deletes a specific WhatsApp message QR code by its ID for a given business phone number. The function sends a DELETE request to the Graph API's `message_qrdls` endpoint to remove the specified QR code.

        Args:
            api_version (string): api-version
            business_phone_number_id (string): business-phone-number-id

        Returns:
            dict[str, Any]: Example Response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            QR codes
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'.")
        if business_phone_number_id is None:
            raise ValueError("Missing required parameter 'business-phone-number-id'.")
        url = f"{self.base_url}/{api_version}/{business_phone_number_id}/message_qrdls/<QR_CODE_ID>"
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

    def list_qr_codes(
        self,
        api_version: str,
        business_phone_number_id: str,
        fields: str | None = None,
        code: str | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of QR codes for a business phone number. This function allows optional filtering by a specific QR code identifier and customization of the fields returned in the response, such as the image format.

        Args:
            api_version (string): api-version
            business_phone_number_id (string): business-phone-number-id
            fields (string): .format can be SVG or PNG Example: 'code,prefilled_message,qr_image_url.format(SVG)'.
            code (string): The unique identifier code used to filter messages associated with the specified business phone number. Example: '<QR_CODE_ID>'.

        Returns:
            dict[str, Any]: Example Response / Example Response / Example Response / Example Response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            QR codes
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'.")
        if business_phone_number_id is None:
            raise ValueError("Missing required parameter 'business-phone-number-id'.")
        url = f"{self.base_url}/{api_version}/{business_phone_number_id}/message_qrdls"
        query_params = {
            k: v for k, v in [("fields", fields), ("code", code)] if v is not None
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

    def create_qr_code(
        self,
        api_version: str,
        business_phone_number_id: str,
        code: str | None = None,
        prefilled_message: str | None = None,
    ) -> dict[str, Any]:
        """
        Generates a WhatsApp Business QR code for a specific phone number. This function allows setting a prefilled message for user convenience and can optionally include a custom identifier. It returns the details of the newly created QR code upon successful generation.

        Args:
            api_version (string): api-version
            business_phone_number_id (string): business-phone-number-id
            code (string): code Example: 'WOMVT6TJ2BP7A1'.
            prefilled_message (string): prefilled_message Example: 'Tell me about your new workshops'.

        Returns:
            dict[str, Any]: Example Response / Example Response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            QR codes
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'.")
        if business_phone_number_id is None:
            raise ValueError("Missing required parameter 'business-phone-number-id'.")
        request_body_data = None
        request_body_data = {
            "code": code,
            "prefilled_message": prefilled_message,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/{api_version}/{business_phone_number_id}/message_qrdls"
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

    def get_template_by_id(self, api_version: str) -> dict[str, Any]:
        """
        Retrieves a specific WhatsApp message template by its unique identifier. Unlike `get_template_by_name`, which searches within a business account, this function directly fetches a single template resource. Note: The function signature is missing the required `template_id` parameter to build a valid URL.

        Args:
            api_version (string): api-version

        Returns:
            dict[str, Any]: Example response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Templates
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'.")
        url = f"{self.base_url}/{api_version}/<TEMPLATE_ID>"
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

    def update_template_by_id(
        self,
        api_version: str,
        category: str | None = None,
        components: list[dict[str, Any]] | None = None,
        language: str | None = None,
        name: str | None = None,
    ) -> dict[str, Any]:
        """
        Updates an existing WhatsApp message template, identified by its ID within the request URL. This function modifies the template's category, components, language, and name by submitting new data via a POST request, returning the API response upon successful completion.

        Args:
            api_version (string): api-version
            category (string): category Example: 'MARKETING'.
            components (array): components Example: "[{'format': 'TEXT', 'text': 'Fall Sale', 'type': 'HEADER'}, {'example': {'body_text': [['Mark', 'FALL25']]}, 'text': 'Hi {{1}}, our Fall Sale is on! Use promo code {{2}} Get an extra 25% off every order above $350!', 'type': 'BODY'}, {'text': 'Not interested in any of our sales? Tap Stop Promotions', 'type': 'FOOTER'}, {'buttons': [{'text': 'Stop promotions', 'type': 'QUICK_REPLY'}], 'type': 'BUTTONS'}]".
            language (string): language Example: 'en_US'.
            name (string): name Example: '2023_april_promo'.

        Returns:
            dict[str, Any]: Example response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Templates
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'.")
        request_body_data = None
        request_body_data = {
            "category": category,
            "components": components,
            "language": language,
            "name": name,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/{api_version}/<TEMPLATE_ID>"
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

    def get_message_templates(
        self, api_version: str, waba_id: str, name: str | None = None
    ) -> dict[str, Any]:
        """
        Retrieves message templates for a specific WhatsApp Business Account (WABA). It can list all templates or, if a name is provided, filter for an exact match. This differs from `get_template_by_id_default_fields`, which fetches a single template by its unique ID.

        Args:
            api_version (string): api-version
            waba_id (string): waba-id
            name (string): Filters message templates by exact name match. Example: '<TEMPLATE_NAME>'.

        Returns:
            dict[str, Any]: Example response / Example response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Templates
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'.")
        if waba_id is None:
            raise ValueError("Missing required parameter 'waba-id'.")
        url = f"{self.base_url}/{api_version}/{waba_id}/message_templates"
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

    def create_message_template(
        self,
        api_version: str,
        waba_id: str,
        category: str | None = None,
        components: list[dict[str, Any]] | None = None,
        language: str | None = None,
        name: str | None = None,
    ) -> dict[str, Any]:
        """
        Creates a new message template for a specified WhatsApp Business Account (WABA). This function sends a POST request with the template's name, language, category, and structural components, enabling the creation of standardized, reusable messages.

        Args:
            api_version (string): api-version
            waba_id (string): waba-id
            category (string): category Example: 'UTILITY'.
            components (array): components Example: "[{'example': {'header_handle': ['4::YXBwbGljYXRpb24vcGRm:ARZVv4zuogJMxmAdS3_6T4o_K4ll2806avA7rWpikisTzYPsXXUeKk0REjS-hIM1rYrizHD7rQXj951TKgUFblgd_BDWVROCwRkg9Vhjj-cHNQ:e:1681237341:634974688087057:100089620928913:ARa1ZDhwbLZM3EENeeg']}, 'format': 'DOCUMENT', 'type': 'HEADER'}, {'example': {'body_text': [['Mark', '860198-230332']]}, 'text': 'Thank you for your order, {{1}}! Your order number is {{2}}. Tap the PDF linked above to view your receipt. If you have any questions, please use the buttons below to contact support. Thanks again!', 'type': 'BODY'}, {'buttons': [{'phone_number': '16467043595', 'text': 'Call', 'type': 'PHONE_NUMBER'}, {'text': 'Contact Support', 'type': 'URL', 'url': 'https://www.examplesite.com/support'}], 'type': 'BUTTONS'}]".
            language (string): language Example: 'en_US'.
            name (string): name Example: 'order_confirmation'.

        Returns:
            dict[str, Any]: Example response / Example response / Example response / Example response / Example response / Example response / Example response / Example response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Templates, important
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'.")
        if waba_id is None:
            raise ValueError("Missing required parameter 'waba-id'.")
        request_body_data = None
        request_body_data = {
            "category": category,
            "components": components,
            "language": language,
            "name": name,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/{api_version}/{waba_id}/message_templates"
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

    def delete_message_template(
        self,
        api_version: str,
        waba_id: str,
        name: str | None = None,
        hsm_id: str | None = None,
    ) -> dict[str, Any]:
        """
        Deletes a message template from a WhatsApp Business Account. Templates can be targeted for deletion by providing either a template name, which deletes all language versions, or a specific template ID (`hsm_id`).

        Args:
            api_version (string): api-version
            waba_id (string): waba-id
            name (string): The name of the message template to delete. Example: '<TEMPLATE_NAME>'.
            hsm_id (string): Template ID Example: '<HSM_ID>'.

        Returns:
            dict[str, Any]: Example response / Example response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Templates
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'.")
        if waba_id is None:
            raise ValueError("Missing required parameter 'waba-id'.")
        url = f"{self.base_url}/{api_version}/{waba_id}/message_templates"
        query_params = {
            k: v for k, v in [("name", name), ("hsm_id", hsm_id)] if v is not None
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

    def get_subscribed_apps(self, api_version: str, waba_id: str) -> dict[str, Any]:
        """
        Retrieves a list of all applications subscribed to receive webhook notifications for a given WhatsApp Business Account (WABA). This function provides a read-only view of current webhook subscriptions, complementing the functions for subscribing and unsubscribing apps.

        Args:
            api_version (string): api-version
            waba_id (string): waba-id

        Returns:
            dict[str, Any]: Example response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Webhooks
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'.")
        if waba_id is None:
            raise ValueError("Missing required parameter 'waba-id'.")
        url = f"{self.base_url}/{api_version}/{waba_id}/subscribed_apps"
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

    def subscribe_app_to_webhooks(
        self, api_version: str, waba_id: str
    ) -> dict[str, Any]:
        """
        Subscribes an application to a specific WhatsApp Business Account's (WABA) webhooks using its ID. This enables the app to receive real-time event notifications, differentiating it from functions that list or remove subscriptions.

        Args:
            api_version (string): api-version
            waba_id (string): waba-id

        Returns:
            dict[str, Any]: Example response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Webhooks
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'.")
        if waba_id is None:
            raise ValueError("Missing required parameter 'waba-id'.")
        request_body_data = None
        url = f"{self.base_url}/{api_version}/{waba_id}/subscribed_apps"
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

    def unsubscribe_app_from_waba(
        self, api_version: str, waba_id: str
    ) -> dict[str, Any]:
        """
        Removes the webhook subscription for the calling app from a specified WhatsApp Business Account (WABA), stopping it from receiving notifications. This function complements `get_subscribed_apps` and `subscribe_app_to_waba_swebhooks` by handling the deletion of a subscription.

        Args:
            api_version (string): api-version
            waba_id (string): waba-id

        Returns:
            dict[str, Any]: Example response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Webhooks
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'.")
        if waba_id is None:
            raise ValueError("Missing required parameter 'waba-id'.")
        url = f"{self.base_url}/{api_version}/{waba_id}/subscribed_apps"
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

    def get_all_client_wabas(self, api_version: str, business_account_id: str) -> Any:
        """
        Retrieves all client WhatsApp Business Accounts (WABAs) associated with a specific business account ID. It's used by Solution Partners to list WABAs they manage for other businesses, distinguishing them from accounts they directly own (`get_all_owned_wabas`).

        Args:
            api_version (string): api-version
            business_account_id (string): business-account-id

        Returns:
            Any: API response data.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            WhatsApp Business Accounts (WABA)
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'.")
        if business_account_id is None:
            raise ValueError("Missing required parameter 'business-account-id'.")
        url = f"{self.base_url}/{api_version}/{business_account_id}/client_whatsapp_business_accounts"
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

    def get_all_owned_wabas(
        self, api_version: str, business_account_id: str
    ) -> dict[str, Any]:
        """
        Retrieves a list of all WhatsApp Business Accounts (WABAs) directly owned by a specified business account. This is distinct from `get_all_shared_wabas`, which fetches WABAs shared with clients, providing specific access to owned assets instead of associated ones.

        Args:
            api_version (string): api-version
            business_account_id (string): business-account-id

        Returns:
            dict[str, Any]: Example response

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            WhatsApp Business Accounts (WABA)
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'.")
        if business_account_id is None:
            raise ValueError("Missing required parameter 'business-account-id'.")
        url = f"{self.base_url}/{api_version}/{business_account_id}/owned_whatsapp_business_accounts"
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

    def list_tools(self):
        return [
            self.get_whatsapp_business_account,
            self.get_business_account_credit_lines,
            self.get_business_account,
            self.get_commerce_settings,
            self.update_commerce_settings,
            self.create_upload_session,
            self.upload_file_to_session,
            self.get_business_phone_number,
            self.list_waba_phone_numbers,
            self.get_qr_code_by_id,
            self.delete_qr_code_by_id,
            self.list_qr_codes,
            self.create_qr_code,
            self.get_template_by_id,
            self.update_template_by_id,
            self.get_message_templates,
            self.create_message_template,
            self.delete_message_template,
            self.get_subscribed_apps,
            self.subscribe_app_to_webhooks,
            self.unsubscribe_app_from_waba,
            self.get_all_client_wabas,
            self.get_all_owned_wabas,
        ]
