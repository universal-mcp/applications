from dotenv import load_dotenv

load_dotenv()

from typing import Any

from loguru import logger
from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration

from universal_mcp.applications.unipile import UnipileApp


class ScraperApp(APIApplication):
    """
    Application for interacting with LinkedIn API.
    Provides a simplified interface for LinkedIn search operations.
    """

    def __init__(self, integration: Integration, **kwargs: Any) -> None:
        """
        Initialize the ScraperApp.

        Args:
            integration: The integration configuration containing credentials and other settings.
                         It is expected that the integration provides the necessary credentials
                         for LinkedIn API access.
        """
        super().__init__(name="scraper", integration=integration, **kwargs)
        if self.integration:
            credentials = self.integration.get_credentials()
            self.account_id = credentials.get("account_id")
            self._unipile_app = UnipileApp(integration=self.integration)
        else:
            logger.warning("Integration not found")
            self.account_id = None
            self._unipile_app = None

    def linkedin_post_search(
        self,
        category: str = "posts",
        api: str = "classic",
        cursor: str | None = None,
        limit: int | None = None,
        keywords: str | None = None,
        sort_by: str | None = None,
        date_posted: str | None = None,
        content_type: str | None = None,
    ) -> dict[str, Any]:
        """
        Performs a general LinkedIn search for posts using keywords and filters like date and content type. It supports pagination and can utilize either the 'classic' or 'sales_navigator' API, searching broadly across the platform rather than fetching posts from a specific user's profile.

        Args:
            category: Type of search to perform (defaults to "posts").
            api: Which LinkedIn API to use - "classic" or "sales_navigator".
            cursor: Pagination cursor for the next page of entries.
            limit: Number of items to return (up to 50 for Classic search).
            keywords: Keywords to search for.
            sort_by: How to sort the results, e.g., "relevance" or "date".
            date_posted: Filter posts by when they were posted.
            content_type: Filter by the type of content in the post. Example: "videos", "images", "live_videos", "collaborative_articles", "documents"

        Returns:
            A dictionary containing search results and pagination details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, search, posts, api, scrapper, important
        """

        return self._unipile_app.search(
            account_id=self.account_id,
            category=category,
            api=api,
            cursor=cursor,
            limit=limit,
            keywords=keywords,
            sort_by=sort_by,
            date_posted=date_posted,
            content_type=content_type,
        )

    def linkedin_list_profile_posts(
        self,
        identifier: str,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        """
        Fetches a paginated list of all LinkedIn posts from a specific user or company profile using their unique identifier. This function retrieves content directly from a profile, unlike `linkedin_post_search` which finds posts across LinkedIn based on keywords and other filters.

        Args:
            identifier: The entity's provider internal ID (LinkedIn ID).starts with ACo for users, while for companies it's a series of numbers.
            cursor: Pagination cursor for the next page of entries.
            limit: Number of items to return (1-100, though spec allows up to 250).

        Returns:
            A dictionary containing a list of post objects and pagination details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, post, list, user_posts, company_posts, content, api, important
        """

        return self._unipile_app.list_profile_posts(
            identifier=identifier,
            account_id=self.account_id,
            cursor=cursor,
            limit=limit,
        )

    def linkedin_retrieve_profile(
        self,
        identifier: str,
    ) -> dict[str, Any]:
        """
        Retrieves a specific LinkedIn user's profile by their unique identifier, which can be an internal provider ID or a public username. This function simplifies data access by delegating the actual profile retrieval request to the integrated Unipile application, distinct from functions that list posts or comments.

        Args:
            identifier: Can be the provider's internal id OR the provider's public id of the requested user.
                       For example, for https://www.linkedin.com/in/manojbajaj95/, the identifier is "manojbajaj95".

        Returns:
            A dictionary containing the user's profile details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, user, profile, retrieve, get, api, important
        """

        return self._unipile_app.retrieve_user_profile(
            identifier=identifier,
            account_id=self.account_id,
        )

    def linkedin_list_post_comments(
        self,
        post_id: str,
        comment_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        """
        Fetches comments for a specified LinkedIn post. If a `comment_id` is provided, it retrieves replies to that comment instead of top-level comments. This function supports pagination and specifically targets comments, unlike others in the class that search for or list entire posts.

        Args:
            post_id: The social ID of the post. Example rn:li:activity:7342082869034393600
            comment_id: If provided, retrieves replies to this comment ID instead of top-level comments.
            cursor: Pagination cursor.
            limit: Number of comments to return.

        Returns:
            A dictionary containing a list of comment objects and pagination details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, post, comment, list, content, api, important
        """

        return self._unipile_app.list_post_comments(
            post_id=post_id,
            account_id=self.account_id,
            comment_id=comment_id,
            cursor=cursor,
            limit=limit,
        )

    def linkedin_people_search(
        self,
        cursor: str | None = None,
        limit: int | None = None,
        keywords: str | None = None,
        last_viewed_at: int | None = None,
        saved_search_id: str | None = None,
        recent_search_id: str | None = None,
        location: dict[str, Any] | None = None,
        location_by_postal_code: dict[str, Any] | None = None,
        industry: dict[str, Any] | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        tenure: list[dict[str, Any]] | None = None,
        groups: list[str] | None = None,
        school: dict[str, Any] | None = None,
        profile_language: list[str] | None = None,
        company: dict[str, Any] | None = None,
        company_headcount: list[dict[str, Any]] | None = None,
        company_type: list[str] | None = None,
        company_location: dict[str, Any] | None = None,
        tenure_at_company: list[dict[str, Any]] | None = None,
        past_company: dict[str, Any] | None = None,
        function: dict[str, Any] | None = None,
        role: dict[str, Any] | None = None,
        tenure_at_role: list[dict[str, Any]] | None = None,
        seniority: dict[str, Any] | None = None,
        past_role: dict[str, Any] | None = None,
        following_your_company: bool | None = None,
        viewed_your_profile_recently: bool | None = None,
        network_distance: list[str] | None = None,
        connections_of: list[str] | None = None,
        past_colleague: bool | None = None,
        shared_experiences: bool | None = None,
        changed_jobs: bool | None = None,
        posted_on_linkedin: bool | None = None,
        mentionned_in_news: bool | None = None,
        persona: list[str] | None = None,
        account_lists: dict[str, Any] | None = None,
        lead_lists: dict[str, Any] | None = None,
        viewed_profile_recently: bool | None = None,
        messaged_recently: bool | None = None,
        include_saved_leads: bool | None = None,
        include_saved_accounts: bool | None = None,
    ) -> dict[str, Any]:
        """
        Performs a comprehensive LinkedIn Sales Navigator people search with advanced targeting options.
        This function provides access to LinkedIn's Sales Navigator search capabilities for finding people
        with precise filters including experience, company details, education, and relationship criteria.

        Args:
            cursor: Pagination cursor for the next page of entries.
            limit: Number of items to return.
            keywords: LinkedIn native filter: KEYWORDS.
            last_viewed_at: Unix timestamp for saved search filtering.
            saved_search_id: ID of saved search (overrides other parameters).
            recent_search_id: ID of recent search (overrides other parameters).
            location: LinkedIn native filter: GEOGRAPHY. Example: {"include": ["San Francisco Bay Area", "New York City Area"]}
            location_by_postal_code: Location filter by postal code. Example: {"postal_code": "94105", "radius": "25"}
            industry: LinkedIn native filter: INDUSTRY. Example: {"include": ["Information Technology and Services", "Financial Services"]}
            first_name: LinkedIn native filter: FIRST NAME. Example: "John"
            last_name: LinkedIn native filter: LAST NAME. Example: "Smith"
            tenure: LinkedIn native filter: YEARS OF EXPERIENCE. Example: [{"min": 5, "max": 10}]
            groups: LinkedIn native filter: GROUPS. Example: ["group_id_1", "group_id_2"]
            school: LinkedIn native filter: SCHOOL. Example: {"include": ["Stanford University", "Harvard University"]}
            profile_language: ISO 639-1 language codes, LinkedIn native filter: PROFILE LANGUAGE. Example: ["en", "es"]
            company: LinkedIn native filter: CURRENT COMPANY. Example: {"include": ["Google", "Microsoft", "Apple"]}
            company_headcount: LinkedIn native filter: COMPANY HEADCOUNT. Example: [{"min": 100, "max": 1000}]
            company_type: LinkedIn native filter: COMPANY TYPE. Example: ["Public Company", "Privately Held"]
            company_location: LinkedIn native filter: COMPANY HEADQUARTERS LOCATION. Example: {"include": ["San Francisco", "Seattle"]}
            tenure_at_company: LinkedIn native filter: YEARS IN CURRENT COMPANY. Example: [{"min": 2, "max": 5}]
            past_company: LinkedIn native filter: PAST COMPANY. Example: {"include": ["Facebook", "Amazon"]}
            function: LinkedIn native filter: FUNCTION. Example: {"include": ["Engineering", "Sales", "Marketing"]}
            role: LinkedIn native filter: CURRENT JOB TITLE. Example: {"include": ["Software Engineer", "Product Manager"]}
            tenure_at_role: LinkedIn native filter: YEARS IN CURRENT POSITION. Example: [{"min": 1, "max": 3}]
            seniority: LinkedIn native filter: SENIORITY LEVEL. Example: {"include": ["Senior", "Director", "VP"]}
            past_role: LinkedIn native filter: PAST JOB TITLE. Example: {"include": ["Senior Developer", "Team Lead"]}
            following_your_company: LinkedIn native filter: FOLLOWING YOUR COMPANY. Example: True
            viewed_your_profile_recently: LinkedIn native filter: VIEWED YOUR PROFILE RECENTLY. Example: True
            network_distance: First, second, third+ degree or GROUP, LinkedIn native filter: CONNECTION. Example: ["1st", "2nd"]
            connections_of: LinkedIn native filter: CONNECTIONS OF. Example: ["person_id_1", "person_id_2"]
            past_colleague: LinkedIn native filter: PAST COLLEAGUE. Example: True
            shared_experiences: LinkedIn native filter: SHARED EXPERIENCES. Example: True
            changed_jobs: LinkedIn native filter: CHANGED JOBS. Example: True
            posted_on_linkedin: LinkedIn native filter: POSTED ON LINKEDIN. Example: True
            mentionned_in_news: LinkedIn native filter: MENTIONNED IN NEWS. Example: True
            persona: LinkedIn native filter: PERSONA. Example: ["persona_id_1", "persona_id_2"]
            account_lists: LinkedIn native filter: ACCOUNT LISTS. Example: {"include": ["list_id_1"]}
            lead_lists: LinkedIn native filter: LEAD LISTS. Example: {"include": ["lead_list_id_1"]}
            viewed_profile_recently: LinkedIn native filter: PEOPLE YOU INTERACTED WITH / VIEWED PROFILE. Example: True
            messaged_recently: LinkedIn native filter: PEOPLE YOU INTERACTED WITH / MESSAGED. Example: True
            include_saved_leads: LinkedIn native filter: SAVED LEADS AND ACCOUNTS / ALL MY SAVED LEADS. Example: True
            include_saved_accounts: LinkedIn native filter: SAVED LEADS AND ACCOUNTS / ALL MY SAVED ACCOUNTS. Example: True

        Returns:
            A dictionary containing search results and pagination details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, sales_navigator, people, search, advanced, scraper, api, important
        """
        return self._unipile_app.people_search(
            account_id=self.account_id,
            cursor=cursor,
            limit=limit,
            keywords=keywords,
            last_viewed_at=last_viewed_at,
            saved_search_id=saved_search_id,
            recent_search_id=recent_search_id,
            location=location,
            location_by_postal_code=location_by_postal_code,
            industry=industry,
            first_name=first_name,
            last_name=last_name,
            tenure=tenure,
            groups=groups,
            school=school,
            profile_language=profile_language,
            company=company,
            company_headcount=company_headcount,
            company_type=company_type,
            company_location=company_location,
            tenure_at_company=tenure_at_company,
            past_company=past_company,
            function=function,
            role=role,
            tenure_at_role=tenure_at_role,
            seniority=seniority,
            past_role=past_role,
            following_your_company=following_your_company,
            viewed_your_profile_recently=viewed_your_profile_recently,
            network_distance=network_distance,
            connections_of=connections_of,
            past_colleague=past_colleague,
            shared_experiences=shared_experiences,
            changed_jobs=changed_jobs,
            posted_on_linkedin=posted_on_linkedin,
            mentionned_in_news=mentionned_in_news,
            persona=persona,
            account_lists=account_lists,
            lead_lists=lead_lists,
            viewed_profile_recently=viewed_profile_recently,
            messaged_recently=messaged_recently,
            include_saved_leads=include_saved_leads,
            include_saved_accounts=include_saved_accounts,
        )

    def linkedin_company_search(
        self,
        cursor: str | None = None,
        limit: int | None = None,
        keywords: str | None = None,
        last_viewed_at: int | None = None,
        saved_search_id: str | None = None,
        recent_search_id: str | None = None,
        location: dict[str, Any] | None = None,
        location_by_postal_code: dict[str, Any] | None = None,
        industry: dict[str, Any] | None = None,
        company_headcount: list[dict[str, Any]] | None = None,
        company_type: list[str] | None = None,
        company_location: dict[str, Any] | None = None,
        following_your_company: bool | None = None,
        account_lists: dict[str, Any] | None = None,
        include_saved_accounts: bool | None = None,
    ) -> dict[str, Any]:
        """
        Performs a comprehensive LinkedIn Sales Navigator company search with advanced targeting options.
        This function provides access to LinkedIn's Sales Navigator search capabilities for finding companies
        with precise filters including size, location, industry, and relationship criteria.

        Args:
            cursor: Pagination cursor for the next page of entries.
            limit: Number of items to return.
            keywords: LinkedIn native filter: KEYWORDS. Example: "fintech startup"
            last_viewed_at: Unix timestamp for saved search filtering.
            saved_search_id: ID of saved search (overrides other parameters).
            recent_search_id: ID of recent search (overrides other parameters).
            location: LinkedIn native filter: GEOGRAPHY. Example: {"include": ["San Francisco Bay Area", "New York City Area"]}
            location_by_postal_code: Location filter by postal code. Example: {"postal_code": "94105", "radius": "25"}
            industry: LinkedIn native filter: INDUSTRY. Example: {"include": ["Information Technology and Services", "Financial Services"]}
            company_headcount: LinkedIn native filter: COMPANY HEADCOUNT. Example: [{"min": 10, "max": 100}]
            company_type: LinkedIn native filter: COMPANY TYPE. Example: ["Public Company", "Privately Held", "Startup"]
            company_location: LinkedIn native filter: COMPANY HEADQUARTERS LOCATION. Example: {"include": ["San Francisco", "Seattle", "Austin"]}
            following_your_company: LinkedIn native filter: FOLLOWING YOUR COMPANY. Example: True
            account_lists: LinkedIn native filter: ACCOUNT LISTS. Example: {"include": ["account_list_id_1"]}
            include_saved_accounts: LinkedIn native filter: SAVED LEADS AND ACCOUNTS / ALL MY SAVED ACCOUNTS. Example: True

        Returns:
            A dictionary containing search results and pagination details.

        Raises:
            httpx.HTTPError: If the API request fails.

        Tags:
            linkedin, sales_navigator, companies, search, advanced, scraper, api, important
        """
        return self._unipile_app.company_search(
            account_id=self.account_id,
            cursor=cursor,
            limit=limit,
            keywords=keywords,
            last_viewed_at=last_viewed_at,
            saved_search_id=saved_search_id,
            recent_search_id=recent_search_id,
            location=location,
            location_by_postal_code=location_by_postal_code,
            industry=industry,
            company_headcount=company_headcount,
            company_type=company_type,
            company_location=company_location,
            following_your_company=following_your_company,
            account_lists=account_lists,
            include_saved_accounts=include_saved_accounts,
        )

    def list_tools(self):
        """
        Returns a list of available tools/functions in this application.

        Returns:
            A list of functions that can be used as tools.
        """
        return [
            self.linkedin_post_search,
            self.linkedin_list_profile_posts,
            self.linkedin_retrieve_profile,
            self.linkedin_list_post_comments,
            self.linkedin_people_search,
            self.linkedin_company_search,
        ]
