from typing import Any

from loguru import logger

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class ApolloApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="apollo", integration=integration, **kwargs)
        self.base_url = "https://api.apollo.io/api/v1"

    def _get_headers(self) -> dict[str, str]:
        """
        Get the headers for Apollo API requests.
        Overrides the base class method to use X-Api-Key.
        """
        if not self.integration:
            logger.warning(
                "ApolloApp: No integration configured, returning empty headers."
            )
            return {}

        # ApiKeyIntegration's get_credentials() returns a dict like:
        # {'api_key': 'your_actual_key_value'}
        credentials = self.integration.get_credentials()

        # The key in the credentials dict from ApiKeyIntegration is 'api_key'
        api_key = (
            credentials.get("api_key")
            or credentials.get("API_KEY")
            or credentials.get("apiKey")
        )

        if not api_key:
            logger.error(
                "ApolloApp: API key not found in integration credentials for Apollo."
            )
            # You might want to raise an error here if an API key is absolutely required
            # For example: raise ValueError("API key is missing for Apollo integration.")
            return {  # Or return minimal headers if some calls might not need auth (unlikely for Apollo)
                "Content-Type": "application/json",
                "Cache-Control": "no-cache",
            }

        logger.debug("ApolloApp: Using X-Api-Key for authentication.")
        return {
            "X-Api-Key": api_key,
            "Content-Type": "application/json",
            "Cache-Control": "no-cache",  # Often good practice for APIs
        }

    def people_enrichment(
        self,
        first_name: str | None = None,
        last_name: str | None = None,
        name: str | None = None,
        email: str | None = None,
        hashed_email: str | None = None,
        organization_name: str | None = None,
        domain: str | None = None,
        id: str | None = None,
        linkedin_url: str | None = None,
        reveal_personal_emails: bool | None = None,
        reveal_phone_number: bool | None = None,
        webhook_url: str | None = None,
    ) -> dict[str, Any]:
        """
        Matches a person based on provided identifying information such as name, email, organization, or LinkedIn URL, with options to reveal personal emails and phone numbers.

        Args:
            first_name (string): The first name of the person to match, typically used together with the last_name parameter to identify an individual; example: "Tim".
            last_name (string): The last name of the person to match, usually combined with the `first_name` parameter to improve accuracy; for example, `zheng`.
            name (string): Full name of the person, typically a first name and last name separated by a space, replacing `first_name` and `last_name`.
            email (string): Email address of the person to match; must be valid (e.g., example@email.com).
            hashed_email (string): The hashed_email query parameter accepts an email address hashed in MD5 or SHA-256 format, such as `8d935115b9ff4489f2d1f9249503cadf` (MD5) or `97817c0c49994eb500ad0a5e7e2d8aed51977b26424d508f66e4e8887746a152` (SHA-256).
            organization_name (string): The name of the person's current or past employer, used to identify their organization during the matching process. Example: `apollo`.
            domain (string): The domain parameter is the employer's website domain for the person being matched, reflecting either current or previous employment; enter only the domain name without prefixes like www or symbols such as @, for example, apollo.io or microsoft.com.
            id (string): Unique ID for the person in Apollo's database, obtained via the People Search endpoint.
            linkedin_url (string): The URL of the person's LinkedIn profile, typically starting with "https://www.linkedin.com/in/", used to uniquely identify and match the individual in the system.
            reveal_personal_emails (boolean): Enrich person data with personal emails by setting to `true`. This may consume credits and is subject to GDPR restrictions.
            reveal_phone_number (boolean): Set to `true` to enrich person's data with available phone numbers, consuming credits. Requires a `webhook_url` for asynchronous verification and delivery.
            webhook_url (string): If `reveal_phone_number` is true, provide this required webhook URL where Apollo will send a JSON response containing the requested phone number; otherwise, omit this parameter.

        Returns:
            dict[str, Any]: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            People, important
        """
        request_body_data = None
        url = f"{self.base_url}/people/match"
        query_params = {
            k: v
            for k, v in [
                ("first_name", first_name),
                ("last_name", last_name),
                ("name", name),
                ("email", email),
                ("hashed_email", hashed_email),
                ("organization_name", organization_name),
                ("domain", domain),
                ("id", id),
                ("linkedin_url", linkedin_url),
                ("reveal_personal_emails", reveal_personal_emails),
                ("reveal_phone_number", reveal_phone_number),
                ("webhook_url", webhook_url),
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

    def bulk_people_enrichment(
        self,
        reveal_personal_emails: bool | None = None,
        reveal_phone_number: bool | None = None,
        webhook_url: str | None = None,
        details: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """
        Performs a bulk match operation on people data using a POST request to the "/people/bulk_match" endpoint, accepting query parameters to control the reveal of personal emails and phone numbers, and optionally specifying a webhook URL, with the request body containing JSON data.

        Args:
            reveal_personal_emails (boolean): Set to true to enrich matched people with personal emails, consuming credits; defaults to false. Personal emails won’t be revealed for individuals in GDPR-compliant regions.
            reveal_phone_number (boolean): Set to `true` to enrich matched people with available phone numbers, consuming credits. Requires a `webhook_url` for asynchronous verification and delivery of phone details.
            webhook_url (string): Optional webhook URL for receiving a JSON response with phone numbers if `reveal_phone_number` is `true`.
            details (array): Provide info for each person you want to enrich as an object within this array. Add up to 10 people.

        Returns:
            dict[str, Any]: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            People
        """
        request_body_data = None
        request_body_data = {
            "details": details,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/people/bulk_match"
        query_params = {
            k: v
            for k, v in [
                ("reveal_personal_emails", reveal_personal_emails),
                ("reveal_phone_number", reveal_phone_number),
                ("webhook_url", webhook_url),
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

    def organization_enrichment(self, domain: str) -> dict[str, Any]:
        """
        Retrieves enriched organization data for a company specified by its domain name.

        Args:
            domain (string): The domain query parameter specifies the company’s website domain to enrich, excluding prefixes like "www." or symbols such as "@"; for example, use "apollo.io" or "microsoft.com".

        Returns:
            dict[str, Any]: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Organizations
        """
        url = f"{self.base_url}/organizations/enrich"
        query_params = {k: v for k, v in [("domain", domain)] if v is not None}
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

    def bulk_organization_enrichment(self, domains_: list[str]) -> dict[str, Any]:
        """
        Enriches multiple organizations in bulk by submitting an array of domain names and returns detailed company profiles in a single request.

        Args:
            domains_ (array): List of company domains to enrich, without "www.", "@", or similar prefixes—just the base domain, e.g., apollo.io, microsoft.com.

        Returns:
            dict[str, Any]: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Organizations
        """
        request_body_data = None
        url = f"{self.base_url}/organizations/bulk_enrich"
        query_params = {k: v for k, v in [("domains[]", domains_)] if v is not None}
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

    def people_search(
        self,
        person_titles_: list[str] | None = None,
        include_similar_titles: bool | None = None,
        person_locations_: list[str] | None = None,
        person_seniorities_: list[str] | None = None,
        organization_locations_: list[str] | None = None,
        q_organization_domains_list_: list[str] | None = None,
        contact_email_status_: list[str] | None = None,
        organization_ids_: list[str] | None = None,
        organization_num_employees_ranges_: list[str] | None = None,
        q_keywords: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> dict[str, Any]:
        """
        Searches for people matching specified criteria including titles, locations, seniorities, organization details, and keywords, returning paginated results.

        Args:
            person_titles_ (array): Specify job titles to find matching people; only one listed title needs to match, and partial matches are included. Combine with person_seniorities[] for refined results.
            include_similar_titles (boolean): This parameter controls whether the search includes people with job titles similar to those specified in `person_titles[]`; set to false to return only exact title matches. Example: 'true'.
            person_locations_ (array): The locations where people reside, searchable by city, US state, or country; to filter by employer headquarters, use the `organization_locations` parameter instead.
            person_seniorities_ (array): The 'person_seniorities[]' query parameter filters people by their current job seniority level within their employer, such as Director or Senior IC; matching any listed seniority expands results, which reflect only present titles and can be combined
            organization_locations_ (array): The organization_locations[] parameter filters people by the headquarters location of their current employer’s company, searchable by city, state, or country; office locations do not affect results.
            q_organization_domains_list_ (array): The domain names of a person’s current or past employers, without prefixes like `www.` or symbols like `@`; accepts up to 1,000 domains per request, e.g., `apollo.io`, `microsoft.com`.
            contact_email_status_ (array): The contact_email_status[] parameter filters people by their email verification status; you can specify multiple values like verified, unverified, likely to engage, or unavailable to broaden your search.
            organization_ids_ (array): The Apollo IDs of companies (employers) to include in your search results; each company has a unique ID found via the Organization Search endpoint (e.g., `5e66b6381e05b4008c8331b8`).
            organization_num_employees_ranges_ (array): Filter people by the employee count of their company using ranges (e.g., `1,10`, `250,500`). Multiple ranges can be added to expand search results.
            q_keywords (string): A string of keywords used to filter search results.
            page (integer): The page number of Apollo data to retrieve, used with `per_page` to paginate results and optimize endpoint performance; for example, `4`.
            per_page (integer): The number of results to return per page in the search response; limiting this improves performance. Use the `page` parameter to access additional pages of results.

        Returns:
            dict[str, Any]: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            People
        """
        request_body_data = None
        url = f"{self.base_url}/mixed_people/search"
        query_params = {
            k: v
            for k, v in [
                ("person_titles[]", person_titles_),
                ("include_similar_titles", include_similar_titles),
                ("person_locations[]", person_locations_),
                ("person_seniorities[]", person_seniorities_),
                ("organization_locations[]", organization_locations_),
                ("q_organization_domains_list[]", q_organization_domains_list_),
                ("contact_email_status[]", contact_email_status_),
                ("organization_ids[]", organization_ids_),
                (
                    "organization_num_employees_ranges[]",
                    organization_num_employees_ranges_,
                ),
                ("q_keywords", q_keywords),
                ("page", page),
                ("per_page", per_page),
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

    def organization_search(
        self,
        organization_num_employees_ranges_: list[str] | None = None,
        organization_locations_: list[str] | None = None,
        organization_not_locations_: list[str] | None = None,
        revenue_range_min: int | None = None,
        revenue_range_max: int | None = None,
        currently_using_any_of_technology_uids_: list[str] | None = None,
        q_organization_keyword_tags_: list[str] | None = None,
        q_organization_name: str | None = None,
        organization_ids_: list[str] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> dict[str, Any]:
        """
        Searches mixed companies based on various criteria such as employee ranges, locations, revenue range, technology usage, keyword tags, organization names, and IDs, supporting pagination.

        Args:
            organization_num_employees_ranges_ (array): Specify company employee headcount ranges by listing strings like "1,10" or "250,500"; multiple ranges are allowed.
            organization_locations_ (array): The organization_locations[] parameter filters companies by their headquarters' location—city, state, or country; multiple office locations are ignored, and to exclude locations, use organization_not_locations.
            organization_not_locations_ (array): Exclude companies headquartered in specified locations such as cities, US states, or countries from search results to avoid prospecting in unwanted territories (e.g., `ireland`, `minnesota`, `seoul`).
            revenue_range_min (integer): Sets the minimum revenue value for filtering organizations; enter only digits, without currency symbols, commas, or decimals.
            revenue_range_max (integer): Set the maximum organization revenue for search filtering as an integer without currency symbols, commas, or decimals; pair with `revenue_range[min]` to define a revenue range (e.g., 50000000).
            currently_using_any_of_technology_uids_ (array): Filter organizations by the technologies they currently use from over 1,500 options, identified with underscores replacing spaces and periods as in the provided technology list.
            q_organization_keyword_tags_ (array): Filter search results by specifying keywords related to company industries, services, or focus areas, such as "mining," "sales strategy," or "consulting," to return matching companies.
            q_organization_name (string): Filters results to companies whose names contain the specified value (partial match allowed); unmatched names are excluded, regardless of other criteria.
            organization_ids_ (array): The Apollo unique company IDs to filter search results by specific organizations; each ID corresponds to a company in the Apollo database, e.g., `5e66b6381e05b4008c8331b8`.
            page (integer): The page number of Apollo data to retrieve, used with `per_page` to paginate results and optimize performance; for example, `4` returns the fourth page of results.
            per_page (integer): The number of search results returned per page to limit response size and improve performance; use the `page` parameter to access additional pages. Example: `10`.

        Returns:
            dict[str, Any]: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Organizations
        """
        request_body_data = None
        url = f"{self.base_url}/mixed_companies/search"
        query_params = {
            k: v
            for k, v in [
                (
                    "organization_num_employees_ranges[]",
                    organization_num_employees_ranges_,
                ),
                ("organization_locations[]", organization_locations_),
                ("organization_not_locations[]", organization_not_locations_),
                ("revenue_range[min]", revenue_range_min),
                ("revenue_range[max]", revenue_range_max),
                (
                    "currently_using_any_of_technology_uids[]",
                    currently_using_any_of_technology_uids_,
                ),
                ("q_organization_keyword_tags[]", q_organization_keyword_tags_),
                ("q_organization_name", q_organization_name),
                ("organization_ids[]", organization_ids_),
                ("page", page),
                ("per_page", per_page),
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

    def organization_jobs_postings(
        self,
        organization_id: str,
        page: int | None = None,
        per_page: int | None = None,
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of job postings for a specified organization using the "GET" method, allowing optional pagination parameters for page and items per page.

        Args:
            organization_id (string): organization_id
            page (integer): The page query parameter specifies which page of job postings to retrieve, used with per_page to paginate results and improve response performance.
            per_page (integer): The number of results to return per page in the response, which improves performance by limiting data size; use the `page` parameter to access other pages. Example: 10

        Returns:
            dict[str, Any]: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Organizations
        """
        if organization_id is None:
            raise ValueError("Missing required parameter 'organization_id'.")
        url = f"{self.base_url}/organizations/{organization_id}/job_postings"
        query_params = {
            k: v for k, v in [("page", page), ("per_page", per_page)] if v is not None
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

    def create_an_account(
        self,
        name: str | None = None,
        domain: str | None = None,
        owner_id: str | None = None,
        account_stage_id: str | None = None,
        phone: str | None = None,
        raw_address: str | None = None,
    ) -> dict[str, Any]:
        """
        Creates a new account resource using the provided query parameters such as name, domain, owner ID, account stage ID, phone, and raw address.

        Args:
            name (string): A unique, human-readable name for the new account, such as "The Irish Copywriters."
            domain (string): The domain name for the account, entered without any prefixes like "www."; for example, use "apollo.io" or "microsoft.com".
            owner_id (string): The unique identifier of the account owner within your team's Apollo account, required to assign ownership; retrieve valid user IDs using the Get a List of Users endpoint.
            account_stage_id (string): Apollo ID of the account stage to assign the account to; otherwise, it defaults to your team's settings.
            phone (string): The primary phone number for the account, which may be for headquarters, a branch, or a main contact; any format is accepted and sanitized for consistency in the response.
            raw_address (string): Corporate location for the account, including city, state, and country, matched to a pre-defined location by Apollo.

        Returns:
            dict[str, Any]: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Accounts
        """
        request_body_data = None
        url = f"{self.base_url}/accounts"
        query_params = {
            k: v
            for k, v in [
                ("name", name),
                ("domain", domain),
                ("owner_id", owner_id),
                ("account_stage_id", account_stage_id),
                ("phone", phone),
                ("raw_address", raw_address),
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

    def update_an_account(
        self,
        account_id: str,
        name: str | None = None,
        domain: str | None = None,
        owner_id: str | None = None,
        account_stage_id: str | None = None,
        raw_address: str | None = None,
        phone: str | None = None,
    ) -> dict[str, Any]:
        """
        Updates an account identified by `{account_id}` with specified parameters such as `name`, `domain`, `owner_id`, `account_stage_id`, `raw_address`, and `phone`, returning a status message upon successful modification.

        Args:
            account_id (string): account_id
            name (string): Specify the account's human-readable name. Example: "The Fast Irish Copywriters"
            domain (string): Specify the account's domain name to update, excluding any prefixes like "www."; use only the base domain such as "example.com" or "company.org".
            owner_id (string): The ID of the user within your Apollo team to assign as the account owner; changing this updates the account owner. Retrieve valid user IDs via the Get a List of Users endpoint.
            account_stage_id (string): The Apollo ID of the account stage to assign or update the account's stage; omit to auto-assign based on your team's default settings. Use List Account Stages to find IDs.
            raw_address (string): Update the corporate location for the account. Provide a city, state, and country to match our pre-defined locations. Examples: `Belfield, Dublin 4, Ireland`; `Dallas, United States`.
            phone (string): Update the account's primary phone number, which may be the corporate headquarters, a branch, or a direct contact; input in any format, sanitized and returned formatted.

        Returns:
            dict[str, Any]: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Accounts
        """
        if account_id is None:
            raise ValueError("Missing required parameter 'account_id'.")
        request_body_data = None
        url = f"{self.base_url}/accounts/{account_id}"
        query_params = {
            k: v
            for k, v in [
                ("name", name),
                ("domain", domain),
                ("owner_id", owner_id),
                ("account_stage_id", account_stage_id),
                ("raw_address", raw_address),
                ("phone", phone),
            ]
            if v is not None
        }
        response = self._put(
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

    def search_for_accounts(
        self,
        q_organization_name: str | None = None,
        account_stage_ids_: list[str] | None = None,
        sort_by_field: str | None = None,
        sort_ascending: bool | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> dict[str, Any]:
        """
        Searches for accounts based on organization name, account stage IDs, sorting, and pagination parameters, returning matching results.

        Args:
            q_organization_name (string): Search for accounts by name using keywords. Matches part of the name, e.g., 'marketing' returns 'NY Marketing Unlimited'.
            account_stage_ids_ (array): Specify Apollo IDs for account stages to include in search results. Multiple stages will match any of them.
            sort_by_field (string): Sort matching accounts by one of these fields: `account_last_activity_date` (most recent activity first), `account_created_at` (newest accounts first), or `account_updated_at` (most recently updated first).
            sort_ascending (boolean): Sort results in ascending order using the specified `sort_by_field`.
            page (integer): The page number of the Apollo data to retrieve, used with the `per_page` parameter to paginate search results and optimize endpoint performance; for example, `4`.
            per_page (integer): The number of search results returned per page to improve response performance; use the `page` parameter to access additional pages. Example value: `10`.

        Returns:
            dict[str, Any]: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Accounts
        """
        request_body_data = None
        url = f"{self.base_url}/accounts/search"
        query_params = {
            k: v
            for k, v in [
                ("q_organization_name", q_organization_name),
                ("account_stage_ids[]", account_stage_ids_),
                ("sort_by_field", sort_by_field),
                ("sort_ascending", sort_ascending),
                ("page", page),
                ("per_page", per_page),
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

    def update_account_stage(
        self, account_ids_: list[str], account_stage_id: str
    ) -> dict[str, Any]:
        """
        Updates multiple account records in bulk by their specified IDs, assigning each to the given account stage ID.

        Args:
            account_ids_ (array): The Apollo ID(s) of the account(s) to update; obtain these IDs by using the Search for Accounts endpoint and referencing each account’s `id` value.
            account_stage_id (string): Specify the Apollo account stage ID to assign to accounts; find available IDs via the List Account Stages endpoint.

        Returns:
            dict[str, Any]: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Accounts
        """
        request_body_data = None
        url = f"{self.base_url}/accounts/bulk_update"
        query_params = {
            k: v
            for k, v in [
                ("account_ids[]", account_ids_),
                ("account_stage_id", account_stage_id),
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

    def update_account_ownership(
        self, account_ids_: list[str], owner_id: str
    ) -> dict[str, Any]:
        """
        Updates the owners of multiple accounts by assigning a specified owner ID to the given list of account IDs.

        Args:
            account_ids_ (array): The Apollo IDs of the accounts to assign new owners; obtain these IDs by using the Search for Accounts endpoint and referencing each account's `id` value.
            owner_id (string): The owner_id is the unique identifier of the user in your Apollo team who will be assigned as the owner of the specified accounts; retrieve user IDs via the Get a List of Users endpoint.

        Returns:
            dict[str, Any]: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Accounts
        """
        request_body_data = None
        url = f"{self.base_url}/accounts/update_owners"
        query_params = {
            k: v
            for k, v in [("account_ids[]", account_ids_), ("owner_id", owner_id)]
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

    def list_account_stages(self) -> dict[str, Any]:
        """
        Retrieves a list of account stages.

        Returns:
            dict[str, Any]: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Accounts
        """
        url = f"{self.base_url}/account_stages"
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

    def create_a_contact(
        self,
        first_name: str | None = None,
        last_name: str | None = None,
        organization_name: str | None = None,
        title: str | None = None,
        account_id: str | None = None,
        email: str | None = None,
        website_url: str | None = None,
        label_names_: list[str] | None = None,
        contact_stage_id: str | None = None,
        present_raw_address: str | None = None,
        direct_phone: str | None = None,
        corporate_phone: str | None = None,
        mobile_phone: str | None = None,
        home_phone: str | None = None,
        other_phone: str | None = None,
    ) -> dict[str, Any]:
        """
        Creates a new contact with specified details such as name, organization, contact information, and labels.

        Args:
            first_name (string): The first name of the contact to be created, provided as a readable human name (e.g., "Tim"). This value identifies the contact in the system.
            last_name (string): The last name of the contact to create, ideally a human-readable full surname.
            organization_name (string): The current employer's exact company name for the contact, used to ensure correct assignment in the Apollo contact base; verify using the Organization Search endpoint if needed.
            title (string): The current job title of the contact, such as 'senior research analyst'.
            account_id (string): Unique Apollo ID for the account to assign the contact, retrieved from Organization Search or enrichment endpoints.
            email (string): String: The email address of the contact; must be a valid, properly formatted email, e.g., example@email.com.
            website_url (string): The full corporate website URL of the contact's current employer, including the domain (e.g., .com), without any subdirectories or social media links, to ensure accurate data enrichment.
            label_names_ (array): Add contact to existing or new lists using any list name; unmatched names create new lists automatically. Example: "2024 big marketing conference attendees".
            contact_stage_id (string): Specify the Apollo contact stage ID to assign the contact; if omitted, Apollo will assign a default stage per your settings. Example: 6095a710bd01d100a506d4ae
            present_raw_address (string): The contact's personal location, which can include city, state, and country, matched to the closest predefined location for accurate identification (e.g., "Atlanta, United States").
            direct_phone (string): Primary phone number for the contact. Enter in any format; Apollo sanitizes it. Examples: `555-303-1234`, `+44 7911 123456`.
            corporate_phone (string): The direct work/office phone number for the contact (not the headquarters), which is sanitized and can be provided in any format; examples: 555-303-1234 or +44 7911 123456.
            mobile_phone (string): Mobile phone number for the contact. Enter in any format; Apollo sanitizes and returns the standardized number.
            home_phone (string): Enter the contact's home phone number in any format; Apollo sanitizes and returns the standardized value in the response.
            other_phone (string): Specifies an alternative or unknown phone type for the contact; Apollo accepts any format and returns sanitized numbers in the response, e.g., '555-303-1234', '+44 7911 123456'.

        Returns:
            dict[str, Any]: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Contacts, important
        """
        request_body_data = None
        url = f"{self.base_url}/contacts"
        query_params = {
            k: v
            for k, v in [
                ("first_name", first_name),
                ("last_name", last_name),
                ("organization_name", organization_name),
                ("title", title),
                ("account_id", account_id),
                ("email", email),
                ("website_url", website_url),
                ("label_names[]", label_names_),
                ("contact_stage_id", contact_stage_id),
                ("present_raw_address", present_raw_address),
                ("direct_phone", direct_phone),
                ("corporate_phone", corporate_phone),
                ("mobile_phone", mobile_phone),
                ("home_phone", home_phone),
                ("other_phone", other_phone),
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

    def update_a_contact(
        self,
        contact_id: str,
        first_name: str | None = None,
        last_name: str | None = None,
        organization_name: str | None = None,
        title: str | None = None,
        account_id: str | None = None,
        email: str | None = None,
        website_url: str | None = None,
        label_names_: list[str] | None = None,
        contact_stage_id: str | None = None,
        present_raw_address: str | None = None,
        direct_phone: str | None = None,
        corporate_phone: str | None = None,
        mobile_phone: str | None = None,
        home_phone: str | None = None,
        other_phone: str | None = None,
    ) -> dict[str, Any]:
        """
        Updates or replaces the details of a specific contact identified by contact_id using the provided parameters as new values for the contact record.

        Args:
            contact_id (string): contact_id
            first_name (string): Update the contact's first name with a human-readable string representing their given name, such as "Tim".
            last_name (string): Sets the contact's last name; expects a readable value (e.g. 'Zheng') for identification purposes.
            organization_name (string): Update the contact's current employer name to match the exact company name in the Apollo database for accurate assignment. Example: `apollo`.
            title (string): Specify the new job title for the contact, e.g., "senior research analyst."
            account_id (string): Unique Apollo ID for updating the account assigned to a contact. Use Organization Search to find account IDs for enriched companies.
            email (string): Update the contact's email address with a valid, unique email string (e.g., example@email.com); duplicate emails will cause an error response.
            website_url (string): Update the full corporate website URL for the contact’s current employer, including the domain (e.g., .com) but excluding any subdirectories or social media links like LinkedIn, to ensure accurate data enrichment.
            label_names_ (array): Update lists the contact belongs to in your Apollo account. If a list does not exist, Apollo creates it. Adding lists removes existing ones unless they are included again.
            contact_stage_id (string): Specifies the Apollo contact stage ID; use this to assign or update the contact stage, available via List Contact Stages. Example: 6095a710bd01d100a506d4af.
            present_raw_address (string): Set the contact's location by providing a city, state, and country, which will be matched to a predefined location.
            direct_phone (string): Update the contact's primary phone number in any format; Apollo automatically sanitizes and standardizes the number, which is returned in the response for confirmation.
            corporate_phone (string): Update the direct office phone number for the contact at their employer; Apollo sanitizes all formats and the cleaned number appears in the response.
            mobile_phone (string): Sets or updates the contact's mobile phone number; accepts any format—Apollo sanitizes and returns the standardized version in the response.
            home_phone (string): Specify the contact’s home phone number; Apollo accepts any format, sanitizes the input, and returns the clean version in the response.
            other_phone (string): Update an alternative or unspecified phone number for the contact; Apollo automatically sanitizes any phone format, with the cleaned number shown in the response.

        Returns:
            dict[str, Any]: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Contacts
        """
        if contact_id is None:
            raise ValueError("Missing required parameter 'contact_id'.")
        request_body_data = None
        url = f"{self.base_url}/contacts/{contact_id}"
        query_params = {
            k: v
            for k, v in [
                ("first_name", first_name),
                ("last_name", last_name),
                ("organization_name", organization_name),
                ("title", title),
                ("account_id", account_id),
                ("email", email),
                ("website_url", website_url),
                ("label_names[]", label_names_),
                ("contact_stage_id", contact_stage_id),
                ("present_raw_address", present_raw_address),
                ("direct_phone", direct_phone),
                ("corporate_phone", corporate_phone),
                ("mobile_phone", mobile_phone),
                ("home_phone", home_phone),
                ("other_phone", other_phone),
            ]
            if v is not None
        }
        response = self._put(
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

    def search_for_contacts(
        self,
        q_keywords: str | None = None,
        contact_stage_ids_: list[str] | None = None,
        sort_by_field: str | None = None,
        sort_ascending: bool | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> dict[str, Any]:
        """
        Searches contacts based on keywords, contact stage IDs, sorting, and pagination parameters, returning a filtered and sorted list of contacts.

        Args:
            q_keywords (string): Narrow search results by adding keywords such as names, job titles, companies, or email addresses.
            contact_stage_ids_ (array): The Apollo IDs of the contact stages to include in the search; multiple IDs return contacts matching any listed stage combined with other search filters.
            sort_by_field (string): Specify which field to sort results by: contact_last_activity_date, contact_email_last_opened_at, contact_email_last_clicked_at, contact_created_at, or contact_updated_at.
            sort_ascending (boolean): Set to `true` to sort matching contacts in ascending order, but only if the `sort_by_field` parameter is specified; otherwise, sorting is ignored.
            per_page (integer): Specifies the number of results to return per page, enhancing search result navigation and performance.
            page (integer): Page size for search results; limits the number of results per page to improve performance.

        Returns:
            dict[str, Any]: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Contacts, important
        """
        request_body_data = None
        url = f"{self.base_url}/contacts/search"
        query_params = {
            k: v
            for k, v in [
                ("q_keywords", q_keywords),
                ("contact_stage_ids[]", contact_stage_ids_),
                ("sort_by_field", sort_by_field),
                ("sort_ascending", sort_ascending),
                ("per_page", per_page),
                ("page", page),
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

    def update_contact_stage(
        self, contact_ids_: list[str], contact_stage_id: str
    ) -> dict[str, Any]:
        """
        Updates the stage of multiple contacts by specifying their IDs and the new contact stage ID via a POST request.

        Args:
            contact_ids_ (array): The Apollo contact IDs to update, provided as an array of strings; obtain these IDs from the Search for Contacts endpoint's `id` field. Example: `66e34b81740c50074e3d1bd4`
            contact_stage_id (string): The Apollo ID of the contact stage to assign to contacts; retrieve valid IDs via the List Contact Stages endpoint. Example: `6095a710bd01d100a506d4af`.

        Returns:
            dict[str, Any]: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Contacts
        """
        request_body_data = None
        url = f"{self.base_url}/contacts/update_stages"
        query_params = {
            k: v
            for k, v in [
                ("contact_ids[]", contact_ids_),
                ("contact_stage_id", contact_stage_id),
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

    def update_contact_ownership(
        self, contact_ids_: list[str], owner_id: str
    ) -> dict[str, Any]:
        """
        Updates the owners of specified contacts by assigning a new owner ID to the provided list of contact IDs.

        Args:
            contact_ids_ (array): The Apollo contact IDs to update ownership for; provide one or more IDs obtained from the Search for Contacts endpoint to assign new owners.
            owner_id (string): Specifies the Apollo account user ID to assign as owner for the contacts; find user IDs via the Get List of Users endpoint. Example: 66302798d03b9601c7934ebf.

        Returns:
            dict[str, Any]: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Contacts
        """
        request_body_data = None
        url = f"{self.base_url}/contacts/update_owners"
        query_params = {
            k: v
            for k, v in [("contact_ids[]", contact_ids_), ("owner_id", owner_id)]
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

    def list_contact_stages(self) -> Any:
        """
        Retrieves a list of all available contact stage IDs from the Apollo account[2][4].

        Returns:
            Any: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Contacts
        """
        url = f"{self.base_url}/contact_stages"
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

    def create_deal(
        self,
        name: str,
        owner_id: str | None = None,
        account_id: str | None = None,
        amount: str | None = None,
        opportunity_stage_id: str | None = None,
        closed_date: str | None = None,
    ) -> dict[str, Any]:
        """
        Creates a new opportunity with specified details such as name, owner, account, amount, stage, and closed date.

        Args:
            name (string): Specify a short, descriptive, human-readable name for the opportunity or deal being created, such as "Massive Q3 Deal."
            owner_id (string): Specify the unique Apollo user ID (found via Get Users endpoint) responsible for the opportunity as the deal owner.
            account_id (string): The unique Apollo account ID for the company targeted in this deal; retrieve via Organization Search as organization_id—example: 5e66b6381e05b4008c8331b8.
            amount (string): The monetary value of the deal to create, entered as a numeric amount without commas or currency symbols; the currency is set automatically from your Apollo account settings.
            opportunity_stage_id (string): The unique identifier for the deal stage in your team's Apollo account; use the List Deal Stages endpoint to retrieve valid IDs for this parameter.
            closed_date (string): The estimated close date for the deal, in YYYY-MM-DD format.

        Returns:
            dict[str, Any]: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Deals
        """
        request_body_data = None
        url = f"{self.base_url}/opportunities"
        query_params = {
            k: v
            for k, v in [
                ("name", name),
                ("owner_id", owner_id),
                ("account_id", account_id),
                ("amount", amount),
                ("opportunity_stage_id", opportunity_stage_id),
                ("closed_date", closed_date),
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

    def list_all_deals(
        self,
        sort_by_field: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> dict[str, Any]:
        """
        Searches and retrieves a paginated list of opportunities with optional sorting by a specified field.

        Args:
            sort_by_field (string): Sort opportunities by one of the following: amount for highest deal values first, is_closed for closed deals first, or is_won for deals marked as won first.
            page (integer): The page query parameter specifies which page of results to retrieve when searching opportunities; use with `per_page` to paginate and optimize response performance.
            per_page (integer): The number of results returned per page in the search response; limiting this improves performance. Use the `page` parameter to access additional pages. Example: `10`.

        Returns:
            dict[str, Any]: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Deals, important
        """
        url = f"{self.base_url}/opportunities/search"
        query_params = {
            k: v
            for k, v in [
                ("sort_by_field", sort_by_field),
                ("page", page),
                ("per_page", per_page),
            ]
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

    def update_deal(
        self,
        opportunity_id: str,
        owner_id: str | None = None,
        name: str | None = None,
        amount: str | None = None,
        opportunity_stage_id: str | None = None,
        closed_date: str | None = None,
        is_closed: bool | None = None,
        is_won: bool | None = None,
        source: str | None = None,
        account_id: str | None = None,
    ) -> dict[str, Any]:
        """
        Updates specific fields of an opportunity resource identified by opportunity_id using a PATCH request[2][4][5].

        Args:
            opportunity_id (string): opportunity_id
            owner_id (string): The ID of the user within your Apollo team to assign as the new owner of the deal; use the List Users endpoint to find valid user IDs.
            name (string): Update the deal’s name with a clear, human-readable title that identifies the opportunity, such as "Massive Q3 Deal."
            amount (string): The monetary value of the deal to update; enter a numeric value without commas or currency symbols—currency is set by your Apollo account settings. Example: 55123478 represents $55,123,478 if USD.
            opportunity_stage_id (string): Unique ID of the deal stage to update an opportunity's status. Replace with a different ID to change the stage.
            closed_date (string): Update the estimated close date for the opportunity, which can be any past or future date, formatted as YYYY-MM-DD (e.g., 2025-10-30).
            is_closed (boolean): Set to true to mark the opportunity as closed, or omit/use false to keep it open.
            is_won (boolean): Set this parameter to `true` in the query to mark the opportunity as won and update the deal status accordingly.
            source (string): Update the source of the deal, e.g., '2024 InfoSec Conference', overriding the default 'api' source for API-created deals.
            account_id (string): Specify the unique account ID to associate or update the company linked to this opportunity; find IDs using the Organization Search endpoint.

        Returns:
            dict[str, Any]: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Deals
        """
        if opportunity_id is None:
            raise ValueError("Missing required parameter 'opportunity_id'.")
        request_body_data = None
        url = f"{self.base_url}/opportunities/{opportunity_id}"
        query_params = {
            k: v
            for k, v in [
                ("owner_id", owner_id),
                ("name", name),
                ("amount", amount),
                ("opportunity_stage_id", opportunity_stage_id),
                ("closed_date", closed_date),
                ("is_closed", is_closed),
                ("is_won", is_won),
                ("source", source),
                ("account_id", account_id),
            ]
            if v is not None
        }
        response = self._patch(url, data=request_body_data, params=query_params)
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

    def list_deal_stages(self) -> dict[str, Any]:
        """
        Retrieves a list of opportunity stages representing the different phases in the sales pipeline.

        Returns:
            dict[str, Any]: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Deals
        """
        url = f"{self.base_url}/opportunity_stages"
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

    def add_contacts_to_sequence(
        self,
        sequence_id: str,
        emailer_campaign_id: str,
        contact_ids_: list[str],
        send_email_from_email_account_id: str,
        sequence_no_email: bool | None = None,
        sequence_unverified_email: bool | None = None,
        sequence_job_change: bool | None = None,
        sequence_active_in_other_campaigns: bool | None = None,
        sequence_finished_in_other_campaigns: bool | None = None,
        user_id: str | None = None,
    ) -> dict[str, Any]:
        """
        Adds specified contact IDs to an email campaign sequence, configuring how and when emails are sent to each contact and supporting various filtering options.

        Args:
            sequence_id (string): sequence_id
            emailer_campaign_id (string): The emailer_campaign_id query parameter must match the sequence_id path parameter and represents the unique identifier of the email campaign to which contacts are being added.
            contact_ids_ (array): Apollo IDs of contacts to add to the sequence. Use the Search for Contacts endpoint to find IDs.
            send_email_from_email_account_id (string): The Apollo ID of the email account used to send emails to contacts added to the sequence; obtain this ID from the Get a List of Email Accounts endpoint.
            sequence_no_email (boolean): Add contacts to the sequence even if they lack an email address by setting this to `true`.
            sequence_unverified_email (boolean): Indicates whether to allow adding contacts with unverified email addresses to the sequence.
            sequence_job_change (boolean): Set to `true` to add contacts to the email sequence even if they have recently changed jobs, overriding any default restrictions on re-adding such contacts.
            sequence_active_in_other_campaigns (boolean): When true, allows adding contacts even if they are already in other sequences, regardless of those sequences’ status (active or paused).
            sequence_finished_in_other_campaigns (boolean): Set to `true` to add contacts to this sequence even if they have completed a different sequence and are marked as finished there.
            user_id (string): The user_id query parameter specifies the ID of the Apollo team user performing the action to add contacts to a sequence, which appears in the sequence's activity log to identify who added the contacts.

        Returns:
            dict[str, Any]: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Contacts
        """
        if sequence_id is None:
            raise ValueError("Missing required parameter 'sequence_id'.")
        request_body_data = None
        url = f"{self.base_url}/emailer_campaigns/{sequence_id}/add_contact_ids"
        query_params = {
            k: v
            for k, v in [
                ("emailer_campaign_id", emailer_campaign_id),
                ("contact_ids[]", contact_ids_),
                ("send_email_from_email_account_id", send_email_from_email_account_id),
                ("sequence_no_email", sequence_no_email),
                ("sequence_unverified_email", sequence_unverified_email),
                ("sequence_job_change", sequence_job_change),
                (
                    "sequence_active_in_other_campaigns",
                    sequence_active_in_other_campaigns,
                ),
                (
                    "sequence_finished_in_other_campaigns",
                    sequence_finished_in_other_campaigns,
                ),
                ("user_id", user_id),
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

    def update_contact_status_sequence(
        self, emailer_campaign_ids_: list[str], contact_ids_: list[str], mode: str
    ) -> dict[str, Any]:
        """
        Posts a request to remove or stop specified contact IDs from given emailer campaign IDs based on the selected mode.

        Args:
            emailer_campaign_ids_ (array): The Apollo sequence IDs to update contact statuses in; providing multiple IDs updates contacts across all specified sequences. Use the Search for Sequences endpoint to find these IDs.
            contact_ids_ (array): Specify the Apollo IDs of contacts to update their sequence status. Obtain IDs via the Search for Contacts endpoint.
            mode (string): Choose one option to update contacts' sequence status: `mark_as_finished` to mark as completed, `remove` to delete from the sequence, or `stop` to pause their progression.

        Returns:
            dict[str, Any]: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Contacts
        """
        request_body_data = None
        url = f"{self.base_url}/emailer_campaigns/remove_or_stop_contact_ids"
        query_params = {
            k: v
            for k, v in [
                ("emailer_campaign_ids[]", emailer_campaign_ids_),
                ("contact_ids[]", contact_ids_),
                ("mode", mode),
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

    def create_task(
        self,
        user_id: str,
        contact_ids_: list[str],
        priority: str,
        due_at: str,
        type: str,
        status: str,
        note: str | None = None,
    ) -> Any:
        """
        Creates multiple tasks in bulk with specified user, contact IDs, priority, due date, type, status, and optional note parameters.

        Args:
            user_id (string): The user_id query parameter specifies the unique identifier of the Apollo team member who will own and take action on the created tasks; retrieve user IDs from the Get a List of Users endpoint.
            contact_ids_ (array): Apollo IDs of contacts to receive the action; multiple IDs create separate tasks with the same details.
            priority (string): Specify the priority level for each task being created in bulk; valid values are "high," "medium," or "low" to indicate urgency.
            due_at (string): The full date and time when the task is due, in ISO 8601 format. Use GMT by default or specify a time zone offset (e.g., `2025-02-15T08:10:30Z`, `2025-03-25T10:15:30+05:00`).
            type (string): Specify the task type to clarify the action required: `call` to call contacts, `outreach_manual_email` to email, `linkedin_step_connect` to send connection invites, `linkedin_step_message` to message on LinkedIn, `linkedin_step_view_profile` to view
            status (string): The status of the task being created. Use `scheduled` for future tasks, `completed` for finished tasks, or `archived` for completed tasks no longer needed.
            note (string): Optional task note: human-readable description to give context for the action required. Example: "Contact interested in Sequences; discuss details."

        Returns:
            Any: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tasks
        """
        request_body_data = None
        url = f"{self.base_url}/tasks/bulk_create"
        query_params = {
            k: v
            for k, v in [
                ("user_id", user_id),
                ("contact_ids[]", contact_ids_),
                ("priority", priority),
                ("due_at", due_at),
                ("type", type),
                ("status", status),
                ("note", note),
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

    def search_tasks(
        self,
        sort_by_field: str | None = None,
        open_factor_names_: list[str] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> dict[str, Any]:
        """
        Searches for tasks using specified parameters and returns a paginated list of results, allowing users to sort by a field and filter by open factor names.

        Args:
            sort_by_field (string): Specify field to sort tasks: 'task_due_at' (most future first) or 'task_priority' (highest first).
            open_factor_names_ (array): Enter `task_types` to receive a count of tasks grouped by each task type; the response will include a `task_types` array with counts for each type.
            page (integer): The page query parameter specifies which page of Apollo data to retrieve, used with per_page to paginate results and optimize search performance; for example, 4.
            per_page (integer): The number of search results returned per page to improve response performance; use the `page` parameter to access additional pages. Example: `10`.

        Returns:
            dict[str, Any]: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Tasks
        """
        request_body_data = None
        url = f"{self.base_url}/tasks/search"
        query_params = {
            k: v
            for k, v in [
                ("sort_by_field", sort_by_field),
                ("open_factor_names[]", open_factor_names_),
                ("page", page),
                ("per_page", per_page),
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

    def get_a_list_of_users(
        self, page: int | None = None, per_page: int | None = None
    ) -> dict[str, Any]:
        """
        Searches for users with optional pagination parameters to specify the page number and number of results per page.

        Args:
            page (integer): The page number of results to retrieve in the search, used with `per_page` to paginate and improve response performance; for example, `4`.
            per_page (integer): The number of search results returned per page to control response size and improve performance; use the `page` parameter to access additional pages. Example: 10.

        Returns:
            dict[str, Any]: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Users
        """
        url = f"{self.base_url}/users/search"
        query_params = {
            k: v for k, v in [("page", page), ("per_page", per_page)] if v is not None
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

    def get_a_list_of_email_accounts(self) -> dict[str, Any]:
        """
        Retrieves a list of all available email accounts and their summary information.

        Returns:
            dict[str, Any]: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Email Accounts
        """
        url = f"{self.base_url}/email_accounts"
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

    def get_a_list_of_all_liststags(self) -> list[Any]:
        """
        Retrieves a list of labels.

        Returns:
            list[Any]: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Labels
        """
        url = f"{self.base_url}/labels"
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

    def get_a_list_of_all_custom_fields(self) -> dict[str, Any]:
        """
        Retrieves a list of all typed custom fields configured in the system.

        Returns:
            dict[str, Any]: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Custom Fields
        """
        url = f"{self.base_url}/typed_custom_fields"
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

    def view_deal(self, opportunity_id: str) -> dict[str, Any]:
        """
        View Deal by opportunity_id

        Args:
            opportunity_id (string): opportunity_id

        Returns:
            dict[str, Any]: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        if opportunity_id is None:
            raise ValueError("Missing required parameter 'opportunity_id'.")
        url = f"{self.base_url}/opportunities/{opportunity_id}"
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

    def search_for_sequences(
        self,
        q_name: str | None = None,
        page: str | None = None,
        per_page: str | None = None,
    ) -> dict[str, Any]:
        """
        Search for Sequences by name

        Args:
            q_name (string): Add keywords to narrow the search of the sequences in your team's Apollo account. <br><br>Keywords should directly match at least part of a sequence's name. For example, searching the keyword `marketing` might return the result `NY Marketing Sequence`, but not `NY Marketer Conference 2025 attendees`. <br><br>This parameter only searches sequence names, not other sequence fields. <br><br>Example: `marketing conference attendees`
            page (string): The page number of the Apollo data that you want to retrieve. <br><br>Use this parameter in combination with the `per_page` parameter to make search results for navigable and improve the performance of the endpoint. <br><br>Example: `4`
            per_page (string): The number of search results that should be returned for each page. Limited the number of results per page improves the endpoint's performance. <br><br>Use the `page` parameter to search the different pages of data. <br><br>Example: `10`

        Returns:
            dict[str, Any]: 200

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.
        """
        request_body_data = None
        url = f"{self.base_url}/emailer_campaigns/search"
        query_params = {
            k: v
            for k, v in [("q_name", q_name), ("page", page), ("per_page", per_page)]
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

    def list_tools(self):
        return [
            self.people_enrichment,
            self.bulk_people_enrichment,
            self.organization_enrichment,
            self.bulk_organization_enrichment,
            self.people_search,
            self.organization_search,
            self.organization_jobs_postings,
            self.create_an_account,
            self.update_an_account,
            self.search_for_accounts,
            self.update_account_stage,
            self.update_account_ownership,
            self.list_account_stages,
            self.create_a_contact,
            self.update_a_contact,
            self.search_for_contacts,
            self.update_contact_stage,
            self.update_contact_ownership,
            self.list_contact_stages,
            self.create_deal,
            self.list_all_deals,
            self.update_deal,
            self.list_deal_stages,
            self.add_contacts_to_sequence,
            self.update_contact_status_sequence,
            self.create_task,
            self.search_tasks,
            self.get_a_list_of_users,
            self.get_a_list_of_email_accounts,
            self.get_a_list_of_all_liststags,
            self.get_a_list_of_all_custom_fields,
            self.view_deal,
            self.search_for_sequences,
        ]
