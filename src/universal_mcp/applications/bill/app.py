from typing import Any

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class BillApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="bill", integration=integration, **kwargs)
        self.base_url = "https://gateway.stage.bill.com/connect"

    def list_customer_attachments(
        self, customerId: str, max: int | None = None, page: str | None = None
    ) -> dict[str, Any]:
        """
        Get list of customer attachments

        Args:
            customerId (string): customerId
            max (integer): No description provided.
            page (string): No description provided.

        Returns:
            dict[str, Any]: Get list of customer attachments response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            attachments
        """
        if customerId is None:
            raise ValueError("Missing required parameter 'customerId'.")
        url = f"{self.base_url}/v3/attachments/customers/{customerId}"
        query_params = {
            k: v for k, v in [("max", max), ("page", page)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_customer_attachment(
        self, customerId: str, name: str, items: list[bytes]
    ) -> dict[str, Any]:
        """
        Upload customer attachment

        Args:
            customerId (string): customerId
            name (string): No description provided.

        Returns:
            dict[str, Any]: Upload customer attachment response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            attachments
        """
        if customerId is None:
            raise ValueError("Missing required parameter 'customerId'.")
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/v3/attachments/customers/{customerId}"
        query_params = {k: v for k, v in [("name", name)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/octet-stream",
        )
        return self._handle_response(response)

    def list_invoice_attachments(
        self, invoiceId: str, max: int | None = None, page: str | None = None
    ) -> dict[str, Any]:
        """
        Get list of invoice attachments

        Args:
            invoiceId (string): invoiceId
            max (integer): No description provided.
            page (string): No description provided.

        Returns:
            dict[str, Any]: Get list of invoice attachments response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            attachments
        """
        if invoiceId is None:
            raise ValueError("Missing required parameter 'invoiceId'.")
        url = f"{self.base_url}/v3/attachments/invoices/{invoiceId}"
        query_params = {
            k: v for k, v in [("max", max), ("page", page)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_invoice_attachment(
        self, invoiceId: str, name: str, items: list[bytes]
    ) -> dict[str, Any]:
        """
        Upload invoice attachment

        Args:
            invoiceId (string): invoiceId
            name (string): No description provided.

        Returns:
            dict[str, Any]: Upload invoice attachment response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            attachments
        """
        if invoiceId is None:
            raise ValueError("Missing required parameter 'invoiceId'.")
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/v3/attachments/invoices/{invoiceId}"
        query_params = {k: v for k, v in [("name", name)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/octet-stream",
        )
        return self._handle_response(response)

    def list_vendor_attachments(
        self, vendorId: str, max: int | None = None, page: str | None = None
    ) -> dict[str, Any]:
        """
        Get list of vendor attachments

        Args:
            vendorId (string): vendorId
            max (integer): No description provided.
            page (string): No description provided.

        Returns:
            dict[str, Any]: Get list of vendor attachments response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            attachments
        """
        if vendorId is None:
            raise ValueError("Missing required parameter 'vendorId'.")
        url = f"{self.base_url}/v3/attachments/vendors/{vendorId}"
        query_params = {
            k: v for k, v in [("max", max), ("page", page)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_vendor_attachment(
        self, vendorId: str, name: str, items: list[bytes]
    ) -> dict[str, Any]:
        """
        Upload vendor attachment

        Args:
            vendorId (string): vendorId
            name (string): No description provided.

        Returns:
            dict[str, Any]: Upload vendor attachment response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            attachments
        """
        if vendorId is None:
            raise ValueError("Missing required parameter 'vendorId'.")
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/v3/attachments/vendors/{vendorId}"
        query_params = {k: v for k, v in [("name", name)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/octet-stream",
        )
        return self._handle_response(response)

    def get_attachment(self, attachmentId: str) -> dict[str, Any]:
        """
        Get attachment details

        Args:
            attachmentId (string): attachmentId

        Returns:
            dict[str, Any]: Get attachment details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            attachments
        """
        if attachmentId is None:
            raise ValueError("Missing required parameter 'attachmentId'.")
        url = f"{self.base_url}/v3/attachments/{attachmentId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def list_bills(
        self,
        max: int | None = None,
        sort: str | None = None,
        filters: str | None = None,
        page: str | None = None,
    ) -> dict[str, Any]:
        """
        Get list of bills

        Args:
            max (integer): No description provided.
            sort (string): No description provided.
            filters (string): No description provided.
            page (string): No description provided.

        Returns:
            dict[str, Any]: Get list of bills response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            bills, , important
        """
        url = f"{self.base_url}/v3/bills"
        query_params = {
            k: v
            for k, v in [
                ("max", max),
                ("sort", sort),
                ("filters", filters),
                ("page", page),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_bill(
        self,
        vendorId: str,
        dueDate: str,
        billLineItems: list[dict[str, Any]],
        invoice: Any,
        description: str | None = None,
        payFromChartOfAccountId: str | None = None,
        classifications: Any | None = None,
    ) -> dict[str, Any]:
        """
        Create a bill

        Args:
            vendorId (string): BILL-generated ID of the vendor. The value begins with `009`.
            dueDate (string): Bill due date. The value is in the `yyyy-MM-dd` format.
            billLineItems (array): Bill line items information
            invoice (string): invoice
            description (string): Bill description
            payFromChartOfAccountId (string): BILL-generated ID of the chart of accounts for the bill payment. The value begins with `0ca`.
            classifications (string): classifications

        Returns:
            dict[str, Any]: Create a bill response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            bills
        """
        request_body_data = None
        request_body_data = {
            "vendorId": vendorId,
            "description": description,
            "dueDate": dueDate,
            "billLineItems": billLineItems,
            "invoice": invoice,
            "payFromChartOfAccountId": payFromChartOfAccountId,
            "classifications": classifications,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/bills"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def create_bulk_bills(self, items: list[dict[str, Any]]) -> list[Any]:
        """
        Create multiple bills

        Args:

        Returns:
            list[Any]: Create multiple bills response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            bills
        """
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/v3/bills/bulk"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_bill(self, billId: str) -> dict[str, Any]:
        """
        Get bill details

        Args:
            billId (string): billId

        Returns:
            dict[str, Any]: Get bill details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            bills, important
        """
        if billId is None:
            raise ValueError("Missing required parameter 'billId'.")
        url = f"{self.base_url}/v3/bills/{billId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def replace_bill(
        self,
        billId: str,
        vendorId: str,
        dueDate: str,
        billLineItems: list[dict[str, Any]],
        invoice: Any,
        description: str | None = None,
        payFromChartOfAccountId: str | None = None,
        classifications: Any | None = None,
    ) -> dict[str, Any]:
        """
        Replace a bill

        Args:
            billId (string): billId
            vendorId (string): BILL-generated ID of the vendor. The value begins with `009`.
            dueDate (string): Bill due date. The value is in the `yyyy-MM-dd` format.
            billLineItems (array): Bill line items information
            invoice (string): invoice
            description (string): Bill description
            payFromChartOfAccountId (string): BILL-generated ID of the chart of accounts for the bill payment. The value begins with `0ca`.
            classifications (string): classifications

        Returns:
            dict[str, Any]: Replace a bill response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            bills
        """
        if billId is None:
            raise ValueError("Missing required parameter 'billId'.")
        request_body_data = None
        request_body_data = {
            "vendorId": vendorId,
            "description": description,
            "dueDate": dueDate,
            "billLineItems": billLineItems,
            "invoice": invoice,
            "payFromChartOfAccountId": payFromChartOfAccountId,
            "classifications": classifications,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/bills/{billId}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def update_bill(
        self,
        billId: str,
        vendorId: str | None = None,
        description: str | None = None,
        dueDate: str | None = None,
        billLineItems: list[dict[str, Any]] | None = None,
        invoice: Any | None = None,
        payFromChartOfAccountId: str | None = None,
        classifications: Any | None = None,
    ) -> dict[str, Any]:
        """
        Update a bill

        Args:
            billId (string): billId
            vendorId (string): BILL-generated ID of the vendor. The value begins with `009`.
            description (string): Bill description
            dueDate (string): Bill due date. The value is in the `yyyy-MM-dd` format.
            billLineItems (array): Bill line items information
            invoice (string): invoice
            payFromChartOfAccountId (string): BILL-generated ID of the chart of accounts for the bill payment. The value begins with `0ca`.
            classifications (string): classifications

        Returns:
            dict[str, Any]: Update a bill response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            bills
        """
        if billId is None:
            raise ValueError("Missing required parameter 'billId'.")
        request_body_data = None
        request_body_data = {
            "vendorId": vendorId,
            "description": description,
            "dueDate": dueDate,
            "billLineItems": billLineItems,
            "invoice": invoice,
            "payFromChartOfAccountId": payFromChartOfAccountId,
            "classifications": classifications,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/bills/{billId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def archive_bill(self, billId: str) -> dict[str, Any]:
        """
        Archive a bill

        Args:
            billId (string): billId

        Returns:
            dict[str, Any]: Archive a bill response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            bills
        """
        if billId is None:
            raise ValueError("Missing required parameter 'billId'.")
        request_body_data = None
        url = f"{self.base_url}/v3/bills/{billId}/archive"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def restore_bill(self, billId: str) -> dict[str, Any]:
        """
        Restore an archived bill

        Args:
            billId (string): billId

        Returns:
            dict[str, Any]: Restore an archived bill response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            bills
        """
        if billId is None:
            raise ValueError("Missing required parameter 'billId'.")
        request_body_data = None
        url = f"{self.base_url}/v3/bills/{billId}/restore"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def list_classification_accounting_classes(
        self,
        max: int | None = None,
        sort: str | None = None,
        filters: str | None = None,
        page: str | None = None,
    ) -> dict[str, Any]:
        """
        Get list of accounting classes

        Args:
            max (integer): No description provided.
            sort (string): No description provided.
            filters (string): No description provided.
            page (string): No description provided.

        Returns:
            dict[str, Any]: Get list of accounting classes response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        url = f"{self.base_url}/v3/classifications/accounting-classes"
        query_params = {
            k: v
            for k, v in [
                ("max", max),
                ("sort", sort),
                ("filters", filters),
                ("page", page),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_classification_accounting_class(
        self,
        name: str | None = None,
        shortName: str | None = None,
        description: str | None = None,
        parentId: str | None = None,
    ) -> dict[str, Any]:
        """
        Create an accounting class

        Args:
            name (string): Accounting class name
            shortName (string): Accounting class short name
            description (string): Accounting class description
            parentId (string): BILL-generated ID of the parent accounting class. You can set this field if this accounting class is a child object.

        Returns:
            dict[str, Any]: Create an accounting class response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "shortName": shortName,
            "description": description,
            "parentId": parentId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/classifications/accounting-classes"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def bulk_create_classification_accounting_class(
        self, items: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """
        Create multiple accounting classes

        Args:

        Returns:
            dict[str, Any]: Create multiple accounting classes response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/v3/classifications/accounting-classes/bulk"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def bulk_update_classification_accounting_class(
        self, items: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """
        Update multiple accounting classes

        Args:

        Returns:
            dict[str, Any]: Update multiple accounting classes response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/v3/classifications/accounting-classes/bulk"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def bulk_archive_classification_accounting_class(self, ids: str) -> dict[str, Any]:
        """
        Archive multiple accounting classes

        Args:
            ids (string): No description provided.

        Returns:
            dict[str, Any]: Archive multiple accounting classes response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        url = f"{self.base_url}/v3/classifications/accounting-classes/bulk/archive"
        query_params = {k: v for k, v in [("ids", ids)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def bulk_restore_classification_accounting_class(self, ids: str) -> dict[str, Any]:
        """
        Restore multiple accounting classes

        Args:
            ids (string): No description provided.

        Returns:
            dict[str, Any]: Restore multiple accounting classes response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        url = f"{self.base_url}/v3/classifications/accounting-classes/bulk/restore"
        query_params = {k: v for k, v in [("ids", ids)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_classification_accounting_class(self, id: str) -> dict[str, Any]:
        """
        Get accounting class details

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Get accounting class details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/v3/classifications/accounting-classes/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def update_classification_accounting_class(
        self,
        id: str,
        name: str | None = None,
        shortName: str | None = None,
        description: str | None = None,
        parentId: str | None = None,
    ) -> dict[str, Any]:
        """
        Update an accounting class

        Args:
            id (string): id
            name (string): Accounting class name
            shortName (string): Accounting class short name
            description (string): Accounting class description
            parentId (string): BILL-generated ID of the parent accounting class. You can set this field if this accounting class is a child object.

        Returns:
            dict[str, Any]: Update an accounting class response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "shortName": shortName,
            "description": description,
            "parentId": parentId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/classifications/accounting-classes/{id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def archive_classification_accounting_class(self, id: str) -> dict[str, Any]:
        """
        Archive an accounting class

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Archive an accounting class response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/v3/classifications/accounting-classes/{id}/archive"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def restore_classification_accounting_class(self, id: str) -> dict[str, Any]:
        """
        Restore an archived accounting class

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Restore an accounting class response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/v3/classifications/accounting-classes/{id}/restore"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def list_classification_chart_of_accounts(
        self,
        max: int | None = None,
        sort: str | None = None,
        filters: str | None = None,
        page: str | None = None,
    ) -> dict[str, Any]:
        """
        Get list of chart of accounts

        Args:
            max (integer): No description provided.
            sort (string): No description provided.
            filters (string): No description provided.
            page (string): No description provided.

        Returns:
            dict[str, Any]: Get list of chart of accounts response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        url = f"{self.base_url}/v3/classifications/chart-of-accounts"
        query_params = {
            k: v
            for k, v in [
                ("max", max),
                ("sort", sort),
                ("filters", filters),
                ("page", page),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_classification_chart_of_accounts(
        self,
        name: str,
        description: str | None = None,
        parentId: str | None = None,
        account: Any | None = None,
    ) -> dict[str, Any]:
        """
        Create a chart of accounts

        Args:
            name (string): Chart of accounts name
            description (string): Chart of accounts description
            parentId (string): BILL-generated ID of the parent chart of accounts. You can set this field if this chart of accounts is a child object.
            account (string): account

        Returns:
            dict[str, Any]: Create a chart of accounts response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "description": description,
            "parentId": parentId,
            "account": account,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/classifications/chart-of-accounts"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def bulk_create_classification_chart_of_accounts(
        self, items: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """
        Create multiple chart of accounts

        Args:

        Returns:
            dict[str, Any]: Create multiple chart of accounts response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/v3/classifications/chart-of-accounts/bulk"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def bulk_update_classification_chart_of_accounts(
        self, items: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """
        Update multiple chart of accounts

        Args:

        Returns:
            dict[str, Any]: Update multiple chart of accounts response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/v3/classifications/chart-of-accounts/bulk"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def bulk_archive_classification_chart_of_accounts(self, ids: str) -> dict[str, Any]:
        """
        Archive mutliple chart of accounts

        Args:
            ids (string): No description provided.

        Returns:
            dict[str, Any]: Archive multiple chart of accounts response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        url = f"{self.base_url}/v3/classifications/chart-of-accounts/bulk/archive"
        query_params = {k: v for k, v in [("ids", ids)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def bulk_restore_classification_chart_of_accounts(self, ids: str) -> dict[str, Any]:
        """
        Restore multiple chart of accounts

        Args:
            ids (string): No description provided.

        Returns:
            dict[str, Any]: Restore multiple chart of accounts response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        url = f"{self.base_url}/v3/classifications/chart-of-accounts/bulk/restore"
        query_params = {k: v for k, v in [("ids", ids)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_classification_chart_of_accounts(self, id: str) -> dict[str, Any]:
        """
        Get chart of accounts details

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Get chart of accounts details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/v3/classifications/chart-of-accounts/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def update_classification_chart_of_accounts(
        self,
        id: str,
        name: str | None = None,
        description: str | None = None,
        parentId: str | None = None,
        account: Any | None = None,
    ) -> dict[str, Any]:
        """
        Update a chart of accounts

        Args:
            id (string): id
            name (string): Chart of accounts name
            description (string): Chart of accounts description
            parentId (string): BILL-generated ID of the parent chart of accounts. You can set this field if this chart of accounts is a child object.
            account (string): account

        Returns:
            dict[str, Any]: Update a chart of accounts response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "description": description,
            "parentId": parentId,
            "account": account,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/classifications/chart-of-accounts/{id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def archive_classification_chart_of_accounts(self, id: str) -> dict[str, Any]:
        """
        Archive a chart of accounts

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Archive a chart of accounts response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/v3/classifications/chart-of-accounts/{id}/archive"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def restore_classification_chart_of_accounts(self, id: str) -> dict[str, Any]:
        """
        Restore an archived chart of accounts

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Restore a chart of accounts response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/v3/classifications/chart-of-accounts/{id}/restore"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def list_classification_departments(
        self,
        max: int | None = None,
        sort: str | None = None,
        filters: str | None = None,
        page: str | None = None,
    ) -> dict[str, Any]:
        """
        Get list of departments

        Args:
            max (integer): No description provided.
            sort (string): No description provided.
            filters (string): No description provided.
            page (string): No description provided.

        Returns:
            dict[str, Any]: Get list of classification departments response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        url = f"{self.base_url}/v3/classifications/departments"
        query_params = {
            k: v
            for k, v in [
                ("max", max),
                ("sort", sort),
                ("filters", filters),
                ("page", page),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_classification_department(
        self,
        name: str,
        shortName: str | None = None,
        description: str | None = None,
        parentId: str | None = None,
    ) -> dict[str, Any]:
        """
        Create a department

        Args:
            name (string): Department name
            shortName (string): Department short name
            description (string): Department description
            parentId (string): BILL-generated ID of the parent department. You can set this field if this department is a child object.

        Returns:
            dict[str, Any]: Create a department response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "shortName": shortName,
            "description": description,
            "parentId": parentId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/classifications/departments"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def bulk_create_classification_department(
        self, items: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """
        Create multiple departments

        Args:

        Returns:
            dict[str, Any]: Create multiple departments response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/v3/classifications/departments/bulk"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def bulk_update_classification_department(
        self, items: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """
        Update multiple departments

        Args:

        Returns:
            dict[str, Any]: Update multiple departments response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/v3/classifications/departments/bulk"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def bulk_archive_classification_department(self, ids: str) -> dict[str, Any]:
        """
        Archive multiple departments

        Args:
            ids (string): No description provided.

        Returns:
            dict[str, Any]: Archive multiple departments response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        url = f"{self.base_url}/v3/classifications/departments/bulk/archive"
        query_params = {k: v for k, v in [("ids", ids)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def bulk_restore_classification_department(self, ids: str) -> dict[str, Any]:
        """
        Restore multiple departments

        Args:
            ids (string): No description provided.

        Returns:
            dict[str, Any]: Restore multiple departments response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        url = f"{self.base_url}/v3/classifications/departments/bulk/restore"
        query_params = {k: v for k, v in [("ids", ids)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_classification_department(self, id: str) -> dict[str, Any]:
        """
        Get department details

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Get department details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/v3/classifications/departments/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def update_classification_department(
        self,
        id: str,
        name: str | None = None,
        shortName: str | None = None,
        description: str | None = None,
        parentId: str | None = None,
    ) -> dict[str, Any]:
        """
        Update a department

        Args:
            id (string): id
            name (string): Department name
            shortName (string): Department short name
            description (string): Department description
            parentId (string): BILL-generated ID of the parent department. You can set this field if this department is a child object.

        Returns:
            dict[str, Any]: Update a department response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "shortName": shortName,
            "description": description,
            "parentId": parentId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/classifications/departments/{id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def archive_classification_department(self, id: str) -> dict[str, Any]:
        """
        Archive a department

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Archive a department response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/v3/classifications/departments/{id}/archive"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def restore_classification_department(self, id: str) -> dict[str, Any]:
        """
        Restore an archived department

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Restore a department response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/v3/classifications/departments/{id}/restore"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def list_classification_employees(
        self,
        max: int | None = None,
        sort: str | None = None,
        filters: str | None = None,
        page: str | None = None,
    ) -> dict[str, Any]:
        """
        Get list of employees

        Args:
            max (integer): No description provided.
            sort (string): No description provided.
            filters (string): No description provided.
            page (string): No description provided.

        Returns:
            dict[str, Any]: Get list of employees response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        url = f"{self.base_url}/v3/classifications/employees"
        query_params = {
            k: v
            for k, v in [
                ("max", max),
                ("sort", sort),
                ("filters", filters),
                ("page", page),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_classification_employee(
        self,
        firstName: str | None = None,
        lastName: str | None = None,
        shortName: str | None = None,
        parentId: str | None = None,
    ) -> dict[str, Any]:
        """
        Create an employee

        Args:
            firstName (string): Employee first name
            lastName (string): Employee last name
            shortName (string): Employee short name
            parentId (string): BILL-generated ID of the parent employee. You can set this field if this employee is a child object.

        Returns:
            dict[str, Any]: Create an employee response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        request_body_data = {
            "firstName": firstName,
            "lastName": lastName,
            "shortName": shortName,
            "parentId": parentId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/classifications/employees"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def bulk_create_classification_employee(
        self, items: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """
        Create multiple employees

        Args:

        Returns:
            dict[str, Any]: Create multiple employees response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/v3/classifications/employees/bulk"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def bulk_update_classification_employee(
        self, items: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """
        Update multiple employees

        Args:

        Returns:
            dict[str, Any]: Update multiple employees response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/v3/classifications/employees/bulk"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def bulk_archive_classification_employee(self, ids: str) -> dict[str, Any]:
        """
        Archive multiple employees

        Args:
            ids (string): No description provided.

        Returns:
            dict[str, Any]: Archive multiple employees response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        url = f"{self.base_url}/v3/classifications/employees/bulk/archive"
        query_params = {k: v for k, v in [("ids", ids)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def bulk_restore_classification_employee(self, ids: str) -> dict[str, Any]:
        """
        Restore multiple employees

        Args:
            ids (string): No description provided.

        Returns:
            dict[str, Any]: Restore multiple employees response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        url = f"{self.base_url}/v3/classifications/employees/bulk/restore"
        query_params = {k: v for k, v in [("ids", ids)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_classification_employee(self, id: str) -> dict[str, Any]:
        """
        Get employee details

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Get employee details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/v3/classifications/employees/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def update_classification_employee(
        self,
        id: str,
        firstName: str | None = None,
        lastName: str | None = None,
        shortName: str | None = None,
        parentId: str | None = None,
    ) -> dict[str, Any]:
        """
        Update an employee

        Args:
            id (string): id
            firstName (string): Employee first name
            lastName (string): Employee last name
            shortName (string): Employee short name
            parentId (string): BILL-generated ID of the parent employee. You can set this field if this employee is a child object.

        Returns:
            dict[str, Any]: Update an employee response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        request_body_data = {
            "firstName": firstName,
            "lastName": lastName,
            "shortName": shortName,
            "parentId": parentId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/classifications/employees/{id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def archive_classification_employee(self, id: str) -> dict[str, Any]:
        """
        Archive an employee

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Archive an employee response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/v3/classifications/employees/{id}/archive"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def restore_classification_employee(self, id: str) -> dict[str, Any]:
        """
        Restore an archived employee

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Restore an archived employee response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/v3/classifications/employees/{id}/restore"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def list_classification_items(
        self,
        max: int | None = None,
        sort: str | None = None,
        filters: str | None = None,
        page: str | None = None,
    ) -> dict[str, Any]:
        """
        Get list of items

        Args:
            max (integer): No description provided.
            sort (string): No description provided.
            filters (string): No description provided.
            page (string): No description provided.

        Returns:
            dict[str, Any]: Get list of items response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        url = f"{self.base_url}/v3/classifications/items"
        query_params = {
            k: v
            for k, v in [
                ("max", max),
                ("sort", sort),
                ("filters", filters),
                ("page", page),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_classification_item(
        self,
        type: Any,
        name: str,
        shortName: str | None = None,
        description: str | None = None,
        parentId: str | None = None,
        price: float | None = None,
        expenseChartOfAccountId: str | None = None,
        purchaseDescription: str | None = None,
        purchaseCost: float | None = None,
        chartOfAccountId: str | None = None,
        taxable: bool | None = None,
    ) -> dict[str, Any]:
        """
        Create an item

        Args:
            type (string): type
            name (string): Item name
            shortName (string): Item short name
            description (string): Item description
            parentId (string): BILL-generated ID of the parent item. You can set this field if this item is a child object.
            price (number): Item price
            expenseChartOfAccountId (string): BILL-generated ID of the chart of accounts for the item when it is used for bills or purchases in your accounting system. The value begins with `0ca`.
            purchaseDescription (string): Item description when it is used for bills or purchases in your accounting system
            purchaseCost (number): Item purchase cost set in your accounting system
            chartOfAccountId (string): BILL-generated ID of the chart of accounts for the item. The value begins with `0ca`.
            taxable (boolean): Set as `true` if the item is taxable

        Returns:
            dict[str, Any]: Create an item response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        request_body_data = {
            "type": type,
            "shortName": shortName,
            "name": name,
            "description": description,
            "parentId": parentId,
            "price": price,
            "expenseChartOfAccountId": expenseChartOfAccountId,
            "purchaseDescription": purchaseDescription,
            "purchaseCost": purchaseCost,
            "chartOfAccountId": chartOfAccountId,
            "taxable": taxable,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/classifications/items"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def bulk_create_classification_item(
        self, items: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """
        Create multiple items

        Args:

        Returns:
            dict[str, Any]: Create multiple items response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/v3/classifications/items/bulk"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def bulk_update_classification_item(
        self, items: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """
        Update multiple items

        Args:

        Returns:
            dict[str, Any]: Update multiple items response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/v3/classifications/items/bulk"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def bulk_archive_classification_item(self, ids: str) -> dict[str, Any]:
        """
        Archive multiple items

        Args:
            ids (string): No description provided.

        Returns:
            dict[str, Any]: Archive multiple items response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        url = f"{self.base_url}/v3/classifications/items/bulk/archive"
        query_params = {k: v for k, v in [("ids", ids)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def bulk_restore_classification_item(self, ids: str) -> dict[str, Any]:
        """
        Restore multiple items

        Args:
            ids (string): No description provided.

        Returns:
            dict[str, Any]: Restore multiple items response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        url = f"{self.base_url}/v3/classifications/items/bulk/restore"
        query_params = {k: v for k, v in [("ids", ids)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_classification_item(self, id: str) -> dict[str, Any]:
        """
        Get item details

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Get item details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/v3/classifications/items/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def update_classification_item(
        self,
        id: str,
        type: Any | None = None,
        shortName: str | None = None,
        name: str | None = None,
        description: str | None = None,
        parentId: str | None = None,
        price: float | None = None,
        expenseChartOfAccountId: str | None = None,
        purchaseDescription: str | None = None,
        purchaseCost: float | None = None,
        chartOfAccountId: str | None = None,
        taxable: bool | None = None,
    ) -> dict[str, Any]:
        """
        Update an item

        Args:
            id (string): id
            type (string): type
            shortName (string): Item short name
            name (string): Item name
            description (string): Item description
            parentId (string): BILL-generated ID of the parent item. You can set this field if this item is a child object.
            price (number): Item price
            expenseChartOfAccountId (string): BILL-generated ID of the chart of accounts for the item when it is used for bills or purchases in your accounting system. The value begins with `0ca`.
            purchaseDescription (string): Item description when it is used for bills or purchases in your accounting system
            purchaseCost (number): Item purchase cost set in your accounting system
            chartOfAccountId (string): BILL-generated ID of the chart of accounts for the item. The value begins with `0ca`.
            taxable (boolean): Set as `true` if the item is taxable

        Returns:
            dict[str, Any]: Update an item response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        request_body_data = {
            "type": type,
            "shortName": shortName,
            "name": name,
            "description": description,
            "parentId": parentId,
            "price": price,
            "expenseChartOfAccountId": expenseChartOfAccountId,
            "purchaseDescription": purchaseDescription,
            "purchaseCost": purchaseCost,
            "chartOfAccountId": chartOfAccountId,
            "taxable": taxable,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/classifications/items/{id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def archive_classification_item(self, id: str) -> dict[str, Any]:
        """
        Archive an item

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Archive an item response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/v3/classifications/items/{id}/archive"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def restore_classification_item(self, id: str) -> dict[str, Any]:
        """
        Restore an archived item

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Restore classification item response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/v3/classifications/items/{id}/restore"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def list_classification_jobs(
        self,
        max: int | None = None,
        sort: str | None = None,
        filters: str | None = None,
        page: str | None = None,
    ) -> dict[str, Any]:
        """
        Get list of jobs

        Args:
            max (integer): No description provided.
            sort (string): No description provided.
            filters (string): No description provided.
            page (string): No description provided.

        Returns:
            dict[str, Any]: Get list of jobs response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        url = f"{self.base_url}/v3/classifications/jobs"
        query_params = {
            k: v
            for k, v in [
                ("max", max),
                ("sort", sort),
                ("filters", filters),
                ("page", page),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_classification_job(
        self,
        name: str | None = None,
        shortName: str | None = None,
        description: str | None = None,
        parentId: str | None = None,
    ) -> dict[str, Any]:
        """
        Create a job

        Args:
            name (string): Job name
            shortName (string): Job short name
            description (string): Job description
            parentId (string): BILL-generated ID of the parent job. You can set this field if this job is a child object.

        Returns:
            dict[str, Any]: Create a job response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "shortName": shortName,
            "description": description,
            "parentId": parentId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/classifications/jobs"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def bulk_create_classification_job(
        self, items: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """
        Create multiple jobs

        Args:

        Returns:
            dict[str, Any]: Create multiple jobs response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/v3/classifications/jobs/bulk"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def bulk_update_classification_job(
        self, items: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """
        Update multiple jobs

        Args:

        Returns:
            dict[str, Any]: Update multiple jobs response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/v3/classifications/jobs/bulk"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def bulk_archive_classification_job(self, ids: str) -> dict[str, Any]:
        """
        Archive multiple jobs

        Args:
            ids (string): No description provided.

        Returns:
            dict[str, Any]: Archive multiple jobs response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        url = f"{self.base_url}/v3/classifications/jobs/bulk/archive"
        query_params = {k: v for k, v in [("ids", ids)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def bulk_restore_classification_job(self, ids: str) -> dict[str, Any]:
        """
        Restore multiple jobs

        Args:
            ids (string): No description provided.

        Returns:
            dict[str, Any]: Restore multiple jobs response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        url = f"{self.base_url}/v3/classifications/jobs/bulk/restore"
        query_params = {k: v for k, v in [("ids", ids)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_classification_job(self, id: str) -> dict[str, Any]:
        """
        Get job details

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Get job details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/v3/classifications/jobs/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def update_classification_job(
        self,
        id: str,
        name: str | None = None,
        shortName: str | None = None,
        description: str | None = None,
        parentId: str | None = None,
    ) -> dict[str, Any]:
        """
        Update a job

        Args:
            id (string): id
            name (string): Job name
            shortName (string): Job short name
            description (string): Job description
            parentId (string): BILL-generated ID of the parent job. You can set this field if this job is a child object.

        Returns:
            dict[str, Any]: Update a job response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "shortName": shortName,
            "description": description,
            "parentId": parentId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/classifications/jobs/{id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def archive_classification_job(self, id: str) -> dict[str, Any]:
        """
        Archive a job

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Archive a job response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/v3/classifications/jobs/{id}/archive"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def restore_classification_job(self, id: str) -> dict[str, Any]:
        """
        Restore an archived job

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Restore an archived job response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/v3/classifications/jobs/{id}/restore"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def list_classification_locations(
        self,
        max: int | None = None,
        sort: str | None = None,
        filters: str | None = None,
        page: str | None = None,
    ) -> dict[str, Any]:
        """
        Get list of locations

        Args:
            max (integer): No description provided.
            sort (string): No description provided.
            filters (string): No description provided.
            page (string): No description provided.

        Returns:
            dict[str, Any]: Get list of locations response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        url = f"{self.base_url}/v3/classifications/locations"
        query_params = {
            k: v
            for k, v in [
                ("max", max),
                ("sort", sort),
                ("filters", filters),
                ("page", page),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_classification_location(
        self,
        name: str | None = None,
        shortName: str | None = None,
        description: str | None = None,
        parentId: str | None = None,
    ) -> dict[str, Any]:
        """
        Create a location

        Args:
            name (string): Location name
            shortName (string): Location short name
            description (string): Location description
            parentId (string): BILL-generated ID of the parent location. You can set this field if this location is a child object.

        Returns:
            dict[str, Any]: Create a location response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "shortName": shortName,
            "description": description,
            "parentId": parentId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/classifications/locations"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def bulk_create_classification_location(
        self, items: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """
        Create multiple locations

        Args:

        Returns:
            dict[str, Any]: Create multiple locations response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/v3/classifications/locations/bulk"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def bulk_update_classification_location(
        self, items: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """
        Update multiple locations

        Args:

        Returns:
            dict[str, Any]: Update multiple locations response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/v3/classifications/locations/bulk"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def bulk_archive_classification_location(self, ids: str) -> dict[str, Any]:
        """
        Archive multiple locations

        Args:
            ids (string): No description provided.

        Returns:
            dict[str, Any]: Archive multiple locations response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        url = f"{self.base_url}/v3/classifications/locations/bulk/archive"
        query_params = {k: v for k, v in [("ids", ids)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def bulk_restore_classification_location(self, ids: str) -> dict[str, Any]:
        """
        Restore multiple locations

        Args:
            ids (string): No description provided.

        Returns:
            dict[str, Any]: Restore multiple locations response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        request_body_data = None
        url = f"{self.base_url}/v3/classifications/locations/bulk/restore"
        query_params = {k: v for k, v in [("ids", ids)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_classification_location(self, id: str) -> dict[str, Any]:
        """
        Get location details

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Get location details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f"{self.base_url}/v3/classifications/locations/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def update_classification_location(
        self,
        id: str,
        name: str | None = None,
        shortName: str | None = None,
        description: str | None = None,
        parentId: str | None = None,
    ) -> dict[str, Any]:
        """
        Update a location

        Args:
            id (string): id
            name (string): Location name
            shortName (string): Location short name
            description (string): Location description
            parentId (string): BILL-generated ID of the parent location. You can set this field if this location is a child object.

        Returns:
            dict[str, Any]: Update a location response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "shortName": shortName,
            "description": description,
            "parentId": parentId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/classifications/locations/{id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def archive_classification_location(self, id: str) -> dict[str, Any]:
        """
        Archive a location

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Archive a location response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/v3/classifications/locations/{id}/archive"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def restore_classification_location(self, id: str) -> dict[str, Any]:
        """
        Restore an archived location

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Restore an archived location response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            classifications
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        request_body_data = None
        url = f"{self.base_url}/v3/classifications/locations/{id}/restore"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def list_customers(
        self,
        max: int | None = None,
        sort: str | None = None,
        filters: str | None = None,
        page: str | None = None,
    ) -> dict[str, Any]:
        """
        Get list of customers

        Args:
            max (integer): No description provided.
            sort (string): No description provided.
            filters (string): No description provided.
            page (string): No description provided.

        Returns:
            dict[str, Any]: Get list of customers response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            customers
        """
        url = f"{self.base_url}/v3/customers"
        query_params = {
            k: v
            for k, v in [
                ("max", max),
                ("sort", sort),
                ("filters", filters),
                ("page", page),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_customer(
        self,
        name: str,
        email: str,
        companyName: str | None = None,
        contact: Any | None = None,
        phone: str | None = None,
        fax: str | None = None,
        description: str | None = None,
        invoiceCurrency: Any | None = None,
        accountType: Any | None = None,
        paymentTermId: str | None = None,
        accountNumber: str | None = None,
        billingAddress: Any | None = None,
        shippingAddress: Any | None = None,
    ) -> dict[str, Any]:
        """
        Create a customer

        Args:
            name (string): Customer name
            email (string): Customer email address
            companyName (string): Customer company name
            contact (string): contact
            phone (string): Customer phone number
            fax (string): Customer fax number
            description (string): Customer description
            invoiceCurrency (string): invoiceCurrency
            accountType (string): accountType
            paymentTermId (string): BILL-generated ID of the payment term. The payment term defines the number of days the customer has to pay an invoice.
            accountNumber (string): Customer account number. The number appears in customer invoices.
            billingAddress (string): billingAddress
            shippingAddress (string): shippingAddress

        Returns:
            dict[str, Any]: Create a customer response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            customers
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "companyName": companyName,
            "contact": contact,
            "email": email,
            "phone": phone,
            "fax": fax,
            "description": description,
            "invoiceCurrency": invoiceCurrency,
            "accountType": accountType,
            "paymentTermId": paymentTermId,
            "accountNumber": accountNumber,
            "billingAddress": billingAddress,
            "shippingAddress": shippingAddress,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/customers"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_customer(self, customerId: str) -> dict[str, Any]:
        """
        Get customer details

        Args:
            customerId (string): customerId

        Returns:
            dict[str, Any]: Get customer details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            customers, important
        """
        if customerId is None:
            raise ValueError("Missing required parameter 'customerId'.")
        url = f"{self.base_url}/v3/customers/{customerId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def update_customer(
        self,
        customerId: str,
        name: str | None = None,
        companyName: str | None = None,
        contact: Any | None = None,
        email: str | None = None,
        phone: str | None = None,
        fax: str | None = None,
        description: str | None = None,
        invoiceCurrency: Any | None = None,
        accountType: Any | None = None,
        paymentTermId: str | None = None,
        accountNumber: str | None = None,
        billingAddress: Any | None = None,
        shippingAddress: Any | None = None,
    ) -> dict[str, Any]:
        """
        Update a customer

        Args:
            customerId (string): customerId
            name (string): Customer name
            companyName (string): Customer company name
            contact (string): contact
            email (string): Customer email address
            phone (string): Customer phone number
            fax (string): Customer fax number
            description (string): Customer description
            invoiceCurrency (string): invoiceCurrency
            accountType (string): accountType
            paymentTermId (string): BILL-generated ID of the payment term. The payment term defines the number of days the customer has to pay an invoice.
            accountNumber (string): Customer account number. The number appears in customer invoices.
            billingAddress (string): billingAddress
            shippingAddress (string): shippingAddress

        Returns:
            dict[str, Any]: Update a customer response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            customers
        """
        if customerId is None:
            raise ValueError("Missing required parameter 'customerId'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "companyName": companyName,
            "contact": contact,
            "email": email,
            "phone": phone,
            "fax": fax,
            "description": description,
            "invoiceCurrency": invoiceCurrency,
            "accountType": accountType,
            "paymentTermId": paymentTermId,
            "accountNumber": accountNumber,
            "billingAddress": billingAddress,
            "shippingAddress": shippingAddress,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/customers/{customerId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def archive_customer(self, customerId: str) -> dict[str, Any]:
        """
        Archive a customer

        Args:
            customerId (string): customerId

        Returns:
            dict[str, Any]: Archive a customer response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            customers
        """
        if customerId is None:
            raise ValueError("Missing required parameter 'customerId'.")
        request_body_data = None
        url = f"{self.base_url}/v3/customers/{customerId}/archive"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def restore_customer(self, customerId: str) -> dict[str, Any]:
        """
        Restore an archived customer

        Args:
            customerId (string): customerId

        Returns:
            dict[str, Any]: Restore an archived customer response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            customers
        """
        if customerId is None:
            raise ValueError("Missing required parameter 'customerId'.")
        request_body_data = None
        url = f"{self.base_url}/v3/customers/{customerId}/restore"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def list_documents(
        self, billId: str, max: int | None = None, page: str | None = None
    ) -> dict[str, Any]:
        """
        Get list of documents

        Args:
            billId (string): billId
            max (integer): No description provided.
            page (string): No description provided.

        Returns:
            dict[str, Any]: Get list of documents response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            documents
        """
        if billId is None:
            raise ValueError("Missing required parameter 'billId'.")
        url = f"{self.base_url}/v3/documents/bills/{billId}"
        query_params = {
            k: v for k, v in [("max", max), ("page", page)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_bill_document(
        self, billId: str, name: str, items: list[bytes]
    ) -> dict[str, Any]:
        """
        Upload bill document

        Args:
            billId (string): billId
            name (string): No description provided.

        Returns:
            dict[str, Any]: Upload bill document response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            documents
        """
        if billId is None:
            raise ValueError("Missing required parameter 'billId'.")
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/v3/documents/bills/{billId}"
        query_params = {k: v for k, v in [("name", name)] if v is not None}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/octet-stream",
        )
        return self._handle_response(response)

    def upload_status(self, ids: str) -> list[Any]:
        """
        Get document upload status

        Args:
            ids (string): No description provided.

        Returns:
            list[Any]: Get document upload status response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            documents
        """
        url = f"{self.base_url}/v3/documents/upload-status"
        query_params = {k: v for k, v in [("ids", ids)] if v is not None}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_document(self, documentId: str) -> dict[str, Any]:
        """
        Get document details

        Args:
            documentId (string): documentId

        Returns:
            dict[str, Any]: Get document details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            documents
        """
        if documentId is None:
            raise ValueError("Missing required parameter 'documentId'.")
        url = f"{self.base_url}/v3/documents/{documentId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def list_payable_apcards(self) -> list[Any]:
        """
        Get list of AP Cards

        Returns:
            list[Any]: Get list of AP Cards response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            funding accounts
        """
        url = f"{self.base_url}/v3/funding-accounts/ap-cards"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def list_bank_accounts(
        self,
        max: int | None = None,
        sort: str | None = None,
        filters: str | None = None,
        page: str | None = None,
    ) -> dict[str, Any]:
        """
        Get list of bank accounts

        Args:
            max (integer): No description provided.
            sort (string): No description provided.
            filters (string): No description provided.
            page (string): No description provided.

        Returns:
            dict[str, Any]: Get list of bank accounts response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            funding accounts
        """
        url = f"{self.base_url}/v3/funding-accounts/banks"
        query_params = {
            k: v
            for k, v in [
                ("max", max),
                ("sort", sort),
                ("filters", filters),
                ("page", page),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_bank_account(
        self,
        nameOnAccount: str,
        type: Any,
        ownerType: Any,
        bankName: str,
        routingNumber: str | None = None,
        accountNumber: str | None = None,
        accessToAdmins: bool | None = None,
        chartOfAccountId: str | None = None,
    ) -> dict[str, Any]:
        """
        Create a bank account

        Args:
            nameOnAccount (string): Full name on bank account
            type (string): type
            ownerType (string): ownerType
            bankName (string): Bank name. Set this field as a nickname for your bank account.
            routingNumber (string): Bank routing number. This field is required.
            accountNumber (string): Bank account number. This field is required.
            accessToAdmins (boolean): Set as `true` to enable access to all users with the `ADMINISTRATOR` user role
            chartOfAccountId (string): BILL-generated ID of the chart of accounts for the bank account. The value begins with `0ca`.

        Returns:
            dict[str, Any]: Create a bank account response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            funding accounts
        """
        request_body_data = None
        request_body_data = {
            "nameOnAccount": nameOnAccount,
            "routingNumber": routingNumber,
            "accountNumber": accountNumber,
            "type": type,
            "ownerType": ownerType,
            "bankName": bankName,
            "accessToAdmins": accessToAdmins,
            "chartOfAccountId": chartOfAccountId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/funding-accounts/banks"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def list_bank_account_users(
        self,
        max: int | None = None,
        sort: str | None = None,
        filters: str | None = None,
        page: str | None = None,
        currentUser: bool | None = None,
    ) -> dict[str, Any]:
        """
        Get list of bank account users

        Args:
            max (integer): No description provided.
            sort (string): No description provided.
            filters (string): No description provided.
            page (string): No description provided.
            currentUser (boolean): No description provided.

        Returns:
            dict[str, Any]: Get list of bank account users response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            funding accounts
        """
        url = f"{self.base_url}/v3/funding-accounts/banks/users"
        query_params = {
            k: v
            for k, v in [
                ("max", max),
                ("sort", sort),
                ("filters", filters),
                ("page", page),
                ("currentUser", currentUser),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def nominate_bank_account_user(
        self, userId: str, bankAccountId: str
    ) -> dict[str, Any]:
        """
        Nominate a bank account user

        Args:
            userId (string): BILL-generated ID of the user. The value begins with `006`.
            bankAccountId (string): BILL-generated ID of the bank account. The value begins with `bac`.

        **Note**: The bank account `status` must be set as `VERIFIED`.


        Returns:
            dict[str, Any]: Nominate a bank account user response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            funding accounts
        """
        request_body_data = None
        request_body_data = {
            "userId": userId,
            "bankAccountId": bankAccountId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/funding-accounts/banks/users/nominate"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def archive_bank_account_user(self, bankAccountUserId: str) -> dict[str, Any]:
        """
        Archive a bank account user

        Args:
            bankAccountUserId (string): bankAccountUserId

        Returns:
            dict[str, Any]: Archive a bank account user response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            funding accounts
        """
        if bankAccountUserId is None:
            raise ValueError("Missing required parameter 'bankAccountUserId'.")
        request_body_data = None
        url = f"{self.base_url}/v3/funding-accounts/banks/users/{bankAccountUserId}/archive"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_bank_account(self, bankAccountId: str) -> dict[str, Any]:
        """
        Get bank account details

        Args:
            bankAccountId (string): bankAccountId

        Returns:
            dict[str, Any]: Get bank account details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            funding accounts
        """
        if bankAccountId is None:
            raise ValueError("Missing required parameter 'bankAccountId'.")
        url = f"{self.base_url}/v3/funding-accounts/banks/{bankAccountId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def update_bank_account(
        self,
        bankAccountId: str,
        nameOnAccount: str | None = None,
        ownerType: Any | None = None,
        bankName: str | None = None,
        accessToAdmins: bool | None = None,
        default: Any | None = None,
        chartOfAccountId: str | None = None,
    ) -> dict[str, Any]:
        """
        Update a bank account

        Args:
            bankAccountId (string): bankAccountId
            nameOnAccount (string): Full name on bank account
            ownerType (string): ownerType
            bankName (string): Bank name. Set this field as a nickname for your bank account.
            accessToAdmins (boolean): Set as `true` to enable access to all users with the `ADMINISTRATOR` user role
            default (string): default
            chartOfAccountId (string): BILL-generated ID of the chart of accounts for the organization bank account. The value begins with `0ca`.

        Returns:
            dict[str, Any]: Update a bank account response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            funding accounts
        """
        if bankAccountId is None:
            raise ValueError("Missing required parameter 'bankAccountId'.")
        request_body_data = None
        request_body_data = {
            "nameOnAccount": nameOnAccount,
            "ownerType": ownerType,
            "bankName": bankName,
            "accessToAdmins": accessToAdmins,
            "default": default,
            "chartOfAccountId": chartOfAccountId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/funding-accounts/banks/{bankAccountId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def archive_bank_account(self, bankAccountId: str) -> dict[str, Any]:
        """
        Archive a bank account

        Args:
            bankAccountId (string): bankAccountId

        Returns:
            dict[str, Any]: Archive a bank account response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            funding accounts
        """
        if bankAccountId is None:
            raise ValueError("Missing required parameter 'bankAccountId'.")
        request_body_data = None
        url = f"{self.base_url}/v3/funding-accounts/banks/{bankAccountId}/archive"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def verify_bank_account(
        self, bankAccountId: str, depositAmount: float
    ) -> dict[str, Any]:
        """
        Verify a bank account

        Args:
            bankAccountId (string): bankAccountId
            depositAmount (number): Verify deposit amount.

        Enter an amount between `0.01` and `0.99`. In the sandbox environment, set this field as `0.50` to complete bank account verification.

        Returns:
            dict[str, Any]: Verify a bank account response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            funding accounts
        """
        if bankAccountId is None:
            raise ValueError("Missing required parameter 'bankAccountId'.")
        request_body_data = None
        request_body_data = {
            "depositAmount": depositAmount,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/funding-accounts/banks/{bankAccountId}/verify"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def list_payable_card_accounts(self, cardUserStatus: Any) -> dict[str, Any]:
        """
        Get list of card accounts

        Args:
            cardUserStatus (string): No description provided.

        Returns:
            dict[str, Any]: Get list of card accounts response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            funding accounts
        """
        url = f"{self.base_url}/v3/funding-accounts/cards"
        query_params = {
            k: v for k, v in [("cardUserStatus", cardUserStatus)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def list_card_funding_purposes(self, vendorId: str, brand: str) -> dict[str, Any]:
        """
        Get card funding purpose

        Args:
            vendorId (string): No description provided.
            brand (string): No description provided.

        Returns:
            dict[str, Any]: Get card funding purpose response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            funding accounts
        """
        url = f"{self.base_url}/v3/funding-accounts/cards/funding-purposes"
        query_params = {
            k: v for k, v in [("vendorId", vendorId), ("brand", brand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def list_card_account_users(
        self,
        max: int | None = None,
        sort: str | None = None,
        filters: str | None = None,
        page: str | None = None,
        currentUser: bool | None = None,
    ) -> dict[str, Any]:
        """
        Get list of card account users

        Args:
            max (integer): No description provided.
            sort (string): No description provided.
            filters (string): No description provided.
            page (string): No description provided.
            currentUser (boolean): No description provided.

        Returns:
            dict[str, Any]: Get list of card account users response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            funding accounts
        """
        url = f"{self.base_url}/v3/funding-accounts/cards/users"
        query_params = {
            k: v
            for k, v in [
                ("max", max),
                ("sort", sort),
                ("filters", filters),
                ("page", page),
                ("currentUser", currentUser),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_card_account(self, cardAccountId: str) -> dict[str, Any]:
        """
        Get card account details

        Args:
            cardAccountId (string): cardAccountId

        Returns:
            dict[str, Any]: Get card account details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            funding accounts
        """
        if cardAccountId is None:
            raise ValueError("Missing required parameter 'cardAccountId'.")
        url = f"{self.base_url}/v3/funding-accounts/cards/{cardAccountId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_funding_account_permission(self) -> dict[str, Any]:
        """
        Get funding account permissions

        Returns:
            dict[str, Any]: Get funding account permissions response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            funding accounts
        """
        url = f"{self.base_url}/v3/funding-accounts/permissions"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_health_check(self) -> dict[str, Any]:
        """
        Check app health

        Returns:
            dict[str, Any]: getHealthCheck 200 response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            health
        """
        url = f"{self.base_url}/v3/health"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def list_invoices(
        self,
        max: int | None = None,
        sort: str | None = None,
        filters: str | None = None,
        page: str | None = None,
    ) -> dict[str, Any]:
        """
        Get list of invoices

        Args:
            max (integer): No description provided.
            sort (string): No description provided.
            filters (string): No description provided.
            page (string): No description provided.

        Returns:
            dict[str, Any]: Get list of invoices response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            invoices
        """
        url = f"{self.base_url}/v3/invoices"
        query_params = {
            k: v
            for k, v in [
                ("max", max),
                ("sort", sort),
                ("filters", filters),
                ("page", page),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_invoice(
        self,
        customer: Any,
        invoiceLineItems: list[dict[str, Any]],
        invoiceNumber: str | None = None,
        invoiceDate: str | None = None,
        dueDate: str | None = None,
        processingOptions: Any | None = None,
        payToChartOfAccountId: str | None = None,
        classifications: Any | None = None,
    ) -> dict[str, Any]:
        """
        Create an invoice

        Args:
            customer (string): customer
            invoiceLineItems (array): Invoice line item information
            invoiceNumber (string): User-generated invoice number. This value can be your chosen number scheme.

        If you do not set this value, `invoiceNumber` is auto-generated.
            invoiceDate (string): Invoice creation date. This value is in the `yyyy-MM-dd` format.

        If you do not set this value, `invoiceDate` is set as the date when the invoice is created.
            dueDate (string): Invoice due date. The value is in the `yyyy-MM-dd` format.

        If you do not set this value, `dueDate` is set as the date when the invoice is created.
            processingOptions (string): processingOptions
            payToChartOfAccountId (string): BILL-generated ID of the chart of accounts for the invoice payment. The value begins with `0ca`.
            classifications (string): classifications

        Returns:
            dict[str, Any]: Create an invoice response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            invoices
        """
        request_body_data = None
        request_body_data = {
            "invoiceNumber": invoiceNumber,
            "invoiceDate": invoiceDate,
            "dueDate": dueDate,
            "customer": customer,
            "invoiceLineItems": invoiceLineItems,
            "processingOptions": processingOptions,
            "payToChartOfAccountId": payToChartOfAccountId,
            "classifications": classifications,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/invoices"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def record_invoice(
        self,
        paymentDate: str,
        paymentType: Any,
        amount: float,
        invoices: list[dict[str, Any]],
        customerId: str | None = None,
        description: str | None = None,
    ) -> dict[str, Any]:
        """
        Record AR payment

        Args:
            paymentDate (string): Payment date. The value is in the `yyyy-MM-dd` format.
            paymentType (string): paymentType
            amount (number): Payment amount
            invoices (array): List of invoices being paid
            customerId (string): BILL-generated ID of the customer. The value begins with `0cu`.
            description (string): Payment description

        Returns:
            dict[str, Any]: Record AR payment response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            invoices
        """
        request_body_data = None
        request_body_data = {
            "customerId": customerId,
            "paymentDate": paymentDate,
            "paymentType": paymentType,
            "amount": amount,
            "description": description,
            "invoices": invoices,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/invoices/record-payment"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_invoice(self, invoiceId: str) -> dict[str, Any]:
        """
        Get invoice details

        Args:
            invoiceId (string): invoiceId

        Returns:
            dict[str, Any]: Get invoice details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            invoices
        """
        if invoiceId is None:
            raise ValueError("Missing required parameter 'invoiceId'.")
        url = f"{self.base_url}/v3/invoices/{invoiceId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def replace_invoice(
        self,
        invoiceId: str,
        customer: Any,
        invoiceLineItems: list[dict[str, Any]],
        invoiceNumber: str | None = None,
        invoiceDate: str | None = None,
        dueDate: str | None = None,
        processingOptions: Any | None = None,
        payToChartOfAccountId: str | None = None,
        classifications: Any | None = None,
    ) -> dict[str, Any]:
        """
        Replace an invoice

        Args:
            invoiceId (string): invoiceId
            customer (string): customer
            invoiceLineItems (array): Invoice line item information
            invoiceNumber (string): User-generated invoice number. This value can be your chosen number scheme.

        If you do not set this value, `invoiceNumber` is auto-generated.
            invoiceDate (string): Invoice creation date. This value is in the `yyyy-MM-dd` format.

        If you do not set this value, `invoiceDate` is set as the date when the invoice is created.
            dueDate (string): Invoice due date. The value is in the `yyyy-MM-dd` format.

        If you do not set this value, `dueDate` is set as the date when the invoice is created.
            processingOptions (string): processingOptions
            payToChartOfAccountId (string): BILL-generated ID of the chart of accounts for the invoice payment. The value begins with `0ca`.
            classifications (string): classifications

        Returns:
            dict[str, Any]: Replace an invoice response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            invoices
        """
        if invoiceId is None:
            raise ValueError("Missing required parameter 'invoiceId'.")
        request_body_data = None
        request_body_data = {
            "invoiceNumber": invoiceNumber,
            "invoiceDate": invoiceDate,
            "dueDate": dueDate,
            "customer": customer,
            "invoiceLineItems": invoiceLineItems,
            "processingOptions": processingOptions,
            "payToChartOfAccountId": payToChartOfAccountId,
            "classifications": classifications,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/invoices/{invoiceId}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def update_invoice(
        self,
        invoiceId: str,
        invoiceNumber: str | None = None,
        invoiceDate: str | None = None,
        dueDate: str | None = None,
        customer: Any | None = None,
        invoiceLineItems: list[dict[str, Any]] | None = None,
        processingOptions: Any | None = None,
        payToChartOfAccountId: str | None = None,
        classifications: Any | None = None,
    ) -> dict[str, Any]:
        """
        Update an invoice

        Args:
            invoiceId (string): invoiceId
            invoiceNumber (string): User-generated invoice number. This value can be your chosen number scheme.

        If you do not set this value, `invoiceNumber` is auto-generated.
            invoiceDate (string): Invoice creation date. This value is in the `yyyy-MM-dd` format.

        If you do not set this value, `invoiceDate` is set as the date when the invoice is created.
            dueDate (string): Invoice due date. The value is in the `yyyy-MM-dd` format.

        If you do not set this value, `dueDate` is set as the date when the invoice is created.
            customer (string): customer
            invoiceLineItems (array): Invoice line item information
            processingOptions (string): processingOptions
            payToChartOfAccountId (string): BILL-generated ID of the chart of accounts for the invoice payment. The value begins with `0ca`.
            classifications (string): classifications

        Returns:
            dict[str, Any]: Update an invoice response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            invoices
        """
        if invoiceId is None:
            raise ValueError("Missing required parameter 'invoiceId'.")
        request_body_data = None
        request_body_data = {
            "invoiceNumber": invoiceNumber,
            "invoiceDate": invoiceDate,
            "dueDate": dueDate,
            "customer": customer,
            "invoiceLineItems": invoiceLineItems,
            "processingOptions": processingOptions,
            "payToChartOfAccountId": payToChartOfAccountId,
            "classifications": classifications,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/invoices/{invoiceId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def archive_invoice(self, invoiceId: str) -> dict[str, Any]:
        """
        Archive an invoice

        Args:
            invoiceId (string): invoiceId

        Returns:
            dict[str, Any]: Archive an invoice response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            invoices
        """
        if invoiceId is None:
            raise ValueError("Missing required parameter 'invoiceId'.")
        request_body_data = None
        url = f"{self.base_url}/v3/invoices/{invoiceId}/archive"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def send_invoice(self, invoiceId: str, replyTo: Any, recipient: Any) -> Any:
        """
        Send an invoice

        Args:
            invoiceId (string): invoiceId
            replyTo (string): replyTo
            recipient (string): recipient

        Returns:
            Any: Send an invoice response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            invoices
        """
        if invoiceId is None:
            raise ValueError("Missing required parameter 'invoiceId'.")
        request_body_data = None
        request_body_data = {
            "replyTo": replyTo,
            "recipient": recipient,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/invoices/{invoiceId}/email"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def restore_invoice(self, invoiceId: str) -> dict[str, Any]:
        """
        Restore an archived invoice

        Args:
            invoiceId (string): invoiceId

        Returns:
            dict[str, Any]: Restore an archived invoice response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            invoices
        """
        if invoiceId is None:
            raise ValueError("Missing required parameter 'invoiceId'.")
        request_body_data = None
        url = f"{self.base_url}/v3/invoices/{invoiceId}/restore"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def login(
        self,
        devKey: str,
        username: str,
        password: str,
        organizationId: str,
        rememberMeId: str | None = None,
        device: str | None = None,
    ) -> dict[str, Any]:
        """
        API login

        Args:
            devKey (string): Developer key sent to you by BILL when you create a developer account
            username (string): Email address used to sign in to your BILL account
            password (string): Password used to sign in to your BILL account
            organizationId (string): Organization ID
            rememberMeId (string): MFA ID. Set this field for creating an MFA-trusted API session.

        This MFA ID is generated when you set `rememberMe` as `true` in your `POST /v3/mfa/challenge/validate` request. This value expires in 30 days.

        See [Validate MFA challenge](ref:validatechallenge) for more information.
            device (string): Mobile device name. This is a nickname for your mobile device. Set this field when you set `rememberMeId`.

        Returns:
            dict[str, Any]: API login response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            authentication
        """
        request_body_data = None
        request_body_data = {
            "devKey": devKey,
            "username": username,
            "password": password,
            "organizationId": organizationId,
            "rememberMeId": rememberMeId,
            "device": device,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/login"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_session_info(self) -> dict[str, Any]:
        """
        Get API session details

        Returns:
            dict[str, Any]: Get API session details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            authentication
        """
        url = f"{self.base_url}/v3/login/session"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def logout(self) -> Any:
        """
        API logout

        Returns:
            Any: API logout response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            authentication
        """
        request_body_data = None
        url = f"{self.base_url}/v3/logout"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def generate_challenge(self, useBackup: bool | None = None) -> dict[str, Any]:
        """
        Generate MFA challenge

        Args:
            useBackup (boolean): Set as `true` to generate the token with the backup device. The default value is `false`.

        Returns:
            dict[str, Any]: Generate MFA challenge response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            mfa
        """
        request_body_data = None
        request_body_data = {
            "useBackup": useBackup,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/mfa/challenge"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def validate_challenge(
        self,
        challengeId: str,
        token: str,
        device: str | None = None,
        machineName: str | None = None,
        rememberMe: bool | None = None,
    ) -> dict[str, Any]:
        """
        Validate MFA challenge

        Args:
            challengeId (string): MFA `challengeId` from the `POST /v3/mfa/challenge` response
            token (string): Validation `token` sent to the registered phone number
            device (string): Mobile device name. This is a nickname for your mobile device. Set this field when `rememberMe` is set as `true`.
            machineName (string): Machine name. This is a nickname for the machine used to complete MFA sign in. Set this field when `rememberMe` is set as `true`.
            rememberMe (boolean): Set as `true` for the generated MFA ID to expire in 30 days

        Returns:
            dict[str, Any]: Validate MFA challenge response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            mfa
        """
        request_body_data = None
        request_body_data = {
            "challengeId": challengeId,
            "token": token,
            "device": device,
            "machineName": machineName,
            "rememberMe": rememberMe,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/mfa/challenge/validate"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def list_mfa_phones(self) -> dict[str, Any]:
        """
        Get list of MFA phone numbers

        Returns:
            dict[str, Any]: Get list of MFA phone numbers response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            mfa
        """
        url = f"{self.base_url}/v3/mfa/phones"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def setup(self, phone: str, type: Any, primary: bool) -> dict[str, Any]:
        """
        Add phone for MFA setup

        Args:
            phone (string): Phone number for MFA setup. The validation `token` is sent to this number.
            type (string): type
            primary (boolean): * Set as `true` if the phone number belongs to the primary mobile device.
        * Set as `false` if the phone number belongs to the backup mobile device.

        Returns:
            dict[str, Any]: Add phone for MFA setup response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            mfa
        """
        request_body_data = None
        request_body_data = {
            "phone": phone,
            "type": type,
            "primary": primary,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/mfa/setup"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def validate(self, setupId: str, type: Any, token: str) -> dict[str, Any]:
        """
        Validate phone for MFA setup

        Args:
            setupId (string): MFA `setupId` from the `POST /v3/mfa/setup` response
            type (string): type
            token (string): Validation `token` sent to the registered phone number

        Returns:
            dict[str, Any]: Validate phone for MFA setup response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            mfa
        """
        request_body_data = None
        request_body_data = {
            "setupId": setupId,
            "type": type,
            "token": token,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/mfa/setup/validate"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def step_up_session(
        self, rememberMeId: str | None = None, device: str | None = None
    ) -> dict[str, Any]:
        """
        MFA step-up for API session

        Args:
            rememberMeId (string): MFA ID. Set this field for creating an MFA-trusted API session.

        This MFA ID is generated when you set `rememberMe` as `true` in your `POST /v3/mfa/challenge/validate` request. This value expires in 30 days.

        See [Validate MFA challenge](ref:validatechallenge) for more information.
            device (string): Mobile device name. This is a nickname for your mobile device. Set this field when you set `rememberMeId`.

        Returns:
            dict[str, Any]: MFA step-up for API session response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            mfa
        """
        request_body_data = None
        request_body_data = {
            "rememberMeId": rememberMeId,
            "device": device,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/mfa/step-up"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def search(
        self,
        name: str,
        scope: Any | None = None,
        zipOrPostalCode: str | None = None,
        accountNumber: str | None = None,
    ) -> dict[str, Any]:
        """
        Search for an organization in the BILL networks

        Args:
            name (string): No description provided.
            scope (string): No description provided.
            zipOrPostalCode (string): No description provided.
            accountNumber (string): No description provided.

        Returns:
            dict[str, Any]: Network search response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            network
        """
        url = f"{self.base_url}/v3/network"
        query_params = {
            k: v
            for k, v in [
                ("name", name),
                ("scope", scope),
                ("zipOrPostalCode", zipOrPostalCode),
                ("accountNumber", accountNumber),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def accept_invitation(
        self,
        networkId: str,
        type: Any,
        id: str | None = None,
        name: str | None = None,
    ) -> Any:
        """
        Accept network invitation

        Args:
            networkId (string): Payment Network ID (PNI) of the customer or vendor that sent the invitation. For a verified national vendor, the value begins with `0rv`. BILL uses the PNI to send and receive electronic payments.

        You can retrieve `networkId` from your `GET /v3/network` search result.
            type (string): type
            id (string): BILL-generated ID of the existing vendor or customer in your organization that you want to connect with. The value begins with `009` (vendor) or `0cu` (customer).

        When you set this field, you cannot set `name` in your request.
            name (string): Name of the new vendor or customer that you want to add in your organization. BILL creates a new vendor or customer with this name.

        When you set this field, you cannot set `id` in your request.

        Returns:
            Any: Accept network invitation response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            network
        """
        request_body_data = None
        request_body_data = {
            "networkId": networkId,
            "type": type,
            "id": id,
            "name": name,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/network/invitation/accept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_customer_invitation(self, customerId: str) -> dict[str, Any]:
        """
        Get customer invitation status

        Args:
            customerId (string): customerId

        Returns:
            dict[str, Any]: Get customer invitation status response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            network
        """
        if customerId is None:
            raise ValueError("Missing required parameter 'customerId'.")
        url = f"{self.base_url}/v3/network/invitation/customer/{customerId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_customer_invitation(
        self,
        customerId: str,
        networkId: str,
        networkType: Any,
        rppsInformation: Any | None = None,
    ) -> Any:
        """
        Invite a customer in the BILL network

        Args:
            customerId (string): customerId
            networkId (string): Payment Network ID (PNI) of the organization you want to connect with. For a verified national vendor, the value begins with `0rv`. BILL uses the PNI to send and receive electronic payments.

        You can retrieve `networkId` from your `GET /v3/network` search result.
            networkType (string): networkType
            rppsInformation (string): rppsInformation

        Returns:
            Any: Invite a customer in the BILL network response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            network
        """
        if customerId is None:
            raise ValueError("Missing required parameter 'customerId'.")
        request_body_data = None
        request_body_data = {
            "networkId": networkId,
            "networkType": networkType,
            "rppsInformation": rppsInformation,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/network/invitation/customer/{customerId}"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def delete_customer_invitation(self, customerId: str) -> Any:
        """
        Delete customer connection

        Args:
            customerId (string): customerId

        Returns:
            Any: Delete customer connection response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            network
        """
        if customerId is None:
            raise ValueError("Missing required parameter 'customerId'.")
        url = f"{self.base_url}/v3/network/invitation/customer/{customerId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def get_vendor_invitation(self, vendorId: str) -> dict[str, Any]:
        """
        Get vendor invitation status

        Args:
            vendorId (string): vendorId

        Returns:
            dict[str, Any]: Get vendor invitation status response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            network
        """
        if vendorId is None:
            raise ValueError("Missing required parameter 'vendorId'.")
        url = f"{self.base_url}/v3/network/invitation/vendor/{vendorId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_vendor_invitation(
        self,
        vendorId: str,
        networkId: str,
        networkType: Any,
        rppsInformation: Any | None = None,
    ) -> Any:
        """
        Invite a vendor in the BILL network

        Args:
            vendorId (string): vendorId
            networkId (string): Payment Network ID (PNI) of the organization you want to connect with. For a verified national vendor, the value begins with `0rv`. BILL uses the PNI to send and receive electronic payments.

        You can retrieve `networkId` from your `GET /v3/network` search result.
            networkType (string): networkType
            rppsInformation (string): rppsInformation

        Returns:
            Any: Invite a vendor in the BILL network response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            network
        """
        if vendorId is None:
            raise ValueError("Missing required parameter 'vendorId'.")
        request_body_data = None
        request_body_data = {
            "networkId": networkId,
            "networkType": networkType,
            "rppsInformation": rppsInformation,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/network/invitation/vendor/{vendorId}"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def delete_vendor_invitation(self, vendorId: str) -> Any:
        """
        Delete vendor connection

        Args:
            vendorId (string): vendorId

        Returns:
            Any: Delete vendor connection response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            network
        """
        if vendorId is None:
            raise ValueError("Missing required parameter 'vendorId'.")
        url = f"{self.base_url}/v3/network/invitation/vendor/{vendorId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def list_industries(self) -> dict[str, Any]:
        """
        Get list of organization industries

        Returns:
            dict[str, Any]: Get list of organization industries response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            organizations
        """
        url = f"{self.base_url}/v3/organizations/industries"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_organization(self, organizationId: str) -> dict[str, Any]:
        """
        Get organization details

        Args:
            organizationId (string): organizationId

        Returns:
            dict[str, Any]: Get organization details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            organizations
        """
        if organizationId is None:
            raise ValueError("Missing required parameter 'organizationId'.")
        url = f"{self.base_url}/v3/organizations/{organizationId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def update_organization(
        self,
        organizationId: str,
        name: str | None = None,
        address: Any | None = None,
        mailingAddress: Any | None = None,
        phone: str | None = None,
        companyOwner: Any | None = None,
        taxId: str | None = None,
        taxIdType: Any | None = None,
        industry: str | None = None,
        businessCategory: Any | None = None,
        accountType: Any | None = None,
        processingOptions: Any | None = None,
    ) -> dict[str, Any]:
        """
        Update an organization

        Args:
            organizationId (string): organizationId
            name (string): Organization name
            address (string): address
            mailingAddress (string): mailingAddress
            phone (string): Organization phone number
            companyOwner (string): companyOwner
            taxId (string): Organization tax ID. This value is required by the IRS for tax purposes.
            taxIdType (string): taxIdType
            industry (string): Organization industry
            businessCategory (string): businessCategory
            accountType (string): accountType
            processingOptions (string): processingOptions

        Returns:
            dict[str, Any]: Update an organization response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            organizations
        """
        if organizationId is None:
            raise ValueError("Missing required parameter 'organizationId'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "address": address,
            "mailingAddress": mailingAddress,
            "phone": phone,
            "companyOwner": companyOwner,
            "taxId": taxId,
            "taxIdType": taxIdType,
            "industry": industry,
            "businessCategory": businessCategory,
            "accountType": accountType,
            "processingOptions": processingOptions,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/organizations/{organizationId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def get_price_plan(self, organizationId: str) -> dict[str, Any]:
        """
        Get organization price plan details

        Args:
            organizationId (string): organizationId

        Returns:
            dict[str, Any]: Get organization price plan details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            organizations
        """
        if organizationId is None:
            raise ValueError("Missing required parameter 'organizationId'.")
        url = f"{self.base_url}/v3/organizations/{organizationId}/price-plan"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def partner_login(
        self, appKey: str, username: str, password: str
    ) -> dict[str, Any]:
        """
        API partner login

        Args:
            appKey (string): Application key sent to you by BILL when you create a partner account
            username (string): Email address used to sign in to your BILL account
            password (string): Password used to sign in to your BILL account

        Returns:
            dict[str, Any]: API partner login response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            partner
        """
        request_body_data = None
        request_body_data = {
            "appKey": appKey,
            "username": username,
            "password": password,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/partner/login"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def login_as_user(
        self,
        userId: str,
        organizationId: str,
        rememberMeId: str | None = None,
        device: str | None = None,
    ) -> dict[str, Any]:
        """
        API login as user

        Args:
            userId (string): BILL-generated ID of the user you want to sign in as
            organizationId (string): BILL-generated ID of the organization you want to sign in to
            rememberMeId (string): MFA ID. Set this field for creating an MFA-trusted API session.

        This MFA ID is generated when you set `rememberMe` as `true` in your `POST /v3/mfa/challenge/validate` request. This value expires in 30 days.

        See [Validate MFA challenge](ref:validatechallenge) for more information.
            device (string): Mobile device name. This is a nickname for your mobile device. Set this field when you set `rememberMeId`.

        Returns:
            dict[str, Any]: API login as user response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            partner
        """
        request_body_data = None
        request_body_data = {
            "userId": userId,
            "organizationId": organizationId,
            "rememberMeId": rememberMeId,
            "device": device,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/partner/login-as-user"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def list_partner_organizations(
        self,
        max: int | None = None,
        sort: str | None = None,
        filters: str | None = None,
        page: str | None = None,
    ) -> dict[str, Any]:
        """
        Get list of organizations

        Args:
            max (integer): No description provided.
            sort (string): No description provided.
            filters (string): No description provided.
            page (string): No description provided.

        Returns:
            dict[str, Any]: Get list of organizations response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            partner
        """
        url = f"{self.base_url}/v3/partner/organizations"
        query_params = {
            k: v
            for k, v in [
                ("max", max),
                ("sort", sort),
                ("filters", filters),
                ("page", page),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_organization(
        self,
        name: str,
        address: Any,
        mailingAddress: Any | None = None,
        phone: str | None = None,
        companyOwner: Any | None = None,
        taxId: str | None = None,
        taxIdType: Any | None = None,
        industry: str | None = None,
        businessCategory: Any | None = None,
        accountType: Any | None = None,
        processingOptions: Any | None = None,
    ) -> dict[str, Any]:
        """
        Create an organization

        Args:
            name (string): Organization name
            address (string): address
            mailingAddress (string): mailingAddress
            phone (string): Organization phone number
            companyOwner (string): companyOwner
            taxId (string): Organization tax ID. This value is required by the IRS for tax purposes.
            taxIdType (string): taxIdType
            industry (string): Organization industry
            businessCategory (string): businessCategory
            accountType (string): accountType
            processingOptions (string): processingOptions

        Returns:
            dict[str, Any]: Create an organization response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            partner
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "address": address,
            "mailingAddress": mailingAddress,
            "phone": phone,
            "companyOwner": companyOwner,
            "taxId": taxId,
            "taxIdType": taxIdType,
            "industry": industry,
            "businessCategory": businessCategory,
            "accountType": accountType,
            "processingOptions": processingOptions,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/partner/organizations"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def create_phone(self, userId: str, phoneNumber: str, phoneType: Any) -> Any:
        """
        Add phone for risk verification

        Args:
            userId (string): userId
            phoneNumber (string): Phone number
            phoneType (string): phoneType

        Returns:
            Any: Add phone for risk verification response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            partner
        """
        if userId is None:
            raise ValueError("Missing required parameter 'userId'.")
        request_body_data = None
        request_body_data = {
            "phoneNumber": phoneNumber,
            "phoneType": phoneType,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/partner/risk-verifications/{userId}/phone"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def list_partner_user_roles(
        self,
        max: int | None = None,
        sort: str | None = None,
        filters: str | None = None,
        page: str | None = None,
    ) -> dict[str, Any]:
        """
        Get list of user roles

        Args:
            max (integer): No description provided.
            sort (string): No description provided.
            filters (string): No description provided.
            page (string): No description provided.

        Returns:
            dict[str, Any]: Get list of user roles response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            partner
        """
        url = f"{self.base_url}/v3/partner/roles"
        query_params = {
            k: v
            for k, v in [
                ("max", max),
                ("sort", sort),
                ("filters", filters),
                ("page", page),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_partner_user_role(self, roleId: str) -> dict[str, Any]:
        """
        Get user role details

        Args:
            roleId (string): roleId

        Returns:
            dict[str, Any]: Get user role details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            partner
        """
        if roleId is None:
            raise ValueError("Missing required parameter 'roleId'.")
        url = f"{self.base_url}/v3/partner/roles/{roleId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def list_partner_users(
        self,
        max: int | None = None,
        sort: str | None = None,
        filters: str | None = None,
        page: str | None = None,
    ) -> dict[str, Any]:
        """
        Get list of users

        Args:
            max (integer): No description provided.
            sort (string): No description provided.
            filters (string): No description provided.
            page (string): No description provided.

        Returns:
            dict[str, Any]: Get list of users response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            partner
        """
        url = f"{self.base_url}/v3/partner/users"
        query_params = {
            k: v
            for k, v in [
                ("max", max),
                ("sort", sort),
                ("filters", filters),
                ("page", page),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_partner_user(
        self,
        firstName: str,
        email: str,
        username: str,
        acceptTermsOfService: bool,
        lastName: str | None = None,
        roleId: str | None = None,
        externalReferenceId: str | None = None,
    ) -> dict[str, Any]:
        """
        Create a user

        Args:
            firstName (string): User first name
            email (string): User email address
            username (string): Username for signing in as the user.

        Set `username` as a unique alphanumeric value. Do not set the value as an email address or any PII value.
            acceptTermsOfService (boolean): Set as `true` if the user accepts the BILL terms of service
            lastName (string): User last name
            roleId (string): BILL-generated ID of the user role. The value begins with `0po`.

        If you do not set `roleId`, the default `ADMINISTRATOR` user role is assigned to the created user. You can get the list of available user roles with `GET /v3/partner/roles`.
            externalReferenceId (string): Set the reference ID of the user in the partner system.

        Returns:
            dict[str, Any]: Create a user response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            partner
        """
        request_body_data = None
        request_body_data = {
            "firstName": firstName,
            "lastName": lastName,
            "email": email,
            "roleId": roleId,
            "username": username,
            "externalReferenceId": externalReferenceId,
            "acceptTermsOfService": acceptTermsOfService,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/partner/users"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_partner_user(self, userId: str) -> dict[str, Any]:
        """
        Get user details

        Args:
            userId (string): userId

        Returns:
            dict[str, Any]: Get user details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            partner
        """
        if userId is None:
            raise ValueError("Missing required parameter 'userId'.")
        url = f"{self.base_url}/v3/partner/users/{userId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def update_partner_user(
        self,
        userId: str,
        firstName: str | None = None,
        lastName: str | None = None,
        email: str | None = None,
        roleId: str | None = None,
    ) -> dict[str, Any]:
        """
        Update a user

        Args:
            userId (string): userId
            firstName (string): User first name
            lastName (string): User last name
            email (string): User email address
            roleId (string): BILL-generated ID of the user role. The value begins with `0po`.

        If you do not set `roleId`, the default `ADMINISTRATOR` user role is assigned to the created user. You can get the list of available user roles with `GET /v3/partner/roles`.

        Returns:
            dict[str, Any]: Update a user response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            partner
        """
        if userId is None:
            raise ValueError("Missing required parameter 'userId'.")
        request_body_data = None
        request_body_data = {
            "firstName": firstName,
            "lastName": lastName,
            "email": email,
            "roleId": roleId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/partner/users/{userId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def archive_partner_user(self, userId: str) -> dict[str, Any]:
        """
        Archive a user

        Args:
            userId (string): userId

        Returns:
            dict[str, Any]: Archive a user response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            partner
        """
        if userId is None:
            raise ValueError("Missing required parameter 'userId'.")
        request_body_data = None
        url = f"{self.base_url}/v3/partner/users/{userId}/archive"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def restore_partner_user(self, userId: str) -> dict[str, Any]:
        """
        Restore an archived user

        Args:
            userId (string): userId

        Returns:
            dict[str, Any]: Restore an archived user response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            partner
        """
        if userId is None:
            raise ValueError("Missing required parameter 'userId'.")
        request_body_data = None
        url = f"{self.base_url}/v3/partner/users/{userId}/restore"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def list_payments(
        self,
        max: int | None = None,
        sort: str | None = None,
        filters: str | None = None,
        page: str | None = None,
    ) -> dict[str, Any]:
        """
        Get list of payments

        Args:
            max (integer): No description provided.
            sort (string): No description provided.
            filters (string): No description provided.
            page (string): No description provided.

        Returns:
            dict[str, Any]: Get list of payments response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            payments
        """
        url = f"{self.base_url}/v3/payments"
        query_params = {
            k: v
            for k, v in [
                ("max", max),
                ("sort", sort),
                ("filters", filters),
                ("page", page),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_payment(
        self,
        fundingAccount: Any,
        amount: float,
        processingOptions: Any,
        vendorId: str | None = None,
        billId: str | None = None,
        description: str | None = None,
        processDate: str | None = None,
        paymentPurpose: Any | None = None,
        transactionNumber: str | None = None,
        cardFundingPurpose: str | None = None,
    ) -> dict[str, Any]:
        """
        Create a payment

        Args:
            fundingAccount (string): fundingAccount
            amount (number): Payment amount. For a payment in an international currency (not USD), this value is in the local currency.
            processingOptions (string): processingOptions
            vendorId (string): BILL-generated ID of the vendor to be paid. The value begins with `009`.
        * If `vendorId` is set, it must match your bill’s vendor ID.
        * If `vendorId` is not set, the bill’s `vendorId` is automatically set.
            billId (string): BILL-generated ID of the bill to be paid. The value begins with `00n`. If `createBill` is `true`, do not set `billId` in your payment request.
            description (string): Bill payment description. This value is included in the check memo or in the bank descriptor for electronic payments.
            processDate (string): Bill payment processing date in the `yyyy-MM-dd` format. Funds are withdrawn from the sender's funding account on this date.

        If the funding account `type` is set as `WALLET` or `AP_CARD`, `processDate` is required. For other funding account types, if `processDate` is not set, the date is automatically set as the next available payment date.
            paymentPurpose (string): paymentPurpose
            transactionNumber (string): Payment transaction reference used as an external identifier.

        You can set this field as a unique alphanumeric value for your system to track the payment transaction. The value must be 50 characters or fewer. If you do not set `transactionNumber`, BILL sets this field as a unique alphanumeric payment identification value.
            cardFundingPurpose (string): Card funding purpose. This field is required for the `CARD_ACCOUNT` funding account `type` if BILL cannot identify the vendor industry.

        See [Get card funding purpose](ref:listcardfundingpurposes) for more information.

        Returns:
            dict[str, Any]: Create a payment response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            payments
        """
        request_body_data = None
        request_body_data = {
            "vendorId": vendorId,
            "billId": billId,
            "description": description,
            "processDate": processDate,
            "fundingAccount": fundingAccount,
            "amount": amount,
            "processingOptions": processingOptions,
            "paymentPurpose": paymentPurpose,
            "transactionNumber": transactionNumber,
            "cardFundingPurpose": cardFundingPurpose,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/payments"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def create_bulk_payment(
        self,
        fundingAccount: Any,
        payments: list[dict[str, Any]],
        vendorId: str | None = None,
        description: str | None = None,
        processDate: str | None = None,
        processingOptions: Any | None = None,
        transactionNumber: str | None = None,
        cardFundingPurpose: str | None = None,
    ) -> dict[str, Any]:
        """
        Create a bulk payment

        Args:
            fundingAccount (string): fundingAccount
            payments (array): payments
            vendorId (string): BILL-generated ID of the vendor to be paid. The value begins with `009`.
        * If `vendorId` is set, it must match each bill’s vendor ID.
        * Do not set `vendorId` when you are paying multiple vendors with one request.
            description (string): Bill payment description. This value is included in the check memo or in the bank descriptor for electronic payments.
            processDate (string): Bill payment processing date in the `yyyy-MM-dd` format. Funds are withdrawn from the sender's funding account on this date.

        If the funding account `type` is set as `WALLET` or `AP_CARD`, `processDate` is required. For other funding account types, if `processDate` is not set, the date is automatically set as the next available payment date.
            processingOptions (string): processingOptions
            transactionNumber (string): Payment transaction reference used as an external identifier.

        You can set this field as a unique alphanumeric value for your system to track the payment transaction. The value must be 50 characters or fewer. If you do not set `transactionNumber`, BILL sets this field as a unique alphanumeric payment identification value.
            cardFundingPurpose (string): Card funding purpose. This field is required for the `CARD_ACCOUNT` funding account `type` if BILL cannot identify the vendor industry.

        See [Get card funding purpose](ref:listcardfundingpurposes) for more information.

        Returns:
            dict[str, Any]: Create a bulk payment response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            payments
        """
        request_body_data = None
        request_body_data = {
            "vendorId": vendorId,
            "description": description,
            "processDate": processDate,
            "fundingAccount": fundingAccount,
            "payments": payments,
            "processingOptions": processingOptions,
            "transactionNumber": transactionNumber,
            "cardFundingPurpose": cardFundingPurpose,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/payments/bulk"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def list_payment_options(self, vendorId: str, amount: float) -> dict[str, Any]:
        """
        Get list of vendor payment options

        Args:
            vendorId (string): No description provided.
            amount (number): No description provided.

        Returns:
            dict[str, Any]: Get list of vendor payment options response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            payments
        """
        url = f"{self.base_url}/v3/payments/options"
        query_params = {
            k: v
            for k, v in [("vendorId", vendorId), ("amount", amount)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_payment(self, paymentId: str) -> dict[str, Any]:
        """
        Get payment details

        Args:
            paymentId (string): paymentId

        Returns:
            dict[str, Any]: Get payment details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            payments
        """
        if paymentId is None:
            raise ValueError("Missing required parameter 'paymentId'.")
        url = f"{self.base_url}/v3/payments/{paymentId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def cancel_payment(self, paymentId: str) -> dict[str, Any]:
        """
        Cancel a payment

        Args:
            paymentId (string): paymentId

        Returns:
            dict[str, Any]: Cancel a payment response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            payments
        """
        if paymentId is None:
            raise ValueError("Missing required parameter 'paymentId'.")
        request_body_data = None
        url = f"{self.base_url}/v3/payments/{paymentId}/cancel"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_check_image_data(self, paymentId: str) -> dict[str, Any]:
        """
        Get check image data

        Args:
            paymentId (string): paymentId

        Returns:
            dict[str, Any]: Get check image data response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            payments
        """
        if paymentId is None:
            raise ValueError("Missing required parameter 'paymentId'.")
        url = f"{self.base_url}/v3/payments/{paymentId}/check-image"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def void_payment(self, paymentId: str, type: Any, reason: str) -> dict[str, Any]:
        """
        Void a payment

        Args:
            paymentId (string): paymentId
            type (string): type
            reason (string): Void payment request reason

        Returns:
            dict[str, Any]: Void a payment response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            payments
        """
        if paymentId is None:
            raise ValueError("Missing required parameter 'paymentId'.")
        request_body_data = None
        request_body_data = {
            "type": type,
            "reason": reason,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/payments/{paymentId}/void"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def list_recurring_bills(
        self,
        max: int | None = None,
        sort: str | None = None,
        filters: str | None = None,
        page: str | None = None,
    ) -> dict[str, Any]:
        """
        Get list of recurring bills

        Args:
            max (integer): No description provided.
            sort (string): No description provided.
            filters (string): No description provided.
            page (string): No description provided.

        Returns:
            dict[str, Any]: Get list of recurring bills response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            recurringbills
        """
        url = f"{self.base_url}/v3/recurringbills"
        query_params = {
            k: v
            for k, v in [
                ("max", max),
                ("sort", sort),
                ("filters", filters),
                ("page", page),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_recurring_bill(
        self,
        vendorId: str,
        schedule: Any,
        recurringBillLineItems: list[dict[str, Any]],
        description: str | None = None,
        processingOptions: Any | None = None,
        paymentInformation: Any | None = None,
    ) -> dict[str, Any]:
        """
        Create a recurring bill

        Args:
            vendorId (string): BILL-generated ID of the vendor. The value begins with `009`.
            schedule (string): schedule
            recurringBillLineItems (array): Recurring bill line item information
            description (string): User-generated invoice number. This value can be your chosen number scheme or bill due date.
            processingOptions (string): processingOptions
            paymentInformation (string): paymentInformation

        Returns:
            dict[str, Any]: Create a recurring bill response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            recurringbills
        """
        request_body_data = None
        request_body_data = {
            "vendorId": vendorId,
            "description": description,
            "schedule": schedule,
            "recurringBillLineItems": recurringBillLineItems,
            "processingOptions": processingOptions,
            "paymentInformation": paymentInformation,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/recurringbills"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_recurring_bill(self, recurringBillId: str) -> dict[str, Any]:
        """
        Get recurring bill details

        Args:
            recurringBillId (string): recurringBillId

        Returns:
            dict[str, Any]: Get recurring bill details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            recurringbills
        """
        if recurringBillId is None:
            raise ValueError("Missing required parameter 'recurringBillId'.")
        url = f"{self.base_url}/v3/recurringbills/{recurringBillId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def replace_recurring_bill(
        self,
        recurringBillId: str,
        vendorId: str,
        schedule: Any,
        recurringBillLineItems: list[dict[str, Any]],
        description: str | None = None,
        processingOptions: Any | None = None,
        paymentInformation: Any | None = None,
    ) -> dict[str, Any]:
        """
        Replace a recurring bill

        Args:
            recurringBillId (string): recurringBillId
            vendorId (string): BILL-generated ID of the vendor. The value begins with `009`.
            schedule (string): schedule
            recurringBillLineItems (array): Recurring bill line item information
            description (string): User-generated invoice number. This value can be your chosen number scheme or bill due date.
            processingOptions (string): processingOptions
            paymentInformation (string): paymentInformation

        Returns:
            dict[str, Any]: Replace a recurring bill response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            recurringbills
        """
        if recurringBillId is None:
            raise ValueError("Missing required parameter 'recurringBillId'.")
        request_body_data = None
        request_body_data = {
            "vendorId": vendorId,
            "description": description,
            "schedule": schedule,
            "recurringBillLineItems": recurringBillLineItems,
            "processingOptions": processingOptions,
            "paymentInformation": paymentInformation,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/recurringbills/{recurringBillId}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def update_recurring_bill(
        self,
        recurringBillId: str,
        vendorId: str | None = None,
        description: str | None = None,
        schedule: Any | None = None,
        recurringBillLineItems: list[dict[str, Any]] | None = None,
        processingOptions: Any | None = None,
        paymentInformation: Any | None = None,
    ) -> dict[str, Any]:
        """
        Update a recurring bill

        Args:
            recurringBillId (string): recurringBillId
            vendorId (string): BILL-generated ID of the vendor. The value begins with `009`.
            description (string): User-generated invoice number. This value can be your chosen number scheme or bill due date.
            schedule (string): schedule
            recurringBillLineItems (array): Recurring bill line item information
            processingOptions (string): processingOptions
            paymentInformation (string): paymentInformation

        Returns:
            dict[str, Any]: Update a recurring bill response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            recurringbills
        """
        if recurringBillId is None:
            raise ValueError("Missing required parameter 'recurringBillId'.")
        request_body_data = None
        request_body_data = {
            "vendorId": vendorId,
            "description": description,
            "schedule": schedule,
            "recurringBillLineItems": recurringBillLineItems,
            "processingOptions": processingOptions,
            "paymentInformation": paymentInformation,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/recurringbills/{recurringBillId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def archive_recurring_bill(self, recurringBillId: str) -> dict[str, Any]:
        """
        Archive a recurring bill

        Args:
            recurringBillId (string): recurringBillId

        Returns:
            dict[str, Any]: Archive a recurring bill response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            recurringbills
        """
        if recurringBillId is None:
            raise ValueError("Missing required parameter 'recurringBillId'.")
        request_body_data = None
        url = f"{self.base_url}/v3/recurringbills/{recurringBillId}/archive"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def restore_recurring_bill(self, recurringBillId: str) -> dict[str, Any]:
        """
        Restore an archived recurring bill

        Args:
            recurringBillId (string): recurringBillId

        Returns:
            dict[str, Any]: Restore an archived recurring bill response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            recurringbills
        """
        if recurringBillId is None:
            raise ValueError("Missing required parameter 'recurringBillId'.")
        request_body_data = None
        url = f"{self.base_url}/v3/recurringbills/{recurringBillId}/restore"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_vendor_audit_trail(
        self,
        vendorId: str,
        includeArchived: bool | None = None,
        start: int | None = None,
        max: int | None = None,
    ) -> list[Any]:
        """
        Get audit trail details for a vendor

        Args:
            vendorId (string): vendorId
            includeArchived (boolean): No description provided.
            start (integer): No description provided.
            max (integer): No description provided.

        Returns:
            list[Any]: Get audit trail details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            reports
        """
        if vendorId is None:
            raise ValueError("Missing required parameter 'vendorId'.")
        url = f"{self.base_url}/v3/reports/audit-trail/vendor/{vendorId}"
        query_params = {
            k: v
            for k, v in [
                ("includeArchived", includeArchived),
                ("start", start),
                ("max", max),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_risk_verifications(self) -> dict[str, Any]:
        """
        Get risk verification details

        Returns:
            dict[str, Any]: Get risk verification details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            risk verifications
        """
        url = f"{self.base_url}/v3/risk-verifications"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def initiate_risk_verifications(self) -> dict[str, Any]:
        """
        Initiate risk verification for an organization

        Returns:
            dict[str, Any]: Initiate risk verification for an organization response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            risk verifications
        """
        request_body_data = None
        url = f"{self.base_url}/v3/risk-verifications"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_risk_verification_phone(self) -> dict[str, Any]:
        """
        Get phone status for risk verification

        Returns:
            dict[str, Any]: Get phone status for risk verification response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            risk verifications
        """
        url = f"{self.base_url}/v3/risk-verifications/phone"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_risk_verification_phone(self, phoneNumber: str, phoneType: Any) -> Any:
        """
        Add phone for risk verification

        Args:
            phoneNumber (string): Phone number
            phoneType (string): phoneType

        Returns:
            Any: Add phone for risk verification response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            risk verifications
        """
        request_body_data = None
        request_body_data = {
            "phoneNumber": phoneNumber,
            "phoneType": phoneType,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/risk-verifications/phone"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def list_organization_user_roles(
        self,
        max: int | None = None,
        sort: str | None = None,
        filters: str | None = None,
        page: str | None = None,
    ) -> dict[str, Any]:
        """
        Get list of user roles

        Args:
            max (integer): No description provided.
            sort (string): No description provided.
            filters (string): No description provided.
            page (string): No description provided.

        Returns:
            dict[str, Any]: Get list of user roles response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            roles
        """
        url = f"{self.base_url}/v3/roles"
        query_params = {
            k: v
            for k, v in [
                ("max", max),
                ("sort", sort),
                ("filters", filters),
                ("page", page),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_organization_user_role(self, roleId: str) -> dict[str, Any]:
        """
        Get user role details

        Args:
            roleId (string): roleId

        Returns:
            dict[str, Any]: Get user role details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            roles
        """
        if roleId is None:
            raise ValueError("Missing required parameter 'roleId'.")
        url = f"{self.base_url}/v3/roles/{roleId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def list_budgets(
        self,
        nextPage: str | None = None,
        prevPage: str | None = None,
        max: int | None = None,
        sort: str | None = None,
        filters: str | None = None,
    ) -> dict[str, Any]:
        """
        Get list of budgets

        Args:
            nextPage (string): No description provided.
            prevPage (string): No description provided.
            max (integer): No description provided.
            sort (string): No description provided.
            filters (string): No description provided.

        Returns:
            dict[str, Any]: Get list of budgets response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            budgets
        """
        url = f"{self.base_url}/v3/spend/budgets"
        query_params = {
            k: v
            for k, v in [
                ("nextPage", nextPage),
                ("prevPage", prevPage),
                ("max", max),
                ("sort", sort),
                ("filters", filters),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_budget(
        self,
        name: str,
        owners: list[str],
        recurringInterval: Any,
        description: str | None = None,
        members: list[str] | None = None,
        observers: list[str] | None = None,
        expirationDate: str | None = None,
        recurMonth: int | None = None,
        timezone: str | None = None,
        autoAddUsers: bool | None = None,
        receiptRequired: bool | None = None,
        maxTxSize: float | None = None,
        carryOver: bool | None = None,
        parentBudgetId: str | None = None,
        budgetGroup: bool | None = None,
        limitlessOverspend: bool | None = None,
        limit: float | None = None,
        limitlessGoal: float | None = None,
        recurringLimit: float | None = None,
        overspendBuffer: float | None = None,
        shareFunds: Any | None = None,
    ) -> dict[str, Any]:
        """
        Create a budget

        Args:
            name (string): Budget name
            owners (array): List of user IDs that are budget owners. At least one owner must be specified.
            recurringInterval (string): recurringInterval
            description (string): Budget description
            members (array): List of user IDs that are budget members
            observers (array): List of user IDs that are budget observers
            expirationDate (string): Budget expiration date. This value is in the `yyyy-MM-dd` format. Set to null for no expiration.
            recurMonth (integer): Which month the budget will recur on, for quarterly or yearly budgets. Should be an integer in the range 1-12. Current month is assumed if not specified. Do not set for a `recurringInterval` other than `QUARTERLY` or `YEARLY`. Defaults to current month.
            timezone (string): Budget funds are reset at midnight in this timezone. Defaults to the timezone of the company's billing address.
            autoAddUsers (boolean): Set to `true` to automatically add all new users to this budget
            receiptRequired (boolean): Set to `true` if a receipt is required for transactions in the budget
            maxTxSize (number): Maximum transaction size for the budget. Any single transactions for an amount greater than this will be declined
            carryOver (boolean): When set to `true`, users and cards assigned funds under this budget will carry over from one budget period to the next
            parentBudgetId (string): BILL-generated ID of the parent budget
            budgetGroup (boolean): Set as `true` if the budget is a budget group, i.e. it can be set as the parent of other budgets
            limitlessOverspend (boolean): When set to `true`, any amount of spend over the budget limit will be allowed. Budgets with limitless overspend cannot have a recurringInterval of `DAILY` or `WEEKLY`.
            limit (number): Spend limit for the initial budget period. Must be set unless `limitlessOverspend` is true.
            limitlessGoal (number): Spend goal for a limitless budget. Do not set unless `limitlessOverspend` is true.
            recurringLimit (number): Spend limit for all future budget periods. Must be set if recurringInterval is anything other than `NONE`.
            overspendBuffer (number): Amount over budget limit to allow spending before transactions will be declined. `overspendBuffer` cannot be set for limitless budgets or budgets with a recurringInterval of `DAILY` or `WEEKLY`.
            shareFunds (string): shareFunds

        Returns:
            dict[str, Any]: Create a budget response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            budgets
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "description": description,
            "owners": owners,
            "members": members,
            "observers": observers,
            "expirationDate": expirationDate,
            "recurringInterval": recurringInterval,
            "recurMonth": recurMonth,
            "timezone": timezone,
            "autoAddUsers": autoAddUsers,
            "receiptRequired": receiptRequired,
            "maxTxSize": maxTxSize,
            "carryOver": carryOver,
            "parentBudgetId": parentBudgetId,
            "budgetGroup": budgetGroup,
            "limitlessOverspend": limitlessOverspend,
            "limit": limit,
            "limitlessGoal": limitlessGoal,
            "recurringLimit": recurringLimit,
            "overspendBuffer": overspendBuffer,
            "shareFunds": shareFunds,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/spend/budgets"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_budget(self, budgetId: str) -> dict[str, Any]:
        """
        Get budget details

        Args:
            budgetId (string): budgetId

        Returns:
            dict[str, Any]: Get budget details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            budgets
        """
        if budgetId is None:
            raise ValueError("Missing required parameter 'budgetId'.")
        url = f"{self.base_url}/v3/spend/budgets/{budgetId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def delete_budget(self, budgetId: str) -> Any:
        """
        Delete a budget

        Args:
            budgetId (string): budgetId

        Returns:
            Any: Delete a budget response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            budgets
        """
        if budgetId is None:
            raise ValueError("Missing required parameter 'budgetId'.")
        url = f"{self.base_url}/v3/spend/budgets/{budgetId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def update_budget(
        self,
        budgetId: str,
        name: str | None = None,
        description: str | None = None,
        expirationDate: str | None = None,
        recurringInterval: Any | None = None,
        recurMonth: int | None = None,
        timezone: str | None = None,
        autoAddUsers: bool | None = None,
        receiptRequired: bool | None = None,
        maxTxSize: float | None = None,
        carryOver: bool | None = None,
        limitlessOverspend: bool | None = None,
        limit: float | None = None,
        limitlessGoal: float | None = None,
        recurringLimit: float | None = None,
        overspendBuffer: float | None = None,
        shareFunds: Any | None = None,
    ) -> dict[str, Any]:
        """
        Update a budget

        Args:
            budgetId (string): budgetId
            name (string): Budget name
            description (string): Budget description
            expirationDate (string): Budget expiration date. This value is in the `yyyy-MM-dd` format. Set to null for no expiration.
            recurringInterval (string): recurringInterval
            recurMonth (integer): Which month the budget will recur on, for quarterly or yearly budgets. Should be an integer in the range 1-12. Current month is assumed if not specified. Do not set for a `recurringInterval` other than `QUARTERLY` or `YEARLY`. Defaults to current month.
            timezone (string): Budget funds are reset at midnight in this timezone. Defaults to the timezone of the company's billing address.
            autoAddUsers (boolean): Set to `true` to automatically add all new users to this budget
            receiptRequired (boolean): Set to `true` if a receipt is required for transactions in the budget
            maxTxSize (number): Maximum transaction size for the budget. Any single transactions for an amount greater than this will be declined
            carryOver (boolean): When set to `true`, users and cards assigned funds under this budget will carry over from one budget period to the next
            limitlessOverspend (boolean): When set to `true`, any amount of spend over the budget limit will be allowed. Budgets with limitless overspend cannot have a recurringInterval of `DAILY` or `WEEKLY`.
            limit (number): Spend limit for the initial budget period.
            limitlessGoal (number): Spend goal for a limitless budget. Do not set unless `limitlessOverspend` is true.
            recurringLimit (number): Spend limit for all future budget periods. Must be set if recurringInterval is anything other than `NONE`.
            overspendBuffer (number): Amount over budget limit to allow spending before transactions will be declined. `overspendBuffer` cannot be set for limitless budgets or budgets with a recurringInterval of `DAILY` or `WEEKLY`.
            shareFunds (string): shareFunds

        Returns:
            dict[str, Any]: Update a budget response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            budgets
        """
        if budgetId is None:
            raise ValueError("Missing required parameter 'budgetId'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "description": description,
            "expirationDate": expirationDate,
            "recurringInterval": recurringInterval,
            "recurMonth": recurMonth,
            "timezone": timezone,
            "autoAddUsers": autoAddUsers,
            "receiptRequired": receiptRequired,
            "maxTxSize": maxTxSize,
            "carryOver": carryOver,
            "limitlessOverspend": limitlessOverspend,
            "limit": limit,
            "limitlessGoal": limitlessGoal,
            "recurringLimit": recurringLimit,
            "overspendBuffer": overspendBuffer,
            "shareFunds": shareFunds,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/spend/budgets/{budgetId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def list_budget_members(
        self,
        budgetId: str,
        max: int | None = None,
        nextPage: str | None = None,
        prevPage: str | None = None,
        sort: str | None = None,
        filters: str | None = None,
    ) -> dict[str, Any]:
        """
        Get list of members for a budget

        Args:
            budgetId (string): budgetId
            max (integer): No description provided.
            nextPage (string): No description provided.
            prevPage (string): No description provided.
            sort (string): No description provided.
            filters (string): No description provided.

        Returns:
            dict[str, Any]: Get list of members for a budget response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            budgets
        """
        if budgetId is None:
            raise ValueError("Missing required parameter 'budgetId'.")
        url = f"{self.base_url}/v3/spend/budgets/{budgetId}/members"
        query_params = {
            k: v
            for k, v in [
                ("max", max),
                ("nextPage", nextPage),
                ("prevPage", prevPage),
                ("sort", sort),
                ("filters", filters),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def upsert_bulk_budget_users(
        self, budgetId: str, members: list[dict[str, Any]]
    ) -> Any:
        """
        Update a list of budget members in a budget

        Args:
            budgetId (string): budgetId
            members (array): List of budget member updates

        Returns:
            Any: Update a list of budget members in a budget.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            budgets
        """
        if budgetId is None:
            raise ValueError("Missing required parameter 'budgetId'.")
        request_body_data = None
        request_body_data = {
            "members": members,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/spend/budgets/{budgetId}/members/bulk"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_budget_member(self, budgetId: str, userId: str) -> dict[str, Any]:
        """
        Get a single member for a budget

        Args:
            budgetId (string): budgetId
            userId (string): userId

        Returns:
            dict[str, Any]: Get a single member for a budget response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            budgets
        """
        if budgetId is None:
            raise ValueError("Missing required parameter 'budgetId'.")
        if userId is None:
            raise ValueError("Missing required parameter 'userId'.")
        url = f"{self.base_url}/v3/spend/budgets/{budgetId}/members/{userId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def upsert_budget_member(
        self,
        budgetId: str,
        userId: str,
        limit: float | None = None,
        recurringLimit: float | None = None,
        role: Any | None = None,
        shareBudgetFunds: bool | None = None,
    ) -> dict[str, Any]:
        """
        Add a member to a budget or update an existing member of the budget

        Args:
            budgetId (string): budgetId
            userId (string): userId
            limit (number): Funds assigned to the user during the current budget period. If shareBudgetFunds is false, limit must be set.
            recurringLimit (number): Funds assigned to the user in all future budget periods. If shareBudgetFunds is false, recurringLimit must be set.
            role (string): role
            shareBudgetFunds (boolean): Share all budget funds with the user. When set to `true`, limit and recurringLimit must be null.

        Returns:
            dict[str, Any]: Add a member to a budget or update an existing member of the budget

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            budgets
        """
        if budgetId is None:
            raise ValueError("Missing required parameter 'budgetId'.")
        if userId is None:
            raise ValueError("Missing required parameter 'userId'.")
        request_body_data = None
        request_body_data = {
            "limit": limit,
            "recurringLimit": recurringLimit,
            "role": role,
            "shareBudgetFunds": shareBudgetFunds,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/spend/budgets/{budgetId}/members/{userId}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def delete_budget_member(self, budgetId: str, userId: str) -> Any:
        """
        Delete a member from a budget

        Args:
            budgetId (string): budgetId
            userId (string): userId

        Returns:
            Any: Delete a member from a budget response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            budgets
        """
        if budgetId is None:
            raise ValueError("Missing required parameter 'budgetId'.")
        if userId is None:
            raise ValueError("Missing required parameter 'userId'.")
        url = f"{self.base_url}/v3/spend/budgets/{budgetId}/members/{userId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def list_cards(
        self,
        nextPage: str | None = None,
        prevPage: str | None = None,
        max: int | None = None,
        sort: str | None = None,
        filters: str | None = None,
    ) -> dict[str, Any]:
        """
        Get list of cards

        Args:
            nextPage (string): No description provided.
            prevPage (string): No description provided.
            max (integer): No description provided.
            sort (string): No description provided.
            filters (string): No description provided.

        Returns:
            dict[str, Any]: Get list of cards response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            cards
        """
        url = f"{self.base_url}/v3/spend/cards"
        query_params = {
            k: v
            for k, v in [
                ("nextPage", nextPage),
                ("prevPage", prevPage),
                ("max", max),
                ("sort", sort),
                ("filters", filters),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_budget_card(
        self,
        name: str,
        userId: str,
        budgetId: str,
        limit: float | None = None,
        recurringLimit: float | None = None,
        expirationDate: str | None = None,
        shareBudgetFunds: bool | None = None,
    ) -> dict[str, Any]:
        """
        Create a vendor card

        Args:
            name (string): Card name
            userId (string): BILL-generated ID of the user linked with the card
            budgetId (string): BILL-generated ID of the budget linked with the card
            limit (number): Budget amount of funds added to the card
            recurringLimit (number): Recurring budget amount added to the card each month
            expirationDate (string): Card expiration date. The value is in the `yyyy-MM-dd` format.
            shareBudgetFunds (boolean): Set as `true` if the user can spend from unallocated budget funds when the allocation is empty

        Returns:
            dict[str, Any]: Create a vendor card response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            cards
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "userId": userId,
            "budgetId": budgetId,
            "limit": limit,
            "recurringLimit": recurringLimit,
            "expirationDate": expirationDate,
            "shareBudgetFunds": shareBudgetFunds,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/spend/cards"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_card(self, cardId: str) -> dict[str, Any]:
        """
        Get card details

        Args:
            cardId (string): cardId

        Returns:
            dict[str, Any]: Get card details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            cards
        """
        if cardId is None:
            raise ValueError("Missing required parameter 'cardId'.")
        url = f"{self.base_url}/v3/spend/cards/{cardId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def delete_card(self, cardId: str, reason: Any | None = None) -> Any:
        """
        Delete a card

        Args:
            cardId (string): cardId
            reason (string): No description provided.

        Returns:
            Any: Delete a card response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            cards
        """
        if cardId is None:
            raise ValueError("Missing required parameter 'cardId'.")
        url = f"{self.base_url}/v3/spend/cards/{cardId}"
        query_params = {k: v for k, v in [("reason", reason)] if v is not None}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def update_card(
        self,
        cardId: str,
        name: str | None = None,
        budgetId: str | None = None,
        limit: float | None = None,
        recurringLimit: float | None = None,
        expirationDate: str | None = None,
        shareBudgetFunds: bool | None = None,
        recurring: bool | None = None,
    ) -> dict[str, Any]:
        """
        Update a vendor card

        Args:
            cardId (string): cardId
            name (string): Card name
            budgetId (string): BILL-generated ID of the budget linked with the card
            limit (number): Budget amount of funds added to the card
            recurringLimit (number): Recurring budget amount added to the card each month
            expirationDate (string): Card expiration date. The value is in the `yyyy-MM-dd` format. Set to null to remove the card's expiration date.
            shareBudgetFunds (boolean): Set as `true` to allow the card to use all available budget funds. If set to `true`, `limit` and `recurringLimit` may not be set.
            recurring (boolean): Set as `true` to set card as `RECURRING`, Set as `false` to set card as `ONE_TIME`, or leave blank to have the card retain type.

        Returns:
            dict[str, Any]: Update a vendor card response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            cards
        """
        if cardId is None:
            raise ValueError("Missing required parameter 'cardId'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "budgetId": budgetId,
            "limit": limit,
            "recurringLimit": recurringLimit,
            "expirationDate": expirationDate,
            "shareBudgetFunds": shareBudgetFunds,
            "recurring": recurring,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/spend/cards/{cardId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def get_pan_jwt(self, cardId: str) -> dict[str, Any]:
        """
        Get PAN JWT

        Args:
            cardId (string): cardId

        Returns:
            dict[str, Any]: Get PAN JWT response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            cards
        """
        if cardId is None:
            raise ValueError("Missing required parameter 'cardId'.")
        url = f"{self.base_url}/v3/spend/cards/{cardId}/pan-jwt"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def list_custom_fields(
        self,
        max: int | None = None,
        nextPage: str | None = None,
        prevPage: str | None = None,
        sort: str | None = None,
        filters: str | None = None,
    ) -> dict[str, Any]:
        """
        Get list of custom fields

        Args:
            max (integer): No description provided.
            nextPage (string): No description provided.
            prevPage (string): No description provided.
            sort (string): No description provided.
            filters (string): No description provided.

        Returns:
            dict[str, Any]: Get list of custom fields response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            custom-fields
        """
        url = f"{self.base_url}/v3/spend/custom-fields"
        query_params = {
            k: v
            for k, v in [
                ("max", max),
                ("nextPage", nextPage),
                ("prevPage", prevPage),
                ("sort", sort),
                ("filters", filters),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_custom_field(
        self,
        name: str,
        allowCustomValues: bool,
        required: bool,
        global_: bool,
        description: str | None = None,
        multiSelect: bool | None = None,
        minimumAmountForRequirement: float | None = None,
        values: list[str] | None = None,
        selectedBudgetIds: list[str] | None = None,
        requiredBudgetIds: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Create custom field

        Args:
            name (string): Name of the custom field.
            allowCustomValues (boolean): Set to `true` if the custom field should allow custom values.
            required (boolean): Set to `true` if the custom field is required. Defaults to false.
            global_ (boolean): Set to `true` if the custom field is global, i.e. it applies to all budgets. Defaults to false.
            description (string): Description of the custom field.
            multiSelect (boolean): Set to `true` to allow multiple values to be selected for this custom field.
            minimumAmountForRequirement (number): Minimum transaction amount this custom field will be required for.
            values (array): Initial set of values for the custom field.
            selectedBudgetIds (array): Budget IDs to have the new custom field assigned to it but not be required.
            requiredBudgetIds (array): Budget IDs that will require the new custom field to be required.

        Returns:
            dict[str, Any]: The newly created custom field

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            custom-fields
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "description": description,
            "multiSelect": multiSelect,
            "allowCustomValues": allowCustomValues,
            "minimumAmountForRequirement": minimumAmountForRequirement,
            "required": required,
            "global": global_,
            "values": values,
            "selectedBudgetIds": selectedBudgetIds,
            "requiredBudgetIds": requiredBudgetIds,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/spend/custom-fields"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_custom_field(self, customFieldId: str) -> dict[str, Any]:
        """
        Get custom field details

        Args:
            customFieldId (string): customFieldId

        Returns:
            dict[str, Any]: Get custom field response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            custom-fields
        """
        if customFieldId is None:
            raise ValueError("Missing required parameter 'customFieldId'.")
        url = f"{self.base_url}/v3/spend/custom-fields/{customFieldId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def delete_custom_field(self, customFieldId: str) -> Any:
        """
        Delete a custom field

        Args:
            customFieldId (string): customFieldId

        Returns:
            Any: Delete custom field

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            custom-fields
        """
        if customFieldId is None:
            raise ValueError("Missing required parameter 'customFieldId'.")
        url = f"{self.base_url}/v3/spend/custom-fields/{customFieldId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def update_custom_field(
        self,
        customFieldId: str,
        name: str | None = None,
        description: str | None = None,
        allowCustomValues: bool | None = None,
        minimumAmountForRequirement: float | None = None,
        required: bool | None = None,
        global_: bool | None = None,
        selectedBudgetIds: list[str] | None = None,
        requiredBudgetIds: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Update custom field details

        Args:
            customFieldId (string): customFieldId
            name (string): Custom field name.
            description (string): Custom field description.
            allowCustomValues (boolean): Set as `true` if the custom field should allow custom values.
            minimumAmountForRequirement (number): Minimum transaction amount to make custom field required.
            required (boolean): Set as `true` if the custom field is required.
            global_ (boolean): Set to `true` if the custom field is global, i.e. it applies to all budgets.
            selectedBudgetIds (array): Budget IDs to have the new custom field assigned to it but not be required.
            requiredBudgetIds (array): Budget IDs that will require the new custom field to be required.

        Returns:
            dict[str, Any]: Update custom field response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            custom-fields
        """
        if customFieldId is None:
            raise ValueError("Missing required parameter 'customFieldId'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "description": description,
            "allowCustomValues": allowCustomValues,
            "minimumAmountForRequirement": minimumAmountForRequirement,
            "required": required,
            "global": global_,
            "selectedBudgetIds": selectedBudgetIds,
            "requiredBudgetIds": requiredBudgetIds,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/spend/custom-fields/{customFieldId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def list_custom_field_values(
        self,
        customFieldId: str,
        max: int | None = None,
        nextPage: str | None = None,
        prevPage: str | None = None,
        filters: str | None = None,
    ) -> dict[str, Any]:
        """
        Get list of values for custom field

        Args:
            customFieldId (string): customFieldId
            max (integer): No description provided.
            nextPage (string): No description provided.
            prevPage (string): No description provided.
            filters (string): No description provided.

        Returns:
            dict[str, Any]: Get list of values for custom fields response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            custom-fields
        """
        if customFieldId is None:
            raise ValueError("Missing required parameter 'customFieldId'.")
        url = f"{self.base_url}/v3/spend/custom-fields/{customFieldId}/values"
        query_params = {
            k: v
            for k, v in [
                ("max", max),
                ("nextPage", nextPage),
                ("prevPage", prevPage),
                ("filters", filters),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_custom_field_values(
        self, customFieldId: str, values: list[str]
    ) -> dict[str, Any]:
        """
        Create custom field values

        Args:
            customFieldId (string): customFieldId
            values (array): Values for the custom field.

        Returns:
            dict[str, Any]: The newly created custom field values

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            custom-fields
        """
        if customFieldId is None:
            raise ValueError("Missing required parameter 'customFieldId'.")
        request_body_data = None
        request_body_data = {
            "values": values,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/spend/custom-fields/{customFieldId}/values"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def delete_custom_field_value(self, customFieldId: str) -> Any:
        """
        Delete custom field values

        Args:
            customFieldId (string): customFieldId

        Returns:
            Any: Delete custom field values

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            custom-fields
        """
        if customFieldId is None:
            raise ValueError("Missing required parameter 'customFieldId'.")
        url = f"{self.base_url}/v3/spend/custom-fields/{customFieldId}/values"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def get_custom_field_values(
        self, customFieldId: str, customFieldValueId: str
    ) -> dict[str, Any]:
        """
        Get custom field value

        Args:
            customFieldId (string): customFieldId
            customFieldValueId (string): customFieldValueId

        Returns:
            dict[str, Any]: Get custom field values response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            custom-fields
        """
        if customFieldId is None:
            raise ValueError("Missing required parameter 'customFieldId'.")
        if customFieldValueId is None:
            raise ValueError("Missing required parameter 'customFieldValueId'.")
        url = f"{self.base_url}/v3/spend/custom-fields/{customFieldId}/values/{customFieldValueId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def list_reimbursements(
        self,
        nextPage: str | None = None,
        prevPage: str | None = None,
        max: int | None = None,
        sort: str | None = None,
        filters: str | None = None,
    ) -> dict[str, Any]:
        """
        Get list of reimbursements

        Args:
            nextPage (string): No description provided.
            prevPage (string): No description provided.
            max (integer): No description provided.
            sort (string): No description provided.
            filters (string): No description provided.

        Returns:
            dict[str, Any]: Get list of reimbursements response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            reimbursements
        """
        url = f"{self.base_url}/v3/spend/reimbursements"
        query_params = {
            k: v
            for k, v in [
                ("nextPage", nextPage),
                ("prevPage", prevPage),
                ("max", max),
                ("sort", sort),
                ("filters", filters),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_reimbursement(
        self,
        userId: str,
        budgetId: str,
        amount: float,
        note: str,
        merchantName: str,
        occurredDate: str,
        receipts: list[dict[str, Any]],
        customFields: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """
        Create a reimbursement

        Args:
            userId (string): BILL-generated ID of the user to be reimbursed
            budgetId (string): BILL-generated ID of the budget that the funds for this reimbursement will come from
            amount (number): Amount to be reimbursed to the user
            note (string): Note provided by the submitter that describes the business purpose for the expense
            merchantName (string): Name of the merchant for the transaction that this reimbursement is for
            occurredDate (string): Date when the user made the purchase. The value is in the `yyyy-MM-dd` format.
            receipts (array): List of receipts associated with the reimbursement
            customFields (array): List of custom fields and selected values for the reimbursement

        Returns:
            dict[str, Any]: Create a reimbursement response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            reimbursements
        """
        request_body_data = None
        request_body_data = {
            "userId": userId,
            "budgetId": budgetId,
            "amount": amount,
            "note": note,
            "merchantName": merchantName,
            "occurredDate": occurredDate,
            "receipts": receipts,
            "customFields": customFields,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/spend/reimbursements"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def create_image_upload_url(self) -> dict[str, Any]:
        """
        Create an image upload URL for a reimbursement.

        Returns:
            dict[str, Any]: Create reimbursement image upload URL response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            reimbursements
        """
        request_body_data = None
        url = f"{self.base_url}/v3/spend/reimbursements/image-upload-url"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_reimbursement(self, reimbursementId: str) -> dict[str, Any]:
        """
        Get reimbursement details

        Args:
            reimbursementId (string): reimbursementId

        Returns:
            dict[str, Any]: Get reimbursement details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            reimbursements
        """
        if reimbursementId is None:
            raise ValueError("Missing required parameter 'reimbursementId'.")
        url = f"{self.base_url}/v3/spend/reimbursements/{reimbursementId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def delete_reimbursement(self, reimbursementId: str) -> Any:
        """
        Delete a reimbursement

        Args:
            reimbursementId (string): reimbursementId

        Returns:
            Any: Reimbursement deleted successfully

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            reimbursements
        """
        if reimbursementId is None:
            raise ValueError("Missing required parameter 'reimbursementId'.")
        url = f"{self.base_url}/v3/spend/reimbursements/{reimbursementId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def update_reimbursement(
        self,
        reimbursementId: str,
        userId: str | None = None,
        budgetId: str | None = None,
        amount: float | None = None,
        note: str | None = None,
        merchantName: str | None = None,
        occurredDate: str | None = None,
        receipts: list[dict[str, Any]] | None = None,
        customFields: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """
        Update a reimbursement

        Args:
            reimbursementId (string): reimbursementId
            userId (string): BILL-generated ID of the user to be reimbursed
            budgetId (string): BILL-generated ID of the budget that the funds for this reimbursement will come from
            amount (number): Amount to be reimbursed to the user
            note (string): Note provided by the submitter that describes the business purpose for the expense
            merchantName (string): Name of the merchant for the transaction that this reimbursement is for
            occurredDate (string): Date when the user made the purchase. The value is in the `yyyy-MM-dd` format.
            receipts (array): Replace the list of receipts associated with the reimbursement
            customFields (array): List of custom fields and selected values for the reimbursement

        Returns:
            dict[str, Any]: Update a reimbursement response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            reimbursements
        """
        if reimbursementId is None:
            raise ValueError("Missing required parameter 'reimbursementId'.")
        request_body_data = None
        request_body_data = {
            "userId": userId,
            "budgetId": budgetId,
            "amount": amount,
            "note": note,
            "merchantName": merchantName,
            "occurredDate": occurredDate,
            "receipts": receipts,
            "customFields": customFields,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/spend/reimbursements/{reimbursementId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def approve_or_deny_reimbursement(
        self, reimbursementId: str, action: Any, note: str | None = None
    ) -> dict[str, Any]:
        """
        Approve or deny a reimbursement

        Args:
            reimbursementId (string): reimbursementId
            action (string): action
            note (string): Optional note for the action taken

        Returns:
            dict[str, Any]: Successfully processed reimbursement action

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            reimbursements
        """
        if reimbursementId is None:
            raise ValueError("Missing required parameter 'reimbursementId'.")
        request_body_data = None
        request_body_data = {
            "action": action,
            "note": note,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/spend/reimbursements/{reimbursementId}/action"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def list_transactions(
        self,
        max: int | None = None,
        nextPage: str | None = None,
        prevPage: str | None = None,
        sort: str | None = None,
        filters: str | None = None,
        showCustomFieldIds: str | None = None,
    ) -> dict[str, Any]:
        """
        Get list of transactions

        Args:
            max (integer): No description provided.
            nextPage (string): No description provided.
            prevPage (string): No description provided.
            sort (string): No description provided.
            filters (string): No description provided.
            showCustomFieldIds (string): No description provided.

        Returns:
            dict[str, Any]: Get list of transactions response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            transactions
        """
        url = f"{self.base_url}/v3/spend/transactions"
        query_params = {
            k: v
            for k, v in [
                ("max", max),
                ("nextPage", nextPage),
                ("prevPage", prevPage),
                ("sort", sort),
                ("filters", filters),
                ("showCustomFieldIds", showCustomFieldIds),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_transaction(
        self, transactionId: str, showCustomFieldIds: str | None = None
    ) -> dict[str, Any]:
        """
        Get transaction details

        Args:
            transactionId (string): transactionId
            showCustomFieldIds (string): No description provided.

        Returns:
            dict[str, Any]: Get transaction details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            transactions
        """
        if transactionId is None:
            raise ValueError("Missing required parameter 'transactionId'.")
        url = f"{self.base_url}/v3/spend/transactions/{transactionId}"
        query_params = {
            k: v
            for k, v in [("showCustomFieldIds", showCustomFieldIds)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def update_transaction(self, transactionId: str, budgetId: str) -> dict[str, Any]:
        """
        Update transaction

        Args:
            transactionId (string): transactionId
            budgetId (string): BILL-generated ID of the budget to assign this transaction to

        Returns:
            dict[str, Any]: Update transaction response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            transactions
        """
        if transactionId is None:
            raise ValueError("Missing required parameter 'transactionId'.")
        request_body_data = None
        request_body_data = {
            "budgetId": budgetId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/spend/transactions/{transactionId}"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def list_transaction_custom_fields(
        self, transactionId: str, filters: str | None = None
    ) -> dict[str, Any]:
        """
        Get transaction custom field details

        Args:
            transactionId (string): transactionId
            filters (string): No description provided.

        Returns:
            dict[str, Any]: Get transaction custom field details

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            transactions
        """
        if transactionId is None:
            raise ValueError("Missing required parameter 'transactionId'.")
        url = f"{self.base_url}/v3/spend/transactions/{transactionId}/custom-fields"
        query_params = {k: v for k, v in [("filters", filters)] if v is not None}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def update_transaction_custom_fields(
        self, transactionId: str, customFields: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """
        Update a custom field and values on a transaction

        Args:
            transactionId (string): transactionId
            customFields (array): List of updates to perform on the custom fields and values

        Returns:
            dict[str, Any]: Update a custom field and values on a transaction response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            transactions
        """
        if transactionId is None:
            raise ValueError("Missing required parameter 'transactionId'.")
        request_body_data = None
        request_body_data = {
            "customFields": customFields,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/spend/transactions/{transactionId}/custom-fields"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def list_transaction_custom_field_values(
        self,
        transactionId: str,
        customFieldId: str,
        max: int | None = None,
        nextPage: str | None = None,
        prevPage: str | None = None,
    ) -> dict[str, Any]:
        """
        Get transaction custom field value details

        Args:
            transactionId (string): transactionId
            customFieldId (string): customFieldId
            max (integer): No description provided.
            nextPage (string): No description provided.
            prevPage (string): No description provided.

        Returns:
            dict[str, Any]: Get transaction custom field value response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            transactions
        """
        if transactionId is None:
            raise ValueError("Missing required parameter 'transactionId'.")
        if customFieldId is None:
            raise ValueError("Missing required parameter 'customFieldId'.")
        url = f"{self.base_url}/v3/spend/transactions/{transactionId}/custom-fields/{customFieldId}/values"
        query_params = {
            k: v
            for k, v in [("max", max), ("nextPage", nextPage), ("prevPage", prevPage)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def list_users(
        self,
        nextPage: str | None = None,
        prevPage: str | None = None,
        max: int | None = None,
        filters: str | None = None,
    ) -> dict[str, Any]:
        """
        Get list of users

        Args:
            nextPage (string): No description provided.
            prevPage (string): No description provided.
            max (integer): No description provided.
            filters (string): No description provided.

        Returns:
            dict[str, Any]: Get list of users response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users
        """
        url = f"{self.base_url}/v3/spend/users"
        query_params = {
            k: v
            for k, v in [
                ("nextPage", nextPage),
                ("prevPage", prevPage),
                ("max", max),
                ("filters", filters),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_user(
        self,
        firstName: str,
        lastName: str,
        email: str,
        role: Any,
        dateOfBirth: str | None = None,
    ) -> dict[str, Any]:
        """
        Create a user

        Args:
            firstName (string): User first name
            lastName (string): User last name
            email (string): User email address
            role (string): role
            dateOfBirth (string): User's date of birth in the format `yyyy-MM-dd`

        Returns:
            dict[str, Any]: Create a user response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users
        """
        request_body_data = None
        request_body_data = {
            "firstName": firstName,
            "lastName": lastName,
            "email": email,
            "role": role,
            "dateOfBirth": dateOfBirth,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/spend/users"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_current_user(self) -> dict[str, Any]:
        """
        Get current user details

        Returns:
            dict[str, Any]: Get current user details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users
        """
        url = f"{self.base_url}/v3/spend/users/current"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_user(self, userId: str) -> dict[str, Any]:
        """
        Get user details

        Args:
            userId (string): userId

        Returns:
            dict[str, Any]: Get user details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users
        """
        if userId is None:
            raise ValueError("Missing required parameter 'userId'.")
        url = f"{self.base_url}/v3/spend/users/{userId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def delete_user(self, userId: str) -> Any:
        """
        Delete a user

        Args:
            userId (string): userId

        Returns:
            Any: Delete a user response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users
        """
        if userId is None:
            raise ValueError("Missing required parameter 'userId'.")
        url = f"{self.base_url}/v3/spend/users/{userId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def update_user(
        self,
        userId: str,
        firstName: str | None = None,
        lastName: str | None = None,
        email: str | None = None,
        role: Any | None = None,
        dateOfBirth: str | None = None,
    ) -> dict[str, Any]:
        """
        Update a user

        Args:
            userId (string): userId
            firstName (string): User first name
            lastName (string): User last name
            email (string): User email address
            role (string): role
            dateOfBirth (string): Users date of birth in the format `yyyy-MM-dd`

        Returns:
            dict[str, Any]: Update a user response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users
        """
        if userId is None:
            raise ValueError("Missing required parameter 'userId'.")
        request_body_data = None
        request_body_data = {
            "firstName": firstName,
            "lastName": lastName,
            "email": email,
            "role": role,
            "dateOfBirth": dateOfBirth,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/spend/users/{userId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def list_organization_users(
        self,
        max: int | None = None,
        sort: str | None = None,
        filters: str | None = None,
        page: str | None = None,
    ) -> dict[str, Any]:
        """
        Get list of users

        Args:
            max (integer): No description provided.
            sort (string): No description provided.
            filters (string): No description provided.
            page (string): No description provided.

        Returns:
            dict[str, Any]: Get list of users response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            organization users
        """
        url = f"{self.base_url}/v3/users"
        query_params = {
            k: v
            for k, v in [
                ("max", max),
                ("sort", sort),
                ("filters", filters),
                ("page", page),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_organization_user(
        self,
        firstName: str,
        lastName: str,
        email: str,
        roleId: str,
        acceptTermsOfService: bool,
    ) -> dict[str, Any]:
        """
        Create a user

        Args:
            firstName (string): User first name
            lastName (string): User last name
            email (string): User email address
            roleId (string): BILL-generated ID of the user role. The value begins with `0po`.

        If you do not set `roleId`, the default `ADMINISTRATOR` user role is assigned to the created user. You can get the list of available user roles with `GET /v3/roles`.
            acceptTermsOfService (boolean): Set as `true` if the user accepts the BILL terms of service

        Returns:
            dict[str, Any]: Create a user response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            organization users
        """
        request_body_data = None
        request_body_data = {
            "firstName": firstName,
            "lastName": lastName,
            "email": email,
            "roleId": roleId,
            "acceptTermsOfService": acceptTermsOfService,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/users"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_organization_user(self, userId: str) -> dict[str, Any]:
        """
        Get user details

        Args:
            userId (string): userId

        Returns:
            dict[str, Any]: Get user details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            organization users
        """
        if userId is None:
            raise ValueError("Missing required parameter 'userId'.")
        url = f"{self.base_url}/v3/users/{userId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def update_organization_user(
        self,
        userId: str,
        firstName: str | None = None,
        lastName: str | None = None,
        roleId: str | None = None,
    ) -> dict[str, Any]:
        """
        Update a user

        Args:
            userId (string): userId
            firstName (string): User first name
            lastName (string): User last name
            roleId (string): BILL-generated ID of the user role. The value begins with `0po`.

        If you do not set `roleId`, the default `ADMINISTRATOR` user role is assigned to the created user. You can get the list of available user roles with `GET /v3/roles`.

        Returns:
            dict[str, Any]: Update a user response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            organization users
        """
        if userId is None:
            raise ValueError("Missing required parameter 'userId'.")
        request_body_data = None
        request_body_data = {
            "firstName": firstName,
            "lastName": lastName,
            "roleId": roleId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/users/{userId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def archive_organization_user(self, userId: str) -> dict[str, Any]:
        """
        Archive a user

        Args:
            userId (string): userId

        Returns:
            dict[str, Any]: Archive a user response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            organization users
        """
        if userId is None:
            raise ValueError("Missing required parameter 'userId'.")
        request_body_data = None
        url = f"{self.base_url}/v3/users/{userId}/archive"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def restore_organization_user(self, userId: str) -> dict[str, Any]:
        """
        Restore an archived user

        Args:
            userId (string): userId

        Returns:
            dict[str, Any]: Restore an archived user response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            organization users
        """
        if userId is None:
            raise ValueError("Missing required parameter 'userId'.")
        request_body_data = None
        url = f"{self.base_url}/v3/users/{userId}/restore"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def list_vendors(
        self,
        max: int | None = None,
        sort: str | None = None,
        filters: str | None = None,
        page: str | None = None,
    ) -> dict[str, Any]:
        """
        Get list of vendors

        Args:
            max (integer): No description provided.
            sort (string): No description provided.
            filters (string): No description provided.
            page (string): No description provided.

        Returns:
            dict[str, Any]: Get list of vendors response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            vendors
        """
        url = f"{self.base_url}/v3/vendors"
        query_params = {
            k: v
            for k, v in [
                ("max", max),
                ("sort", sort),
                ("filters", filters),
                ("page", page),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_vendor(
        self,
        name: str,
        address: Any,
        shortName: str | None = None,
        accountNumber: str | None = None,
        accountType: Any | None = None,
        email: str | None = None,
        phone: str | None = None,
        paymentInformation: Any | None = None,
        additionalInfo: Any | None = None,
        billCurrency: Any | None = None,
        autoPay: Any | None = None,
    ) -> dict[str, Any]:
        """
        Create a vendor

        Args:
            name (string): Vendor name
            address (string): address
            shortName (string): Vendor short name
            accountNumber (string): User account number set by the vendor. Set this field as the billing statement account number for vendor services such as utility or credit card bills.

        When you pay the vendor, this value appears on the check memo or electronic payment record.
            accountType (string): accountType
            email (string): Vendor email address
            phone (string): Vendor phone number
            paymentInformation (string): paymentInformation
            additionalInfo (string): additionalInfo
            billCurrency (string): billCurrency
            autoPay (string): autoPay

        Returns:
            dict[str, Any]: Create a vendor response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            vendors
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "shortName": shortName,
            "accountNumber": accountNumber,
            "accountType": accountType,
            "email": email,
            "phone": phone,
            "address": address,
            "paymentInformation": paymentInformation,
            "additionalInfo": additionalInfo,
            "billCurrency": billCurrency,
            "autoPay": autoPay,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/vendors"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def create_bulk_vendor(self, items: list[dict[str, Any]]) -> dict[str, Any]:
        """
        Create multiple vendors

        Args:

        Returns:
            dict[str, Any]: Create multiple vendors response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            vendors
        """
        request_body_data = None
        # Using array parameter 'items' directly as request body
        request_body_data = items
        url = f"{self.base_url}/v3/vendors/bulk"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_intl_config(
        self, country: Any, billCurrency: Any, accountType: Any
    ) -> dict[str, Any]:
        """
        Get international payments configuration

        Args:
            country (string): No description provided.
            billCurrency (string): No description provided.
            accountType (string): No description provided.

        Returns:
            dict[str, Any]: Get international payments configuration response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            vendors
        """
        url = f"{self.base_url}/v3/vendors/configuration/international-payments"
        query_params = {
            k: v
            for k, v in [
                ("country", country),
                ("billCurrency", billCurrency),
                ("accountType", accountType),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def get_vendor(self, vendorId: str) -> dict[str, Any]:
        """
        Get vendor details

        Args:
            vendorId (string): vendorId

        Returns:
            dict[str, Any]: Get vendor details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            vendors
        """
        if vendorId is None:
            raise ValueError("Missing required parameter 'vendorId'.")
        url = f"{self.base_url}/v3/vendors/{vendorId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def update_vendor(
        self,
        vendorId: str,
        name: str | None = None,
        shortName: str | None = None,
        accountNumber: str | None = None,
        accountType: Any | None = None,
        email: str | None = None,
        phone: str | None = None,
        address: Any | None = None,
        paymentInformation: Any | None = None,
        additionalInfo: Any | None = None,
        billCurrency: Any | None = None,
        autoPay: Any | None = None,
    ) -> dict[str, Any]:
        """
        Update a vendor

        Args:
            vendorId (string): vendorId
            name (string): Vendor name
            shortName (string): Vendor short name
            accountNumber (string): User account number set by the vendor. Set this field as the billing statement account number for vendor services such as utility or credit card bills.

        When you pay the vendor, this value appears on the check memo or electronic payment record.
            accountType (string): accountType
            email (string): Vendor email address
            phone (string): Vendor phone number
            address (string): address
            paymentInformation (string): paymentInformation
            additionalInfo (string): additionalInfo
            billCurrency (string): billCurrency
            autoPay (string): autoPay

        Returns:
            dict[str, Any]: Update a vendor response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            vendors
        """
        if vendorId is None:
            raise ValueError("Missing required parameter 'vendorId'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "shortName": shortName,
            "accountNumber": accountNumber,
            "accountType": accountType,
            "email": email,
            "phone": phone,
            "address": address,
            "paymentInformation": paymentInformation,
            "additionalInfo": additionalInfo,
            "billCurrency": billCurrency,
            "autoPay": autoPay,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/vendors/{vendorId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def archive_vendor(self, vendorId: str) -> dict[str, Any]:
        """
        Archive a vendor

        Args:
            vendorId (string): vendorId

        Returns:
            dict[str, Any]: Archive a vendor response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            vendors
        """
        if vendorId is None:
            raise ValueError("Missing required parameter 'vendorId'.")
        request_body_data = None
        url = f"{self.base_url}/v3/vendors/{vendorId}/archive"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_vendor_bank_account(self, vendorId: str) -> dict[str, Any]:
        """
        Get vendor bank account details

        Args:
            vendorId (string): vendorId

        Returns:
            dict[str, Any]: Get vendor bank account details response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            vendors
        """
        if vendorId is None:
            raise ValueError("Missing required parameter 'vendorId'.")
        url = f"{self.base_url}/v3/vendors/{vendorId}/bank-account"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_vendor_bank_account(
        self,
        vendorId: str,
        accountNumber: str,
        nameOnAccount: str | None = None,
        routingNumber: str | None = None,
        type: Any | None = None,
        ownerType: Any | None = None,
        regulatoryFields: list[dict[str, Any]] | None = None,
        paymentCurrency: Any | None = None,
    ) -> dict[str, Any]:
        """
        Create a vendor bank account

        Args:
            vendorId (string): vendorId
            accountNumber (string): Vendor bank account number. This field is required for enabling electronic payments to vendors.

        See [Creating an international vendor](doc:creating-an-international-vendor) for more information on how to set up vendor payment information for an international (not US) vendor.
            nameOnAccount (string): Vendor bank account name
            routingNumber (string): Vendor bank routing number. This field is required for enabling electronic payments to vendors. This field is empty for an IBAN `accountNumber`.

        See [Creating an international vendor](doc:creating-an-international-vendor) for more information on how to set up vendor payment information for an international (not US) vendor.
            type (string): type
            ownerType (string): ownerType
            regulatoryFields (array): International bank account regulatory information. The `name` and `value` fields are required for each required bank account regulatory field.

        See [Creating an international vendor](doc:creating-an-international-vendor) for more information on how to set `regulatoryFields`.
            paymentCurrency (string): paymentCurrency

        Returns:
            dict[str, Any]: Create a vendor bank account response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            vendors
        """
        if vendorId is None:
            raise ValueError("Missing required parameter 'vendorId'.")
        request_body_data = None
        request_body_data = {
            "nameOnAccount": nameOnAccount,
            "accountNumber": accountNumber,
            "routingNumber": routingNumber,
            "type": type,
            "ownerType": ownerType,
            "regulatoryFields": regulatoryFields,
            "paymentCurrency": paymentCurrency,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v3/vendors/{vendorId}/bank-account"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def delete_vendor_bank_account(self, vendorId: str) -> Any:
        """
        Delete a vendor bank account

        Args:
            vendorId (string): vendorId

        Returns:
            Any: Delete a vendor bank account response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            vendors
        """
        if vendorId is None:
            raise ValueError("Missing required parameter 'vendorId'.")
        url = f"{self.base_url}/v3/vendors/{vendorId}/bank-account"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def get_configuration_by_vendor_id(self, vendorId: str) -> dict[str, Any]:
        """
        Get vendor configuration

        Args:
            vendorId (string): vendorId

        Returns:
            dict[str, Any]: Get vendor configuration response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            vendors
        """
        if vendorId is None:
            raise ValueError("Missing required parameter 'vendorId'.")
        url = f"{self.base_url}/v3/vendors/{vendorId}/configuration"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def restore_vendor(self, vendorId: str) -> dict[str, Any]:
        """
        Restore an archived vendor

        Args:
            vendorId (string): vendorId

        Returns:
            dict[str, Any]: Restore an archived vendor response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            vendors
        """
        if vendorId is None:
            raise ValueError("Missing required parameter 'vendorId'.")
        request_body_data = None
        url = f"{self.base_url}/v3/vendors/{vendorId}/restore"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def list_tools(self):
        return [
            self.list_customer_attachments,
            self.create_customer_attachment,
            self.list_invoice_attachments,
            self.create_invoice_attachment,
            self.list_vendor_attachments,
            self.create_vendor_attachment,
            self.get_attachment,
            self.list_bills,
            self.create_bill,
            self.create_bulk_bills,
            self.get_bill,
            self.replace_bill,
            self.update_bill,
            self.archive_bill,
            self.restore_bill,
            self.list_classification_accounting_classes,
            self.create_classification_accounting_class,
            self.bulk_create_classification_accounting_class,
            self.bulk_update_classification_accounting_class,
            self.bulk_archive_classification_accounting_class,
            self.bulk_restore_classification_accounting_class,
            self.get_classification_accounting_class,
            self.update_classification_accounting_class,
            self.archive_classification_accounting_class,
            self.restore_classification_accounting_class,
            self.list_classification_chart_of_accounts,
            self.create_classification_chart_of_accounts,
            self.bulk_create_classification_chart_of_accounts,
            self.bulk_update_classification_chart_of_accounts,
            self.bulk_archive_classification_chart_of_accounts,
            self.bulk_restore_classification_chart_of_accounts,
            self.get_classification_chart_of_accounts,
            self.update_classification_chart_of_accounts,
            self.archive_classification_chart_of_accounts,
            self.restore_classification_chart_of_accounts,
            self.list_classification_departments,
            self.create_classification_department,
            self.bulk_create_classification_department,
            self.bulk_update_classification_department,
            self.bulk_archive_classification_department,
            self.bulk_restore_classification_department,
            self.get_classification_department,
            self.update_classification_department,
            self.archive_classification_department,
            self.restore_classification_department,
            self.list_classification_employees,
            self.create_classification_employee,
            self.bulk_create_classification_employee,
            self.bulk_update_classification_employee,
            self.bulk_archive_classification_employee,
            self.bulk_restore_classification_employee,
            self.get_classification_employee,
            self.update_classification_employee,
            self.archive_classification_employee,
            self.restore_classification_employee,
            self.list_classification_items,
            self.create_classification_item,
            self.bulk_create_classification_item,
            self.bulk_update_classification_item,
            self.bulk_archive_classification_item,
            self.bulk_restore_classification_item,
            self.get_classification_item,
            self.update_classification_item,
            self.archive_classification_item,
            self.restore_classification_item,
            self.list_classification_jobs,
            self.create_classification_job,
            self.bulk_create_classification_job,
            self.bulk_update_classification_job,
            self.bulk_archive_classification_job,
            self.bulk_restore_classification_job,
            self.get_classification_job,
            self.update_classification_job,
            self.archive_classification_job,
            self.restore_classification_job,
            self.list_classification_locations,
            self.create_classification_location,
            self.bulk_create_classification_location,
            self.bulk_update_classification_location,
            self.bulk_archive_classification_location,
            self.bulk_restore_classification_location,
            self.get_classification_location,
            self.update_classification_location,
            self.archive_classification_location,
            self.restore_classification_location,
            self.list_customers,
            self.create_customer,
            self.get_customer,
            self.update_customer,
            self.archive_customer,
            self.restore_customer,
            self.list_documents,
            self.create_bill_document,
            self.upload_status,
            self.get_document,
            self.list_payable_apcards,
            self.list_bank_accounts,
            self.create_bank_account,
            self.list_bank_account_users,
            self.nominate_bank_account_user,
            self.archive_bank_account_user,
            self.get_bank_account,
            self.update_bank_account,
            self.archive_bank_account,
            self.verify_bank_account,
            self.list_payable_card_accounts,
            self.list_card_funding_purposes,
            self.list_card_account_users,
            self.get_card_account,
            self.get_funding_account_permission,
            self.get_health_check,
            self.list_invoices,
            self.create_invoice,
            self.record_invoice,
            self.get_invoice,
            self.replace_invoice,
            self.update_invoice,
            self.archive_invoice,
            self.send_invoice,
            self.restore_invoice,
            self.login,
            self.get_session_info,
            self.logout,
            self.generate_challenge,
            self.validate_challenge,
            self.list_mfa_phones,
            self.setup,
            self.validate,
            self.step_up_session,
            self.search,
            self.accept_invitation,
            self.get_customer_invitation,
            self.create_customer_invitation,
            self.delete_customer_invitation,
            self.get_vendor_invitation,
            self.create_vendor_invitation,
            self.delete_vendor_invitation,
            self.list_industries,
            self.get_organization,
            self.update_organization,
            self.get_price_plan,
            self.partner_login,
            self.login_as_user,
            self.list_partner_organizations,
            self.create_organization,
            self.create_phone,
            self.list_partner_user_roles,
            self.get_partner_user_role,
            self.list_partner_users,
            self.create_partner_user,
            self.get_partner_user,
            self.update_partner_user,
            self.archive_partner_user,
            self.restore_partner_user,
            self.list_payments,
            self.create_payment,
            self.create_bulk_payment,
            self.list_payment_options,
            self.get_payment,
            self.cancel_payment,
            self.get_check_image_data,
            self.void_payment,
            self.list_recurring_bills,
            self.create_recurring_bill,
            self.get_recurring_bill,
            self.replace_recurring_bill,
            self.update_recurring_bill,
            self.archive_recurring_bill,
            self.restore_recurring_bill,
            self.get_vendor_audit_trail,
            self.get_risk_verifications,
            self.initiate_risk_verifications,
            self.get_risk_verification_phone,
            self.create_risk_verification_phone,
            self.list_organization_user_roles,
            self.get_organization_user_role,
            self.list_budgets,
            self.create_budget,
            self.get_budget,
            self.delete_budget,
            self.update_budget,
            self.list_budget_members,
            self.upsert_bulk_budget_users,
            self.get_budget_member,
            self.upsert_budget_member,
            self.delete_budget_member,
            self.list_cards,
            self.create_budget_card,
            self.get_card,
            self.delete_card,
            self.update_card,
            self.get_pan_jwt,
            self.list_custom_fields,
            self.create_custom_field,
            self.get_custom_field,
            self.delete_custom_field,
            self.update_custom_field,
            self.list_custom_field_values,
            self.create_custom_field_values,
            self.delete_custom_field_value,
            self.get_custom_field_values,
            self.list_reimbursements,
            self.create_reimbursement,
            self.create_image_upload_url,
            self.get_reimbursement,
            self.delete_reimbursement,
            self.update_reimbursement,
            self.approve_or_deny_reimbursement,
            self.list_transactions,
            self.get_transaction,
            self.update_transaction,
            self.list_transaction_custom_fields,
            self.update_transaction_custom_fields,
            self.list_transaction_custom_field_values,
            self.list_users,
            self.create_user,
            self.get_current_user,
            self.get_user,
            self.delete_user,
            self.update_user,
            self.list_organization_users,
            self.create_organization_user,
            self.get_organization_user,
            self.update_organization_user,
            self.archive_organization_user,
            self.restore_organization_user,
            self.list_vendors,
            self.create_vendor,
            self.create_bulk_vendor,
            self.get_intl_config,
            self.get_vendor,
            self.update_vendor,
            self.archive_vendor,
            self.get_vendor_bank_account,
            self.create_vendor_bank_account,
            self.delete_vendor_bank_account,
            self.get_configuration_by_vendor_id,
            self.restore_vendor,
        ]
