from typing import Any

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class SemanticscholarApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="semanticscholar", integration=integration, **kwargs)
        self.base_url = "/graph/v1"

    def post_graph_get_authors(self, fields=None, ids=None) -> dict[str, Any]:
        """
        Creates a batch of authors using the provided JSON data in the request body, optionally specifying fields to include in the response via a query parameter.

        Args:
            fields (string): Specifies the fields to be included in the API response for the POST operation, allowing customization of the returned data by explicitly listing the desired fields.
            ids (array): ids

        Returns:
            dict[str, Any]: List of authors with default or requested fields

        Tags:
            Author Data
        """
        request_body = {
            "ids": ids,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/author/batch"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_graph_get_author_search(
        self, query, offset=None, limit=None, fields=None
    ) -> dict[str, Any]:
        """
        Searches for authors based on a query string with optional pagination and field selection parameters.

        Args:
            query (string): Search query string for author search, specifying the terms to find matching authors.
            offset (integer): The offset query parameter specifies the number of initial items to skip in the result set, used for pagination starting from zero by default.
            limit (integer): Number of results to return for the search query, defaults to 100 if not specified.
            fields (string): Specifies which fields of the author data to include in the search results, allowing clients to select only the necessary information.

        Returns:
            dict[str, Any]: Batch of authors with default or requested fields

        Tags:
            Author Data
        """
        url = f"{self.base_url}/author/search"
        query_params = {
            k: v
            for k, v in [
                ("offset", offset),
                ("limit", limit),
                ("fields", fields),
                ("query", query),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_graph_get_author(self, author_id, fields=None) -> dict[str, Any]:
        """
        Retrieves the profile information for a specific author identified by the `author_id` and returns it with optional fields specified in the `fields` query parameter.

        Args:
            author_id (string): author_id
            fields (string): Specify the fields to include in the response for the author; for example, "id,name,email" to retrieve only the author's ID, name, and email.

        Returns:
            dict[str, Any]: Author with default or requested fields

        Tags:
            Author Data
        """
        if author_id is None:
            raise ValueError("Missing required parameter 'author_id'")
        url = f"{self.base_url}/author/{author_id}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_graph_get_author_papers(
        self, author_id, offset=None, limit=None, fields=None
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of papers authored by the specified author, with optional field selection.

        Args:
            author_id (string): author_id
            offset (integer): The "offset" parameter is an integer value used to exclude the first N items from the response, determining the starting point for retrieving a subset of the author's papers.
            limit (integer): The number of papers to return per page, defaults to 100.
            fields (string): A comma-separated list of fields to include in the response for the author's papers, allowing clients to specify only the fields they need.

        Returns:
            dict[str, Any]: List of papers with default or requested fields

        Tags:
            Author Data
        """
        if author_id is None:
            raise ValueError("Missing required parameter 'author_id'")
        url = f"{self.base_url}/author/{author_id}/papers"
        query_params = {
            k: v
            for k, v in [("offset", offset), ("limit", limit), ("fields", fields)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_graph_get_paper_autocomplete(self, query) -> dict[str, Any]:
        """
        Provides an autocomplete suggestion list based on a required query string parameter.

        Args:
            query (string): Mandatory search string used to retrieve autocomplete suggestions for papers.

        Returns:
            dict[str, Any]: Batch of papers with default or requested fields

        Tags:
            Paper Data
        """
        url = f"{self.base_url}/paper/autocomplete"
        query_params = {k: v for k, v in [("query", query)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def post_graph_get_papers(self, fields=None, ids=None) -> dict[str, Any]:
        """
        Creates a batch of papers using JSON data in the request body and optionally specifies fields to include in the response.

        Args:
            fields (string): Specifies the fields to be included in the response for the batch paper operation, allowing clients to select only the needed fields.
            ids (array): ids

        Returns:
            dict[str, Any]: List of papers with default or requested fields

        Tags:
            Paper Data
        """
        request_body = {
            "ids": ids,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/paper/batch"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_graph_paper_relevance_search(
        self,
        query,
        fields=None,
        publicationTypes=None,
        openAccessPdf=None,
        minCitationCount=None,
        publicationDateOrYear=None,
        year=None,
        venue=None,
        fieldsOfStudy=None,
        offset=None,
        limit=None,
    ) -> dict[str, Any]:
        """
        Searches for academic papers using the "GET" method at the "/paper/search" endpoint, allowing filtering by query, publication types, open access PDF availability, citation count, publication date or year, venue, fields of study, and pagination parameters.

        Args:
            query (string): A required string parameter used to specify the search query for retrieving papers.
            fields (string): Specifies the fields to be included in the search results, allowing selective retrieval of relevant data.
            publicationTypes (string): Filter by specific types of publications, such as books, articles, or journals, using a comma-separated list of string values.
            openAccessPdf (string): Filter search results to only include papers that have an open access PDF available.
            minCitationCount (string): Restricts search results to academic papers with a minimum number of citations specified by the user.
            publicationDateOrYear (string): Optional query parameter to filter search results by specifying either the exact publication date or the year of publication.
            year (string): The **year** parameter is a query string parameter of type **string** used to filter search results by a specific year when retrieving papers via the **GET /paper/search** operation.
            venue (string): Filter search results to include only papers published in the specified venue.
            fieldsOfStudy (string): Specifies the fields of study to filter the search results by, accepting a string value.
            offset (integer): The offset query parameter specifies the number of items to skip before starting to return results, enabling pagination by defining the starting point in the dataset (default is 0).
            limit (integer): Specifies the maximum number of results to return in the response, with a default value of 100.

        Returns:
            dict[str, Any]: Batch of papers with default or requested fields

        Tags:
            Paper Data
        """
        url = f"{self.base_url}/paper/search"
        query_params = {
            k: v
            for k, v in [
                ("query", query),
                ("fields", fields),
                ("publicationTypes", publicationTypes),
                ("openAccessPdf", openAccessPdf),
                ("minCitationCount", minCitationCount),
                ("publicationDateOrYear", publicationDateOrYear),
                ("year", year),
                ("venue", venue),
                ("fieldsOfStudy", fieldsOfStudy),
                ("offset", offset),
                ("limit", limit),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_graph_paper_bulk_search(
        self,
        query,
        token=None,
        fields=None,
        sort=None,
        publicationTypes=None,
        openAccessPdf=None,
        minCitationCount=None,
        publicationDateOrYear=None,
        year=None,
        venue=None,
        fieldsOfStudy=None,
    ) -> dict[str, Any]:
        """
        Retrieves bulk search results of academic papers based on various query parameters such as keywords, fields of study, publication types, and sorting criteria.

        Args:
            query (string): Mandatory search query string to specify the search criteria for bulk paper search.
            token (string): Required authentication token for secure access to the bulk paper search operation.
            fields (string): A comma-separated list of fields to include in the bulk search response, allowing clients to specify which fields they need.
            sort (string): Specifies the field to sort the search results by, allowing clients to order the data in ascending or descending order based on the specified field.
            publicationTypes (string): Filter search results by specifying one or more publication types, using a comma-separated list of string values.
            openAccessPdf (string): A query parameter to specify whether to include open access PDFs in the bulk paper search results.
            minCitationCount (string): Restricts the search results to include only papers with a minimum number of citations specified by this parameter.
            publicationDateOrYear (string): The publication date or year of papers to search for, specified as a string.
            year (string): Specifies the year to filter the search results for bulk paper data.
            venue (string): Specifies the venue to filter papers in the bulk search results.
            fieldsOfStudy (string): A query string parameter to specify fields of study for filtering search results in bulk paper searches.

        Returns:
            dict[str, Any]: Batch of papers with default or requested fields

        Tags:
            Paper Data
        """
        url = f"{self.base_url}/paper/search/bulk"
        query_params = {
            k: v
            for k, v in [
                ("query", query),
                ("token", token),
                ("fields", fields),
                ("sort", sort),
                ("publicationTypes", publicationTypes),
                ("openAccessPdf", openAccessPdf),
                ("minCitationCount", minCitationCount),
                ("publicationDateOrYear", publicationDateOrYear),
                ("year", year),
                ("venue", venue),
                ("fieldsOfStudy", fieldsOfStudy),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_graph_paper_title_search(
        self,
        query,
        fields=None,
        publicationTypes=None,
        openAccessPdf=None,
        minCitationCount=None,
        publicationDateOrYear=None,
        year=None,
        venue=None,
        fieldsOfStudy=None,
    ) -> dict[str, Any]:
        """
        Searches for matching papers based on specified query parameters, such as query string, fields, publication types, open access status, citation count, publication date, year, venue, and fields of study, using the "GET" method.

        Args:
            query (string): **Search term to match papers by keyword or phrase.**
            fields (string): Allows users to specify which fields to include in the response for the matched paper search results.
            publicationTypes (string): Filter search results to include only papers matching the specified publication types.
            openAccessPdf (string): Filter search results to only include papers that have an open access PDF available.
            minCitationCount (string): Restricts search results to papers with a citation count greater than or equal to the specified minimum value.
            publicationDateOrYear (string): Specifies the publication date or year for filtering papers in the search results.
            year (string): Specifies the year filter for the search results.
            venue (string): The "venue" query parameter specifies the name of the publication venue to filter papers in the search results.
            fieldsOfStudy (string): A comma-separated list of fields of study to match during the search operation.

        Returns:
            dict[str, Any]: Best Title match paper with default or requested fields

        Tags:
            Paper Data ,important
        """
        url = f"{self.base_url}/paper/search/match"
        query_params = {
            k: v
            for k, v in [
                ("query", query),
                ("fields", fields),
                ("publicationTypes", publicationTypes),
                ("openAccessPdf", openAccessPdf),
                ("minCitationCount", minCitationCount),
                ("publicationDateOrYear", publicationDateOrYear),
                ("year", year),
                ("venue", venue),
                ("fieldsOfStudy", fieldsOfStudy),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_graph_get_paper(self, paper_id, fields=None) -> dict[str, Any]:
        """
        Retrieves details of a paper by its ID, optionally specifying fields to include in the response.

        Args:
            paper_id (string): paper_id
            fields (string): Specifies the fields to include in the response when retrieving a paper by ID, allowing clients to select only the necessary data.

        Returns:
            dict[str, Any]: Paper with default or requested fields

        Tags:
            Paper Data
        """
        if paper_id is None:
            raise ValueError("Missing required parameter 'paper_id'")
        url = f"{self.base_url}/paper/{paper_id}"
        query_params = {k: v for k, v in [("fields", fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_graph_get_paper_authors(
        self, paper_id, offset=None, limit=None, fields=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of authors for a specific paper identified by the `paper_id`, allowing optional parameters for offset, limit, and fields to customize the response.

        Args:
            paper_id (string): paper_id
            offset (integer): The "offset" parameter specifies the starting point for retrieving authors, excluding the first N items from the response, with a default value of 0.
            limit (integer): The "limit" parameter, located in the query string, specifies the maximum number of authors to return in the response for the given paper ID, with a default value of 100.
            fields (string): Optional string parameter to specify which fields of the authors should be included in the response.

        Returns:
            dict[str, Any]: List of Authors with default or requested fields

        Tags:
            Paper Data
        """
        if paper_id is None:
            raise ValueError("Missing required parameter 'paper_id'")
        url = f"{self.base_url}/paper/{paper_id}/authors"
        query_params = {
            k: v
            for k, v in [("offset", offset), ("limit", limit), ("fields", fields)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_graph_get_paper_citations(
        self, paper_id, offset=None, limit=None, fields=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of citations for a specific paper, identified by its paper ID, with optional parameters for offset, limit, and fields.

        Args:
            paper_id (string): paper_id
            offset (integer): The "offset" parameter specifies the starting point for retrieving citations, skipping the first N items in the list, with a default value of 0.
            limit (integer): The "limit" parameter specifies the maximum number of citations to return for the specified paper, with a default value of 100.
            fields (string): Specifies the fields to be included in the response for the citations of a paper.

        Returns:
            dict[str, Any]: Batch of citations with default or requested fields

        Tags:
            Paper Data
        """
        if paper_id is None:
            raise ValueError("Missing required parameter 'paper_id'")
        url = f"{self.base_url}/paper/{paper_id}/citations"
        query_params = {
            k: v
            for k, v in [("offset", offset), ("limit", limit), ("fields", fields)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_graph_get_paper_references(
        self, paper_id, offset=None, limit=None, fields=None
    ) -> dict[str, Any]:
        """
        Retrieves references for a specific paper by its ID using the "GET" method and allows optional filtering by offset, limit, and fields for customizable output.

        Args:
            paper_id (string): paper_id
            offset (integer): Determines the starting point in the list of references for the specified paper by excluding the first N items.
            limit (integer): The "limit" parameter, an integer value, specifies the maximum number of references to return for a given paper, defaulting to 100 if not provided.
            fields (string): Specifies the fields to include in the response for the references of a paper, allowing clients to select specific data to retrieve.

        Returns:
            dict[str, Any]: Batch of references with default or requested fields

        Tags:
            Paper Data
        """
        if paper_id is None:
            raise ValueError("Missing required parameter 'paper_id'")
        url = f"{self.base_url}/paper/{paper_id}/references"
        query_params = {
            k: v
            for k, v in [("offset", offset), ("limit", limit), ("fields", fields)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_snippet_search(self, query, limit=None) -> dict[str, Any]:
        """
        Retrieves a list of search results based on a specified query string, optionally limited by a user-defined number of results, using the "GET" method at the "/snippet/search" endpoint.

        Args:
            query (string): The search query string used to specify the text or keywords to search for snippets.
            limit (integer): Maximum number of snippet results to return in the search response, defaulting to 10.

        Returns:
            dict[str, Any]: Best snippet match with default fields

        Tags:
            Snippet Text
        """
        url = f"{self.base_url}/snippet/search"
        query_params = {
            k: v for k, v in [("query", query), ("limit", limit)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [
            self.post_graph_get_authors,
            self.get_graph_get_author_search,
            self.get_graph_get_author,
            self.get_graph_get_author_papers,
            self.get_graph_get_paper_autocomplete,
            self.post_graph_get_papers,
            self.get_graph_paper_relevance_search,
            self.get_graph_paper_bulk_search,
            self.get_graph_paper_title_search,
            self.get_graph_get_paper,
            self.get_graph_get_paper_authors,
            self.get_graph_get_paper_citations,
            self.get_graph_get_paper_references,
            self.get_snippet_search,
        ]
