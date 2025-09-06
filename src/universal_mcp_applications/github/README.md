# GithubApp MCP Server

An MCP Server for the GithubApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the GithubApp API.


| Tool | Description |
|------|-------------|
| `star_repository` | Stars a GitHub repository using the GitHub API and returns a status message. |
| `list_commits` | Retrieves and formats a list of recent commits from a GitHub repository |
| `list_branches` | Lists all branches for a specified GitHub repository and returns them in a formatted string representation. |
| `list_pull_requests` | Retrieves and formats a list of pull requests for a specified GitHub repository. |
| `list_issues` | Retrieves a list of issues from a specified GitHub repository with optional filtering parameters. |
| `get_pull_request` | Retrieves and formats detailed information about a specific GitHub pull request from a repository |
| `create_pull_request` | Creates a new pull request in a GitHub repository, optionally converting an existing issue into a pull request. |
| `create_issue` | Creates a new issue in a specified GitHub repository with a title, body content, and optional labels. |
| `update_issue` | Updates an existing GitHub issue with specified parameters including title, body, assignee, state, and state reason. |
| `list_repo_activities` | Retrieves and formats a list of activities for a specified GitHub repository. |
| `meta_root` | Retrieves data or information from the root resource using the "GET" method at the path "/". |
| `list_advisories` | Retrieves global security advisories from GitHub's database, filtered by parameters such as GHSA ID, CVE ID, severity, ecosystem, and publication date. |
| `get_advisory_by_id` | Retrieves details of a specific global security advisory using its GitHub Security Advisory (GHSA) identifier. |
| `apps_get_authenticated` | Retrieves data from the application at the "/app" path using the GET method. |
| `apps_create_from_manifest` | Converts a specific app manifest identified by the code using the POST method and returns a successful creation status. |
| `get_app_hook_config` | Retrieves the configuration for an application hook using the GET method at the "/app/hook/config" endpoint. |
| `update_hook_config` | Updates the configuration of an application hook using PATCH and returns a status message upon success. |
| `apps_list_webhook_deliveries` | Retrieves a list of webhook deliveries with pagination support via per-page and cursor parameters. |
| `apps_get_webhook_delivery` | Retrieves a specific delivery record by its unique ID from a webhook's delivery history. |
| `add_delivery_attempt` | Registers an attempt for a specific delivery using the "POST" method at the path "/app/hook/deliveries/{delivery_id}/attempts". |
| `get_installation_requests` | Retrieves a paginated list of application installation requests. |
| `apps_list_installations` | Retrieves a list of installations for an application, allowing filtering by page, per page results, since a specific time, and whether installations are outdated, using the GET method at the "/app/installations" endpoint. |
| `apps_get_installation` | Retrieves information about a specific GitHub App installation by its ID using the GitHub API. |
| `apps_delete_installation` | Deletes a GitHub App installation identified by the `installation_id` using the GitHub API and returns a status message when successful. |
| `create_access_token` | Generates an installation access token for a GitHub App at a specified installation ID using the POST method, allowing authentication for actions within that installation. |
| `apps_suspend_installation` | Suspends a GitHub App installation using the GitHub API, blocking the app's access to resources owned by the installation account. |
| `apps_unsuspend_installation` | Removes a GitHub App installation suspension using the GitHub API and returns a status code indicating success or failure. |
| `apps_delete_authorization` | Revokes an application's OAuth grant and deletes associated user tokens for a GitHub application. |
| `apps_check_token` | Issues a token for a specified client application using the POST method at "/applications/{client_id}/token", returning a response based on the client's authentication status. |
| `apps_reset_token` | Updates the token configuration for a specified client application using the OAuth 2.0 framework and returns the operation status. |
| `apps_delete_token` | Deletes an application token by client ID using the DELETE method, returning a successful response with a 204 status code if the operation is completed without content. |
| `apps_scope_token` | Generates a scoped access token for a specified client application with the provided client ID. |
| `apps_get_by_slug` | Retrieves details for the specified application using its unique app slug identifier. |
| `classroom_get_an_assignment` | Retrieves the details of a specific assignment using the provided assignment ID. |
| `get_accepted_assignments_by_id` | Retrieves a list of accepted assignments for a specified assignment using pagination control. |
| `get_assignment_grades` | Retrieves the grades associated with a specific assignment using the provided assignment ID and returns the grade data. |
| `classroom_list_classrooms` | Retrieves a paginated list of classroom resources with support for page size and number parameters. |
| `classroom_get_a_classroom` | Retrieves details for a specific classroom using its unique identifier in the API. |
| `list_classroom_assignments` | Retrieves a list of assignments for a specified classroom, allowing for pagination by page and per-page parameters. |
| `list_codes_of_conduct` | Retrieves a list of GitHub's codes of conduct using the GitHub REST API. |
| `get_conduct_by_key` | Retrieves a specific code of conduct identified by the "key" parameter using the "GET" method. |
| `credentials_revoke` | Revokes a list of credentials by submitting them using the POST method to the "/credentials/revoke" endpoint. |
| `emojis_get` | Retrieves a list of emojis using the "GET" method at the "/emojis" path and returns the result with a status message. |
| `fetch_enterprise_code_sec_config` | Retrieves a paginated list of code security configurations available for an enterprise using the GitHub API. |
| `create_code_security_config` | Creates a custom code security configuration for an enterprise with specified security settings. |
| `get_enterprise_security_defaults` | Retrieves the default code security configuration for an enterprise using the GitHub API. |
| `get_enterprise_config` | Retrieves details of a specific code security configuration for a GitHub enterprise. |
| `update_code_security_config` | Sets a code security configuration as the default for new repositories in a GitHub enterprise, applying it to specified repository types by default. |
| `delete_configuration_by_id` | Deletes a code security configuration from a GitHub enterprise, detaching associated repositories while preserving their existing settings. |
| `attach_configuration` | Attaches an enterprise code security configuration to repositories and returns a status code indicating success or failure. |
| `update_code_security_defaults` | Sets a code security configuration as the default for new repositories in a GitHub enterprise. |
| `get_repo_config` | Retrieves a paginated list of repositories associated with a specific code security configuration for an enterprise, including pagination parameters and status filtering. |
| `list_enterprise_dependabot_alerts` | Retrieves Dependabot security alerts for repositories within an enterprise, filtered by state, severity, ecosystem, package, and other parameters. |
| `list_enterprise_secret_alerts` | Retrieves a list of secret scanning alerts for eligible repositories within an enterprise, from newest to oldest, based on specified filters such as alert state, secret type, resolution, and more. |
| `activity_list_public_events` | Retrieves a list of events using the "GET" method at the "/events" endpoint, allowing pagination with "per-page" and "page" parameters. |
| `activity_get_feeds` | Retrieves a list of feeds from the API. |
| `gists_list` | Retrieves a paginated list of public gists using GitHub's REST API. |
| `gists_create` | Creates a new public or secret GitHub gist using the GitHub API and returns the created gist details. |
| `gists_list_public` | Retrieves a list of public gists from GitHub using the GET method at the "/gists/public" path, allowing for filtering by date and pagination. |
| `gists_list_starred` | Retrieves a list of starred gists owned by the authenticated user with pagination support. |
| `gists_get` | Retrieves the content of a GitHub gist identified by its ID using the "GET" method. |
| `gists_update` | Updates an existing GitHub gist using the provided parameters and returns the modified gist. |
| `gists_delete` | Deletes a GitHub gist using the GitHub API and returns a status message indicating success or failure based on the HTTP status code. |
| `gists_list_comments` | Retrieves a list of comments for a specific GitHub gist. |
| `gists_create_comment` | Creates a new comment on a specified GitHub gist using the "POST" method and returns a status message with a "201 Created" response upon success. |
| `gists_get_comment` | Retrieves a specific comment from a GitHub gist using the provided gist and comment IDs. |
| `gists_update_comment` | Updates a specific comment on a GitHub gist using the provided ID and returns the modified comment. |
| `gists_delete_comment` | Deletes a GitHub gist comment specified by the gist ID and comment ID using the GitHub API. |
| `gists_list_commits` | Retrieves paginated commit history for a specified GitHub gist. |
| `gists_list_forks` | Retrieves a list of forks for a specified GitHub gist using the GitHub API. |
| `gists_fork` | Creates a fork of a specified gist using the GitHub API and returns a status message. |
| `gists_check_is_starred` | Checks if a gist is starred by the authenticated user using the GitHub API. |
| `gists_star` | Stars a GitHub gist using the GitHub API by sending a PUT request to the specified path. |
| `gists_unstar` | Removes a star from a GitHub gist using the GitHub API and returns a success status upon removal. |
| `gists_get_revision` | Retrieves a specific version of a GitHub gist by its ID and SHA, returning details about that version. |
| `gitignore_get_all_templates` | Retrieves available .gitignore templates for ignoring files and directories in repositories. |
| `gitignore_get_template` | Retrieves a .gitignore template by name for specifying files or directories to be ignored in a repository using the GitHub API. |
| `get_installation_repositories` | Retrieves a paginated list of repositories accessible to the authenticated installation, supporting pagination via page and per-page parameters. |
| `delete_installation_token` | Revokes a GitHub App installation access token, invalidating it and requiring a new token for future requests. |
| `issues_list` | Retrieves a list of issues from a repository using the GitHub API, allowing filtering by criteria such as state, labels, and sort order, and returns issue details in response. |
| `licenses_get_all_commonly_used` | Retrieves a paginated list of licenses, optionally filtered by featured status. |
| `licenses_get` | Retrieves information about a specific license identified by the "{license}" path parameter using the GET method. |
| `markdown_render` | Renders Markdown content as formatted HTML or raw text using a POST request to the specified endpoint. |
| `markdown_render_raw` | Renders Markdown text into raw format using the "POST" method at the "/markdown/raw" endpoint. |
| `get_account_details` | Retrieves account information for a specified marketplace listing account using the GET method, returning relevant details associated with the provided account ID. |
| `apps_list_plans` | Retrieves a paginated list of marketplace plans using the GET method, allowing users to navigate through pages of plan details based on parameters such as per page and page number. |
| `apps_list_accounts_for_plan` | Retrieves a list of accounts associated with a specified marketplace plan, allowing sorting by direction and pagination for per-page results. |
| `get_stubbed_account` | Retrieves stubbed account information for a specified marketplace listing account ID using a GET request. |
| `apps_list_plans_stubbed` | Retrieves paginated listings of marketplace plans with optional page size and number parameters. |
| `get_plan_accounts` | Retrieves user and organization accounts associated with a specific GitHub Marketplace plan, including subscription details and pending changes. |
| `meta_get` | Retrieves metadata information using the "GET" method at the "/meta" path. |
| `get_network_repo_events` | Retrieves a paginated list of public events for a repository's network with latency up to 6 hours. |
| `get_notifications` | Retrieves a list of notifications using the GET method at the "/notifications" path, allowing filters by parameters such as participating, since, before, page, and per_page. |
| `update_notification` | Updates or creates a notification resource at the specified path by replacing or creating it with the provided data. |
| `activity_get_thread` | Retrieves information about a specific notification thread by its ID, using the "GET" method. |
| `activity_mark_thread_as_read` | Updates a notification thread with the specified ID using the PATCH method, allowing partial modifications to its properties. |
| `activity_mark_thread_as_done` | Deletes a notification thread subscription at the specified thread ID using the "DELETE" method, effectively muting future notifications for that conversation. |
| `get_thread_subscription` | Retrieves the subscription details for a specific notification thread using the provided thread ID. |
| `update_thread_subscription` | Subscribes to a GitHub notification thread and returns the subscription status. |
| `unsubscribe_thread` | Mutes future notifications for a GitHub thread until user interaction occurs. |
| `meta_get_octocat` | Retrieves the GitHub Octocat mascot as ASCII art with optional text in a speech bubble via the "s" query parameter. |
| `orgs_list` | Retrieves a list of organizations using the "GET" method at the "/organizations" path, allowing optional filtering by parameters such as "since" and "per page". |
| `get_org_billing_usage` | Retrieves billing usage data for an organization, allowing for the specification of year, month, day, and hour parameters to filter the results. |
| `orgs_get` | Retrieves detailed information about a specified GitHub organization. |
| `orgs_update` | Updates an organization's configuration in the GitHub API and returns the modified organization details. |
| `orgs_delete` | Deletes a GitHub organization and all its repositories, returning status codes for success or failure. |
| `get_org_cache_usage` | Retrieves GitHub Actions cache usage for an organization, providing information on how much storage the caches consume across its repositories. |
| `get_org_cache_usage_by_repo` | Retrieves cache usage details across all repositories in an organization using the GitHub API. |
| `get_org_hosted_runners` | Retrieves a paginated list of GitHub-hosted runners available to an organization. |
| `create_hosted_runner` | Creates a GitHub-hosted runner for an organization using the GitHub API. |
| `get_org_images` | Retrieves GitHub-owned images for GitHub-hosted runners within a specified organization, returning relevant details for these images. |
| `list_hosted_images_by_org_id` | Retrieves the list of partner-hosted runner images available for GitHub-hosted runners in an organization. |
| `get_org_runner_limits` | Retrieves the usage limits for hosted runners in a GitHub organization using the GitHub API. |
| `get_org_actions_hosted_runner_sizes` | Retrieves the available machine sizes and specifications for GitHub-hosted runners within a specified organization. |
| `list_hosted_platforms` | Retrieves a list of platforms available for GitHub-hosted runners in an organization. |
| `get_hosted_runner_by_id` | Retrieves information about a specific GitHub-hosted runner in an organization using the GitHub API. |
| `patch_org_hosted_runner` | Updates configuration details for a GitHub-hosted runner in an organization. |
| `delete_hosted_runner_by_id` | Deletes a hosted runner from an organization using the GitHub API, returning a status code indicating success or failure. |
| `get_oidc_customization_sub` | Retrieves the customization template for an OpenID Connect (OIDC) subject claim for an organization, providing the current configuration used in GitHub Actions. |
| `update_org_oidc_customization` | Configures the OIDC subject claim customization template for a GitHub organization using specified claim keys. |
| `get_org_permissions` | Retrieves the GitHub Actions permissions policy for repositories and allowed actions in an organization. |
| `update_org_permissions` | Sets GitHub Actions permissions (enabled repositories and allowed actions) for an organization. |
| `get_org_repo_permissions` | Lists selected repositories enabled for GitHub Actions in an organization. |
| `update_org_repo_permissions` | Sets the list of repositories enabled for GitHub Actions in an organization, requiring admin permissions and returning a 204 status code on success. |
| `update_repo_permissions` | Updates the GitHub Actions permissions for a specific repository within an organization using the "PUT" method. |
| `delete_org_repo_permission` | Disables a repository for running GitHub Actions within an organization using the GitHub API. |
| `list_org_actions` | Retrieves the selected actions for a GitHub organization using the "GET" method at the "/orgs/{org}/actions/permissions/selected-actions" path. |
| `update_org_actions_permissions` | Configures the allowed GitHub Actions and reusable workflows for an organization, restricting them to selected options. |
| `get_org_workflow_permissions` | Retrieves the default workflow permissions configured for a GitHub organization. |
| `update_org_workflow_permissions` | Updates the default workflow permissions for GitHub Actions across all repositories in an organization. |
| `list_runner_groups` | Retrieves a list of self-hosted runner groups for a GitHub organization, with optional pagination and repository visibility filtering. |
| `create_runner_group` | Creates a new self-hosted runner group for a GitHub organization, allowing customized repository access and runner management policies. |
| `get_runner_group` | Retrieves a list of GitHub-hosted runners in a specific runner group for an organization using the GitHub Actions API. |
| `patch_org_runner_group` | Updates the name and visibility settings of a self-hosted runner group for a GitHub organization. |
| `delete_runner_group` | Deletes a self-hosted runner group from a GitHub organization and returns a 204 No Content status upon success. |
| `get_org_runner_group_hosted_runners` | Retrieves a list of GitHub-hosted runners within a specified runner group in an organization using the GitHub API. |
| `get_org_runner_group_repos` | Retrieves a paginated list of repositories associated with a specific runner group in a GitHub organization. |
| `update_runner_group_repo` | Sets the list of repositories with access to a self-hosted runner group in a GitHub organization. |
| `update_runner_group_repository` | Adds a repository to a self-hosted runner group in GitHub Actions, enabling workflow access to the group's runners. |
| `delete_repo_from_runner_group` | Removes repository access from a self-hosted runner group in an organization using the GitHub API. |
| `get_org_runner_group_runners` | Retrieves a paginated list of self-hosted runners associated with a specific runner group in a GitHub organization. |
| `update_runner_group_runners` | Updates a self-hosted runner in a specified runner group for an organization using the GitHub API. |
| `update_runner_group_runner_by_id` | Adds a self-hosted runner to a specified organization runner group using the GitHub API and returns a success status upon completion. |
| `delete_runner` | Deletes a self-hosted runner from a GitHub Actions runner group within an organization using the "DELETE" method. |
| `list_org_runners` | Lists all self-hosted runners configured in an organization, with optional filtering by runner name. |
| `get_org_runner_downloads` | Lists runner applications for an organization, returning details such as operating system and download URL for managing self-hosted runners. |
| `generate_jit_config` | Generates a configuration for a just-in-time runner for an organization using the GitHub API. |
| `register_runner_token` | Generates a registration token for adding self-hosted runners to a GitHub organization. |
| `remove_org_token` | Creates a temporary token to remove a self-hosted runner from a GitHub organization, valid for one hour. |
| `get_runner_info` | Retrieves details for a specific self-hosted runner in an organization using the GitHub Actions API. |
| `delete_runner_by_id` | Deletes a self-hosted runner from a specified GitHub organization using the GitHub Actions API. |
| `get_org_runner_labels` | Retrieves the labels associated with a self-hosted runner in an organization using the GitHub API. |
| `add_runner_labels` | Replaces all custom labels for a self-hosted runner in a GitHub organization with new labels. |
| `update_runner_labels` | Adds custom labels to a self-hosted runner for an organization in GitHub Actions using the specified runner ID. |
| `delete_runner_label` | Removes a specified custom label from a self-hosted runner in a GitHub organization and returns the remaining labels. |
| `delete_label_by_runner_id` | Removes a custom label from a self-hosted runner for an organization, returning the remaining labels from the runner if successful. |
| `actions_list_org_secrets` | Retrieves a list of organization-level GitHub Actions secrets without exposing their encrypted values. |
| `actions_get_org_public_key` | Retrieves the public key required to encrypt secrets for GitHub Actions at the organization level. |
| `actions_get_org_secret` | Retrieves a specific GitHub Actions secret by name for an organization without revealing its encrypted value. |
| `update_secret` | Creates or updates an organization GitHub Actions secret with an encrypted value using the GitHub REST API. |
| `actions_delete_org_secret` | Deletes a GitHub Actions organization secret and returns a 204 No Content status upon success. |
| `get_org_secret_repositories` | Retrieves a list of repositories that have access to a specific organization secret using the GitHub API. |
| `put_org_secret_repo_access` | Updates the list of repositories that can access a specific organization secret in GitHub Actions, returning a 204 status upon success. |
| `update_secret_repo` | Updates a secret for a specified repository within an organization using the GitHub API, allowing the secret to be used in GitHub Actions workflows for that repository. |
| `delete_org_secret_repo_by_id` | Deletes a secret from a specific repository within an organization using the GitHub API. |
| `actions_list_org_variables` | Retrieves a list of organization-level GitHub Actions variables using the GitHub API. |
| `actions_create_org_variable` | Creates an organization variable using the GitHub Actions API, allowing the variable to be referenced across workflows in the specified organization. |
| `actions_get_org_variable` | Retrieves a specific organization-level GitHub Actions variable by name. |
| `actions_update_org_variable` | Updates an organization variable in a GitHub organization using the "PATCH" method, allowing dynamic adjustments to GitHub Actions workflows by changing the variable's value. |
| `actions_delete_org_variable` | Deletes an organization variable in GitHub Actions using the specified organization name and variable name, returning a successful status when completed. |
| `get_org_variable_repos` | Retrieves a list of repositories within an organization where a specific GitHub Actions variable is used, using the GET method. |
| `update_variable_repository` | Adds or updates the list of repositories with access to a specific organization variable in GitHub Actions. |
| `update_org_action_variable_repo` | Updates organization-scoped variables for a specific repository using the GitHub API, allowing you to manage variable accessibility across selected repositories within an organization. |
| `delete_repository_variable` | Removes a specific repository's association with an organization-level variable in GitHub Actions. |
| `orgs_list_attestations` | Retrieves artifact attestations for a specified subject digest within an organization, allowing for the verification of software build provenance and integrity. |
| `orgs_list_blocked_users` | Retrieves a list of users blocked by the specified GitHub organization. |
| `orgs_check_blocked_user` | Checks if a specified user is blocked by a given GitHub organization. |
| `orgs_block_user` | Blocks a specified user from a GitHub organization and returns a `204` status code upon success. |
| `orgs_unblock_user` | Unblocks a specified user from a GitHub organization using the GitHub API. |
| `campaigns_list_org_campaigns` | Retrieves security campaigns for a GitHub organization, requiring owner or security manager permissions. |
| `campaigns_create_campaign` | Creates a new campaign within a specified organization using the POST method and returns a response based on the operation's success or failure. |
| `campaigns_get_campaign_summary` | Retrieves campaign details for a specific organization using the provided campaign number. |
| `campaigns_update_campaign` | Updates a specific campaign within an organization using the PATCH method, allowing for partial modifications to campaign details. |
| `campaigns_delete_campaign` | Deletes a security campaign in an organization using the GitHub API. |
| `list_org_code_scanning_alerts` | Retrieves a list of code scanning alerts for all repositories in a GitHub organization, optionally filtered by state, severity, and analysis tool. |
| `get_org_code_configurations` | Retrieves code security configurations for a GitHub organization with pagination support. |
| `create_org_code_config` | Creates a custom code security configuration for a GitHub organization, enabling specific security features like advanced security, dependabot alerts, and secret scanning. |
| `get_org_code_security_defaults` | Retrieves the default code security configurations for an organization. |
| `detach_code_security_config` | Detaches code security configurations from specified repositories while preserving their individual security settings. |
| `get_org_config_by_id` | Retrieves a specific code security configuration for an organization using its unique identifier. |
| `patch_org_code_security_config` | Updates a code security configuration for a GitHub organization via the GitHub API. |
| `delete_code_security_config` | Deletes a code security configuration from an organization, detaching repositories while retaining their existing security settings. |
| `attach_code_config` | Attaches a code security configuration to repositories in an organization via the GitHub API. |
| `set_default_code_security_config` | Configures a specified code security configuration as the default for new repositories within an organization using the GitHub API. |
| `get_org_repo_config` | Retrieves a list of repositories for a specific code security configuration in an organization using the GitHub API. |
| `get_org_codespaces` | Lists all codespaces associated with a specified organization using the "GET" method. |
| `update_org_codespaces_access` | Updates access control for GitHub Codespaces in an organization, allowing you to manage which users can access codespaces within the specified organization. |
| `select_codespace_users` | Adds selected users to access control for GitHub Codespaces within an organization using the GitHub API. |
| `delete_selected_users_access` | Removes selected users from accessing Codespaces in an organization using the GitHub API. |
| `codespaces_list_org_secrets` | Retrieves a list of organization secrets for GitHub Codespaces using the "GET" method at the path "/orgs/{org}/codespaces/secrets". |
| `codespaces_get_org_public_key` | Retrieves the public key for encrypting secrets in an organization's GitHub Codespaces. |
| `codespaces_get_org_secret` | Retrieves a specific organization-level Codespaces secret without exposing its encrypted value. |
| `put_org_codespace_secret` | Updates or creates a secret for an organization in GitHub Codespaces, specifying the organization and secret name, and returns a status indicating the outcome of the operation. |
| `codespaces_delete_org_secret` | Deletes a Codespaces organization secret and removes access from all associated codespaces. |
| `get_org_codespace_secret_repos` | Retrieves the list of repositories that a GitHub organization Codespaces secret is configured to access. |
| `put_org_codespace_secret_repo` | Assigns a specific organization-level Codespaces secret to repositories using the GitHub API, returning an empty response on success. |
| `update_org_secret_repository` | Assigns a GitHub Codespaces secret to a specified repository within an organization. |
| `delete_org_secret_repo` | Removes a repository from a GitHub organization's Codespaces secret access list when repository visibility is set to selected repositories. |
| `get_org_billing` | Retrieves the billing information for a GitHub Copilot subscription for a specified organization. |
| `copilot_list_copilot_seats` | Retrieves Copilot seat information and billing settings for an organization, including seat breakdown and feature policies. |
| `select_teams_for_billing` | Adds specified teams to an organization's GitHub Copilot subscription, provisioning seats for all members of those teams. |
| `unselect_teams` | Removes teams from the GitHub Copilot subscription for an organization, setting their seats to "pending cancellation" and ending their access at the end of the current billing cycle unless retained through another team. |
| `select_copilot_billing_users` | Adds users to a GitHub Copilot subscription for an organization and returns the count of newly created and refreshed seats. |
| `delete_selected_users` | Removes specified users from an organization's Copilot subscription, scheduling cancellation of their access at the next billing cycle unless retained via team membership. |
| `get_org_metrics` | Retrieves aggregated Copilot usage metrics for an organization, including active and engaged user data, with optional date range filtering. |
| `dependabot_list_alerts_for_org` | Retrieves a list of Dependabot alerts (filterable by state, severity, ecosystem, package, EPSS score, scope, and other parameters) for repositories within a specified GitHub organization. |
| `dependabot_list_org_secrets` | Retrieves a list of Dependabot secrets for an organization using the GitHub API. |
| `dependabot_get_org_public_key` | Retrieves the public key required to encrypt secrets for Dependabot in a GitHub organization before creating or updating secrets. |
| `dependabot_get_org_secret` | Retrieves a specific Dependabot secret for an organization from the GitHub API. |
| `update_dependabot_secret` | Creates or updates an organization-level Dependabot secret, encrypting and storing sensitive data for dependency updates. |
| `dependabot_delete_org_secret` | Deletes a specified Dependabot secret from a GitHub organization, returning a 204 status upon success. |
| `list_secret_repos` | Retrieves the list of selected repositories for an organization's Dependabot secret, including pagination details. |
| `put_dependabot_secret_repos` | Updates a list of repositories that have access to a specified Dependabot secret using the GitHub API. |
| `put_dependabot_secret_repo_access` | Adds a repository to an organization Dependabot secret's selected repositories list, returning a 204 response on success. |
| `delete_dependabot_secret_repo` | Removes a specified repository from the list of repositories that have access to a Dependabot secret within an organization using the GitHub API and returns a status message. |
| `get_org_docker_conflicts` | Lists packages in a GitHub organization that encountered conflicts during a Docker migration, requiring authentication with the `read:packages` scope for private resources. |
| `get_org_events` | Retrieves a paginated list of public activity events for a specified GitHub organization. |
| `orgs_list_failed_invitations` | Lists failed organization invitations for a specified organization using the GitHub API, returning details such as the time and reason for the failure. |
| `orgs_list_webhooks` | Retrieves a paginated list of organization webhooks configured to receive event payloads. |
| `orgs_create_webhook` | Creates an organization webhook in GitHub to receive HTTP POST payloads for specified events. |
| `orgs_get_webhook` | Retrieves details about a specific organization webhook using the GitHub API by its ID. |
| `orgs_update_webhook` | Updates a GitHub organization webhook specified by its ID, allowing modifications to its configuration and event subscriptions. |
| `orgs_delete_webhook` | Deletes an organization webhook using the GitHub API and returns a 204 status code upon successful deletion. |
| `get_hook_config` | Retrieves the configuration details for a specified organization webhook using the GitHub API. |
| `patch_org_hook_config` | Updates the configuration settings for an organization webhook in GitHub and returns the updated configuration upon success. |
| `orgs_list_webhook_deliveries` | Retrieves a paginated list of webhook deliveries for a specified organization webhook, including details about each delivery's payload and status. |
| `orgs_get_webhook_delivery` | Retrieves details about a specific webhook delivery for an organization using the GitHub API. |
| `retry_delivery_attempt` | Retries a failed webhook delivery attempt for an organization-level hook using the GitHub API. |
| `orgs_ping_webhook` | Triggers a test ping to the specified organization webhook and returns an empty response on success. |
| `get_route_stats_by_actor` | Retrieves API request statistics including total and rate-limited counts for a specific actor (user/app) broken down by routes within a specified timeframe[1]. |
| `api_insights_get_subject_stats` | Retrieves API request statistics for all subjects (users or GitHub Apps) within an organization within a specified time frame using the GitHub API. |
| `api_insights_get_summary_stats` | Retrieves overall statistics of API requests made within an organization by all users and apps within a specified time frame. |
| `get_org_user_summary_stats` | Retrieves API request statistics for a specific user within an organization during a specified time period. |
| `get_org_summary_stats` | Retrieves summary statistics of API requests within an organization for a specified actor type and ID, allowing insights into API usage over a defined time period. |
| `api_insights_get_time_stats` | Retrieves the number of API requests and rate-limited requests made within an organization over a specified time period. |
| `get_user_time_stats` | Retrieves the number of API requests and rate-limited requests made by a specific user within an organization over a specified time period using the GitHub API. |
| `get_org_insights_time_stats_by_actor` | Retrieves API request and rate-limited request counts for a specific actor (user or GitHub App) within an organization over a specified time period. |
| `api_insights_get_user_stats` | Retrieves API request statistics for a specific user within an organization during a specified time period, including pagination and filtering options. |
| `apps_get_org_installation` | Retrieves installation details for a GitHub App associated with the specified organization. |
| `orgs_list_app_installations` | Retrieves a list of GitHub App installations for a specified organization using the path "/orgs/{org}/installations" with the "GET" method. |
| `get_org_interaction_limits` | Retrieves the interaction limits for an organization's public repositories using the GitHub API, showing which types of users are allowed to interact and when the restrictions expire. |
| `update_interaction_limits` | Temporarily restricts which type of user can comment, open issues, or create pull requests in an organization's public repositories, with restrictions that automatically expire. |
| `delete_org_interaction_limits` | Removes all interaction restrictions for public repositories in a specified organization using the GitHub API. |
| `orgs_list_pending_invitations` | Retrieves a list of pending invitations for an organization using the GitHub API, allowing for filtering by role and invitation source. |
| `orgs_create_invitation` | Invites a user to join a specified GitHub organization using their GitHub user ID or email address via the POST method at the "/orgs/{org}/invitations" endpoint. |
| `orgs_cancel_invitation` | Cancels an organization invitation using the GitHub API by sending a DELETE request to the specified invitation ID within an organization. |
| `orgs_list_invitation_teams` | Retrieves the list of teams associated with a specific organization invitation using GitHub's API. |
| `orgs_list_issue_types` | Retrieves a list of all issue types configured for a GitHub organization. |
| `orgs_create_issue_type` | Creates a new issue type for a specified GitHub organization. |
| `orgs_update_issue_type` | Updates an issue type for an organization using the GitHub API, including its name, description, and status. |
| `orgs_delete_issue_type` | Deletes an issue type for a specified organization using the GitHub API. |
| `issues_list_for_org` | Retrieves a list of issues for a specified GitHub organization using the "GET" method at the "/orgs/{org}/issues" path, allowing filtering by state, labels, type, and sorting options. |
| `orgs_list_members` | Retrieves a paginated list of organization members optionally filtered by role and membership status. |
| `orgs_check_membership_for_user` | Retrieves information about a specific GitHub organization member using the provided organization and username. |
| `orgs_remove_member` | Removes a user from an organization using the GitHub API. |
| `get_org_member_codespaces` | Retrieves a list of codespaces for a specified organization member using the "GET" method. |
| `delete_org_member_codespace` | Deletes a GitHub Codespace for a specified member in an organization, identified by the organization name, member username, and codespace name. |
| `stop_codespace` | Stops a specific codespace for an organization member using the GitHub API and returns a status message. |
| `get_org_member_copilot` | Retrieves Copilot settings and seat information for a specified user within an organization using the GitHub API. |
| `orgs_get_membership_for_user` | Retrieves the membership details for a specified user within a GitHub organization using the GitHub API. |
| `orgs_set_membership_for_user` | Sets or updates a user's organization membership (including role) with invitation handling and role-based permissions. |
| `delete_org_membership_by_username` | Removes a user's membership from an organization using the GitHub API by canceling their invitation or deleting their active membership, requiring an authenticated organization admin. |
| `migrations_list_for_org` | Retrieves a paginated list of organization migration archives, including repositories and user data, from GitHub.com to GitHub Enterprise Server. |
| `migrations_start_for_org` | Initiates an organization migration to export repositories from GitHub.com for transfer to GitHub Enterprise Server. |
| `migrations_get_status_for_org` | Retrieves the details of a specific organization migration by its ID, including optional exclusion parameters. |
| `get_org_migration_archive` | Downloads a migration archive for a specified organization migration using the GitHub API, redirecting to the archive location if found. |
| `delete_migration_archive_by_org` | Deletes a GitHub organization migration archive, which is automatically removed after seven days if not deleted manually. |
| `migrations_unlock_repo_for_org` | Unlocks a repository locked during a GitHub organization migration using the GitHub API. |
| `migrations_list_repos_for_org` | Retrieves the list of repositories associated with a specific GitHub organization migration using the GitHub API. |
| `orgs_list_org_roles` | Retrieves all organization roles available in a specified GitHub organization. |
| `orgs_revoke_all_org_roles_team` | Removes all organization roles assigned to a specific team in a GitHub organization. |
| `orgs_assign_team_to_org_role` | Assigns an organization role to a team using the GitHub API, updating the team's permissions within the specified organization. |
| `orgs_revoke_org_role_team` | Removes a specific organization role from a team using the GitHub API and returns a successful status upon completion. |
| `orgs_revoke_all_org_roles_user` | Removes all assigned organization roles from a user via the GitHub API. |
| `orgs_assign_user_to_org_role` | Assigns a specified organization role to a user in a GitHub organization using the PUT method. |
| `orgs_revoke_org_role_user` | Removes a specific organization role from a user using the GitHub API. |
| `orgs_get_org_role` | Retrieves a specific organization role's details for a GitHub organization using the provided role ID. |
| `orgs_list_org_role_teams` | Lists the teams that are assigned to a specific organization role using the GitHub API, returning a list of teams with the provided role. |
| `orgs_list_org_role_users` | Retrieves a list of users assigned to a specific organization role within a GitHub organization using the "GET" method. |
| `get_org_outside_collaborators` | Retrieves a list of outside collaborators for a specified GitHub organization using the "GET" method at the "/orgs/{org}/outside_collaborators" path. |
| `update_outside_collaborator` | Converts an organization member to an outside collaborator asynchronously and returns a status message. |
| `delete_outside_collaborator` | Removes a specified outside collaborator from all repositories in a GitHub organization. |
| `list_org_packages` | Retrieves a paginated list of packages for a specified organization, filtered by package type and visibility. |
| `get_package_details` | Retrieves package details for a specified organization and package type using the GitHub API. |
| `delete_package` | Deletes a specific package from an organization's GitHub Packages registry. |
| `restore_package` | Restores a deleted package for an organization using the GitHub API. |
| `get_org_package_versions` | Retrieves a list of versions for a specified package within an organization's package registry, including pagination and optional state filtering. |
| `get_package_version` | Retrieves a specific version of a package from an organization's registry using the GitHub API. |
| `delete_package_version` | Deletes a specific version of a GitHub package using the provided organization, package type, package name, and package version ID. |
| `restore_package_versionfrombin` | Restores a package version from the recycle bin back into the active feed for a specified package type and name within an organization. |
| `orgs_list_pat_grant_requests` | Lists organization members' requests to access organization resources using fine-grained personal access tokens and returns paginated results. |
| `create_org_pat_request` | Submits a request from an organization member to access organization resources using a fine-grained personal access token, allowing GitHub Apps to manage access to specific resources. |
| `orgs_review_pat_grant_request` | Approves or processes an organization member's request to access organization resources with a fine-grained personal access token via the GitHub API. |
| `get_pat_request_repositories` | Retrieves a list of repositories associated with a specific personal access token request in a GitHub organization using the specified ID. |
| `orgs_list_pat_grants` | Lists requests from organization members to access organization resources using fine-grained personal access tokens, allowing filtering by various parameters such as repository, permission, and token usage time. |
| `orgs_update_pat_accesses` | Creates a new personal access token for an organization member to access organization resources using the GitHub API. |
| `orgs_update_pat_access` | Approves or processes a fine-grained personal access token request for accessing organization resources via the GitHub API. |
| `get_pat_repositories` | Retrieves a paginated list of repositories accessible by a specified personal access token within a GitHub organization. |
| `get_org_private_registries` | Retrieves paginated list of organization's private container registries with optional pagination parameters. |
| `create_private_registry` | Creates a private registry configuration for a specified organization using the POST method, allowing for the setup of an encrypted private registry with controlled access. |
| `get_org_private_registry_public_key` | Retrieves the public key required to encrypt secrets for an organization's private GitHub registries. |
| `get_private_registry_secret` | Retrieves details of a specific private registry configuration for an organization by its secret name. |
| `update_secret_registry` | Updates a private registry secret for an organization using the PATCH method and returns a status code indicating the outcome. |
| `delete_secret_registry` | Deletes a specified private registry secret associated with an organization. |
| `projects_list_for_org` | Retrieves a list of projects for a specified GitHub organization using the "GET" method, allowing filtering by project state and pagination. |
| `projects_create_for_org` | Creates a new project for an organization using the GitHub API and returns a status message upon success. |
| `orgs_get_all_custom_properties` | Retrieves a custom property schema defined for a specified GitHub organization using the "GET" method, returning details like property name, value type, and allowed values. |
| `update_org_schema` | Updates custom properties for an organization in bulk by creating or replacing existing property definitions. |
| `orgs_get_custom_property` | Retrieves the schema of a specified custom property for an organization. |
| `update_custom_property_schema` | Updates the schema for a custom property of an organization using the specified property name and returns the updated schema. |
| `orgs_remove_custom_property` | Deletes a custom property from an organization's schema using the DELETE method. |
| `get_org_property_values` | Retrieves custom property values for all organization repositories, optionally filtered by a search query. |
| `patch_org_properties_values` | Updates custom property values for an organization using the GitHub API, allowing creation or modification of existing properties for the specified organization. |
| `orgs_list_public_members` | Retrieves a list of public members of a specified GitHub organization using the "GET" method. |
| `get_org_public_member_by_username` | Checks if a specified user's membership in an organization is publicly visible and returns a status code indicating visibility or absence. |
| `update_org_member` | Publicizes a GitHub user's membership in a specified organization using the GitHub API and returns a status message. |
| `delete_org_public_member` | Removes a user's public membership visibility for a specified organization using the GitHub API, returning no content on success. |
| `repos_list_for_org` | Lists all repositories for a specified GitHub organization, with optional filtering and sorting parameters. |
| `repos_create_in_org` | Creates a new GitHub repository under a specified organization and returns a 201 status code upon success. |
| `repos_get_org_rulesets` | Retrieves all repository rulesets for an organization, including configurable filters for targets and pagination. |
| `repos_create_org_ruleset` | Creates a new ruleset for an organization using the GitHub API, allowing the management of custom rules to control interactions with repository branches and tags. |
| `repos_get_org_rule_suites` | Retrieves a filtered list of organization repository rule evaluation suites, including parameters for result type, repository name, time period, and pagination. |
| `repos_get_org_rule_suite` | Retrieves a specific rule suite for an organization on GitHub using the "GET" method, returning details about the rule suite with the specified identifier. |
| `repos_get_org_ruleset` | Retrieves a specific ruleset by its ID from a GitHub organization using the "GET" method at the "/orgs/{org}/rulesets/{ruleset_id}" path. |
| `repos_update_org_ruleset` | Updates an organization's ruleset configuration in GitHub using the specified ruleset ID. |
| `repos_delete_org_ruleset` | Deletes a specific ruleset from an organization using the GitHub API, returning a status code indicating the result of the operation. |
| `orgs_get_org_ruleset_history` | Retrieves the history of a specific ruleset for an organization using the GitHub API and returns relevant information about past changes. |
| `orgs_get_org_ruleset_version` | Retrieves a specific historical version of an organization's repository ruleset from the GitHub API based on the provided ruleset ID and version ID. |
| `list_org_secret_scanning_alerts` | Retrieves a paginated list of secret scanning alerts for an organization, filtered by state, secret type, resolution, and other criteria. |
| `get_org_security_advisories` | Lists repository security advisories for a specified organization, including details like advisory status and pagination parameters. |
| `get_org_security_managers` | Retrieves a list of security managers for a specified GitHub organization using the "GET" method. |
| `orgs_add_security_manager_team` | Adds a specified team as a security manager for an organization using the GitHub API, requiring appropriate permissions and returning a successful no-content response if completed. |
| `delete_security_manager_team` | Removes the security manager role from a team in a GitHub organization. |
| `get_org_billing_actions` | Retrieves GitHub Actions billing details for an organization including total minutes used, breakdown by operating system, and included minutes. |
| `get_org_billing_packages` | Retrieves the billing information for GitHub Packages in an organization, including free and paid storage usage in gigabytes. |
| `get_org_billing_shared_storage` | Retrieves an organization's shared storage billing details including estimated usage and remaining billing cycle days. |
| `get_org_network_configurations` | Retrieves a list of hosted compute network configurations for a GitHub organization. |
| `create_org_network_configurations` | Creates a hosted compute network configuration for a specified organization using the GitHub API. |
| `get_org_network_config_by_id` | Retrieves a specific hosted compute network configuration for an organization using the provided identifier. |
| `update_network_configuration` | Updates a hosted compute network configuration for a GitHub organization using specified network settings and compute service. |
| `delete_network_configuration_by_id` | Deletes a hosted compute network configuration from a GitHub organization. |
| `get_org_network_settings_by_id` | Retrieves a specific hosted compute network settings resource for the specified organization using the GitHub API. |
| `get_team_metrics` | Retrieves aggregated GitHub Copilot usage metrics for a specific team within an organization, including parameters for date ranges and pagination. |
| `teams_list` | Retrieves a list of teams in a GitHub organization. |
| `teams_create` | Creates a new team within a specified GitHub organization using the "POST" method at the "/orgs/{org}/teams" path. |
| `teams_get_by_name` | Retrieves details of a specific team in a GitHub organization using the team's slug for identification. |
| `teams_update_in_org` | Updates the details of a GitHub organization team, such as its name, description, or privacy settings, using the given organization and team slug. |
| `teams_delete_in_org` | Deletes a GitHub team using the GitHub API, requiring the organization name and team slug, and returns a status code indicating successful deletion. |
| `teams_list_discussions_in_org` | Retrieves a list of discussions from a specified team's page in a GitHub organization. |
| `teams_create_discussion_in_org` | Creates a new discussion post on a specified team's page within an organization using the GitHub API. |
| `teams_get_discussion_in_org` | Retrieves a specific GitHub team discussion by organization, team slug, and discussion number, using the "GET" method. |
| `teams_update_discussion_in_org` | Edits a GitHub team discussion post using the specified organization, team, and discussion details, updating its title and body text through the `PATCH` method. |
| `teams_delete_discussion_in_org` | Deletes a GitHub team discussion using the specified organization, team, and discussion number, returning a "204 No Content" status upon successful deletion. |
| `get_discussion_comments_org` | Retrieves comments from a specific team discussion in a GitHub organization. |
| `create_comment` | Creates a new comment on a team discussion post in a GitHub organization. |
| `get_comment_details` | Retrieves a specific comment from a team discussion in a GitHub organization using the GitHub API. |
| `update_comment` | Updates a specific comment on a team discussion post within a GitHub organization using the GitHub API. |
| `delete_team_discussion_comment` | Deletes a specified comment from a team discussion in a GitHub organization using the GitHub API. |
| `get_comment_reactions` | Lists reactions for a specific comment in a team discussion within a GitHub organization, allowing filtering by reaction content. |
| `add_comment_reaction` | Adds a reaction to a team discussion comment using specified emoji types and returns success status. |
| `delete_reaction` | Deletes a specific reaction from a team discussion comment within an organization using the GitHub API. |
| `get_discussion_reactions` | Retrieves a list of reactions (👍, 👎, ❤️, etc.) for a team discussion via the GitHub API. |
| `create_team_discussion_reaction` | Creates a new reaction to a team discussion comment on GitHub using the POST method. |
| `delete_reaction_by_id` | Deletes a reaction to a team discussion comment on GitHub using the API. |
| `list_invitations` | Retrieves a list of pending invitations for a specific team within a GitHub organization, including invitee details and invitation status. |
| `teams_list_members_in_org` | Retrieves a list of members for a specific team in an organization using the GitHub API. |
| `get_org_team_membership_by_username` | Retrieves a user's membership status with a team in a GitHub organization using the "GET" method. |
| `update_team_membership` | Adds or updates a user's team membership in a GitHub organization, sending an invitation if unaffiliated, and requires organization owner or team maintainer permissions. |
| `delete_team_membership` | Removes a user's membership from a team in a GitHub organization. |
| `teams_list_projects_in_org` | Retrieves a list of projects for a specified team within an organization using the GitHub API. |
| `get_org_team_project` | Retrieves a specific project associated with a team in a GitHub organization using the provided organization name, team slug, and project ID. |
| `update_project` | Updates a GitHub project for a specified team using the "PUT" method, modifying its details at the path "/orgs/{org}/teams/{team_slug}/projects/{project_id}". |
| `teams_remove_project_in_org` | Deletes a GitHub project associated with a specified team in an organization using the "DELETE" method, as identified by the project ID. |
| `teams_list_repos_in_org` | Checks a team's repository permissions and returns the list of repositories accessible to the team within an organization. |
| `get_team_repo_details` | Retrieves information about a specific repository owned by an organization team, using the GitHub API by providing parameters for the organization, team slug, repository owner, and repository name. |
| `add_team_repo_to_org` | Updates a team's repository permissions for a specified repository and returns a success status (204). |
| `teams_remove_repo_in_org` | Removes a repository from a team's permissions in a GitHub organization. |
| `teams_list_child_in_org` | Retrieves a paginated list of child teams belonging to a parent team within a GitHub organization using the specified organization name and team slug. |
| `enable_security_product` | Enables a security product for an organization using the specified API and returns a status message. |
| `projects_get_card` | Retrieves information about a specific card in a project column using the project API. |
| `projects_update_card` | Updates a specific project card's details using the "PATCH" method at the "/projects/columns/cards/{card_id}" endpoint and returns a status message. |
| `projects_delete_card` | Deletes a specific card from a project's column using the provided card ID and returns relevant status codes. |
| `projects_move_card` | Moves a GitHub project card to a specified location and returns an operation status. |
| `projects_get_column` | Retrieves details for a specific project column identified by the column ID. |
| `projects_update_column` | Updates a project column identified by `{column_id}` using partial data, returning a success status on completion. |
| `projects_delete_column` | Deletes a project column by its specified ID using the GitHub API and returns a success status upon completion. |
| `projects_list_cards` | Retrieves a list of cards from a specified project column in GitHub, supporting pagination and filtering by archived status. |
| `projects_create_card` | Creates a new card in a GitHub project column and returns the created resource. |
| `projects_move_column` | Moves a project column to a specified position using the GitHub API and returns a status message. |
| `projects_get` | Retrieves information for a specific project using the project ID provided in the path. |
| `projects_update` | Updates the specified project's properties using partial modifications and returns a success response upon completion. |
| `projects_delete` | Deletes the specified project by its ID and returns no content upon successful deletion. |
| `projects_list_collaborators` | Retrieves a list of collaborators for a specific project, optionally filtered by affiliation and paginated by page size. |
| `projects_add_collaborator` | Adds a collaborator to a specified project (classic) using their username and returns a success status upon completion. |
| `projects_remove_collaborator` | Removes a collaborator with the specified username from a project identified by its ID using the DELETE method. |
| `get_collaborator_permission` | Retrieves the permission level for a specific collaborator in a project. |
| `projects_list_columns` | Retrieves a list of columns for a specific project using the "GET" method at the path "/projects/{project_id}/columns", with optional pagination parameters. |
| `projects_create_column` | Creates a new column within a specified project structure. |
| `rate_limit_get` | Retrieves information about rate limits, providing details on usage constraints for API access. |
| `repos_get` | Retrieves detailed information about a specific GitHub repository, including its configuration and metadata. |
| `repos_update` | Updates an existing GitHub repository's configuration and returns the modified repository details. |
| `repos_delete` | Deletes a specified GitHub repository using the repository owner and name, but this endpoint does not exist in the standard GitHub API, as deletion is typically done through the UI or other specific endpoints not defined at "/repos/{owner}/{repo}" with the "DELETE" method. |
| `get_artifacts` | Retrieves a list of artifacts for a specified GitHub repository using the GitHub Actions API, allowing access to artifact metadata such as names, sizes, and creation dates. |
| `actions_get_artifact` | Retrieves metadata for a specific GitHub Actions artifact within a repository using the provided artifact ID. |
| `actions_delete_artifact` | Deletes a GitHub Actions artifact identified by its ID within a specified repository. |
| `actions_download_artifact` | Downloads a GitHub Actions workflow artifact in the specified archive format (e.g., zip) from a repository. |
| `get_repo_actions_cache_usage` | Retrieves the GitHub Actions cache usage for a specified repository using the GitHub API. |
| `actions_get_actions_cache_list` | Retrieves a list of GitHub Actions caches for a specified repository, including cache size, key, and creation time, with optional filtering by reference, key, and sorting parameters. |
| `delete_cache` | Deletes GitHub Actions caches for a repository using a cache key, optionally filtering by a Git reference, to manage and clear cache entries. |
| `delete_cache_id` | Deletes a GitHub Actions cache for a specified repository using a cache ID, returning a successful status without content when the operation is completed. |
| `get_repo_action_job_by_id` | Retrieves details about a specific GitHub Actions job identified by its ID within a repository using the GitHub API. |
| `get_repo_actions_job_logs` | Retrieves the download URL for logs of a specific GitHub Actions workflow job. |
| `rerun_job` | Re-runs a specific GitHub Actions job and returns a success status upon job re-run initiation. |
| `get_customization_sub` | Retrieves the customization template for an OpenID Connect (OIDC) subject claim for a specified GitHub repository. |
| `custom_sub_oidc` | Sets the customization template and opt-in or opt-out flag for an OpenID Connect (OIDC) subject claim for a specific GitHub repository using the PUT method. |
| `get_org_secrets` | Retrieves a paginated list of organization-level GitHub Actions secrets accessible to the specified repository without exposing encrypted values. |
| `list_organization_variables` | Retrieves a list of organization variables associated with a GitHub repository using the GitHub API. |
| `get_repo_permissions` | Retrieves the GitHub Actions permissions configuration for a specified repository. |
| `update_repo_actions_permissions` | Configures GitHub Actions permissions for a specified repository using the GitHub API. |
| `get_repo_access` | Retrieves GitHub Actions permissions settings for accessing repositories and allowed actions. |
| `update_repo_access` | Configures access permissions for GitHub Actions within a specified repository using the "PUT" method. |
| `get_selected_actions_permissions` | Retrieves the selected actions allowed for a GitHub repository using the "GET" method at the "/repos/{owner}/{repo}/actions/permissions/selected-actions" path. |
| `update_actions_permissions` | Sets the selected actions for GitHub Actions permissions in a specified repository using the `PUT` method. |
| `get_workflow_permissions` | Retrieves the default workflow permissions for the GitHub Actions GITHUB_TOKEN in a repository, including pull request review approval capabilities. |
| `update_workflow_permissions` | Updates the default workflow permissions and pull request review approval settings for a GitHub repository. |
| `get_repo_actions_runners` | Lists all self-hosted runners configured in a GitHub repository, including their status and configuration details. |
| `get_runner_downloads` | Retrieves a list of available runner applications for a specific GitHub repository, which can be used to set up self-hosted runners in GitHub Actions workflows. |
| `generate_runner_jit_config` | Generates a configuration for a just-in-time (JIT) runner in a GitHub repository, allowing dynamic setup for specific workflows. |
| `create_runner_registration_token` | Creates a registration token for a repository using the GitHub Actions API, allowing the configuration of self-hosted runners to execute workflows on custom infrastructure. |
| `remove_runner_token` | Generates a remove token for a repository using the GitHub API, allowing the secure removal of a self-hosted runner. |
| `get_repo_runner_by_id` | Retrieves the details of a specific GitHub Actions runner for a repository using the "GET" method at the "/repos/{owner}/{repo}/actions/runners/{runner_id}" path. |
| `delete_repo_runner_by_id` | Removes a self-hosted runner from a GitHub repository via the GitHub API and returns a 204 No Content response on success. |
| `get_runner_labels_by_id` | Retrieves a list of labels associated with a specific self-hosted runner in a GitHub repository using the API. |
| `add_runner_label` | Adds custom labels to a self-hosted runner in a GitHub repository and returns the updated labels. |
| `set_runner_labels` | Updates labels for a self-hosted runner in a GitHub repository using the GitHub API. |
| `delete_runner_labels` | Removes a custom label from a specific self-hosted runner for a repository using the GitHub API and returns a status message. |
| `delete_runner_label_by_name` | Removes a custom label from a self-hosted runner in a GitHub repository using the GitHub API and returns the updated labels. |
| `list_repo_actions_runs` | Retrieves a list of workflow runs for a specified GitHub repository, allowing filtering by various criteria such as actor, branch, event, status, and more. |
| `actions_get_workflow_run` | Retrieves detailed information about a specific GitHub Actions workflow run, including its status, conclusion, and logs, using the "GET" method at the "/repos/{owner}/{repo}/actions/runs/{run_id}" endpoint. |
| `actions_delete_workflow_run` | Deletes a specific GitHub Actions workflow run from a repository. |
| `actions_get_reviews_for_run` | Retrieves approval details for a specific GitHub Actions workflow run. |
| `actions_approve_workflow_run` | Approves a GitHub Actions workflow run for a pull request from a public fork, typically used for first-time contributors, using the GitHub API and returns a success status. |
| `get_run_artifacts` | Retrieves a list of workflow run artifacts for a specific GitHub repository and run ID. |
| `get_attempt_run_details` | Retrieves information about a specific workflow run attempt in GitHub Actions, allowing users to view details about the run instance, including its execution status and associated jobs, using the "GET" method. |
| `get_jobs_by_run_attempt` | Retrieves a list of jobs for a specific attempt of a workflow run in a GitHub repository using the GitHub Actions API. |
| `get_action_log` | Retrieves the logs for a specific workflow run attempt using the GitHub Actions API. |
| `actions_cancel_workflow_run` | Cancels a workflow run in a GitHub repository using the GitHub API and returns a status indicating success or conflict. |
| `create_deployment_rule` | Associates a deployment protection rule with a GitHub Actions workflow run using the provided repository, owner, and run ID details. |
| `force_cancel_action_run` | Forcibly cancels a GitHub Actions workflow run, bypassing conditional checks that would normally prevent cancellation. |
| `get_job_runs` | Retrieves a list of jobs associated with a specific workflow run in a GitHub repository, including their status and execution details. |
| `get_repo_actions_run_logs` | Retrieves the logs for a specific GitHub Actions workflow run using the "GET" method, allowing users to access and analyze the execution details of a workflow by providing the repository owner, repository name, and workflow run ID. |
| `delete_repo_actions_run_logs` | Deletes logs associated with a specific workflow run in a GitHub repository using the GitHub API. |
| `get_pending_deployments` | Retrieves a list of pending deployments for a specified GitHub Actions workflow run. |
| `create_deployment` | Sends a request to create or manage pending deployments for a specific workflow run in a GitHub repository, using the provided parameters to identify the repository and workflow run. |
| `actions_re_run_workflow` | Re-runs a specific GitHub Actions workflow run using the POST method at "/repos/{owner}/{repo}/actions/runs/{run_id}/rerun", allowing for the re-execution of a workflow instance. |
| `rerun_failed_jobs` | Re-runs failed jobs for a specific GitHub Actions workflow run via the GitHub API. |
| `actions_get_workflow_run_usage` | Retrieves timing metrics for a specific GitHub Actions workflow run, including duration and billable execution details. |
| `actions_list_repo_secrets` | Retrieves a paginated list of repository secrets for GitHub Actions workflows. |
| `actions_get_repo_public_key` | Retrieves the public key for encrypting secrets in a GitHub repository using the "GET" method at the "/repos/{owner}/{repo}/actions/secrets/public-key" endpoint. |
| `actions_get_repo_secret` | Retrieves a specific GitHub Actions repository secret's metadata (excluding the encrypted value) using authenticated access. |
| `update_repo_secret_by_name` | Creates or updates a repository secret for GitHub Actions workflows and returns a success status. |
| `actions_delete_repo_secret` | Deletes a repository secret for use in GitHub Actions workflows by specifying the repository owner, repository name, and secret name, returning a successful status upon removal. |
| `actions_list_repo_variables` | Retrieves a list of variables configured in a GitHub repository's Actions workflows, including their names and values. |
| `actions_create_repo_variable` | Creates a repository variable for use in GitHub Actions workflows, allowing for the storage of configuration settings or sensitive information, by sending a POST request to the specified path with required parameters including owner, repository, variable name, and value. |
| `actions_get_repo_variable` | Retrieves a specific variable from a GitHub repository using the GitHub API and returns its details. |
| `actions_update_repo_variable` | Updates a repository variable in GitHub Actions using the PATCH method, allowing for modification of the variable's value in a specified repository. |
| `actions_delete_repo_variable` | Deletes a specified repository variable for GitHub Actions workflows using the GitHub API. |
| `actions_list_repo_workflows` | Retrieves a list of GitHub Actions workflows configured in a repository. |
| `actions_get_workflow` | Retrieves details about a specific GitHub Actions workflow in a repository using the "GET" method. |
| `actions_disable_workflow` | Disables a GitHub Actions workflow, setting its state to "disabled_manually", using the PUT method via the API endpoint "/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable". |
| `dispatch_workflow` | Triggers a GitHub Actions workflow run manually using a dispatch event by sending a POST request to the specified workflow endpoint, allowing for controlled execution of workflows. |
| `actions_enable_workflow` | Enables a GitHub Actions workflow in a specified repository and returns no content upon success. |
| `actions_list_workflow_runs` | Retrieves a filtered list of workflow runs for a specific GitHub Actions workflow in a repository, supporting parameters like actor, branch, event type, and status. |
| `actions_get_workflow_usage` | Retrieves timing information for a GitHub Actions workflow using the "GET" method. |
| `repos_list_activities` | Retrieves and formats activity events for a GitHub repository, including filtering by actor, reference, time period, and activity type. |
| `issues_list_assignees` | Retrieves a list of available assignees for issues and pull requests in a specified GitHub repository. |
| `get_assignee` | Retrieves information about a specific assignee in a GitHub repository using the GET method on the "/repos/{owner}/{repo}/assignees/{assignee}" path. |
| `repos_create_attestation` | Creates and stores an artifact attestation for a repository, associating it with the specified subject and predicate. |
| `repos_list_attestations` | Retrieves artifact attestations associated with a specific subject digest for a GitHub repository. |
| `repos_list_autolinks` | Retrieves a list of autolink references configured for a GitHub repository to link external resources like issue trackers. |
| `repos_create_autolink` | Creates an autolink reference for a GitHub repository, allowing users to link external resources like JIRA issues or Zendesk tickets directly from their repository. |
| `repos_get_autolink` | Retrieves a specific autolink for a GitHub repository using the "GET" method, allowing access to the details of the autolink identified by the provided autolink ID. |
| `repos_delete_autolink` | Deletes an autolink reference from a GitHub repository using the repository's owner, name, and the autolink ID. |
| `get_security_fixes` | Retrieves the status of automated security fixes for a GitHub repository. |
| `enable_automated_security_fixes` | Enables or disables automated security fixes for a GitHub repository. |
| `delete_security_fixes` | Deletes automated security fixes for a specified GitHub repository. |
| `repos_list_branches` | Retrieves a list of branches for a specified GitHub repository, optionally filtering by protected status and pagination. |
| `repos_get_branch` | Retrieves all active rules that apply to a specific branch in a GitHub repository, including repository and organization-level rules. |
| `repos_get_branch_protection` | Retrieves the branch protection settings for a specific branch in a GitHub repository using the "GET" method. |
| `repos_update_branch_protection` | Updates branch protection rules for the specified branch in a GitHub repository using the GitHub REST API. |
| `repos_delete_branch_protection` | Removes branch protection rules for the specified branch in a GitHub repository. |
| `get_branch_protection` | Retrieves information about whether admin enforcement is enabled for a branch protection rule in a GitHub repository. |
| `enforce_admins_protection` | Updates branch protection to enforce restrictions on administrators using the GitHub API. |
| `unprotect_branch_admins` | Removes the enforcement of branch protection rules that require administrators to approve changes to a specified branch in a GitHub repository. |
| `get_required_reviews` | Retrieves the required pull request review protection settings for a specific branch in a GitHub repository. |
| `update_branch_protection` | Updates the required pull request review protection rules for a specified repository branch. |
| `delete_pull_request_reviews` | Removes required pull request review protections from a branch in a GitHub repository. |
| `get_required_signatures` | Retrieves commit signature protection status for a specific branch in a GitHub repository. |
| `enable_branch_signatures` | Enables required commit signatures for a specific branch in a GitHub repository, ensuring only signed and verified commits can be pushed to the branch. |
| `delete_branch_protection` | Removes required commit signature verification for a protected branch on GitHub. |
| `get_branch_status_checks` | Retrieves the required status checks configuration for a protected branch in a GitHub repository. |
| `update_branch_protection_checks` | Updates the required status checks configuration for a protected branch in a GitHub repository, enforcing specific checks and strictness rules. |
| `delete_required_status_checks` | Removes required status checks protection from a protected branch in a GitHub repository. |
| `get_branch_protection_contexts` | Retrieves the list of required status check contexts configured for a protected branch's merge restrictions. |
| `create_status_context` | Updates the list of required status check contexts for a GitHub repository's protected branch, defining which checks must pass before merging. |
| `update_status_check_contexts` | Updates the list of required status check contexts for a protected branch in a GitHub repository. |
| `delete_status_check_contexts` | Removes required status check contexts for a protected branch in a GitHub repository using the GitHub API. |
| `repos_get_access_restrictions` | Retrieves access restriction settings (users, teams, and apps) for a protected branch. |
| `delete_branch_restrictions` | Deletes branch protection restrictions for a specific branch in a GitHub repository, effectively removing access limitations for users, teams, or apps from that branch. |
| `get_repo_branch_protection_apps` | Retrieves restrictions on GitHub Apps for a specific branch protection rule, using the specified repository and branch details. |
| `add_branch_protection_app` | Adds app access restrictions to a protected branch in a GitHub repository using the GitHub API. |
| `update_branch_restrictions_apps` | Sets the list of apps with push access to a protected branch, replacing any previous apps in the restrictions list. |
| `delete_branch_protection_apps` | Removes app access restrictions from a GitHub repository's protected branch, disallowing specified apps to push changes. |
| `get_branch_protection_teams` | Retrieves the list of teams with push access to a protected branch in a GitHub repository. |
| `add_branch_protection_teams` | Adds team access restrictions to a protected branch in a GitHub repository using the "POST" method. |
| `update_branch_protection_teams` | Sets the list of teams with push access to a protected branch in a GitHub repository using the GitHub API. |
| `delete_branch_protection_teams` | Removes team access restrictions from a protected branch in a GitHub repository using the "DELETE" method. |
| `get_branch_users` | Retrieves a list of users with permission to push to a protected branch in a GitHub repository using the GitHub API. |
| `add_branch_protection_users` | Adds restrictions to a GitHub repository branch by specifying users who are allowed to push to the protected branch using the GitHub API. |
| `update_branch_protection_users` | Updates the list of users with push access to a protected branch in a GitHub repository using the GitHub API. |
| `delete_branch_restriction_user` | Removes users with push access restrictions for a branch in a GitHub repository using the DELETE method. |
| `repos_rename_branch` | Renames a branch in a GitHub repository using the "POST" method, updating its name and related references. |
| `checks_create` | Creates a new check run for a specific repository commit using the GitHub API. |
| `checks_get` | Retrieves information about a specific check run in a GitHub repository using the provided check run ID. |
| `checks_update` | Updates an existing check run in a GitHub repository using the specified check run ID. |
| `checks_list_annotations` | Retrieves annotations (e.g., errors, warnings, notices) for a specific check run in a GitHub repository. |
| `checks_rerequest_run` | Triggers GitHub to rerequest an existing check run without code changes, resetting its status to queued and clearing previous conclusions. |
| `checks_create_suite` | Creates a manual check suite for a GitHub repository commit when automatic creation is disabled, returning success or creation status. |
| `checks_set_suites_preferences` | Updates the repository preferences for check suites using the GitHub API, allowing control over the automatic creation of check suites on code pushes. |
| `checks_get_suite` | Retrieves a specific check suite by its ID from a GitHub repository, providing details about its status and check runs. |
| `checks_list_for_suite` | Retrieves a list of check runs associated with a specific check suite in a GitHub repository. |
| `checks_rerequest_suite` | Triggers GitHub to rerequest an existing check suite without new code pushes, returning a success status. |
| `list_code_scanning_alerts` | Retrieves a list of code scanning alerts for a specified repository, allowing filtering by parameters such as tool, page, and severity. |
| `code_scanning_get_alert` | Retrieves all instances of a specified code scanning alert from a GitHub repository. |
| `code_scanning_update_alert` | Updates a code scanning alert in a GitHub repository using the "PATCH" method, allowing users to modify the alert status based on parameters like the repository owner, repository name, and alert number. |
| `code_scanning_get_autofix` | Retrieves the status of an autofix for a specific code scanning alert in a repository, providing information about suggested fixes generated by GitHub Copilot Autofix. |
| `code_scanning_create_autofix` | Creates an autofix for a specified code scanning alert in a GitHub repository, allowing users to generate targeted fixes for identified vulnerabilities or errors. |
| `code_scanning_commit_autofix` | Commits an autofix for a code scanning alert in a GitHub repository, returning a 201 Created response if the autofix is successfully committed. |
| `get_alert_instances` | Retrieves all instances of a specified code scanning alert for a repository, including details of each occurrence across branches or pull requests. |
| `get_repo_code_scanning_analyses` | Retrieves a specified code scanning analysis for a GitHub repository, providing details such as the analysis date, tool used, and number of alerts, with optional SARIF-formatted data. |
| `code_scanning_get_analysis` | Retrieves a specified code scanning analysis for a GitHub repository, providing details such as the Git reference, commit SHA, analysis date, tool name, and number of alerts. |
| `code_scanning_delete_analysis` | Deletes a specific code scanning analysis from a GitHub repository, optionally requiring confirmation. |
| `get_code_scanning_databases` | Retrieves information about a CodeQL database for a specified GitHub repository, using the repository's owner and name as parameters. |
| `get_codeql_database_by_language` | Retrieves a CodeQL database for a specific language in a GitHub repository, allowing optional download as a ZIP file by setting the appropriate `Accept` header. |
| `delete_codeql_database` | Deletes a specific CodeQL database for a repository based on the specified programming language. |
| `create_codeql_analysis` | Creates a variant analysis for CodeQL in a GitHub repository using the "POST" method, facilitating the identification of vulnerabilities through multi-repository variant analysis. |
| `get_variant_analysis` | Retrieves the summary of a CodeQL variant analysis for a specific repository, including analysis status and results. |
| `get_codeql_variant_analysis` | Retrieves the analysis status of a specific repository within a CodeQL variant analysis workflow using the GitHub API. |
| `get_code_scanning_setup` | Retrieves the default code scanning configuration setup for a GitHub repository. |
| `patch_default_setup_code_scanning` | Enables or updates the default code scanning configuration for a GitHub repository using CodeQL analysis. |
| `code_scanning_upload_sarif` | Uploads a Static Analysis Results Interchange Format (SARIF) file as code scanning analysis results to a GitHub repository, allowing for the integration of external code analysis tools with GitHub's code scanning feature. |
| `code_scanning_get_sarif` | Retrieves information about a specific SARIF upload for a repository, providing details such as the status and analysis URL associated with the given SARIF ID. |
| `get_code_security_config` | Retrieves a code security configuration for a specified GitHub repository using the GitHub API. |
| `repos_codeowners_errors` | Retrieves a list of errors in a repository's CODEOWNERS file using the GitHub API. |
| `get_repo_codespaces` | Lists the authenticated user's codespaces in a specified GitHub repository. |
| `create_repo_codespace` | Creates a codespace for the specified repository using the GitHub API, initializing the development environment with the repository's configuration. |
| `get_dev_container_config` | Retrieves a list of available dev container configurations for a GitHub repository, supporting pagination. |
| `get_repo_codespaces_machines` | Retrieves available machine types for creating or updating a codespace in a specific repository, considering location, client IP, and branch parameters. |
| `get_new_codespace_for_repo` | Checks if the authenticated user can create a codespace in the specified repository and returns a success response if allowed. |
| `check_codespace_permissions` | Checks the permissions for a codespace in a specified repository using the GitHub API and returns a status message, allowing for verification of access rights based on the provided reference and devcontainer path. |
| `codespaces_list_repo_secrets` | Retrieves a list of Codespaces repository secrets for a specified repository without revealing their encrypted values. |
| `codespaces_get_repo_public_key` | Retrieves a GitHub repository's public key, necessary for encrypting secrets before creating or updating them for use in GitHub Codespaces. |
| `codespaces_get_repo_secret` | Retrieves a specific repository's Codespaces secret (such as access tokens) without exposing its encrypted value. |
| `update_codespace_secret` | Updates or creates a repository secret for a GitHub Codespaces environment using the specified repository and secret name. |
| `codespaces_delete_repo_secret` | Deletes a repository-specific development environment secret for GitHub Codespaces, removing access from all associated codespaces. |
| `repos_list_collaborators` | Retrieves a list of collaborators for a GitHub repository using the "GET" method, allowing filtering by affiliation and permission. |
| `repos_check_collaborator` | Checks if a specified user is a collaborator in a GitHub repository, returning a 204 status code if the user is a collaborator or a 404 status code if not. |
| `repos_add_collaborator` | Adds or updates a repository collaborator's permissions using the GitHub API and returns a success status. |
| `repos_remove_collaborator` | Removes a collaborator from a GitHub repository and deletes their private forks if applicable. |
| `get_repo_collaborator_permission` | Checks the repository permission of a collaborator by retrieving their access level, which can be `admin`, `write`, `read`, or `none`, for a specified GitHub repository using the "GET" method. |
| `get_repo_comments` | Retrieves a paginated list of commit comments for a specified GitHub repository. |
| `repos_get_commit_comment` | Retrieves a specific comment from a GitHub repository using the provided repository owner, repository name, and comment ID. |
| `repos_update_commit_comment` | Updates a commit comment in a GitHub repository and returns the modified comment. |
| `repos_delete_commit_comment` | Deletes a specific comment from a GitHub repository using the GitHub API. |
| `get_repo_comment_reactions` | Retrieves a list of reactions for a specific comment in a GitHub repository using the GitHub API. |
| `create_reaction` | Adds a reaction (e.g., 👍, 😄, ❤️) to a repository's commit comment using the GitHub API. |
| `delete_repo_comment_reaction_by_id` | Deletes a reaction from a repository comment using the GitHub API and returns a success status upon completion. |
| `repos_list_commits` | Retrieves a filtered list of commits from a GitHub repository with optional parameters for author, timeframe, path, and pagination. |
| `get_branches_by_commit` | Retrieves the branches in a GitHub repository where the specified commit is the head (latest commit). |
| `repos_list_comments_for_commit` | Retrieves a list of comments made on a specific commit in a GitHub repository. |
| `repos_create_commit_comment` | Creates a comment on a specific commit in a GitHub repository using the provided commit SHA. |
| `get_commit_pulls_by_repo_owner` | Retrieves a list of pull requests associated with a specific commit in a GitHub repository using the GitHub API. |
| `repos_get_commit` | Retrieves a list of commits for a specified reference in a GitHub repository using the "GET" method. |
| `checks_list_for_ref` | Retrieves a list of check runs for a specific commit in a GitHub repository. |
| `checks_list_suites_for_ref` | Retrieves a list of check suites for a specific commit in a GitHub repository, providing summaries of check runs and their statuses. |
| `get_commit_status` | Retrieves the individual and combined statuses of checks (e.g., CI results) for a specific commit in a GitHub repository. |
| `get_commit_statuses` | Retrieves the commit statuses for a specific reference in a GitHub repository, allowing access to the status states of a commit such as success, failure, or pending. |
| `get_community_profile` | Retrieves community profile metrics for a GitHub repository using the GitHub API, providing information such as health score, presence of key files, and detected license. |
| `repos_compare_commits` | Compares two commits in a GitHub repository and returns a list of commits between them, allowing users to view changes made in the repository. |
| `repos_get_content` | Retrieves the contents of a file or directory in a GitHub repository at the specified path, returning the contents in a JSON format. |
| `put_repo_content_by_path` | Creates or updates a file in a GitHub repository at the specified path using the GitHub API. |
| `repos_delete_file` | Deletes a file in a GitHub repository using the GitHub API, requiring the repository owner, repository name, and file path, and returns a success status upon completion. |
| `repos_list_contributors` | Retrieves a list of contributors for a specified GitHub repository, including commit counts and optional anonymous filtering. |
| `get_dependabot_alerts_by_repo` | Retrieves a list of Dependabot alerts for a specified repository, allowing filtering by state, severity, ecosystem, package, manifest, EPSS, and other criteria, to manage vulnerable dependencies. |
| `dependabot_get_alert` | Retrieves a specific Dependabot alert for a GitHub repository using the provided alert number. |
| `dependabot_update_alert` | Updates a specific Dependabot alert for a repository using the GitHub API and returns a status message. |
| `dependabot_list_repo_secrets` | Retrieves a list of Dependabot secrets for a GitHub repository. |
| `dependabot_get_repo_public_key` | Retrieves the public key for a repository, which is required to encrypt secrets used by Dependabot. |
| `dependabot_get_repo_secret` | Retrieves a Dependabot secret's metadata (excluding the encrypted value) for a specified repository using the GitHub API. |
| `put_repo_dependabot_secret` | Creates or updates a Dependabot secret for a specified repository using the GitHub API, allowing storage of sensitive information for accessing private registries. |
| `dependabot_delete_repo_secret` | Deletes a Dependabot secret from a GitHub repository using the secret name. |
| `dependency_graph_diff_range` | Compares the dependencies between two commits of a repository, returning a diff of dependency changes, including vulnerability data for any updated versions with known vulnerabilities. |
| `dependency_graph_export_sbom` | Retrieves the Software Bill of Materials (SBOM) for a GitHub repository in SPDX format, listing dependencies from the dependency graph. |
| `create_snapshot` | Creates a new snapshot of a repository's dependencies by submitting them to the GitHub Dependency Graph API, allowing for dependency tracking and security analysis. |
| `repos_list_deployments` | Retrieves a list of deployments for a specified GitHub repository, allowing filtering by SHA, reference, task, environment, and pagination parameters. |
| `repos_create_deployment` | Creates a new deployment for a specified GitHub repository using the provided parameters, such as the reference and environment, and returns a success status if the operation is successful. |
| `repos_get_deployment` | Retrieves information about a specific deployment in a GitHub repository using the provided owner, repository name, and deployment ID. |
| `repos_delete_deployment` | Deletes a specific GitHub deployment using the GitHub API and returns status messages for success or error conditions. |
| `repos_list_deployment_statuses` | Retrieves a list of deployment statuses for a specific deployment in a GitHub repository. |
| `repos_create_deployment_status` | Creates a deployment status for a specific deployment in a GitHub repository, allowing tracking of deployment progress through states like pending, success, or failure. |
| `repos_get_deployment_status` | Retrieves a specific deployment status for a given deployment in a GitHub repository using the GitHub API. |
| `repos_create_dispatch_event` | Triggers a GitHub Actions workflow by creating a dispatch event for a specified repository. |
| `repos_get_all_environments` | Retrieves a list of environments for a specified GitHub repository using the "GET" method at the path "/repos/{owner}/{repo}/environments". |
| `repos_get_environment` | Retrieves information about a specific environment for a GitHub repository using the provided owner, repository, and environment name. |
| `update_environment` | Creates or updates a deployment environment configuration for a GitHub repository. |
| `repos_delete_an_environment` | Deletes a specific deployment environment in a GitHub repository and its associated secrets/protection rules. |
| `get_deployment_branch_policies` | Retrieves a list of deployment branch policies for a specific environment in a GitHub repository, defining which branches can deploy to that environment. |
| `create_deployment_policy` | Creates a deployment branch policy for a specified GitHub environment by defining custom branch name patterns that must be matched for deployment, using the GitHub API. |
| `get_branch_policy` | Retrieves a specific deployment branch policy configured for an environment in a GitHub repository. |
| `update_branch_policy` | Updates a deployment branch policy's name pattern for a specific environment in a GitHub repository. |
| `delete_branch_policy` | Deletes a deployment branch policy from a specific environment within a GitHub repository using the GitHub API. |
| `get_deployment_rules` | Retrieves all custom deployment protection rules enabled for a specific environment within a GitHub repository. |
| `create_deployment_protection_rule` | Creates a custom deployment protection rule on a specified environment within a GitHub repository, allowing the integration of third-party systems to control deployments. |
| `list_deployment_apps` | Retrieves all custom deployment protection rules enabled for a GitHub environment, requiring read access to the repository. |
| `get_protection_rule` | Retrieves a specific custom deployment protection rule enabled on a GitHub repository environment. |
| `delete_protection_rule` | Disables a custom deployment protection rule for a specific environment in a GitHub repository. |
| `get_repo_secrets` | Retrieves a list of environment secrets for a specific repository environment (excluding secret values). |
| `get_public_key` | Retrieves the public key required to encrypt secrets for a GitHub repository environment. |
| `actions_get_environment_secret` | Retrieves details about a specific environment secret in a GitHub repository, such as its name and creation date, without revealing the secret value itself. |
| `update_environment_secret_by_name` | Creates or updates an environment secret in a GitHub repository using the PUT method, allowing for the secure storage and management of sensitive information within specific environments. |
| `delete_secret` | Deletes a specific environment secret for a GitHub repository using the GitHub API and returns a 204 status upon success. |
| `get_repo_environment_variables` | Retrieves a paginated list of variables for a specific environment in a GitHub repository using the GitHub API. |
| `create_environment_variable` | Creates environment variables for a specific environment in a GitHub repository using the GitHub API. |
| `get_variable_by_name` | Retrieves a specific variable from a GitHub repository environment using the GitHub API. |
| `update_environment_variable` | Updates an existing environment variable in a specified environment within a GitHub repository using the GitHub API. |
| `delete_variable` | Deletes a variable associated with a specific environment in a GitHub repository using the GitHub API. |
| `activity_list_repo_events` | Retrieves a paginated list of repository events triggered by activity in a specified GitHub repository, including pushes, issues, and other actions. |
| `repos_list_forks` | Retrieves a paginated list of forks for the specified GitHub repository. |
| `repos_create_fork` | Creates a fork of a GitHub repository for the authenticated user and returns a 202 Accepted status indicating asynchronous processing. |
| `git_create_blob` | Creates a new Git blob object in a GitHub repository, allowing the storage of file contents, identified by a unique SHA-1 hash, using the GitHub REST API. |
| `git_get_blob` | Retrieves a Git blob (binary large object) by its SHA-1 hash, returning either raw binary data or a Base64-encoded content string. |
| `git_create_commit` | Creates a new Git commit object in a GitHub repository and returns verification details. |
| `git_get_commit` | Retrieves detailed information about a specific commit in a GitHub repository, including metadata and file changes. |
| `git_list_matching_refs` | Retrieves Git references (branches/tags) matching a specified pattern or all references if no pattern is provided. |
| `git_get_ref` | Retrieves a specific Git reference from a GitHub repository, allowing access to branches or tags by their names. |
| `git_create_ref` | Creates a new Git reference (branch or tag) in a GitHub repository by specifying the ref name and commit SHA-1 hash. |
| `git_update_ref` | Updates a Git reference (branch or tag) for a GitHub repository, allowing modification of the commit hash it points to. |
| `git_delete_ref` | Deletes a Git reference from a GitHub repository using the GitHub API. |
| `git_create_tag` | Creates a tag object in a specified GitHub repository using the Git Tags API, allowing users to create annotated tags that can be used to mark specific commits. |
| `git_get_tag` | Retrieves a specific Git tag object from a GitHub repository using the tag's SHA. |
| `git_create_tree` | Creates a new Git tree structure in the specified repository, allowing hierarchical file/directory relationships to be defined. |
| `git_get_tree` | Retrieves a Git tree object from a GitHub repository using the provided SHA1 value or ref name, optionally including recursive traversal of subtrees when specified. |
| `repos_list_webhooks` | Retrieves a list of webhooks for a GitHub repository using the GitHub API, allowing you to view configurations and event subscriptions for the specified repository. |
| `repos_create_webhook` | Creates and configures a webhook for a GitHub repository to receive event notifications. |
| `repos_get_webhook` | Retrieves the details of a specific webhook configured for a GitHub repository. |
| `repos_update_webhook` | Updates a repository webhook configuration using the GitHub API and returns the modified webhook details. |
| `repos_delete_webhook` | Deletes a specified webhook from a GitHub repository and returns an empty response on success. |
| `get_repo_hook_config_by_id` | Retrieves the configuration details for a specific repository webhook in the GitHub API. |
| `patch_repo_hook_config` | Updates the configuration of a specified webhook in a GitHub repository, including settings like the secret and event triggers. |
| `repos_list_webhook_deliveries` | Retrieves a paginated list of webhook deliveries for a specific repository webhook using the GitHub API. |
| `repos_get_webhook_delivery` | Retrieves a specific webhook delivery event for a repository using the GitHub API. |
| `re_deliver_hook_delivery_attempt` | Retries a failed webhook delivery attempt for a GitHub repository using the specified delivery ID. |
| `repos_ping_webhook` | Triggers a ping event to test a GitHub repository webhook's connectivity and returns a success status. |
| `repos_test_push_webhook` | Triggers a test push event for a repository webhook subscribed to push events using the GitHub API. |
| `migrations_get_import_status` | Retrieves the status of a repository import process for a specified GitHub repository using the GitHub API. |
| `migrations_start_import` | Initiates a repository import from another source using the GitHub API, returning appropriate status codes for success or errors. |
| `migrations_update_import` | Updates authentication for a repository import using the GitHub API, allowing adjustments to the import process from another Git repository. |
| `migrations_cancel_import` | Cancels an ongoing repository import from another Git service using the GitHub API. |
| `migrations_get_commit_authors` | Retrieves commit authors from a repository import, including optional filtering by user ID. |
| `migrations_map_commit_author` | Maps a commit author's identity during a repository import, updating author information for imported commits. |
| `migrations_get_large_files` | Retrieves information about importing large files into a GitHub repository using the specified owner and repository names. |
| `migrations_set_lfs_preference` | Updates the Git LFS preference for a GitHub repository import, enabling or disabling large file support during the migration process. |
| `apps_get_repo_installation` | Retrieves the installation information for a GitHub App in a specific repository using the GitHub API. |
| `get_repo_interaction_limits` | Retrieves the current interaction restrictions (commenting, issues, pull requests) for a public GitHub repository. |
| `update_repo_interaction_limits` | Sets temporary interaction restrictions for a GitHub repository to limit commenting, issue creation, or pull request creation by user type. |
| `delete_interaction_limits` | Removes temporary interaction restrictions for a GitHub repository, allowing all users to comment, open issues, or create pull requests. |
| `repos_list_invitations` | Retrieves a paginated list of open invitations for collaborators to a GitHub repository. |
| `repos_update_invitation` | Updates a repository invitation using the GitHub API by modifying the specified invitation's details, such as permissions, for a repository owned by a specified user. |
| `repos_delete_invitation` | Deletes a GitHub repository invitation using the GitHub API, removing the specified invitation by its ID from the repository. |
| `issues_list_for_repo` | Retrieves a list of issues from a GitHub repository, allowing filtering by parameters such as milestone, state, assignee, and labels, using the GitHub API. |
| `issues_create` | Creates a new issue in a GitHub repository and returns the created issue details. |
| `issues_list_comments_for_repo` | Retrieves comments from issues and pull requests in a GitHub repository, including formatted body content like raw, text, or HTML. |
| `issues_get_comment` | Retrieves a specific comment on an issue or pull request in a GitHub repository using the "GET" method. |
| `issues_update_comment` | Updates an existing issue or pull request comment in a GitHub repository. |
| `issues_delete_comment` | Deletes a specific comment on an issue or pull request in a GitHub repository. |
| `list_reactions_to_comment` | Retrieves a list of reactions (e.g., 👍, ❤️) on a specific GitHub issue or pull request comment. |
| `post_issue_comment_reaction` | Adds an emoji reaction (e.g., 👍, ❤️) to a GitHub issue comment using the GitHub API. |
| `delete_comment_reaction_by_id` | Deletes a reaction from a specific comment on a GitHub issue using the "DELETE" method, returning a successful response if the operation is completed without content. |
| `issues_list_events_for_repo` | Retrieves a list of events for a specified GitHub issue using the GitHub API. |
| `issues_get_event` | Retrieves a specific issue event by its ID from a GitHub repository using the "GET" method. |
| `issues_get` | Retrieves a specific GitHub issue by its number within a repository using the GitHub API. |
| `issues_update` | Updates an issue in a GitHub repository by modifying its properties, including labels, assignees, and body content. |
| `issues_add_assignees` | Assigns users to a specified GitHub issue using the GitHub API. |
| `issues_remove_assignees` | Removes assignees from a GitHub issue using the GitHub API by specifying the repository owner, repository name, and issue number, requiring users to have appropriate permissions such as push access. |
| `get_assignee_to_issue` | Checks if a specific assignee is assigned to a GitHub repository issue and returns a 204 status if assigned, or 404 if not found. |
| `issues_list_comments` | Retrieves a list of comments for a specific issue in a GitHub repository using the GitHub API. |
| `issues_create_comment` | Creates a comment on a GitHub issue using the GitHub API, returning the created comment in response. |
| `issues_list_events` | Retrieves a list of all events triggered by activity in a specific GitHub issue. |
| `issues_list_labels_on_issue` | Retrieves a list of labels associated with a specific GitHub issue, allowing you to view the current labels set for that issue. |
| `issues_add_labels` | Adds labels to a specified GitHub issue, allowing you to manage categorization of issues by passing the names of the labels to be added. |
| `issues_set_labels` | Replaces all labels for a specific GitHub repository issue with the provided labels. |
| `issues_remove_all_labels` | Removes all labels from a specified issue in a GitHub repository using the "DELETE" method. |
| `issues_remove_label` | Removes a specific label from an issue in a GitHub repository using the "DELETE" method. |
| `issues_lock` | Locks an issue in a GitHub repository using the GitHub API, preventing further comments and updates. |
| `issues_unlock` | Unlocks a specified issue in a GitHub repository, allowing comments and interactions. |
| `reactions_list_for_issue` | Retrieves a list of reactions to a specific GitHub issue using the GitHub API. |
| `reactions_create_for_issue` | Creates a reaction to a GitHub issue using the GitHub API by sending a POST request with the desired reaction type to the specified issue. |
| `reactions_delete_for_issue` | Deletes a specific reaction from an issue in a GitHub repository using the GitHub API. |
| `issues_remove_sub_issue` | Removes a sub-issue from an issue in a GitHub repository using the "DELETE" method, requiring the repository owner, repository name, and issue number to identify the target sub-issue. |
| `issues_list_sub_issues` | Retrieves a paginated list of sub-issues linked to a specific GitHub repository issue. |
| `issues_add_sub_issue` | Adds a sub-issue to a parent issue in a GitHub repository and returns the result. |
| `issues_reprioritize_sub_issue` | Reprioritizes a sub-issue's position within a parent issue's sub-issue list using specified positional parameters. |
| `get_issue_timeline` | Retrieves a list of timeline events for a specific GitHub issue using the GitHub API, providing a chronological view of changes and interactions related to the issue. |
| `repos_list_deploy_keys` | Retrieves a list of deploy keys configured for a GitHub repository. |
| `repos_create_deploy_key` | Adds a deploy key to a GitHub repository using the GitHub API, granting access to the repository. |
| `repos_get_deploy_key` | Retrieves a specific key from a GitHub repository using its identifier. |
| `repos_delete_deploy_key` | Removes a specified deploy key from a GitHub repository using the GitHub API, returning a 204 status code upon successful deletion. |
| `issues_list_labels_for_repo` | Retrieves a list of labels for a specified GitHub repository using the GitHub API. |
| `issues_create_label` | Creates a new label for a specified GitHub repository, allowing users to categorize issues and pull requests. |
| `issues_get_label` | Retrieves a specific label from a GitHub repository by owner, repository name, and label name. |
| `issues_update_label` | Updates an existing label in a GitHub repository using the "PATCH" method, allowing modifications to its name, description, or color. |
| `issues_delete_label` | Deletes a specific label from a GitHub repository. |
| `repos_list_languages` | Retrieves the languages used in a GitHub repository, returning a list of the programming languages and their respective byte sizes. |
| `licenses_get_for_repo` | Retrieves the license file content for a specified GitHub repository and returns license information if detected. |
| `repos_merge_upstream` | Merges changes from an upstream repository branch into a forked repository branch using the POST method, allowing synchronization of branches with existing counterparts in both repositories. |
| `repos_merge` | Merges a base branch with a head branch in a GitHub repository and returns merge status details. |
| `issues_list_milestones` | Retrieves a list of milestones for a specified GitHub repository using the "GET" method. |
| `issues_create_milestone` | Creates a new milestone in the specified GitHub repository, tracking progress on issues and pull requests. |
| `issues_get_milestone` | Retrieves information about a specific milestone in a GitHub repository using the given milestone number. |
| `issues_update_milestone` | Updates a GitHub milestone using the PATCH method at the path "/repos/{owner}/{repo}/milestones/{milestone_number}" to modify its details such as title, state, or description. |
| `issues_delete_milestone` | Deletes a specified milestone from a GitHub repository using the API. |
| `get_milestone_labels` | Retrieves the list of labels for issues associated with a specific GitHub repository milestone. |
| `get_repo_notifications` | Retrieves a list of notifications for a specific GitHub repository using the "GET" method. |
| `update_repo_notifications` | Subscribes to notifications for a GitHub repository and returns a status indicating successful subscription. |
| `repos_get_pages` | Retrieves information about a GitHub Pages site associated with the specified repository. |
| `repos_create_pages_site` | Creates a GitHub Pages deployment for a specified repository using the GitHub API, enabling the hosting of static websites. |
| `update_repo_pages` | Configures GitHub Pages for a repository using the GitHub API, returning a status response after updating the pages configuration. |
| `repos_delete_pages_site` | Deletes the GitHub Pages site associated with a repository, requiring repository administrative permissions or specific access rights. |
| `repos_list_pages_builds` | Retrieves a paginated list of GitHub Pages build histories for the specified repository. |
| `repos_request_pages_build` | Creates a GitHub Pages build for a specified repository using the GitHub API and returns a successful status upon completion. |
| `repos_get_latest_pages_build` | Retrieves information about the latest GitHub Pages build for a specified repository using the GitHub API. |
| `repos_get_pages_build` | Retrieves a specific GitHub Pages build for a repository using the provided build identifier. |
| `repos_create_pages_deployment` | Deploys a GitHub Pages site for the specified repository and returns status details. |
| `repos_get_pages_deployment` | Retrieves the status of a specific GitHub Pages deployment by its identifier from a GitHub repository. |
| `repos_cancel_pages_deployment` | Cancels a specific GitHub Pages deployment using the GitHub API, requiring write permissions for the repository. |
| `repos_get_pages_health_check` | Performs a health check on the DNS settings for a GitHub Pages site in a specified repository, returning a status indicating whether the configuration is valid. |
| `get_repo_vulnerabilities` | Checks if private vulnerability reporting is enabled for a specified GitHub repository using the GET method. |
| `enable_private_reporting` | Enables private vulnerability reporting for a GitHub repository using the PUT method at the "/repos/{owner}/{repo}/private-vulnerability-reporting" path, allowing security researchers to privately report vulnerabilities to the repository maintainers. |
| `delete_repo_vulnerability_report` | Disables private vulnerability reporting for a specified GitHub repository using the "DELETE" method, returning a 204 status code upon success. |
| `projects_list_for_repo` | Retrieves a list of projects from a GitHub repository using the "GET" method, allowing filtering by state, page number, and the number of results per page. |
| `projects_create_for_repo` | Creates a new project (classic) in the specified GitHub repository and returns the created project. |
| `get_repo_properties_values` | Retrieves all custom property values assigned to a GitHub repository by its owning organization. |
| `update_repo_property_values` | Updates or removes custom property values for a GitHub repository and returns a success status upon completion. |
| `pulls_list` | Retrieves a list of pull requests from a GitHub repository, optionally filtered by state, branch, or sorting criteria. |
| `pulls_create` | Creates a new pull request from one branch into another within a specified GitHub repository using the GitHub API. |
| `list_pull_comment` | Retrieves and lists review comments for all pull requests in a specified repository, sorted in ascending order by default. |
| `pulls_get_review_comment` | Retrieves a specific pull request comment by its ID from a GitHub repository using the GitHub API. |
| `pulls_update_review_comment` | Updates a review comment for a pull request in a GitHub repository, allowing users to edit the content of a specified comment. |
| `pulls_delete_review_comment` | Deletes a specific pull request review comment from a GitHub repository using the DELETE method, requiring parameters like the repository owner, repository name, and comment ID. |
| `get_pull_comment_reactions` | Retrieves a list of reactions for a specific pull request review comment within a repository using the GitHub API. |
| `create_pull_comment_reaction` | Adds a reaction to a specific pull request review comment using the GitHub API. |
| `delete_reaction_to_comment` | Deletes a reaction from a pull request review comment using the GitHub API and returns a status code indicating success. |
| `pulls_get` | Retrieves detailed information about a specific pull request from a GitHub repository, including branch information, commit details, and merge status. |
| `pulls_update` | Updates a GitHub pull request using the API, modifying its state or details as specified in the request body. |
| `create_pull_codespace` | Creates a codespace for the authenticated user linked to the specified pull request, returning success or retry status codes. |
| `pulls_list_review_comments` | Retrieves a list of comments on a specific pull request in a repository using the GitHub API. |
| `pulls_create_review_comment` | Creates a review comment on a specific pull request's diff or code section using the GitHub API. |
| `create_pull_comment_reply` | Creates a reply to a specific comment on a GitHub pull request using the GitHub API. |
| `pulls_list_commits` | Retrieves a paginated list of commits associated with a pull request in a specified GitHub repository. |
| `pulls_list_files` | Retrieves a list of files modified in a specified GitHub pull request, including pagination parameters. |
| `pulls_check_if_merged` | Retrieves the merge status of a specific GitHub pull request using the API, returning a success status when the pull request can be merged. |
| `pulls_merge` | Merges a pull request into its base branch using the GitHub API, returning success or error messages based on the merge outcome. |
| `pulls_list_requested_reviewers` | Retrieves a list of users or teams who have been requested to review a specified pull request in a GitHub repository. |
| `pulls_request_reviewers` | Requests review from specific users or teams for a GitHub pull request and returns a status message. |
| `delete_pull_request_reviewers` | Removes requested reviewers from a GitHub pull request using the DELETE method at the "/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers" endpoint. |
| `pulls_list_reviews` | Retrieves a chronological list of all reviews for a specified pull request in the GitHub API. |
| `pulls_create_review` | Submits a review for a GitHub pull request with approval, comment, or request changes. |
| `pulls_get_review` | Retrieves a specific review for a pull request using the GitHub API, returning review details by its ID. |
| `pulls_update_review` | Updates a specified review for a pull request using the GitHub API, allowing modification of the review summary comment. |
| `pulls_delete_pending_review` | Deletes a pending review for a pull request using the GitHub API, returning a status message. |
| `pulls_list_comments_for_review` | Retrieves a list of comments for a specific review on a GitHub pull request, allowing users to access detailed feedback provided during the review process. |
| `pulls_dismiss_review` | Dismisses a specified pull request review and adds a dismissal comment using the GitHub API. |
| `pulls_submit_review` | Submits a review event (approval, request changes, or comment) for a specific pull request review using the GitHub API. |
| `pulls_update_branch` | Updates a pull request branch by merging the latest commits from the base branch into the pull request branch using the GitHub API. |
| `repos_get_readme` | Retrieves the contents of a GitHub repository's README file using the GitHub API and returns its details. |
| `repos_get_readme_in_directory` | Retrieves the README file contents from a specified directory in a GitHub repository using the "GET" method, allowing for optional specification of a branch or commit reference. |
| `repos_list_releases` | Retrieves a list of releases from a GitHub repository, including details like tag names, release notes, and associated assets. |
| `repos_create_release` | Creates a GitHub release for a repository, allowing tag-based versioning with optional release notes and metadata. |
| `repos_get_release_asset` | Retrieves a specific release asset from a GitHub repository using the provided owner, repository name, and asset ID, returning the asset details if found. |
| `repos_update_release_asset` | Updates a release asset in a GitHub repository using the PATCH method, allowing users with appropriate permissions to modify the asset's details. |
| `repos_delete_release_asset` | Deletes a release asset by its ID from a specified GitHub repository using the GitHub API and returns a successful status message upon deletion. |
| `repos_generate_release_notes` | Generates release notes content for a GitHub repository using the provided parameters. |
| `repos_get_latest_release` | Retrieves the latest release details for a GitHub repository including tag name, release notes, and associated assets. |
| `repos_get_release_by_tag` | Retrieves a specific release by its associated Git tag from a GitHub repository. |
| `repos_get_release` | Retrieves a specific release from a GitHub repository by release ID, including draft releases for authenticated users with push access. |
| `repos_update_release` | Edits an existing GitHub release using the specified release ID, allowing updates to release details such as name, description, and status. |
| `repos_delete_release` | Deletes a GitHub release using the GitHub API, returning a status code indicating the success of the operation. |
| `repos_list_release_assets` | Retrieves a paginated list of release assets for a specific release in a GitHub repository. |
| `repos_upload_release_asset` | Uploads a release asset to a specified GitHub repository using the POST method, allowing you to add binary files to releases identified by owner, repository, and release ID. |
| `reactions_list_for_release` | Retrieves a list of reactions for a specific release in a GitHub repository. |
| `reactions_create_for_release` | Adds a reaction (like 👍, 🎉, or ❤️) to a GitHub release and returns the reaction status. |
| `reactions_delete_for_release` | Removes a reaction from a GitHub release using the GitHub API and returns a status code indicating success. |
| `repos_get_branch_rules` | Retrieves all active rules applying to a specified branch in a repository, including those configured at repository or organization levels. |
| `repos_get_repo_rulesets` | Retrieves a list of rulesets for a specified GitHub repository, allowing control over how users interact with branches and tags, using the "GET" method at the "/repos/{owner}/{repo}/rulesets" path. |
| `repos_create_repo_ruleset` | Creates a repository ruleset to control branch and tag interaction policies using specified enforcement rules and conditions. |
| `repos_get_repo_rule_suites` | Retrieves a list of rule suites for a GitHub repository, which are collections of rule evaluations that enforce specific behaviors or checks, using the GitHub API. |
| `repos_get_repo_rule_suite` | Retrieves a specific rule suite evaluation result for a GitHub repository by ID. |
| `repos_get_repo_ruleset` | Retrieves a specific ruleset from a GitHub repository, including parent rulesets if specified, using the repository owner, name, and ruleset identifier. |
| `repos_update_repo_ruleset` | Updates a specific ruleset in a GitHub repository using the "PUT" method, allowing for the modification of how interactions are managed for selected branches and tags. |
| `repos_delete_repo_ruleset` | Deletes a ruleset for a specified GitHub repository using the repository's owner, repository name, and ruleset ID. |
| `repos_get_repo_ruleset_history` | Retrieves the history of a repository ruleset using the GitHub API, which provides a record of changes made to the ruleset. |
| `repos_get_repo_ruleset_version` | Retrieves a specific historical version of a repository ruleset configuration using its unique ruleset ID and version ID. |
| `list_secret_scanning_alerts` | Retrieves a list of secret scanning alerts for a specified repository, sorted from newest to oldest. |
| `secret_scanning_get_alert` | Retrieves details of a specific secret scanning alert detected in a GitHub repository using the provided alert number. |
| `secret_scanning_update_alert` | Updates a secret scanning alert in a GitHub repository using the "PATCH" method, allowing actions such as dismissing or modifying the alert's status. |
| `get_secret_locations` | Retrieves the locations of a specific secret scanning alert within a GitHub repository using the provided alert number. |
| `bypass_push_protection` | Submits a request to bypass secret scanning push protection for a repository via the GitHub API. |
| `get_repo_secret_scanning_history` | Retrieves a repository's secret scanning scan history using the GitHub API, providing visibility into when different types of secrets were scanned. |
| `list_security_advisories` | Retrieves a list of security advisories for a specified GitHub repository using the "GET" method, allowing users to manage and view vulnerabilities associated with the repository. |
| `create_security_advisory` | Creates a repository security advisory to report vulnerabilities and track security issues in a GitHub repository. |
| `create_security_advisory_report` | Creates a new repository security advisory report for a specified GitHub repository to track and manage security vulnerabilities. |
| `get_security_advisory_by_id` | Retrieves a specific repository security advisory identified by its GitHub Security Advisory (GHSA) ID, including details like summary, description, and associated CVE. |
| `update_security_advisory` | Updates a specific repository security advisory identified by its GSHA ID using the GitHub API. |
| `post_repo_security_advisory_cve` | Requests a CVE identification number for a specified GitHub Security Advisory (GHSA) in a repository. |
| `fork_security_advisory` | Creates a temporary private fork for a repository security advisory, allowing private collaboration on fixing a security vulnerability. |
| `list_stargazers` | Retrieves a list of users who have starred the specified GitHub repository. |
| `repos_get_code_frequency_stats` | Retrieves a weekly aggregate of the number of additions and deletions pushed to a GitHub repository using the REST API. |
| `get_repo_commit_activity_stats` | Retrieves the commit activity statistics for a GitHub repository using the "GET" method, which includes information such as the number of commits by week. |
| `repos_get_contributors_stats` | Retrieves weekly commit activity statistics for contributors in a GitHub repository, including additions, deletions, and commit counts. |
| `repos_get_participation_stats` | Retrieves the commit participation data (weekly commit counts) for a repository, including owner and contributor activity. |
| `repos_get_punch_card_stats` | Retrieves the hourly commit count for each day of the week from a GitHub repository, providing data in the format of a punch card. |
| `repos_create_commit_status` | Creates a commit status (e.g., success, failure) for a specific SHA in a GitHub repository, including optional context and target URL. |
| `list_subscribers` | Retrieves a paginated list of users subscribed to notifications for a GitHub repository. |
| `activity_get_repo_subscription` | Retrieves a subscription status for a GitHub repository using the "GET" method at "/repos/{owner}/{repo}/subscription", returning a response based on the repository's subscription status. |
| `activity_set_repo_subscription` | Subscribes to notifications for activity in a GitHub repository and returns the subscription status. |
| `unsubscribe_repo` | Removes the authenticated user's subscription to a GitHub repository. |
| `repos_list_tags` | Retrieves a list of repository tags from a GitHub repository. |
| `repos_list_tag_protection` | Retrieves tag protection rules configured for a GitHub repository. |
| `repos_create_tag_protection` | Creates a tag protection rule for a GitHub repository to prevent unauthorized tag operations. |
| `repos_delete_tag_protection` | Deletes a tag protection state for a specified repository using the GitHub API, removing the protection rules associated with the given tag protection ID. |
| `repos_download_tarball_archive` | Redirects to a URL for downloading a tar archive of a GitHub repository, specified by the repository owner, name, and reference (e.g., branch or tag), returning a redirect status (302) with the download link. |
| `repos_list_teams` | Retrieves a list of teams associated with a specific GitHub repository using the "GET /repos/{owner}/{repo}/teams" method. |
| `repos_get_all_topics` | Retrieves a list of repository topics for a specified GitHub repository using the "GET" method. |
| `repos_replace_all_topics` | Updates the topics for a GitHub repository using the GitHub API. |
| `repos_get_clones` | Retrieves the total number of clones and breakdown per day or week for a GitHub repository using the "GET" method, providing traffic data for the specified repository. |
| `repos_get_top_paths` | Retrieves the top 10 popular paths in a GitHub repository over the last 14 days using the "GET" method at the "/repos/{owner}/{repo}/traffic/popular/paths" endpoint. |
| `repos_get_top_referrers` | Retrieves a list of the most popular referrers for a GitHub repository, providing details on traffic sources. |
| `repos_get_views` | Retrieves the total number of views and daily/weekly breakdowns for a GitHub repository over the last 14 days. |
| `repos_transfer` | Transfers ownership of a GitHub repository to another user or organization using the GitHub API and returns a success status upon initiation. |
| `list_vulnerability_alerts` | Retrieves vulnerability alerts for a specific GitHub repository. |
| `update_vulnerability_alerts` | Updates vulnerability alerts for a GitHub repository at the specified path using the PUT method. |
| `delete_vulnerability_alerts` | Disables vulnerability alerts for the specified GitHub repository. |
| `repos_download_zipball_archive` | Downloads a ZIP archive of a GitHub repository at a specified reference using the GitHub API. |
| `repos_create_using_template` | Creates a new GitHub repository from a specified template repository using the GitHub API. |
| `repos_list_public` | Retrieves a list of repositories filtered by a timestamp parameter, returning status codes for successful responses, not modified, or validation errors. |
| `search_code` | Searches code using specified query parameters and returns matching results. |
| `search_commits` | Searches for commits on GitHub using a query and returns a list of matching commits, supporting options for sorting, ordering, and pagination. |
| `search_issues` | Searches GitHub issues and pull requests using specified filters and returns matching results. |
| `search_labels` | Retrieves a list of labels for a specified repository using the "GET" method, allowing filtering by query, sorting, and pagination. |
| `search_repos` | Searches and retrieves a list of GitHub repositories based on search parameters using the GitHub API. |
| `search_topics` | Retrieves a list of topics matching a search query with pagination support. |
| `search_users` | Searches for GitHub users based on specified query parameters and returns matching results. |
| `teams_get_legacy` | Retrieves information for a specific team by its ID using the GET method at the "/teams/{team_id}" endpoint. |
| `teams_update_legacy` | Updates a team's properties by applying partial modifications using the PATCH method at the "/teams/{team_id}" path. |
| `teams_delete_legacy` | Deletes a team with the specified ID from the system, returning appropriate status codes based on the operation's success or failure. |
| `teams_list_discussions_legacy` | Retrieves a paginated list of discussion posts from a specific team's page via GitHub API. |
| `teams_create_discussion_legacy` | Creates a new discussion post on a GitHub team's page using the `POST` method. |
| `teams_get_discussion_legacy` | Retrieves a specific team discussion from a GitHub team using the provided team ID and discussion number. |
| `teams_update_discussion_legacy` | Updates a team discussion's title and body text via the GitHub API. |
| `teams_delete_discussion_legacy` | Deletes a team discussion and returns an empty response. |
| `get_discussion_comments` | Retrieves a paginated list of comments for a specific team discussion via the GitHub API. |
| `create_team_discussion_comment` | Creates a new discussion comment on a specified team discussion post using the GitHub API. |
| `get_comment_by_number` | Retrieves a specific comment from a team discussion on GitHub using the provided team ID, discussion number, and comment number. |
| `patch_team_discussion_comment` | Updates a comment on a team discussion using the GitHub API, returning a success status upon completion. |
| `delete_comment` | Deletes a specific comment within a team discussion on GitHub using the API and returns a successful status message upon deletion. |
| `get_reaction_by_comment` | Lists reactions (e.g., 👍, ❤️) for a specific comment in a team discussion using the GitHub API. |
| `add_team_comment_reaction` | Creates a reaction to a team discussion comment, allowing users to interact with comments on team discussions using the GitHub API. |
| `get_team_discussion_reactions` | Retrieves a list of reactions for a specific discussion post within a team using the GitHub API. |
| `add_reaction_to_discussion` | Adds a reaction to a team discussion comment using the GitHub API. |
| `get_team_invitations` | Retrieves a list of pending invitations for a specified GitHub team using the "GET" method at the "/teams/{team_id}/invitations" path. |
| `teams_list_members_legacy` | Retrieves a list of members for a specified team, optionally filtered by role, with pagination support. |
| `teams_get_member_legacy` | Retrieves a specific team member's details by username within a team. |
| `teams_add_member_legacy` | Adds a user to a team by their username and returns a success status. |
| `teams_remove_member_legacy` | Removes a member with the specified username from a team using the DELETE method. |
| `get_team_membership_by_username` | Retrieves the team membership status for a specific user in a GitHub organization team. |
| `update_membership_for_user` | Adds or updates team membership for a user, granting organization owners/team maintainers the ability to invite new members or modify existing roles. |
| `delete_membership_by_user` | Removes a team membership for a specified user using the GitHub API and returns a status message. |
| `teams_list_projects_legacy` | Retrieves a list of projects for a specified team using the team ID. |
| `get_team_project` | Retrieves a specific project within a designated team using provided identifiers. |
| `update_project_details` | Updates the project details for a specified team and returns a success status upon completion. |
| `teams_remove_project_legacy` | Deletes a project from a specified team using the "DELETE" method and returns a status message based on the operation's success or failure. |
| `teams_list_repos_legacy` | Retrieves a list of repositories accessible to the specified team using the GitHub API. |
| `get_team_repo_by_owner_repo` | Retrieves the permissions and status of a specific repository for a GitHub team using the team ID, repository owner, and repository name. |
| `update_team_repo` | Adds a repository to a GitHub team using the GitHub API, requiring the team ID, repository owner, and repository name. |
| `teams_remove_repo_legacy` | Removes a repository from a team using the GitHub API, deleting the repository's association with the specified team without deleting the repository itself. |
| `teams_list_child_legacy` | Retrieves a list of teams associated with the specified team ID using the GET method. |
| `users_get_authenticated` | Retrieves user information using the "GET" method at the "/user" path. |
| `users_update_authenticated` | Updates a user's information using the PATCH method at the "/user" endpoint, allowing partial modifications to user data. |
| `list_user_blocks` | Retrieves a list of user blocks using the "GET" method at the "/user/blocks" endpoint, allowing for pagination through "per-page" and "page" parameters. |
| `users_check_blocked` | Retrieves information about a blocked user specified by the username parameter. |
| `users_block` | Updates the block status for a user, specified by their username, and returns a status message. |
| `users_unblock` | Unblocks a GitHub user using the GitHub API by deleting the block for the specified username and returns a status message upon success. |
| `list_codespaces` | Retrieves a paginated list of the authenticated user's GitHub Codespaces, optionally filtered by repository ID. |
| `create_user_codespace` | Creates a new GitHub Codespace for the authenticated user and returns status codes indicating success or error conditions. |
| `list_user_secrets` | Retrieves a list of secrets for the authenticated user's GitHub Codespaces using the "GET" method, allowing access to secrets such as access tokens for cloud services without revealing their encrypted values. |
| `get_codespaces_public_key` | Retrieves a public key for encrypting user secrets in GitHub Codespaces, which is necessary for creating or updating encrypted secrets. |
| `get_secret_by_name` | Retrieves a secret for the authenticated user's GitHub Codespaces without revealing its encrypted value, allowing access to sensitive information like access tokens or credentials. |
| `update_secret_code` | Creates or updates a user-specific secret for GitHub Codespaces, making it available to authorized repositories. |
| `delete_secret_by_name` | Deletes a development environment secret for the authenticated user from GitHub Codespaces using the specified secret name, removing access from all associated codespaces. |
| `get_secret_repositories` | Lists the repositories that have been granted access to a specific user secret in GitHub Codespaces. |
| `put_user_codespaces_secret_repos` | Associates a specified secret with one or more repositories in a user's GitHub Codespaces, using the "PUT" method. |
| `update_secrets_repository` | Associates a secret with a specified repository in a user's codespaces using the GitHub API, updating the secret's repository linkage. |
| `delete_secret_repo_access` | Removes a repository from the list of repositories assigned to a user's Codespaces secret using the GitHub API. |
| `get_user_codespace_by_name` | Retrieves details for a specific user-owned GitHub Codespace by name. |
| `update_codespace` | Updates an existing GitHub Codespace (cloud development environment) with configuration changes. |
| `delete_codespace` | Deletes a specified codespace using the GitHub API, returning a status message if successful. |
| `export_codespace` | Initiates an export of a specific GitHub codespace identified by its name, returning a status and details for monitoring the export process. |
| `get_user_codespace_export_by_id` | Retrieves the status and details of a specific export operation for an authenticated user's codespace. |
| `get_codespace_machines` | Retrieves available machine types for a GitHub Codespace to allow changing its compute resources upon restart. |
| `publish_codespace` | Publishes a GitHub Codespace using the GitHub API and returns a status message. |
| `start_codespace` | Starts a GitHub Codespace instance using the GitHub Codespaces API and returns a status message. |
| `stop_user_codespace` | Stops a running GitHub Codespace and returns a status code. |
| `get_user_docker_conflicts` | Retrieves a list of conflicting Docker packages during migration for the authenticated user. |
| `update_email_visibility` | Updates the visibility of the authenticated user's email address (e.g., public/private) and returns the updated email details. |
| `list_user_emails` | Retrieves a paginated list of user email addresses. |
| `add_user_email` | Adds a new email address for the authenticated user and returns a status message. |
| `delete_emails` | Deletes specified email addresses from the authenticated user's GitHub account and returns a 204 No Content status upon success. |
| `list_user_followers` | Retrieves a paginated list of followers associated with the user, supporting pagination via per_page and page parameters. |
| `list_following_users` | Retrieves a list of users that the authenticated user is following, with options to paginate the results. |
| `get_following_user` | Checks if the authenticated user follows a specified user on GitHub and returns a status code indicating the result. |
| `users_follow` | Follows a specified user or updates the following relationship for the current user to the specified username. |
| `users_unfollow` | Unfollows a user using the "DELETE" method, removing the specified user from the list of users being followed. |
| `get_gpg_keys` | Retrieves a list of GPG keys for the authenticated user, allowing pagination through optional page and per-page parameters. |
| `create_gpg_key` | Adds a GPG key to a user's account using the API endpoint at "/user/gpg_keys" with the POST method. |
| `get_gpg_key_by_id` | Retrieves a specific GPG key for a user using the "GET" method, identified by the provided GPG key ID. |
| `delete_user_gpg_key_by_id` | Deletes a GPG key identified by its ID from a user's account using the DELETE method. |
| `get_user_installations` | Retrieves a paginated list of user installations with the specified page and per-page parameters. |
| `list_installation_repositories` | Lists repositories accessible to a specific GitHub App installation with pagination support. |
| `update_repository_installation` | Updates the repository selection for a GitHub App installation using the "PUT" method at the path "/user/installations/{installation_id}/repositories/{repository_id}". |
| `delete_repository_installation` | Removes a specific repository from a GitHub App installation's list of accessible repositories. |
| `get_interaction_limits` | Retrieves the current user-level interaction limits restricting comment, issue, and pull request creation on public repositories. |
| `update_user_interaction_limits` | Sets interaction limits for a GitHub user's repositories using the PUT method at the "/user/interaction-limits" path, allowing control over which types of users can comment, open issues, or create pull requests. |
| `delete_user_interaction_limits` | Removes user interaction limits using the GitHub API, returning a status of "No Content" upon successful deletion. |
| `list_user_issues` | Retrieves a list of user issues using the "GET" method at the "/user/issues" endpoint, allowing filtering by parameters such as filter, state, labels, sort order, since, page size, and page number. |
| `get_keys` | Retrieves a list of user keys with pagination support. |
| `create_user_key` | Creates a new API key for a user account and returns the generated key upon success. |
| `get_user_key_by_id` | Retrieves a specific user key by ID from the API. |
| `delete_user_key_by_id` | Deletes a user API key identified by the key ID using the DELETE method. |
| `get_user_marketplace_purchases` | Retrieves a paginated list of a user's marketplace purchases. |
| `get_marketplace_purchases` | Retrieves a paginated list of stubbed marketplace purchases for the authenticated user. |
| `list_org_memberships` | Retrieves a list of organization memberships for the authenticated user using the "GET" method at the "/user/memberships/orgs" endpoint. |
| `get_user_memberships_org` | Retrieves the authenticated user's membership status for a specified GitHub organization. |
| `update_org_membership` | Updates the authenticated user's organization membership role for the specified organization. |
| `list_user_migrations` | Retrieves a list of user migrations using pagination, allowing users to view their migration history. |
| `create_user_migration` | Initiates user migrations using the "POST" method at the "/user/migrations" endpoint, returning status messages based on the request outcome. |
| `get_migration_by_id` | Retrieves the status and details of a specific user migration using the provided migration ID. |
| `get_user_migration_archive` | Retrieves the archived user migration data from GitHub using the specified migration ID. |
| `delete_user_migration_archive` | Deletes the user migration archive associated with the specified migration ID. |
| `delete_repo_lock` | Unlocks a GitHub repository that was previously locked for migration using the "DELETE" method. |
| `list_migration_repositories` | Retrieves a paginated list of repositories associated with a user's migration using the specified migration ID. |
| `list_user_orgs` | Retrieves a list of organizations associated with a user using the specified page and per-page parameters. |
| `get_packages` | Retrieves a list of user packages filtered by package type and visibility, with options for pagination. |
| `get_user_package_by_type_name` | Retrieves information about a specific package based on the package type and name using the GET method. |
| `delete_package_by_name` | Deletes a specific user package by type and name using the DELETE method at the "/user/packages/{package_type}/{package_name}" path. |
| `restore_user_package_by_type_name` | Restores a specified package for the authenticated user using a provided token. |
| `get_package_versions` | Retrieves a list of versions for a specific package type and name, optionally filtered by state and paginated. |
| `get_user_package_version_by_id` | Retrieves specific version details for a package based on type, name, and version ID. |
| `delete_package_version_by_id` | Deletes a specific package version from the user's package registry. |
| `restore_user_package_version` | Restores a specific version of a user's package from the deleted state using the GitHub API. |
| `create_project` | Adds a user to one or more projects using the API and returns relevant status messages based on the HTTP response codes, such as successful creation, unauthorized access, or validation errors. |
| `get_public_emails` | Retrieves a paginated list of publicly visible email addresses for the user. |
| `list_user_repos` | Lists and retrieves the repositories owned by the authenticated user, allowing filtering by visibility, affiliation, type, and sorting options using the GitHub API. |
| `create_user_repo` | Creates a new repository for the authenticated user on GitHub and returns the repository details upon success. |
| `list_repository_invitations` | Retrieves the authenticated user's pending repository invitations using pagination parameters for page and results per page. |
| `update_invitation` | Updates a specific repository invitation using the GitHub API. |
| `delete_repository_invitation` | Deletes a repository invitation using the GitHub API, returning an appropriate status code based on the outcome. |
| `list_social_accounts` | Retrieves a list of a user's social accounts using the GET method, allowing pagination with per-page and page parameters. |
| `create_social_account` | Adds social media accounts to the authenticated user's GitHub profile using provided URLs and returns a success status upon creation. |
| `delete_social_accounts` | Deletes specified social media accounts linked to the authenticated user's GitHub profile. |
| `list_ssh_signing_keys` | Retrieves SSH signing keys for the authenticated user, supporting pagination via per-page and page parameters. |
| `create_user_ssh_signing_key` | Creates an SSH signing key for the authenticated user's GitHub account using the "POST" method. |
| `get_ssh_signing_key` | Retrieves extended details for a specific SSH signing key associated with a GitHub user account. |
| `delete_user_ssh_signing_key` | Deletes an SSH signing key from a GitHub user account using the GitHub API. |
| `list_starred_users` | Retrieves a list of repositories starred by the authenticated user, optionally filtered by sort order and pagination parameters. |
| `get_user_starred_repo` | Retrieves information about whether a specific repository is starred by the authenticated user using the GitHub API. |
| `star_repo_for_user` | Stars a GitHub repository for the authenticated user using the GitHub API. |
| `delete_starred_repo` | Unstars a GitHub repository using the GitHub API by deleting a star that the authenticated user previously applied to a specified repository owned by `{owner}` and named `{repo}`, returning status messages based on the operation's outcome. |
| `get_user_subscriptions` | Retrieves a list of user subscriptions using pagination. |
| `list_user_teams` | Retrieves a list of teams associated with a user using the API at the "/user/teams" endpoint with pagination options. |
| `users_get_by_id` | Retrieves user details for the specified account ID. |
| `users_list` | Retrieves a paginated list of users, filtered by the specified parameters. |
| `users_get_by_username` | Retrieves user information based on the provided username using the GET method at the "/users/{username}" endpoint. |
| `users_list_attestations` | Retrieves a list of attestations for a specified user and subject digest, supporting pagination and filtering by predicate type. |
| `get_docker_conflicts_by_username` | Retrieves and reports Docker conflicts associated with a specified user, returning access and status codes. |
| `get_user_events` | Retrieves a paginated list of events associated with a specific user, such as user activity or interactions. |
| `get_org_events_by_user` | Retrieves a paginated list of public organization events for a specified user and organization. |
| `get_public_events_by_user` | Retrieves a list of public events for a specified GitHub user using the "GET" method, allowing pagination with parameters such as username, page number, and results per page. |
| `users_list_followers_for_user` | Retrieves a paginated list of followers for the specified user. |
| `users_list_following_for_user` | Retrieves a list of users that the specified user is following. |
| `users_check_following_for_user` | Retrieves whether a user is following another user by fetching the follow status for a specific target user using the GET method. |
| `gists_list_for_user` | Retrieves a list of public gists associated with a specified GitHub user, optionally filtered by creation time and paginated using page size and number parameters. |
| `users_list_gpg_keys_for_user` | Retrieves a list of GPG keys for a specified user using the "GET" method, allowing pagination via optional per-page and page parameters. |
| `users_get_context_for_user` | Retrieves a hovercard, providing contextual information about a user, using the GitHub API at the path "/users/{username}/hovercard" with the "GET" method, optionally specifying subject type and ID. |
| `apps_get_user_installation` | Retrieves a GitHub App installation associated with a specific user account. |
| `get_user_keys` | Retrieves a paginated list of SSH keys associated with the specified user account. |
| `orgs_list_for_user` | Retrieves a list of organizations a specific user belongs to via the GitHub API. |
| `get_packages_by_user` | Retrieves a list of packages for a specific user using the provided username, with options to filter by package type and visibility, and paginate the results. |
| `packages_get_package_for_user` | Retrieves a specific package of a given type associated with the specified user's username. |
| `delete_package_by_user` | Deletes a package of a specified type and name associated with a given user using the DELETE method. |
| `restore_user_package` | Restores a specific package using the POST method at the "/users/{username}/packages/{package_type}/{package_name}/restore" endpoint. |
| `get_user_package_versions` | Retrieves the versions of a specific package for a user using the provided username, package type, and package name, returning the result in response to a GET request. |
| `get_package_version_details` | Retrieves package version details for a specified package name and version under a user's account using the "GET" method. |
| `delete_user_package_version` | Deletes a specific version of a package associated with a user, identified by the package type, name, and version ID, using the DELETE method. |
| `restore_package_version` | Restores a specific package version of a given package type for a user, using the POST method, by moving it back from an archived or deleted state to its original location. |
| `projects_list_for_user` | Retrieves a list of projects for a specified user, filtered by optional state, with pagination options. |
| `get_received_events_for_user` | Retrieves a list of events received by a specified GitHub user using the "GET" method, allowing for pagination through recent activity. |
| `get_user_public_received_events` | Retrieves a list of public events received by a specified GitHub user account, including pagination support. |
| `repos_list_for_user` | Retrieves a list of repositories for a specified GitHub user using the "GET" method, allowing for filtering by repository type, sorting, and pagination. |
| `get_billing_actions_by_user` | Retrieves billing actions for a specific user using the provided username. |
| `get_user_billing_packages` | Retrieves billing package information for a specified user. |
| `get_shared_storage_settings` | Retrieves a user's shared storage billing settings for the specified username. |
| `get_billing_usage` | Retrieves billing usage details for a specified user with parameters for year, month, day, and hour. |
| `get_social_accounts_by_user` | Retrieves a list of social accounts for a specific user using the "GET" method, allowing pagination through optional per-page and page parameters. |
| `list_user_ssh_signing_keys` | Retrieves a list of SSH signing keys associated with the specified GitHub user account. |
| `get_user_starred_repositories` | Retrieves a list of repositories starred by a specified GitHub user, allowing pagination and sorting of the results. |
| `list_user_subscriptions` | Retrieves a paginated list of subscriptions for the specified username. |
| `meta_get_all_versions` | Retrieves a list of available versions supported by the API. |
| `meta_get_zen` | Retrieves data at the "/zen" path using the "GET" method. |
