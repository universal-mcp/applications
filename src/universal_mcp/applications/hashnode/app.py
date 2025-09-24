from gql import gql
from universal_mcp.applications.application import GraphQLApplication
from universal_mcp.integrations import Integration


class HashnodeApp(GraphQLApplication):
    def __init__(self, integration: Integration | None = None, **kwargs) -> None:
        super().__init__(name="hashnode", base_url="https://gql.hashnode.com", **kwargs)
        self.integration = integration

    def publish_post(
        self,
        publication_id: str,
        title: str,
        content: str,
        tags: list[str] = None,
        slug: str = None,
        subtitle: str = None,
        cover_image: str = None,
    ) -> str:
        """
        Publishes a post to Hashnode using the GraphQL API.

        Args:
            publication_id: The ID of the publication to publish the post to
            title: The title of the post
            content: The markdown content of the post
            tags: Optional list of tag names to add to the post. Example: ["blog", "release-notes", "python", "ai"]
            slug: Optional custom URL slug for the post. Example: "my-post"
            subtitle: Optional subtitle for the post. Example: "A subtitle for my post"
            cover_image: Optional: The URL of the cover image for the post. Example: "https://example.com/cover-image.jpg"
        Returns:
            The URL of the published post

        Raises:
            GraphQLError: If the API request fails

        Tags:
            publish, post, hashnode, api, important
        """
        publish_post_mutation = gql("""
        mutation PublishPost($input: PublishPostInput!) {
          publishPost(input: $input) {
            post {
              url
            }
          }
        }
        """)

        variables = {
            "input": {
                "publicationId": publication_id,
                "title": title,
                "contentMarkdown": content,
            }
        }

        if tags:
            variables["input"]["tags"] = [
                {"name": tag, "slug": tag.replace(" ", "-").lower()} for tag in tags
            ]

        if slug:
            variables["input"]["slug"] = slug

        if subtitle:
            variables["input"]["subtitle"] = subtitle

        if cover_image:
            variables["input"]["coverImageOptions"] = {"coverImageURL": cover_image}

        result = self.mutate(publish_post_mutation, variables)
        return result["publishPost"]["post"]["url"]

    def create_draft(
        self,
        publication_id: str,
        title: str,
        content: str,
        tags: list[str] = None,
        slug: str = None,
        subtitle: str = None,
        cover_image: str = None,
    ) -> dict:
        """
        Creates a draft post on Hashnode.

        Args:
            publication_id: The ID of the publication to create the draft in.
            title: The title of the draft.
            content: The markdown content of the draft.
            tags: Optional list of tag names to add to the draft.
            slug: Optional custom URL slug for the draft.
            subtitle: Optional subtitle for the draft.
            cover_image: Optional URL of the cover image for the draft.

        Returns:
            A dictionary containing the created draft's details, including its ID.

        Raises:
            GraphQLError: If the API request fails.

        Tags:
            create, draft, post, hashnode, api, important
        """
        create_draft_mutation = gql("""
        mutation CreateDraft($input: CreateDraftInput!) {
          createDraft(input: $input) {
            draft {
              id
              slug
              title
            }
          }
        }
        """)
        variables = {
            "input": {
                "publicationId": publication_id,
                "title": title,
                "contentMarkdown": content,
            }
        }
        if tags:
            variables["input"]["tags"] = [
                {"name": tag, "slug": tag.replace(" ", "-").lower()} for tag in tags
            ]
        if slug:
            variables["input"]["slug"] = slug
        if subtitle:
            variables["input"]["subtitle"] = subtitle
        if cover_image:
            variables["input"]["coverImageOptions"] = {"coverImageURL": cover_image}

        result = self.mutate(create_draft_mutation, variables)
        return result["createDraft"]["draft"]

    def publish_draft(self, post_id: str) -> str:
        """
        Publishes a draft post.

        Args:
            post_id: The ID of the draft to publish.

        Returns:
            The URL of the published post.

        Raises:
            GraphQLError: If the API request fails.

        Tags:
            publish, draft, post, hashnode, api, important
        """
        publish_draft_mutation = gql("""
        mutation PublishDraft($input: PublishDraftInput!) {
          publishDraft(input: $input) {
            post {
              url
            }
          }
        }
        """)
        variables = {"input": {"draftId": post_id}}
        result = self.mutate(publish_draft_mutation, variables)
        return result["publishDraft"]["post"]["url"]

    def get_me(self) -> dict:
        """
        Fetches details about the authenticated user.

        Returns:
            A dictionary containing the authenticated user's details.

        Raises:
            Exception: If the API request fails or no data is returned.

        Tags:
            get, me, hashnode, api, query, important
        """
        get_me_query = gql("""
        query Me {
          me {
            id
            username
            name
            bio {
              markdown
              html
              text
            }
            profilePicture
            socialMediaLinks {
              website
              github
              twitter
              instagram
              facebook
              stackoverflow
              linkedin
              youtube
              bluesky
            }
            emailNotificationPreferences {
              weeklyNewsletterEmails
              activityNotifications
              generalAnnouncements
              monthlyBlogStats
              newFollowersWeekly
            }
            followersCount
            followingsCount
            tagline
            dateJoined
            location
            availableFor
            email
            unverifiedEmail
            role
          }
        }
        """)

        result = self.query(get_me_query)

        # It's good practice to check if 'me' exists in the result
        if "me" in result:
            return result.get("me")
        else:
            raise Exception("Failed to retrieve 'me' data from Hashnode API response.")

    def get_publication(self, host: str = None, publication_id: str = None) -> dict:
        """
        Fetches details about a publication by host or ID. Only one of host or publication_id should be provided.

        Args:
            host: The host (domain) of the publication. Example: "myblog.hashnode.dev"
            publication_id: The ID of the publication.

        Returns:
            A dictionary containing publication details.

        Raises:
            GraphQLError: If the API request fails.
            ValueError: If neither host nor publication_id is provided.

        Tags:
            get, publication, hashnode, api, query, important
        """
        if not host and not publication_id:
            raise ValueError("Either host or publication_id must be provided.")

        query_string = """
            query Publication($host: String, $id: ObjectId) {
                publication(host: $host, id: $id) {
                    id
                    title
                    url
                    isTeam
                    posts(first: 5) {
                        edges {
                            node {
                                id
                            }
                        }
                    }
                }
            }
            """
        get_publication_query = gql(query_string)

        # Construct variables such that only one of host or id is included
        if host:
            variables = {"host": host}
        else:
            variables = {"id": publication_id}

        result = self.query(get_publication_query, variables)
        return result.get("publication")

    def list_posts(
        self, publication_id: str, first: int = 10, after: str = None
    ) -> dict:
        """
        Lists posts from a publication.

        Args:
            publication_id: The ID of the publication.
            first: The number of posts to fetch. Defaults to 10.
            after: The cursor for pagination.

        Returns:
            A dictionary containing the list of posts and pagination info.

        Raises:
            GraphQLError: If the API request fails.

        Tags:
            list, posts, hashnode, api, query, important
        """
        list_posts_query = gql("""
        query Publication($id: ObjectId!, $first: Int!, $after: String) {
            publication(id: $id) {
                posts(first: $first, after: $after) {
                    edges {
                        node {
                            id
                            title
                            slug
                            url
                        }
                        cursor
                    }
                    pageInfo {
                        endCursor
                        hasNextPage
                    }
                }
            }
        }
        """)
        variables = {"id": publication_id, "first": first}
        if after:
            variables["after"] = after
        result = self.query(list_posts_query, variables)
        return result.get("publication", {}).get("posts")

    def get_post(
        self, post_id: str = None, slug: str = None, hostname: str = None
    ) -> dict:
        """
        Fetches details of a single post by ID, or by slug and hostname.

        Args:
            post_id: The ID of the post to fetch.
            slug: The slug of the post.
            hostname: The hostname of the publication the post belongs to.

        Returns:
            A dictionary containing post details.

        Raises:
            GraphQLError: If the API request fails.
            ValueError: If neither post_id nor both slug and hostname are provided.

        Tags:
            get, post, hashnode, api, query, important
        """
        if not post_id and not (slug and hostname):
            raise ValueError(
                "Either post_id or both slug and hostname must be provided."
            )

        get_post_query = gql("""
        query Post($id: ID, $slug: String, $hostname: String) {
            post(id: $id, slug: $slug, hostname: $hostname) {
                id
                slug
                previousSlugs
                title
                subtitle
    			author {
                  id
                  username
                  name
                }
                comments(first: 5) {
                    edges {
                        node {
                            id
                        }
                    }
                }
            }
        }
        """)
        variables = {}
        if post_id:
            variables["id"] = post_id
        else:
            variables["slug"] = slug
            variables["hostname"] = hostname

        result = self.query(get_post_query, variables)
        return result.get("post")

    def modify_post(
        self,
        post_id: str,
        title: str = None,
        content: str = None,
        tags: list[str] = None,
        slug: str = None,
        subtitle: str = None,
        cover_image: str = None,
    ) -> str:
        """
        Modifies an existing post using the GraphQL API.

        Args:
            post_id: The ID of the post to update.
            title: Optional new title for the post.
            content: Optional new markdown content for the post.
            tags: Optional new list of tag names for the post. Example: ["blog", "release-notes"]
            slug: Optional new custom URL slug for the post.
            subtitle: Optional new subtitle for the post.
            cover_image: Optional new URL of the cover image for the post.

        Returns:
            The URL of the updated post.

        Raises:
            GraphQLError: If the API request fails.

        Tags:
            modify, post, hashnode, api, important
        """
        update_post_mutation = gql("""
        mutation UpdatePost($input: UpdatePostInput!) {
          updatePost(input: $input) {
            post {
              url
            }
          }
        }
        """)

        variables = {
            "input": {
                "id": post_id,
            }
        }

        if title:
            variables["input"]["title"] = title
        if content:
            variables["input"]["contentMarkdown"] = content
        if tags:
            variables["input"]["tags"] = [
                {"name": tag, "slug": tag.replace(" ", "-").lower()} for tag in tags
            ]
        if slug:
            variables["input"]["slug"] = slug
        if subtitle:
            variables["input"]["subtitle"] = subtitle
        if cover_image:
            variables["input"]["coverImageOptions"] = {"coverImageURL": cover_image}

        result = self.mutate(update_post_mutation, variables)
        return result["updatePost"]["post"]["url"]

    def delete_post(self, post_id: str) -> str:
        """
        Deletes a post using the GraphQL API.

        Args:
            post_id: The ID of the post to delete.

        Returns:
            A confirmation message or identifier for the deleted post. (The exact return depends on API response)

        Raises:
            GraphQLError: If the API request fails.

        Tags:
            delete, post, hashnode, api
        """
        delete_post_mutation = gql("""
        mutation  RemovePost($input: RemovePostInput!) {
            removePost(input: $input) {
                post {
                    id
                    slug
                    previousSlugs
                    title
                    subtitle
                }
            }
        }
        """)
        variables = {"input": {"id": post_id}}
        result = self.mutate(delete_post_mutation, variables)
        return result.get("removePost", {}).get("post", "Post deleted successfully")

    def add_comment(self, post_id: str, content: str) -> dict:
        """
        Adds a comment to a post using the GraphQL API.

        Args:
            post_id: The ID of the post to add the comment to.
            content: The markdown content of the comment.

        Returns:
            A dictionary containing details of the added comment.

        Raises:
            GraphQLError: If the API request fails.

        Tags:
            add, comment, post, hashnode, api, important
        """
        add_comment_mutation = gql("""
        mutation AddComment($input: AddCommentInput!) {
          addComment(input: $input) {
            comment {
              id
              content {
                markdown
              }
              author {
                id
                username
              }
            }
          }
        }
        """)
        variables = {
            "input": {
                "postId": post_id,
                "contentMarkdown": content,
            }
        }
        result = self.mutate(add_comment_mutation, variables)
        return result.get("addComment", {}).get("comment")

    def delete_comment(self, comment_id: str) -> str:
        """
        Deletes a comment using the GraphQL API.

        Args:
            comment_id: The ID of the comment to delete. This can be known from when you add a comment using add_comment method or by fetching the post details using get_post method.

        Returns:
            A confirmation message or identifier for the deleted comment. (The exact return depends on API response)

        Raises:
            GraphQLError: If the API request fails.

        Tags:
            delete, comment, hashnode, api
        """
        delete_comment_mutation = gql("""
        mutation RemoveComment($input: RemoveCommentInput!) {
        removeComment(input: $input) {
            comment {
            id
            }
        }
        }
        """)
        variables = {"input": {"id": comment_id}}
        result = self.mutate(delete_comment_mutation, variables)
        return result.get("removeComment", {}).get(
            "comment", "Comment deleted successfully"
        )

    def get_user(self, username: str) -> dict:
        """
        Fetches details about a user by username.

        Args:
            username: The username of the user.

        Returns:
            A dictionary containing user details.

        Raises:
            GraphQLError: If the API request fails.

        Tags:
            get, user, hashnode, api, query
        """
        get_user_query = gql("""
        query User($username: String!) {
          user(username: $username) {
            id
            username
            name
            tagline
            profilePicture
            followersCount
            followingsCount
          }
        }
        """)
        variables = {"username": username}
        result = self.query(get_user_query, variables)
        return result.get("user")

    def list_tools(self):
        return [
            self.publish_post,
            self.create_draft,
            self.publish_draft,
            self.get_me,
            self.get_publication,
            self.list_posts,
            self.get_post,
            self.modify_post,
            self.delete_post,
            self.add_comment,
            self.delete_comment,
            self.get_user,
        ]
