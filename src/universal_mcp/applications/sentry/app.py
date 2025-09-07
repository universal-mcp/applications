from typing import Any

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class SentryApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="sentry", integration=integration, **kwargs)
        self.base_url = "https://us.sentry.io"

    def list_your_organizations(
        self, owner=None, cursor=None, query=None, sortBy=None
    ) -> list[Any]:
        """
        Retrieves a list of organizations using the "GET" method, allowing filtering by owner, query, and sorting, and requires authentication with admin, read, or write permissions.

        Args:
            owner (boolean): Filters results to only include organizations where the current user is the owner (if true) or excludes owner-only organizations (if false).
            cursor (string): A string token used for cursor-based pagination to specify the position in the dataset from which to continue fetching organizations.
            query (string): Filter or search string to narrow results within the specified organizations.
            sortBy (string): Specifies the field to sort the organizations by, allowing users to customize the order of the returned data.

        Returns:
            list[Any]: API response data.

        Tags:
            Users, important
        """
        url = f"{self.base_url}/api/0/organizations/"
        query_params = {
            k: v
            for k, v in [
                ("owner", owner),
                ("cursor", cursor),
                ("query", query),
                ("sortBy", sortBy),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_an_organization(
        self, organization_id_or_slug, detailed=None
    ) -> dict[str, Any]:
        """
        Retrieves detailed information about a specified organization by its ID or slug, optionally including extended details, requiring appropriate organizational permissions.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            detailed (string): Indicates whether to return detailed information for the organization, with possible values specifying the level of detail.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Organizations, important
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/"
        query_params = {k: v for k, v in [("detailed", detailed)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_an_organization(
        self,
        organization_id_or_slug,
        slug=None,
        name=None,
        isEarlyAdopter=None,
        hideAiFeatures=None,
        codecovAccess=None,
        defaultRole=None,
        openMembership=None,
        eventsMemberAdmin=None,
        alertsMemberWrite=None,
        attachmentsRole=None,
        debugFilesRole=None,
        avatarType=None,
        avatar=None,
        require2FA=None,
        allowSharedIssues=None,
        enhancedPrivacy=None,
        scrapeJavaScript=None,
        storeCrashReports=None,
        allowJoinRequests=None,
        dataScrubber=None,
        dataScrubberDefaults=None,
        sensitiveFields=None,
        safeFields=None,
        scrubIPAddresses=None,
        relayPiiConfig=None,
        trustedRelays=None,
        githubPRBot=None,
        githubOpenPRBot=None,
        githubNudgeInvite=None,
        issueAlertsThreadFlag=None,
        metricAlertsThreadFlag=None,
        cancelDeletion=None,
    ) -> dict[str, Any]:
        """
        Updates an existing organization using the provided JSON data, replacing its current details, and requires authentication with permissions to write or administer the organization.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            slug (string): The new slug for the organization, which needs to be unique.
            name (string): The new name for the organization.
            isEarlyAdopter (boolean): Specify `true` to opt-in to new features before they're released to the public.
            hideAiFeatures (boolean): Specify `true` to hide AI features from the organization.
            codecovAccess (boolean): Specify `true` to enable Code Coverage Insights. This feature is only available for organizations on the Team plan and above. Learn more about Codecov [here](/product/codecov/).
            defaultRole (string): The default role new members will receive.

        * `member` - Member
        * `admin` - Admin
        * `manager` - Manager
        * `owner` - Owner
            openMembership (boolean): Specify `true` to allow organization members to freely join any team.
            eventsMemberAdmin (boolean): Specify `true` to allow members to delete events (including the delete & discard action) by granting them the `event:admin` scope.
            alertsMemberWrite (boolean): Specify `true` to allow members to create, edit, and delete alert rules by granting them the `alerts:write` scope.
            attachmentsRole (string): The role required to download event attachments, such as native crash reports or log files.

        * `member` - Member
        * `admin` - Admin
        * `manager` - Manager
        * `owner` - Owner
            debugFilesRole (string): The role required to download debug information files, ProGuard mappings and source maps.

        * `member` - Member
        * `admin` - Admin
        * `manager` - Manager
        * `owner` - Owner
            avatarType (string): The type of display picture for the organization.

        * `letter_avatar` - Use initials
        * `upload` - Upload an image
            avatar (string): The image to upload as the organization avatar, in base64. Required if `avatarType` is `upload`.
            require2FA (boolean): Specify `true` to require and enforce two-factor authentication for all members.
            allowSharedIssues (boolean): Specify `true` to allow sharing of limited details on issues to anonymous users.
            enhancedPrivacy (boolean): Specify `true` to enable enhanced privacy controls to limit personally identifiable information (PII) as well as source code in things like notifications.
            scrapeJavaScript (boolean): Specify `true` to allow Sentry to scrape missing JavaScript source context when possible.
            storeCrashReports (integer): How many native crash reports (such as Minidumps for improved processing and download in issue details) to store per issue.

        * `0` - Disabled
        * `1` - 1 per issue
        * `5` - 5 per issue
        * `10` - 10 per issue
        * `20` - 20 per issue
        * `50` - 50 per issue
        * `100` - 100 per issue
        * `-1` - Unlimited
            allowJoinRequests (boolean): Specify `true` to allow users to request to join your organization.
            dataScrubber (boolean): Specify `true` to require server-side data scrubbing for all projects.
            dataScrubberDefaults (boolean): Specify `true` to apply the default scrubbers to prevent things like passwords and credit cards from being stored for all projects.
            sensitiveFields (array): A list of additional global field names to match against when scrubbing data for all projects.
            safeFields (array): A list of global field names which data scrubbers should ignore.
            scrubIPAddresses (boolean): Specify `true` to prevent IP addresses from being stored for new events on all projects.
            relayPiiConfig (string): Advanced data scrubbing rules that can be configured for each project as a JSON string. The new rules will only apply to new incoming events. For more details on advanced data scrubbing, see our [full documentation](/security-legal-pii/scrubbing/advanced-datascrubbing/).

        > Warning: Calling this endpoint with this field fully overwrites the advanced data scrubbing rules.

        Below is an example of a payload for a set of advanced data scrubbing rules for masking credit card numbers from the log message (equivalent to `[Mask] [Credit card numbers] from [$message]` in the Sentry app) and removing a specific key called `foo` (equivalent to `[Remove] [Anything] from [extra.foo]` in the Sentry app):
        ```json
        {
            relayPiiConfig: "{\"rules":{\"0\":{\"type\":\"creditcard\",\"redaction\":{\"method\":\"mask\"}},\"1\":{\"type\":\"anything\",\"redaction\":{\"method\":\"remove\"}}},\"applications\":{\"$message\":[\"0\"],\"extra.foo\":[\"1\"]}}"
        }
        ```

            trustedRelays (array): A list of local Relays (the name, public key, and description as a JSON) registered for the organization. This feature is only available for organizations on the Business and Enterprise plans. Read more about Relay [here](/product/relay/).

                                                  Below is an example of a list containing a single local Relay registered for the organization:
                                                  ```json
                                                  {
                                                    trustedRelays: [
                                                        {
                                                            name: "my-relay",
                                                            publicKey: "eiwr9fdruw4erfh892qy4493reyf89ur34wefd90h",
                                                            description: "Configuration for my-relay."
                                                        }
                                                    ]
                                                  }
                                                  ```

            githubPRBot (boolean): Specify `true` to allow Sentry to comment on recent pull requests suspected of causing issues. Requires a GitHub integration.
            githubOpenPRBot (boolean): Specify `true` to allow Sentry to comment on open pull requests to show recent error issues for the code being changed. Requires a GitHub integration.
            githubNudgeInvite (boolean): Specify `true` to allow Sentry to detect users committing to your GitHub repositories that are not part of your Sentry organization. Requires a GitHub integration.
            issueAlertsThreadFlag (boolean): Specify `true` to allow the Sentry Slack integration to post replies in threads for an Issue Alert notification. Requires a Slack integration.
            metricAlertsThreadFlag (boolean): Specify `true` to allow the Sentry Slack integration to post replies in threads for a Metric Alert notification. Requires a Slack integration.
            cancelDeletion (boolean): Specify `true` to restore an organization that is pending deletion.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Organizations
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        request_body = {
            "slug": slug,
            "name": name,
            "isEarlyAdopter": isEarlyAdopter,
            "hideAiFeatures": hideAiFeatures,
            "codecovAccess": codecovAccess,
            "defaultRole": defaultRole,
            "openMembership": openMembership,
            "eventsMemberAdmin": eventsMemberAdmin,
            "alertsMemberWrite": alertsMemberWrite,
            "attachmentsRole": attachmentsRole,
            "debugFilesRole": debugFilesRole,
            "avatarType": avatarType,
            "avatar": avatar,
            "require2FA": require2FA,
            "allowSharedIssues": allowSharedIssues,
            "enhancedPrivacy": enhancedPrivacy,
            "scrapeJavaScript": scrapeJavaScript,
            "storeCrashReports": storeCrashReports,
            "allowJoinRequests": allowJoinRequests,
            "dataScrubber": dataScrubber,
            "dataScrubberDefaults": dataScrubberDefaults,
            "sensitiveFields": sensitiveFields,
            "safeFields": safeFields,
            "scrubIPAddresses": scrubIPAddresses,
            "relayPiiConfig": relayPiiConfig,
            "trustedRelays": trustedRelays,
            "githubPRBot": githubPRBot,
            "githubOpenPRBot": githubOpenPRBot,
            "githubNudgeInvite": githubNudgeInvite,
            "issueAlertsThreadFlag": issueAlertsThreadFlag,
            "metricAlertsThreadFlag": metricAlertsThreadFlag,
            "cancelDeletion": cancelDeletion,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_an_organization_s_metric_alert_rules(
        self, organization_id_or_slug
    ) -> list[Any]:
        """
        Retrieves the list of alert rules associated with the specified organization and requires appropriate read and organization permissions.

        Args:
            organization_id_or_slug (string): organization_id_or_slug

        Returns:
            list[Any]: API response data.

        Tags:
            Alerts
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/alert-rules/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_organization_metric_alert_rule(
        self,
        organization_id_or_slug,
        name,
        aggregate,
        timeWindow,
        projects,
        query,
        thresholdType,
        triggers,
        environment=None,
        dataset=None,
        queryType=None,
        eventTypes=None,
        comparisonDelta=None,
        resolveThreshold=None,
        owner=None,
        monitorType=None,
        activationCondition=None,
    ) -> dict[str, Any]:
        """
        Creates a new alert rule for an organization using the provided JSON data and returns a success response upon creation.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            name (string): The name for the rule, which has a maximimum length of 256 characters.
            aggregate (string): A string representing the aggregate function used in this alert rule. Valid aggregate functions are `count`, `count_unique`, `percentage`, `avg`, `apdex`, `failure_rate`, `p50`, `p75`, `p95`, `p99`, `p100`, and `percentile`. See [Metric Alert Rule Types](#metric-alert-rule-types) for valid configurations.
            timeWindow (integer): The time period to aggregate over.

        * `1` - 1 minute
        * `5` - 5 minutes
        * `10` - 10 minutes
        * `15` - 15 minutes
        * `30` - 30 minutes
        * `60` - 1 hour
        * `120` - 2 hours
        * `240` - 4 hours
        * `1440` - 24 hours
            projects (array): Metric alerts are currently limited to one project. The array should contain a single slug, representing the project to filter by.
            query (string): An event search query to subscribe to and monitor for alerts. For example, to filter transactions so that only those with status code 400 are included, you could use `"query": "http.status_code:400"`. Use an empty string for no filter.
            thresholdType (integer): The comparison operator for the critical and warning thresholds. The comparison operator for the resolved threshold is automatically set to the opposite operator. When a percentage change threshold is used, `0` is equivalent to "Higher than" and `1` is equivalent to "Lower than".

        * `0` - Above
        * `1` - Below
            triggers (array):
        A list of triggers, where each trigger is an object with the following fields:
        - `label`: One of `critical` or `warning`. A `critical` trigger is always required.
        - `alertThreshold`: The value that the subscription needs to reach to trigger the
        alert rule.
        - `actions`: A list of actions that take place when the threshold is met.
        ```json
        triggers: [
            {
                "label": "critical",
                "alertThreshold": 50,
                "actions": [
                    {
                        "type": "slack",
                        "targetType": "specific",
                        "targetIdentifier": "#get-crit",
                        "inputChannelId": 2454362
                        "integrationId": 653532,
                    }
                ]
            },
            {
                "label": "warning",
                "alertThreshold": 25,
                "actions": []
            }
        ]
        ```
        Metric alert rule trigger actions follow the following structure:
        - `type`: The type of trigger action. Valid values are `email`, `slack`, `msteams`, `pagerduty`, `sentry_app`, `sentry_notification`, and `opsgenie`.
        - `targetType`: The type of target the notification will be sent to. Valid values are `specific` (`targetIdentifier` is a direct reference used by the service, like an email address or a Slack channel ID), `user` (`targetIdentifier` is a Sentry user ID), `team` (`targetIdentifier` is a Sentry team ID), and `sentry_app` (`targetIdentifier` is a SentryApp ID).
        - `targetIdentifier`: The ID of the target. This must be an integer for PagerDuty and Sentry apps, and a string for all others. Examples of appropriate values include a Slack channel name (`#my-channel`), a user ID, a team ID, a Sentry app ID, etc.
        - `inputChannelId`: The ID of the Slack channel. This is only used for the Slack action, and can be used as an alternative to providing the `targetIdentifier`.
        - `integrationId`: The integration ID. This is required for every action type excluding `email` and `sentry_app.`
        - `sentryAppId`: The ID of the Sentry app. This is required when `type` is `sentry_app`.
        - `priority`: The severity of the Pagerduty alert or the priority of the Opsgenie alert (optional). Defaults for Pagerduty are `critical` for critical and `warning` for warning. Defaults for Opsgenie are `P1` for critical and `P2` for warning.

            environment (string): The name of the environment to filter by. Defaults to all environments.
            dataset (string): The name of the dataset that this query will be executed on. Valid values are `events`, `transactions`, `metrics`, `sessions`, and `generic-metrics`. Defaults to `events`. See [Metric Alert Rule Types](#metric-alert-rule-types) for valid configurations.
            queryType (integer): The type of query. If no value is provided, `queryType` is set to the default for the specified `dataset.` See [Metric Alert Rule Types](#metric-alert-rule-types) for valid configurations.

        * `0` - event.type:error
        * `1` - event.type:transaction
        * `2` - None
            eventTypes (array): List of event types that this alert will be related to. Valid values are `default` (events captured using [Capture Message](/product/sentry-basics/integrate-backend/capturing-errors/#capture-message)), `error` and `transaction`.
            comparisonDelta (integer): An optional int representing the time delta to use as the comparison period, in minutes. Required when using a percentage change threshold ("x%" higher or lower compared to `comparisonDelta` minutes ago). A percentage change threshold cannot be used for [Crash Free Session Rate](#crash-free-session-rate) or [Crash Free User Rate](#crash-free-user-rate).
            resolveThreshold (number): Optional value that the metric needs to reach to resolve the alert. If no value is provided, this is set automatically based on the lowest severity trigger's `alertThreshold`. For example, if the alert is set to trigger at the warning level when the number of errors is above 50, then the alert would be set to resolve when there are less than 50 errors. If `thresholdType` is `0`, `resolveThreshold` must be greater than the critical threshold, otherwise, it must be less than the critical threshold.
            owner (string): The ID of the team or user that owns the rule.
            monitorType (integer): Monitor type represents whether the alert rule is actively being monitored or is monitored given a specific activation condition.
            activationCondition (integer): Optional int that represents a trigger condition for when to start monitoring

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Alerts
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        request_body = {
            "name": name,
            "aggregate": aggregate,
            "timeWindow": timeWindow,
            "projects": projects,
            "query": query,
            "thresholdType": thresholdType,
            "triggers": triggers,
            "environment": environment,
            "dataset": dataset,
            "queryType": queryType,
            "eventTypes": eventTypes,
            "comparisonDelta": comparisonDelta,
            "resolveThreshold": resolveThreshold,
            "owner": owner,
            "monitorType": monitorType,
            "activationCondition": activationCondition,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/alert-rules/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_organization_metric_alert_rule(
        self, organization_id_or_slug, alert_rule_id
    ) -> dict[str, Any]:
        """
        Retrieves an alert rule by its ID within a specified organization using the organization's ID or slug.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            alert_rule_id (string): alert_rule_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Alerts
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if alert_rule_id is None:
            raise ValueError("Missing required parameter 'alert_rule_id'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/alert-rules/{alert_rule_id}/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_a_metric_alert_rule(
        self,
        organization_id_or_slug,
        alert_rule_id,
        name,
        aggregate,
        timeWindow,
        projects,
        query,
        thresholdType,
        triggers,
        environment=None,
        dataset=None,
        queryType=None,
        eventTypes=None,
        comparisonDelta=None,
        resolveThreshold=None,
        owner=None,
        monitorType=None,
        activationCondition=None,
    ) -> dict[str, Any]:
        """
        Updates an alert rule for a specified organization using the provided JSON payload, requiring authentication with the necessary permissions.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            alert_rule_id (string): alert_rule_id
            name (string): The name for the rule.
            aggregate (string): A string representing the aggregate function used in this alert rule. Valid aggregate functions are `count`, `count_unique`, `percentage`, `avg`, `apdex`, `failure_rate`, `p50`, `p75`, `p95`, `p99`, `p100`, and `percentile`. See **Metric Alert Rule Types** under [Create a Metric Alert Rule](/api/alerts/create-a-metric-alert-rule-for-an-organization/#metric-alert-rule-types) for valid configurations.
            timeWindow (integer): The time period to aggregate over.

        * `1` - 1 minute
        * `5` - 5 minutes
        * `10` - 10 minutes
        * `15` - 15 minutes
        * `30` - 30 minutes
        * `60` - 1 hour
        * `120` - 2 hours
        * `240` - 4 hours
        * `1440` - 24 hours
            projects (array): The names of the projects to filter by.
            query (string): An event search query to subscribe to and monitor for alerts. For example, to filter transactions so that only those with status code 400 are included, you could use `"query": "http.status_code:400"`. Use an empty string for no filter.
            thresholdType (integer): The comparison operator for the critical and warning thresholds. The comparison operator for the resolved threshold is automatically set to the opposite operator. When a percentage change threshold is used, `0` is equivalent to "Higher than" and `1` is equivalent to "Lower than".

        * `0` - Above
        * `1` - Below
            triggers (array):
        A list of triggers, where each trigger is an object with the following fields:
        - `label`: One of `critical` or `warning`. A `critical` trigger is always required.
        - `alertThreshold`: The value that the subscription needs to reach to trigger the
        alert rule.
        - `actions`: A list of actions that take place when the threshold is met.
        ```json
        triggers: [
            {
                "label": "critical",
                "alertThreshold": 100,
                "actions": [
                    {
                        "type": "email",
                        "targetType": "user",
                        "targetIdentifier": "23489853",
                        "inputChannelId": None
                        "integrationId": None,
                        "sentryAppId": None
                    }
                ]
            },
            {
                "label": "warning",
                "alertThreshold": 75,
                "actions": []
            }
        ]
        ```
        Metric alert rule trigger actions follow the following structure:
        - `type`: The type of trigger action. Valid values are `email`, `slack`, `msteams`, `pagerduty`, `sentry_app`, `sentry_notification`, and `opsgenie`.
        - `targetType`: The type of target the notification will be sent to. Valid values are `specific`, `user`, `team`, and `sentry_app`.
        - `targetIdentifier`: The ID of the target. This must be an integer for PagerDuty and Sentry apps, and a string for all others. Examples of appropriate values include a Slack channel name (`#my-channel`), a user ID, a team ID, a Sentry app ID, etc.
        - `inputChannelId`: The ID of the Slack channel. This is only used for the Slack action, and can be used as an alternative to providing the `targetIdentifier`.
        - `integrationId`: The integration ID. This is required for every action type except `email` and `sentry_app.`
        - `sentryAppId`: The ID of the Sentry app. This is required when `type` is `sentry_app`.
        - `priority`: The severity of the Pagerduty alert or the priority of the Opsgenie alert (optional). Defaults for Pagerduty are `critical` for critical and `warning` for warning. Defaults for Opsgenie are `P1` for critical and `P2` for warning.

            environment (string): The name of the environment to filter by. Defaults to all environments.
            dataset (string): The name of the dataset that this query will be executed on. Valid values are `events`, `transactions`, `metrics`, `sessions`, and `generic-metrics`. Defaults to `events`. See **Metric Alert Rule Types** under [Create a Metric Alert Rule](/api/alerts/create-a-metric-alert-rule-for-an-organization/#metric-alert-rule-types) for valid configurations.
            queryType (integer): The type of query. If no value is provided, `queryType` is set to the default for the specified `dataset.` See **Metric Alert Rule Types** under [Create a Metric Alert Rule](/api/alerts/create-a-metric-alert-rule-for-an-organization/#metric-alert-rule-types) for valid configurations.

        * `0` - event.type:error
        * `1` - event.type:transaction
        * `2` - None
            eventTypes (array): List of event types that this alert will be related to. Valid values are `default` (events captured using [Capture Message](/product/sentry-basics/integrate-backend/capturing-errors/#capture-message)), `error` and `transaction`.
            comparisonDelta (integer): An optional int representing the time delta to use as the comparison period, in minutes. Required when using a percentage change threshold ("x%" higher or lower compared to `comparisonDelta` minutes ago). A percentage change threshold cannot be used for [Crash Free Session Rate](/api/alerts/create-a-metric-alert-rule-for-an-organization/#crash-free-session-rate) or [Crash Free User Rate](/api/alerts/create-a-metric-alert-rule-for-an-organization/#crash-free-user-rate).
            resolveThreshold (number): Optional value that the metric needs to reach to resolve the alert. If no value is provided, this is set automatically based on the lowest severity trigger's `alertThreshold`. For example, if the alert is set to trigger at the warning level when the number of errors is above 50, then the alert would be set to resolve when there are less than 50 errors. If `thresholdType` is `0`, `resolveThreshold` must be greater than the critical threshold. Otherwise, it must be less than the critical threshold.
            owner (string): The ID of the team or user that owns the rule.
            monitorType (integer): Monitor type represents whether the alert rule is actively being monitored or is monitored given a specific activation condition.
            activationCondition (integer): Optional int that represents a trigger condition for when to start monitoring

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Alerts
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if alert_rule_id is None:
            raise ValueError("Missing required parameter 'alert_rule_id'")
        request_body = {
            "name": name,
            "aggregate": aggregate,
            "timeWindow": timeWindow,
            "projects": projects,
            "query": query,
            "thresholdType": thresholdType,
            "triggers": triggers,
            "environment": environment,
            "dataset": dataset,
            "queryType": queryType,
            "eventTypes": eventTypes,
            "comparisonDelta": comparisonDelta,
            "resolveThreshold": resolveThreshold,
            "owner": owner,
            "monitorType": monitorType,
            "activationCondition": activationCondition,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/alert-rules/{alert_rule_id}/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_a_metric_alert_rule(self, organization_id_or_slug, alert_rule_id) -> Any:
        """
        Deletes the specified alert rule for the given organization using the alert rule identifier, returning a 202 Accepted status if the deletion is initiated.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            alert_rule_id (string): alert_rule_id

        Returns:
            Any: Accepted

        Tags:
            Alerts
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if alert_rule_id is None:
            raise ValueError("Missing required parameter 'alert_rule_id'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/alert-rules/{alert_rule_id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_metric_alert_rule_activations(
        self, organization_id_or_slug, alert_rule_id
    ) -> list[Any]:
        """
        Retrieves a list of activations for a specific alert rule within an organization.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            alert_rule_id (string): alert_rule_id

        Returns:
            list[Any]: API response data.

        Tags:
            Alerts
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if alert_rule_id is None:
            raise ValueError("Missing required parameter 'alert_rule_id'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/alert-rules/{alert_rule_id}/activations/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_integration_provider_information(
        self, organization_id_or_slug, providerKey=None
    ) -> dict[str, Any]:
        """
        Retrieves the list of configured integrations for a specified organization, optionally filtered by provider key, and returns integration details if found.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            providerKey (string): Specifies the unique key identifying the provider of the integration to be retrieved.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Integrations
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/config/integrations/"
        query_params = {
            k: v for k, v in [("providerKey", providerKey)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_an_organization_s_custom_dashboards(
        self, organization_id_or_slug, per_page=None, cursor=None
    ) -> list[Any]:
        """
        Retrieves a list of dashboards for a specified organization using pagination parameters.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            per_page (integer): Specifies the number of items to return per page in the response.
            cursor (string): A unique identifier used for cursor-based pagination, allowing retrieval of the next or previous page of results by specifying the position in the dataset.

        Returns:
            list[Any]: API response data.

        Tags:
            Dashboards
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        url = (
            f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/dashboards/"
        )
        query_params = {
            k: v
            for k, v in [("per_page", per_page), ("cursor", cursor)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_a_new_dashboard_for_an_organization(
        self,
        organization_id_or_slug,
        title,
        id=None,
        widgets=None,
        projects=None,
        environment=None,
        period=None,
        start=None,
        end=None,
        filters=None,
        utc=None,
        permissions=None,
    ) -> dict[str, Any]:
        """
        Creates a new dashboard for the specified organization using provided JSON data, requiring appropriate organization-level authentication.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            title (string): The user defined title for this dashboard.
            id (string): A dashboard's unique id.
            widgets (array): A json list of widgets saved in this dashboard.
            projects (array): The saved projects filter for this dashboard.
            environment (array): The saved environment filter for this dashboard.
            period (string): The saved time range period for this dashboard.
            start (string): The saved start time for this dashboard.
            end (string): The saved end time for this dashboard.
            filters (object): The saved filters for this dashboard.
            utc (boolean): Setting that lets you display saved time range for this dashboard in UTC.
            permissions (string): Permissions that restrict users from editing dashboards

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Dashboards
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        request_body = {
            "title": title,
            "id": id,
            "widgets": widgets,
            "projects": projects,
            "environment": environment,
            "period": period,
            "start": start,
            "end": end,
            "filters": filters,
            "utc": utc,
            "permissions": permissions,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = (
            f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/dashboards/"
        )
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_an_organization_s_custom_dashboard(
        self, organization_id_or_slug, dashboard_id
    ) -> dict[str, Any]:
        """
        Retrieves details of a specific dashboard within an organization using its ID or slug and the dashboard ID.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            dashboard_id (string): dashboard_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Dashboards
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if dashboard_id is None:
            raise ValueError("Missing required parameter 'dashboard_id'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/dashboards/{dashboard_id}/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def edit_an_organization_s_custom_dashboard(
        self,
        organization_id_or_slug,
        dashboard_id,
        id=None,
        title=None,
        widgets=None,
        projects=None,
        environment=None,
        period=None,
        start=None,
        end=None,
        filters=None,
        utc=None,
        permissions=None,
    ) -> dict[str, Any]:
        """
        Updates the specified dashboard within an organization by replacing it with the provided data using the PUT method.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            dashboard_id (string): dashboard_id
            id (string): A dashboard's unique id.
            title (string): The user-defined dashboard title.
            widgets (array): A json list of widgets saved in this dashboard.
            projects (array): The saved projects filter for this dashboard.
            environment (array): The saved environment filter for this dashboard.
            period (string): The saved time range period for this dashboard.
            start (string): The saved start time for this dashboard.
            end (string): The saved end time for this dashboard.
            filters (object): The saved filters for this dashboard.
            utc (boolean): Setting that lets you display saved time range for this dashboard in UTC.
            permissions (string): Permissions that restrict users from editing dashboards

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Dashboards
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if dashboard_id is None:
            raise ValueError("Missing required parameter 'dashboard_id'")
        request_body = {
            "id": id,
            "title": title,
            "widgets": widgets,
            "projects": projects,
            "environment": environment,
            "period": period,
            "start": start,
            "end": end,
            "filters": filters,
            "utc": utc,
            "permissions": permissions,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/dashboards/{dashboard_id}/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_an_organization_s_custom_dashboard(
        self, organization_id_or_slug, dashboard_id
    ) -> Any:
        """
        Deletes a specific dashboard in an organization using the provided organization ID or slug and dashboard ID, requiring authentication with admin or write permissions.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            dashboard_id (string): dashboard_id

        Returns:
            Any: No Content

        Tags:
            Dashboards
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if dashboard_id is None:
            raise ValueError("Missing required parameter 'dashboard_id'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/dashboards/{dashboard_id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_an_organization_s_discover_saved_queries(
        self,
        organization_id_or_slug,
        per_page=None,
        cursor=None,
        query=None,
        sortBy=None,
    ) -> list[Any]:
        """
        Retrieves a list of saved discoveries for an organization, allowing filtering by query, sorting, and pagination.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            per_page (integer): The number of results to return per page in the paginated response.
            cursor (string): A token that marks the position in the dataset and is used to fetch the next or previous page of results when paginating through a large set of items.
            query (string): Search for saved discoveries by specifying a query string to filter results.
            sortBy (string): Specifies the field to sort the results by, allowing for customizable ordering of saved items.

        Returns:
            list[Any]: API response data.

        Tags:
            Discover
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/discover/saved/"
        query_params = {
            k: v
            for k, v in [
                ("per_page", per_page),
                ("cursor", cursor),
                ("query", query),
                ("sortBy", sortBy),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_a_new_saved_query(
        self,
        organization_id_or_slug,
        name,
        projects=None,
        queryDataset=None,
        start=None,
        end=None,
        range=None,
        fields=None,
        orderby=None,
        environment=None,
        query=None,
        yAxis=None,
        display=None,
        topEvents=None,
        interval=None,
    ) -> dict[str, Any]:
        """
        Saves a discovery configuration for a specified organization using the provided JSON data and returns a success status upon completion.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            name (string): The user-defined saved query name.
            projects (array): The saved projects filter for this query.
            queryDataset (string): The dataset you would like to query. Allowed values are:
        - error-events
        - transaction-like


        * `discover`
        * `error-events`
        * `transaction-like`
            start (string): The saved start time for this saved query.
            end (string): The saved end time for this saved query.
            range (string): The saved time range period for this saved query.
            fields (array): The fields, functions, or equations that can be requested for the query. At most 20 fields can be selected per request. Each field can be one of the following types:
        - A built-in key field. See possible fields in the [properties table](/product/sentry-basics/search/searchable-properties/#properties-table), under any field that is an event property.
            - example: `field=transaction`
        - A tag. Tags should use the `tag[]` formatting to avoid ambiguity with any fields
            - example: `field=tag[isEnterprise]`
        - A function which will be in the format of `function_name(parameters,...)`. See possible functions in the [query builder documentation](/product/discover-queries/query-builder/#stacking-functions).
            - when a function is included, Discover will group by any tags or fields
            - example: `field=count_if(transaction.duration,greater,300)`
        - An equation when prefixed with `equation|`. Read more about [equations here](/product/discover-queries/query-builder/query-equations/).
            - example: `field=equation|count_if(transaction.duration,greater,300) / count() * 100`

            orderby (string): How to order the query results. Must be something in the `field` list, excluding equations.
            environment (array): The name of environments to filter by.
            query (string): Filters results by using [query syntax](/product/sentry-basics/search/).
            yAxis (array): Aggregate functions to be plotted on the chart.
            display (string): Visualization type for saved query chart. Allowed values are:
        - default
        - previous
        - top5
        - daily
        - dailytop5
        - bar

            topEvents (integer): Number of top events' timeseries to be visualized.
            interval (string): Resolution of the time series.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Discover
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        request_body = {
            "name": name,
            "projects": projects,
            "queryDataset": queryDataset,
            "start": start,
            "end": end,
            "range": range,
            "fields": fields,
            "orderby": orderby,
            "environment": environment,
            "query": query,
            "yAxis": yAxis,
            "display": display,
            "topEvents": topEvents,
            "interval": interval,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/discover/saved/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_an_organization_s_discover_saved_query(
        self, organization_id_or_slug, query_id
    ) -> dict[str, Any]:
        """
        Retrieves saved discovery data for a specified query within an organization using the provided organization ID or slug and query ID.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            query_id (string): query_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Discover
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if query_id is None:
            raise ValueError("Missing required parameter 'query_id'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/discover/saved/{query_id}/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def edit_organization_discover_saved_query(
        self,
        organization_id_or_slug,
        query_id,
        name,
        projects=None,
        queryDataset=None,
        start=None,
        end=None,
        range=None,
        fields=None,
        orderby=None,
        environment=None,
        query=None,
        yAxis=None,
        display=None,
        topEvents=None,
        interval=None,
    ) -> dict[str, Any]:
        """
        Updates or replaces a saved Discover query for the specified organization using the provided query details.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            query_id (string): query_id
            name (string): The user-defined saved query name.
            projects (array): The saved projects filter for this query.
            queryDataset (string): The dataset you would like to query. Allowed values are:
        - error-events
        - transaction-like


        * `discover`
        * `error-events`
        * `transaction-like`
            start (string): The saved start time for this saved query.
            end (string): The saved end time for this saved query.
            range (string): The saved time range period for this saved query.
            fields (array): The fields, functions, or equations that can be requested for the query. At most 20 fields can be selected per request. Each field can be one of the following types:
        - A built-in key field. See possible fields in the [properties table](/product/sentry-basics/search/searchable-properties/#properties-table), under any field that is an event property.
            - example: `field=transaction`
        - A tag. Tags should use the `tag[]` formatting to avoid ambiguity with any fields
            - example: `field=tag[isEnterprise]`
        - A function which will be in the format of `function_name(parameters,...)`. See possible functions in the [query builder documentation](/product/discover-queries/query-builder/#stacking-functions).
            - when a function is included, Discover will group by any tags or fields
            - example: `field=count_if(transaction.duration,greater,300)`
        - An equation when prefixed with `equation|`. Read more about [equations here](/product/discover-queries/query-builder/query-equations/).
            - example: `field=equation|count_if(transaction.duration,greater,300) / count() * 100`

            orderby (string): How to order the query results. Must be something in the `field` list, excluding equations.
            environment (array): The name of environments to filter by.
            query (string): Filters results by using [query syntax](/product/sentry-basics/search/).
            yAxis (array): Aggregate functions to be plotted on the chart.
            display (string): Visualization type for saved query chart. Allowed values are:
        - default
        - previous
        - top5
        - daily
        - dailytop5
        - bar

            topEvents (integer): Number of top events' timeseries to be visualized.
            interval (string): Resolution of the time series.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Discover
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if query_id is None:
            raise ValueError("Missing required parameter 'query_id'")
        request_body = {
            "name": name,
            "projects": projects,
            "queryDataset": queryDataset,
            "start": start,
            "end": end,
            "range": range,
            "fields": fields,
            "orderby": orderby,
            "environment": environment,
            "query": query,
            "yAxis": yAxis,
            "display": display,
            "topEvents": topEvents,
            "interval": interval,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/discover/saved/{query_id}/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_organization_discover_saved_query(
        self, organization_id_or_slug, query_id
    ) -> Any:
        """
        Deletes a saved query for a specified organization and query ID, returning a 204 (No Content) on success.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            query_id (string): query_id

        Returns:
            Any: No Content

        Tags:
            Discover
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if query_id is None:
            raise ValueError("Missing required parameter 'query_id'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/discover/saved/{query_id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_an_organization_s_environments(
        self, organization_id_or_slug, visibility=None
    ) -> list[Any]:
        """
        Lists all environments for a specified organization, optionally filtered by visibility, when authenticated with sufficient permissions.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            visibility (string): Filter environments by visibility, where options include "all," "hidden," or "visible."

        Returns:
            list[Any]: API response data.

        Tags:
            Environments
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/environments/"
        query_params = {k: v for k, v in [("visibility", visibility)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def query_discover_events_in_table_format(
        self,
        organization_id_or_slug,
        field,
        end=None,
        environment=None,
        project=None,
        start=None,
        statsPeriod=None,
        per_page=None,
        query=None,
        sort=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of events for a specified organization, allowing filtering and sorting by various query parameters such as fields, environment, project, time range, and pagination.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            field (array): **field** (array, required): Specifies the fields to include in the event response.
            end (string): The "end" parameter specifies the ending date or time for filtering events in the response string format.
            environment (array): A list of environment names or identifiers to filter events for the specified organization.
            project (array): Optional array parameter to filter events by specific project IDs.
            start (string): The "start" parameter is a query string parameter of type string, used to specify the starting point for retrieving events in the GET operation at "/api/0/organizations/{organization_id_or_slug}/events/".
            statsPeriod (string): An optional string parameter specifying the time period for which statistics are calculated, with possible values of "24h" and "14d", defaulting to "24h" if not provided.
            per_page (integer): Optional integer parameter to specify the number of items to return per page in the response.
            query (string): Specifies a search query to filter events by keyword, allowing users to find specific events within an organization.
            sort (string): Sorts events by the specified field; valid values include field names like "date" or "name", and optionally "asc" or "desc" for ascending or descending order.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Discover
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/events/"
        query_params = {
            k: v
            for k, v in [
                ("field", field),
                ("end", end),
                ("environment", environment),
                ("project", project),
                ("start", start),
                ("statsPeriod", statsPeriod),
                ("per_page", per_page),
                ("query", query),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_an_external_user(
        self,
        organization_id_or_slug,
        user_id,
        external_name,
        provider,
        integration_id,
        id,
        external_id=None,
    ) -> dict[str, Any]:
        """
        Links a user from an external provider to a Sentry user within the specified organization and returns the external user resource.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            user_id (integer): The user ID in Sentry.
            external_name (string): The associated name for the provider.
            provider (string): The provider of the external actor.

        * `github`
        * `github_enterprise`
        * `slack`
        * `gitlab`
        * `msteams`
        * `custom_scm`
            integration_id (integer): The Integration ID.
            id (integer): The external actor ID.
            external_id (string): The associated user ID for provider.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Integrations
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        request_body = {
            "user_id": user_id,
            "external_name": external_name,
            "provider": provider,
            "integration_id": integration_id,
            "id": id,
            "external_id": external_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/external-users/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_an_external_user(
        self,
        organization_id_or_slug,
        external_user_id,
        user_id,
        external_name,
        provider,
        integration_id,
        id,
        external_id=None,
    ) -> dict[str, Any]:
        """
        Updates the details of a specified external user within an organization using the provided request body.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            external_user_id (string): external_user_id
            user_id (integer): The user ID in Sentry.
            external_name (string): The associated name for the provider.
            provider (string): The provider of the external actor.

        * `github`
        * `github_enterprise`
        * `slack`
        * `gitlab`
        * `msteams`
        * `custom_scm`
            integration_id (integer): The Integration ID.
            id (integer): The external actor ID.
            external_id (string): The associated user ID for provider.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Integrations
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if external_user_id is None:
            raise ValueError("Missing required parameter 'external_user_id'")
        request_body = {
            "user_id": user_id,
            "external_name": external_name,
            "provider": provider,
            "integration_id": integration_id,
            "id": id,
            "external_id": external_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/external-users/{external_user_id}/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_an_external_user(self, organization_id_or_slug, external_user_id) -> Any:
        """
        Removes an external user from an organization using the organization ID or slug and the external user ID.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            external_user_id (string): external_user_id

        Returns:
            Any: No Content

        Tags:
            Integrations
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if external_user_id is None:
            raise ValueError("Missing required parameter 'external_user_id'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/external-users/{external_user_id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_organization_available_integrations(
        self,
        organization_id_or_slug,
        providerKey=None,
        features=None,
        includeConfig=None,
    ) -> list[Any]:
        """
        Retrieves a list of integrations for a specified organization using the provided organization ID or slug, allowing optional filtering by provider key, features, and configuration inclusion.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            providerKey (string): The providerKey query parameter specifies the unique identifier of the integration provider to filter the list of integrations for the given organization.
            features (array): A list of features to filter or include in the response for the organization's integrations.
            includeConfig (boolean): Indicates whether to include configuration details in the response; valid values are true or false.

        Returns:
            list[Any]: API response data.

        Tags:
            Integrations
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/integrations/"
        query_params = {
            k: v
            for k, v in [
                ("providerKey", providerKey),
                ("features", features),
                ("includeConfig", includeConfig),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_organization_integration(
        self, organization_id_or_slug, integration_id
    ) -> dict[str, Any]:
        """
        Retrieves details for a specific integration within an organization using its ID or slug.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            integration_id (string): integration_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Integrations
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if integration_id is None:
            raise ValueError("Missing required parameter 'integration_id'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/integrations/{integration_id}/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_organization_integration(
        self, organization_id_or_slug, integration_id
    ) -> Any:
        """
        Deletes an integration from an organization using the provided organization ID or slug and integration ID, returning a 204 status code upon successful deletion.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            integration_id (string): integration_id

        Returns:
            Any: No Content

        Tags:
            Integrations
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if integration_id is None:
            raise ValueError("Missing required parameter 'integration_id'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/integrations/{integration_id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_an_organization_s_members(self, organization_id_or_slug) -> list[Any]:
        """
        Retrieves a list of members belonging to a specified organization, with access controlled by member-specific permissions.

        Args:
            organization_id_or_slug (string): organization_id_or_slug

        Returns:
            list[Any]: API response data.

        Tags:
            Organizations
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/members/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_a_member_to_an_organization(
        self,
        organization_id_or_slug,
        email,
        orgRole=None,
        teamRoles=None,
        sendInvite=None,
        reinvite=None,
    ) -> dict[str, Any]:
        """
        Invites a new member to the specified organization by creating their membership with the provided details.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            email (string): The email address to send the invitation to.
            orgRole (string): The organization-level role of the new member. Roles include:

        * `billing` - Can manage payment and compliance details.
        * `member` - Can view and act on events, as well as view most other data within the organization.
        * `manager` - Has full management access to all teams and projects. Can also manage
                the organization's membership.
        * `owner` - Has unrestricted access to the organization, its data, and its
                settings. Can add, modify, and delete projects and members, as well as
                make billing and plan changes.
        * `admin` - Can edit global integrations, manage projects, and add/remove teams.
                They automatically assume the Team Admin role for teams they join.
                Note: This role can no longer be assigned in Business and Enterprise plans. Use `TeamRoles` instead.

            teamRoles (array): The team and team-roles assigned to the member. Team roles can be either:
                - `contributor` - Can view and act on issues. Depending on organization settings, they can also add team members.
                - `admin` - Has full management access to their team's membership and projects.
            sendInvite (boolean): Whether or not to send an invite notification through email. Defaults to True.
            reinvite (boolean): Whether or not to re-invite a user who has already been invited to the organization. Defaults to True.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Organizations
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        request_body = {
            "email": email,
            "orgRole": orgRole,
            "teamRoles": teamRoles,
            "sendInvite": sendInvite,
            "reinvite": reinvite,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/members/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_an_organization_member(
        self, organization_id_or_slug, member_id
    ) -> dict[str, Any]:
        """
        Retrieves information about a specific member in an organization using the provided organization ID or slug and member ID.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            member_id (string): member_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Organizations
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if member_id is None:
            raise ValueError("Missing required parameter 'member_id'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/members/{member_id}/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_an_organization_member_s_roles(
        self, organization_id_or_slug, member_id, orgRole=None, teamRoles=None
    ) -> dict[str, Any]:
        """
        Updates a member's details in an organization using the PUT method, requiring the organization ID or slug and member ID in the path, and supports JSON content in the request body.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            member_id (string): member_id
            orgRole (string): The organization role of the member. The options are:

        * `billing` - Can manage payment and compliance details.
        * `member` - Can view and act on events, as well as view most other data within the organization.
        * `manager` - Has full management access to all teams and projects. Can also manage
                the organization's membership.
        * `owner` - Has unrestricted access to the organization, its data, and its
                settings. Can add, modify, and delete projects and members, as well as
                make billing and plan changes.
        * `admin` - Can edit global integrations, manage projects, and add/remove teams.
                They automatically assume the Team Admin role for teams they join.
                Note: This role can no longer be assigned in Business and Enterprise plans. Use `TeamRoles` instead.

            teamRoles (array):
        Configures the team role of the member. The two roles are:
        - `contributor` - Can view and act on issues. Depending on organization settings, they can also add team members.
        - `admin` - Has full management access to their team's membership and projects.
        ```json
        {
            "teamRoles": [
                {
                    "teamSlug": "ancient-gabelers",
                    "role": "admin"
                },
                {
                    "teamSlug": "powerful-abolitionist",
                    "role": "contributor"
                }
            ]
        }
        ```


        Returns:
            dict[str, Any]: API response data.

        Tags:
            Organizations
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if member_id is None:
            raise ValueError("Missing required parameter 'member_id'")
        request_body = {
            "orgRole": orgRole,
            "teamRoles": teamRoles,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/members/{member_id}/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_an_organization_member(self, organization_id_or_slug, member_id) -> Any:
        """
        Deletes a member from an organization using the provided organization ID or slug and member ID.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            member_id (string): member_id

        Returns:
            Any: No Content

        Tags:
            Organizations
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if member_id is None:
            raise ValueError("Missing required parameter 'member_id'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/members/{member_id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_an_organization_member_to_a_team(
        self, organization_id_or_slug, member_id, team_id_or_slug
    ) -> dict[str, Any]:
        """
        Adds a member to a specified team within an organization.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            member_id (string): member_id
            team_id_or_slug (string): team_id_or_slug

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Teams
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if member_id is None:
            raise ValueError("Missing required parameter 'member_id'")
        if team_id_or_slug is None:
            raise ValueError("Missing required parameter 'team_id_or_slug'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/members/{member_id}/teams/{team_id_or_slug}/"
        query_params = {}
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_an_organization_member_s_team_role(
        self, organization_id_or_slug, member_id, team_id_or_slug, teamRole=None
    ) -> dict[str, Any]:
        """
        Updates a team membership for a specific member in an organization using the provided team ID or slug.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            member_id (string): member_id
            team_id_or_slug (string): team_id_or_slug
            teamRole (string): The team-level role to switch to. Valid roles include:

        * `contributor` - Contributors can view and act on events, as well as view most other data within the team's projects.
        * `admin` - Admin privileges on the team. They can create and remove projects, and can manage the team's memberships.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Teams
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if member_id is None:
            raise ValueError("Missing required parameter 'member_id'")
        if team_id_or_slug is None:
            raise ValueError("Missing required parameter 'team_id_or_slug'")
        request_body = {
            "teamRole": teamRole,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/members/{member_id}/teams/{team_id_or_slug}/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_an_organization_member_from_a_team(
        self, organization_id_or_slug, member_id, team_id_or_slug
    ) -> dict[str, Any]:
        """
        Removes a member from a specific team in an organization using the provided organization ID or slug, member ID, and team ID or slug.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            member_id (string): member_id
            team_id_or_slug (string): team_id_or_slug

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Teams
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if member_id is None:
            raise ValueError("Missing required parameter 'member_id'")
        if team_id_or_slug is None:
            raise ValueError("Missing required parameter 'team_id_or_slug'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/members/{member_id}/teams/{team_id_or_slug}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_monitors_for_an_organization(
        self, organization_id_or_slug, project=None, environment=None, owner=None
    ) -> list[Any]:
        """
        Retrieves a list of monitors for an organization using the provided organization ID or slug, with optional filtering by project, environment, and owner.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project (array): Filters the monitors by a list of project IDs or names to retrieve only those associated with the specified projects.
            environment (array): An array of environment identifiers to filter the monitors by environment.
            owner (string): Filters monitors to only those owned by the specified user.

        Returns:
            list[Any]: API response data.

        Tags:
            Crons
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/monitors/"
        query_params = {
            k: v
            for k, v in [
                ("project", project),
                ("environment", environment),
                ("owner", owner),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_a_monitor(
        self,
        organization_id_or_slug,
        name,
        type,
        slug=None,
        status=None,
        owner=None,
        is_muted=None,
    ) -> dict[str, Any]:
        """
        Creates a new monitor for an organization using the provided JSON body and returns a status message, requiring authentication with permissions to read or write within the organization.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            name (string): Name of the monitor. Used for notifications.
            type (string): * `cron_job`
            slug (string): Uniquely identifies your monitor within your organization. Changing this slug will require updates to any instrumented check-in calls.
            status (string): Status of the monitor. Disabled monitors will not accept events and will not count towards the monitor quota.

        * `active`
        * `disabled`
            owner (string): The ID of the team or user that owns the monitor. (eg. user:51 or team:6)
            is_muted (boolean): Disable creation of monitor incidents

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Crons
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        request_body = {
            "name": name,
            "type": type,
            "slug": slug,
            "status": status,
            "owner": owner,
            "is_muted": is_muted,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/monitors/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_a_monitor(
        self, organization_id_or_slug, monitor_id_or_slug, environment=None
    ) -> dict[str, Any]:
        """
        Retrieves details about a specific monitor in an organization based on the provided organization ID or slug and monitor ID or slug, optionally filtered by environment.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            monitor_id_or_slug (string): monitor_id_or_slug
            environment (array): List of environments to filter the monitors by, specified as an array of environment names or identifiers.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Crons
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if monitor_id_or_slug is None:
            raise ValueError("Missing required parameter 'monitor_id_or_slug'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/monitors/{monitor_id_or_slug}/"
        query_params = {
            k: v for k, v in [("environment", environment)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_a_monitor(
        self,
        organization_id_or_slug,
        monitor_id_or_slug,
        name,
        type,
        slug=None,
        status=None,
        owner=None,
        is_muted=None,
    ) -> dict[str, Any]:
        """
        Updates the specified monitor within the given organization by replacing its configuration using the provided JSON data.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            monitor_id_or_slug (string): monitor_id_or_slug
            name (string): Name of the monitor. Used for notifications.
            type (string): * `cron_job`
            slug (string): Uniquely identifies your monitor within your organization. Changing this slug will require updates to any instrumented check-in calls.
            status (string): Status of the monitor. Disabled monitors will not accept events and will not count towards the monitor quota.

        * `active`
        * `disabled`
            owner (string): The ID of the team or user that owns the monitor. (eg. user:51 or team:6)
            is_muted (boolean): Disable creation of monitor incidents

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Crons
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if monitor_id_or_slug is None:
            raise ValueError("Missing required parameter 'monitor_id_or_slug'")
        request_body = {
            "name": name,
            "type": type,
            "slug": slug,
            "status": status,
            "owner": owner,
            "is_muted": is_muted,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/monitors/{monitor_id_or_slug}/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_a_monitor_or_monitor_environments(
        self, organization_id_or_slug, monitor_id_or_slug, environment=None
    ) -> Any:
        """
        Deletes a monitor from a specified organization in an API, identified by organization ID or slug and monitor ID or slug, with optional environment parameters.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            monitor_id_or_slug (string): monitor_id_or_slug
            environment (array): A query parameter used to specify one or more environments for filtering during the deletion of monitors.

        Returns:
            Any: Accepted

        Tags:
            Crons
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if monitor_id_or_slug is None:
            raise ValueError("Missing required parameter 'monitor_id_or_slug'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/monitors/{monitor_id_or_slug}/"
        query_params = {
            k: v for k, v in [("environment", environment)] if v is not None
        }
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_check_ins_for_a_monitor(
        self, organization_id_or_slug, monitor_id_or_slug
    ) -> list[Any]:
        """
        Retrieves check-ins for a specific monitor within an organization using the provided organization ID or slug and monitor ID or slug.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            monitor_id_or_slug (string): monitor_id_or_slug

        Returns:
            list[Any]: API response data.

        Tags:
            Crons
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if monitor_id_or_slug is None:
            raise ValueError("Missing required parameter 'monitor_id_or_slug'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/monitors/{monitor_id_or_slug}/checkins/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_spike_protection_notifications(
        self,
        organization_id_or_slug,
        project=None,
        project_id_or_slug=None,
        triggerType=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of notification actions available for the specified organization, optionally filtered by project or trigger type.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project (array): Filters for notifications related to the specified project IDs.
            project_id_or_slug (array): Specifies one or more project identifiers (ID or slug) to filter notification actions for within the organization.
            triggerType (string): The "triggerType" parameter specifies the type of trigger to filter notification actions by, provided as a string query parameter.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Alerts
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/notifications/actions/"
        query_params = {
            k: v
            for k, v in [
                ("project", project),
                ("project_id_or_slug", project_id_or_slug),
                ("triggerType", triggerType),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_spike_protection_notification(
        self,
        organization_id_or_slug,
        trigger_type,
        service_type,
        integration_id=None,
        target_identifier=None,
        target_display=None,
        projects=None,
    ) -> dict[str, Any]:
        """
        Performs an action on notifications for a specified organization using the provided JSON body and returns a success status.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            trigger_type (string): Type of the trigger that causes the notification. The only supported trigger right now is: `spike-protection`.
            service_type (string): Service that is used for sending the notification.
        - `email`
        - `slack`
        - `sentry_notification`
        - `pagerduty`
        - `opsgenie`

            integration_id (integer): ID of the integration used as the notification service. See
        [List Integrations](https://docs.sentry.io/api/integrations/list-an-organizations-available-integrations/)
        to retrieve a full list of integrations.

        Required if **service_type** is `slack`, `pagerduty` or `opsgenie`.

            target_identifier (string): ID of the notification target, like a Slack channel ID.

        Required if **service_type** is `slack` or `opsgenie`.

            target_display (string): Name of the notification target, like a Slack channel name.

        Required if **service_type** is `slack` or `opsgenie`.

            projects (array): List of projects slugs that the Notification Action is created for.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Alerts
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        request_body = {
            "trigger_type": trigger_type,
            "service_type": service_type,
            "integration_id": integration_id,
            "target_identifier": target_identifier,
            "target_display": target_display,
            "projects": projects,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/notifications/actions/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_a_spike_protection_notification_action(
        self, organization_id_or_slug, action_id
    ) -> dict[str, Any]:
        """
        Retrieves information about a specific notification action for an organization using the provided organization identifier or slug and action ID.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            action_id (string): action_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Alerts
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if action_id is None:
            raise ValueError("Missing required parameter 'action_id'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/notifications/actions/{action_id}/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_a_spike_protection_notification_action(
        self,
        organization_id_or_slug,
        action_id,
        trigger_type,
        service_type,
        integration_id=None,
        target_identifier=None,
        target_display=None,
        projects=None,
    ) -> dict[str, Any]:
        """
        Updates a notification action for a specific organization using the provided JSON data and returns a success status upon completion.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            action_id (string): action_id
            trigger_type (string): Type of the trigger that causes the notification. The only supported trigger right now is: `spike-protection`.
            service_type (string): Service that is used for sending the notification.
        - `email`
        - `slack`
        - `sentry_notification`
        - `pagerduty`
        - `opsgenie`

            integration_id (integer): ID of the integration used as the notification service. See
        [List Integrations](https://docs.sentry.io/api/integrations/list-an-organizations-available-integrations/)
        to retrieve a full list of integrations.

        Required if **service_type** is `slack`, `pagerduty` or `opsgenie`.

            target_identifier (string): ID of the notification target, like a Slack channel ID.

        Required if **service_type** is `slack` or `opsgenie`.

            target_display (string): Name of the notification target, like a Slack channel name.

        Required if **service_type** is `slack` or `opsgenie`.

            projects (array): List of projects slugs that the Notification Action is created for.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Alerts
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if action_id is None:
            raise ValueError("Missing required parameter 'action_id'")
        request_body = {
            "trigger_type": trigger_type,
            "service_type": service_type,
            "integration_id": integration_id,
            "target_identifier": target_identifier,
            "target_display": target_display,
            "projects": projects,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/notifications/actions/{action_id}/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_a_spike_protection_notification_action(
        self, organization_id_or_slug, action_id
    ) -> Any:
        """
        Deletes a notification action by its ID for a specific organization identified by its ID or slug, using the provided authentication token with appropriate permissions.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            action_id (string): action_id

        Returns:
            Any: No Content

        Tags:
            Alerts
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if action_id is None:
            raise ValueError("Missing required parameter 'action_id'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/notifications/actions/{action_id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_an_organization_s_projects(
        self, organization_id_or_slug, cursor=None
    ) -> list[Any]:
        """
        Retrieves a paginated list of projects within the specified organization identified by its ID or slug.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            cursor (string): A string token used for cursor-based pagination to fetch the next set of projects after the specified position in the results.

        Returns:
            list[Any]: API response data.

        Tags:
            Organizations
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/projects/"
        query_params = {k: v for k, v in [("cursor", cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_an_organization_s_trusted_relays(
        self, organization_id_or_slug
    ) -> list[Any]:
        """
        Retrieves relay usage information for a specified organization using its ID or slug, requiring appropriate authentication tokens for administrative or read access.

        Args:
            organization_id_or_slug (string): organization_id_or_slug

        Returns:
            list[Any]: API response data.

        Tags:
            Organizations
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/relay_usage/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_release_threshold_statuses(
        self,
        organization_id_or_slug,
        start,
        end,
        environment=None,
        projectSlug=None,
        release=None,
    ) -> dict[str, Any]:
        """
        Retrieves the current statuses of release thresholds for a specified organization within a given time range, optionally filtered by environment, project, or release.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            start (string): Offset from which to start returning release threshold statuses, expressed as a string; this parameter is required for the request.
            end (string): The "end" parameter specifies the ending point for retrieving release threshold statuses, required as a string in the query.
            environment (array): An array of environment names to filter the release threshold statuses by specific deployment environments.
            projectSlug (array): An array of project slugs used to filter release threshold status results by specific projects within the organization.
            release (array): A comma-separated list of release versions to filter the returned threshold statuses by.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Releases
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/release-threshold-statuses/"
        query_params = {
            k: v
            for k, v in [
                ("start", start),
                ("end", end),
                ("environment", environment),
                ("projectSlug", projectSlug),
                ("release", release),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_an_organization_s_release(
        self,
        organization_id_or_slug,
        version,
        project_id=None,
        health=None,
        adoptionStages=None,
        summaryStatsPeriod=None,
        healthStatsPeriod=None,
        sort=None,
        status=None,
        query=None,
    ) -> dict[str, Any]:
        """
        Retrieves detailed information about a specific release version within an organization, optionally filtered and sorted by project, health metrics, adoption stages, summary statistics, and status.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            version (string): version
            project_id (string): The project_id query parameter specifies the unique identifier of the project to filter the release information within the given organization and version.
            health (boolean): Indicates whether to perform health checks on the releases, returning a boolean value to filter or include health status in the response.
            adoptionStages (boolean): Indicates whether to include adoption stages in the response, accepting a boolean value.
            summaryStatsPeriod (string): The "summaryStatsPeriod" parameter specifies the time period for summary statistics, accepting values such as 1 hour, 1 day, 2 days, 7 days, 14 days, 24 hours, 48 hours, 30 days, and 90 days.
            healthStatsPeriod (string): The "healthStatsPeriod" parameter specifies the time period for retrieving health statistics, with options including 1 hour, 1 day, 2 days, 7 days, 14 days, 24 hours, 48 hours, 30 days, and 90 days.
            sort (string): Sorts the release results by one of the following fields: crash_free_sessions, crash_free_users, date, sessions, or users.
            status (string): Filter releases by status, either "archived" or "open".
            query (string): Optional query string parameter to filter or specify additional details for the release data.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Releases
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if version is None:
            raise ValueError("Missing required parameter 'version'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/releases/{version}/"
        query_params = {
            k: v
            for k, v in [
                ("project_id", project_id),
                ("health", health),
                ("adoptionStages", adoptionStages),
                ("summaryStatsPeriod", summaryStatsPeriod),
                ("healthStatsPeriod", healthStatsPeriod),
                ("sort", sort),
                ("status", status),
                ("query", query),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_an_organization_s_release(
        self,
        organization_id_or_slug,
        version,
        ref=None,
        url=None,
        dateReleased=None,
        commits=None,
        refs=None,
    ) -> dict[str, Any]:
        """
        Updates a specific release version within an organization using the provided JSON data and returns a status message.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            version (string): version
            ref (string): An optional commit reference. This is useful if a tagged version has been provided.
            url (string): A URL that points to the release. For instance, this can be the path to an online interface to the source code, such as a GitHub URL.
            dateReleased (string): An optional date that indicates when the release went live.  If not provided the current time is used.
            commits (array): An optional list of commit data to be associated.
            refs (array): An optional way to indicate the start and end commits for each repository included in a release. Head commits must include parameters ``repository`` and ``commit`` (the HEAD SHA). They can optionally include ``previousCommit`` (the SHA of the HEAD of the previous release), which should be specified if this is the first time you've sent commit data.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Releases
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if version is None:
            raise ValueError("Missing required parameter 'version'")
        request_body = {
            "ref": ref,
            "url": url,
            "dateReleased": dateReleased,
            "commits": commits,
            "refs": refs,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/releases/{version}/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_an_organization_s_release(self, organization_id_or_slug, version) -> Any:
        """
        Deletes a release version associated with an organization in the API, identified by the organization ID or slug and the version number, and returns a successful deletion status with a 204 response code.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            version (string): version

        Returns:
            Any: No Content

        Tags:
            Releases
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if version is None:
            raise ValueError("Missing required parameter 'version'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/releases/{version}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_a_count_of_replays(
        self,
        organization_id_or_slug,
        environment=None,
        start=None,
        end=None,
        statsPeriod=None,
        project=None,
        query=None,
    ) -> dict[str, Any]:
        """
        Retrieves the replay count for a specified organization, filtered by optional parameters such as environment, time range, project, and custom query.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            environment (array): A list of environments to filter the replay count data for the specified organization.
            start (string): A string parameter used in the query to specify the starting point for filtering or offsetting data in the replay count results.
            end (string): The "end" parameter is a string query parameter used to specify the end date or time for fetching replay counts, allowing users to filter results within a specific time range.
            statsPeriod (string): An optional string parameter specifying the time period over which statistics are aggregated, such as "24h" or "14d", influencing the replay count data returned.
            project (array): An array of project identifiers used to filter the replay count results for specific projects within the specified organization.
            query (string): A string parameter to filter or specify additional criteria for retrieving replay counts within an organization.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Replays
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/replay-count/"
        query_params = {
            k: v
            for k, v in [
                ("environment", environment),
                ("start", start),
                ("end", end),
                ("statsPeriod", statsPeriod),
                ("project", project),
                ("query", query),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_an_organization_s_selectors(
        self,
        organization_id_or_slug,
        environment=None,
        statsPeriod=None,
        start=None,
        end=None,
        project=None,
        sort=None,
        cursor=None,
        per_page=None,
        query=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of replay selectors for an organization using the provided parameters such as environment, stats period, project, and query filters.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            environment (array): Filter the replay selectors by one or more environment names.
            statsPeriod (string): Defines the time period for which statistics are retrieved, with options such as "24h" or "14d".
            start (string): A string parameter specifying the starting point for the replay selectors query.
            end (string): The "end" parameter specifies a string value used to define the end point or interval for replay selectors in the query.
            project (array): Filter replay selectors by project IDs; accepts an array of project IDs to narrow the results.
            sort (string): Specifies the field and direction (ascending or descending) by which to sort the returned replay selectors.
            cursor (string): A string parameter used for cursor-based pagination, indicating the position in the dataset from which to retrieve the next set of results.
            per_page (integer): Number of items to return per page for the replay selectors list.
            query (string): Optional string query parameter to filter or specify replay selectors based on specific criteria.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Replays
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/replay-selectors/"
        query_params = {
            k: v
            for k, v in [
                ("environment", environment),
                ("statsPeriod", statsPeriod),
                ("start", start),
                ("end", end),
                ("project", project),
                ("sort", sort),
                ("cursor", cursor),
                ("per_page", per_page),
                ("query", query),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_an_organization_s_replays(
        self,
        organization_id_or_slug,
        statsPeriod=None,
        start=None,
        end=None,
        field=None,
        project=None,
        environment=None,
        sort=None,
        query=None,
        per_page=None,
        cursor=None,
    ) -> list[Any]:
        """
        Retrieves and lists replays for an organization, allowing filtering by various parameters such as statistics period, date range, fields, projects, environment, sorting, and query filters.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            statsPeriod (string): Specifies the time window for event statistics, supporting values such as "24h" (last 24 hours), "14d" (last 14 days), or an empty string for default/organization retention period.
            start (string): Timestamp (in ISO 8601 format) indicating the earliest replay to return in the results.
            end (string): Specifies the end date or time for filtering replays, formatted as a string.
            field (array): An array of fields to include in the replay response, allowing selective retrieval of specific data.
            project (array): Filter replays by including only those associated with specific project IDs, provided as an array in the query string.
            environment (string): Specifies the environment name to filter replay data for the given organization.
            sort (string): Specifies the field(s) to sort replay data by, allowing clients to control the order of the returned list.
            query (string): A string filter to search and filter replay results based on specific criteria.
            per_page (integer): The "per_page" parameter specifies the number of items to include on each page of the replay data for the specified organization.
            cursor (string): A string token used to fetch the next or previous page of results, typically representing a unique identifier or encoded position for stable, incremental pagination.

        Returns:
            list[Any]: API response data.

        Tags:
            Replays
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/replays/"
        query_params = {
            k: v
            for k, v in [
                ("statsPeriod", statsPeriod),
                ("start", start),
                ("end", end),
                ("field", field),
                ("project", project),
                ("environment", environment),
                ("sort", sort),
                ("query", query),
                ("per_page", per_page),
                ("cursor", cursor),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_a_replay_instance(
        self,
        organization_id_or_slug,
        replay_id,
        statsPeriod=None,
        start=None,
        end=None,
        field=None,
        project=None,
        environment=None,
        sort=None,
        query=None,
        per_page=None,
        cursor=None,
    ) -> dict[str, Any]:
        """
        Retrieves replay data for a specified organization and replay ID, allowing filtering by various parameters such as stats period, date range, fields, projects, and environment.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            replay_id (string): replay_id
            statsPeriod (string): Optional time range for statistics aggregation, specified as a string like "24h" or "14d", to filter the replay data by its stats period.
            start (string): The "start" parameter is a string query parameter used in the GET operation to specify the starting point for retrieving replays within the specified organization and replay context.
            end (string): Timestamp of the latest event or record to include in the response, specified as a string.
            field (array): An array of fields to include in the response for the specified replay.
            project (array): An array of project identifiers to filter replays by, allowing multiple projects to be specified in a single query.
            environment (string): The environment query parameter specifies the deployment environment (e.g., production, staging) to filter or scope the replay data returned by the API.
            sort (string): Specifies the field to sort by, allowing clients to customize the order of returned results.
            query (string): A string used to filter or search replay data by matching specified criteria.
            per_page (integer): The "per_page" parameter is used to specify the number of items to return per page for the requested resource.
            cursor (string): A string value used to fetch the next or previous page of results in cursor-based pagination, typically referencing the position in the dataset after which to continue retrieving items.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Replays
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if replay_id is None:
            raise ValueError("Missing required parameter 'replay_id'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/replays/{replay_id}/"
        query_params = {
            k: v
            for k, v in [
                ("statsPeriod", statsPeriod),
                ("start", start),
                ("end", end),
                ("field", field),
                ("project", project),
                ("environment", environment),
                ("sort", sort),
                ("query", query),
                ("per_page", per_page),
                ("cursor", cursor),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_an_organization_s_paginated_teams(
        self,
        organization_id_or_slug,
        startIndex=None,
        count=None,
        filter=None,
        excludedAttributes=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of SCIM groups for a specified organization using query parameters such as startIndex, count, filter, and excludedAttributes.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            startIndex (integer): The startIndex query parameter specifies the 1-based index of the first result to return in the paginated list of groups, with a default value of 1.
            count (integer): Specifies the maximum number of group records to return in the response; defaults to 100.
            filter (string): Specifies a SCIM filter expression to narrow down the list of groups returned, allowing filtering by group attributes such as displayName or other supported fields.
            excludedAttributes (array): Specifies an array of attributes to exclude from the response when retrieving SCIM groups, allowing for reduced data transfer and faster query execution.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            SCIM
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/scim/v2/Groups"
        query_params = {
            k: v
            for k, v in [
                ("startIndex", startIndex),
                ("count", count),
                ("filter", filter),
                ("excludedAttributes", excludedAttributes),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def provision_a_new_team(
        self, organization_id_or_slug, displayName
    ) -> dict[str, Any]:
        """
        Creates a new SCIM group for the specified organization using a POST request to the Groups endpoint, requiring organization details in the request body.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            displayName (string): The slug of the team that is shown in the UI.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            SCIM
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        request_body = {
            "displayName": displayName,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/scim/v2/Groups"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def query_an_individual_team(
        self, organization_id_or_slug, team_id
    ) -> dict[str, Any]:
        """
        Retrieves details about a specific team using its ID within an organization, returning relevant SCIM group information.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            team_id (string): team_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            SCIM
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/scim/v2/Groups/{team_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_a_team_s_attributes(
        self, organization_id_or_slug, team_id, Operations
    ) -> Any:
        """
        Modifies a specific group within an organization using SCIM 2.0, allowing updates to group attributes with the provided JSON payload.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            team_id (string): team_id
            Operations (array): The list of operations to perform. Valid operations are:
        * Renaming a team:
        ```json
        {
            "Operations": [{
                "op": "replace",
                "value": {
                    "id": 23,
                    "displayName": "newName"
                }
            }]
        }
        ```
        * Adding a member to a team:
        ```json
        {
            "Operations": [{
                "op": "add",
                "path": "members",
                "value": [
                    {
                        "value": 23,
                        "display": "testexample@example.com"
                    }
                ]
            }]
        }
        ```
        * Removing a member from a team:
        ```json
        {
            "Operations": [{
                "op": "remove",
                "path": "members[value eq "23"]"
            }]
        }
        ```
        * Replacing an entire member set of a team:
        ```json
        {
            "Operations": [{
                "op": "replace",
                "path": "members",
                "value": [
                    {
                        "value": 23,
                        "display": "testexample2@sentry.io"
                    },
                    {
                        "value": 24,
                        "display": "testexample3@sentry.io"
                    }
                ]
            }]
        }
        ```


        Returns:
            Any: Success

        Tags:
            SCIM
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        request_body = {
            "Operations": Operations,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/scim/v2/Groups/{team_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_an_individual_team(self, organization_id_or_slug, team_id) -> Any:
        """
        Deletes a specific team from an organization using SCIM, identified by a team ID, and removes associated permissions and access.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            team_id (string): team_id

        Returns:
            Any: Success

        Tags:
            SCIM
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if team_id is None:
            raise ValueError("Missing required parameter 'team_id'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/scim/v2/Groups/{team_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_an_organization_s_scim_members(
        self,
        organization_id_or_slug,
        startIndex=None,
        count=None,
        filter=None,
        excludedAttributes=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of users from the specified organization using SCIM 2.0, allowing pagination and filtering based on query parameters such as `startIndex`, `count`, and `filter`.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            startIndex (integer): 1-based index of the first query result, specifying from which user record to start returning results; a value less than 1 defaults to 1.
            count (integer): The "count" query parameter specifies the maximum number of user records to return in the response, with a default value of 100.
            filter (string): Specifies a filter expression to narrow down the user results, using SCIM syntax with attribute names, operators, and values, such as "userName eq 'example'" to match specific user attributes.
            excludedAttributes (array): A query parameter used to specify attributes that should be excluded from the response when retrieving SCIM users, potentially improving response times by reducing the amount of data returned.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            SCIM
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/scim/v2/Users"
        query_params = {
            k: v
            for k, v in [
                ("startIndex", startIndex),
                ("count", count),
                ("filter", filter),
                ("excludedAttributes", excludedAttributes),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def provision_a_new_organization_member(
        self, organization_id_or_slug, userName, sentryOrgRole=None
    ) -> dict[str, Any]:
        """
        Creates a new user in an organization using the SCIM API by sending a POST request to the specified Users endpoint.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            userName (string): The SAML field used for email.
            sentryOrgRole (string): The organization role of the member. If unspecified, this will be
                            set to the organization's default role. The options are:

        * `billing` - Can manage payment and compliance details.
        * `member` - Can view and act on events, as well as view most other data within the organization.
        * `manager` - Has full management access to all teams and projects. Can also manage
                the organization's membership.
        * `admin` - Can edit global integrations, manage projects, and add/remove teams.
                They automatically assume the Team Admin role for teams they join.
                Note: This role can no longer be assigned in Business and Enterprise plans. Use `TeamRoles` instead.


        Returns:
            dict[str, Any]: API response data.

        Tags:
            SCIM
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        request_body = {
            "userName": userName,
            "sentryOrgRole": sentryOrgRole,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/scim/v2/Users"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def query_an_individual_organization_member(
        self, organization_id_or_slug, member_id
    ) -> dict[str, Any]:
        """
        Retrieves a specific member's details within an organization using the SCIM API, based on the organization ID or slug and the member ID.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            member_id (string): member_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            SCIM
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if member_id is None:
            raise ValueError("Missing required parameter 'member_id'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/scim/v2/Users/{member_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_an_organization_member_s_attributes(
        self, organization_id_or_slug, member_id, Operations
    ) -> Any:
        """
        Updates specific attributes of a SCIM user within an organization using a PATCH request.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            member_id (string): member_id
            Operations (array): A list of operations to perform. Currently, the only valid operation is setting
        a member's `active` attribute to false, after which the member will be permanently deleted.
        ```json
        {
            "Operations": [{
                "op": "replace",
                "path": "active",
                "value": False
            }]
        }
        ```


        Returns:
            Any: Success

        Tags:
            SCIM
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if member_id is None:
            raise ValueError("Missing required parameter 'member_id'")
        request_body = {
            "Operations": Operations,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/scim/v2/Users/{member_id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_an_organization_member_via_scim(
        self, organization_id_or_slug, member_id
    ) -> Any:
        """
        Deletes an organization member by ID using the SCIM API, requiring a valid admin token for authentication.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            member_id (string): member_id

        Returns:
            Any: Success

        Tags:
            SCIM
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if member_id is None:
            raise ValueError("Missing required parameter 'member_id'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/scim/v2/Users/{member_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_release_health_session_statistics(
        self,
        organization_id_or_slug,
        field,
        start=None,
        end=None,
        environment=None,
        statsPeriod=None,
        project=None,
        per_page=None,
        interval=None,
        groupBy=None,
        orderBy=None,
        includeTotals=None,
        includeSeries=None,
        query=None,
    ) -> dict[str, Any]:
        """
        Retrieves sessions for a specified organization using the provided filters and parameters, such as fields, date range, environment, and statistics period.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            field (array): Required array parameter specifying the fields to be included in the response for the sessions of an organization.
            start (string): Specifies the starting point for filtering sessions, typically used for pagination or filtering by a specific start date or time.
            end (string): Filters the sessions by specifying the end date for the sessions to retrieve.
            environment (array): An array parameter specifying the environments to filter sessions by in the organization.
            statsPeriod (string): An optional parameter specifying the stat period for query results, which can be set to values like "24h" or "14d" to filter data based on the specified time frame.
            project (array): Filter sessions by one or more project IDs, provided as an array.
            per_page (integer): The number of session records to return per page in the paginated response.
            interval (string): **interval** (string): Specifies the time interval for which session data is retrieved.
            groupBy (array): Specifies an array of fields to group session results by.
            orderBy (string): Specifies the field to sort the returned sessions by.
            includeTotals (integer): Include the total count of sessions in the response alongside the session data when set to a non-zero value.
            includeSeries (integer): If set to 1, includes time series data in the sessions response.
            query (string): A string parameter used to filter session results.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Releases
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/sessions/"
        query_params = {
            k: v
            for k, v in [
                ("field", field),
                ("start", start),
                ("end", end),
                ("environment", environment),
                ("statsPeriod", statsPeriod),
                ("project", project),
                ("per_page", per_page),
                ("interval", interval),
                ("groupBy", groupBy),
                ("orderBy", orderBy),
                ("includeTotals", includeTotals),
                ("includeSeries", includeSeries),
                ("query", query),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_organization_events_count_by_project(
        self,
        organization_id_or_slug,
        field,
        statsPeriod=None,
        interval=None,
        start=None,
        end=None,
        project=None,
        category=None,
        outcome=None,
        reason=None,
        download=None,
    ) -> dict[str, Any]:
        """
        Retrieves a summary of statistics for an organization specified by its ID or slug, allowing for filtering by field, time period, and other criteria, and optionally returns the data in a downloadable format.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            field (string): Specifies the aggregation function and field to summarize; valid values are "sum(quantity)" or "sum(times_seen)".
            statsPeriod (string): Specifies the time period for which to retrieve statistics, using values like "24h" for 24 hours or "14d" for 14 days.
            interval (string): Specifies the time interval for which statistics are summarized, such as a day, week, or month, to filter the results of the organization's statistics.
            start (string): A date string parameter used to specify the start date for retrieving statistical summaries of an organization.
            end (string): The "end" query parameter specifies the end datetime for the stats summary data retrieval period.
            project (array): An optional array parameter specifying the projects to filter the stats summary by.
            category (string): Filter the stats summary by category type, which can be one of the following: error, transaction, attachment, replays, or profiles.
            outcome (string): Filter summary statistics by the outcome of operations, which can be one of the following: accepted, filtered, rate_limited, invalid, abuse, client_discard, or cardinality_limited.
            reason (string): Optional string parameter to specify the reason for retrieving the stats summary for an organization.
            download (boolean): Specifies whether the response data should trigger a file download (true) or be returned inline (false).

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Organizations
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/stats-summary/"
        query_params = {
            k: v
            for k, v in [
                ("field", field),
                ("statsPeriod", statsPeriod),
                ("interval", interval),
                ("start", start),
                ("end", end),
                ("project", project),
                ("category", category),
                ("outcome", outcome),
                ("reason", reason),
                ("download", download),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_organization_event_counts_v2(
        self,
        organization_id_or_slug,
        groupBy,
        field,
        statsPeriod=None,
        interval=None,
        start=None,
        end=None,
        project=None,
        category=None,
        outcome=None,
        reason=None,
    ) -> dict[str, Any]:
        """
        Retrieves statistical data for an organization using the `GET` method, allowing filtering by group, field, and time period.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            groupBy (array): **groupBy**: An array of fields by which to group the statistical results for the specified organization.
            field (string): The "field" parameter is a required string query parameter for the GET operation at "/api/0/organizations/{organization_id_or_slug}/stats_v2/", specifying the field to be used for statistics; it must be either "sum(quantity)" or "sum(times_seen)".
            statsPeriod (string): An optional parameter specifying the time period for which statistics are retrieved, with possible values including "24h", "14d", and others, defaulting to a specific period if not provided.
            interval (string): The interval parameter specifies the time aggregation period for the statistics data, such as FIFTEEN_MIN, THIRTY_MIN, HOUR, DAY, WEEK, or TOTAL, to control how results are grouped over time.
            start (string): Specifies the timestamp or date string marking the beginning of the time range for which statistics should be retrieved.
            end (string): Specifies the end timestamp (as a string) for the time range of the statistics to retrieve.
            project (array): An array of project identifiers used to filter the statistics returned for the specified organization.
            category (string): Filters organization statistics by a specific event category, such as errors, transactions, attachments, replays, profiles, profile durations, or monitors.
            outcome (string): Specifies the outcome status to filter by; possible values include accepted, filtered, rate_limited, invalid, abuse, client_discard, and cardinality_limited.
            reason (string): The "reason" query parameter specifies a string value indicating the rationale or context for the statistics request in the organization's stats endpoint.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Organizations
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/stats_v2/"
        query_params = {
            k: v
            for k, v in [
                ("groupBy", groupBy),
                ("field", field),
                ("statsPeriod", statsPeriod),
                ("interval", interval),
                ("start", start),
                ("end", end),
                ("project", project),
                ("category", category),
                ("outcome", outcome),
                ("reason", reason),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_an_organization_s_teams(
        self, organization_id_or_slug, detailed=None, cursor=None
    ) -> list[Any]:
        """
        Retrieves a list of teams associated with the specified organization, optionally with detailed information and pagination support.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            detailed (string): Include this parameter in the query string to request a more detailed representation of the teams in the organization.
            cursor (string): Specifies the position in the result set from which to start retrieving the next page of data, using a unique identifier or token provided by the server.

        Returns:
            list[Any]: API response data.

        Tags:
            Teams
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/teams/"
        query_params = {
            k: v
            for k, v in [("detailed", detailed), ("cursor", cursor)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_a_new_team(
        self, organization_id_or_slug, slug=None, name=None
    ) -> dict[str, Any]:
        """
        Creates a team within a specified organization using the provided JSON data and returns a status message upon successful creation.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            slug (string): Uniquely identifies a team and is used for the interface. If not
                provided, it is automatically generated from the name.
            name (string): **`[DEPRECATED]`** The name for the team. If not provided, it is
                automatically generated from the slug

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Teams
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        request_body = {
            "slug": slug,
            "name": name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/teams/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_a_user_s_teams_for_an_organization(
        self, organization_id_or_slug
    ) -> list[Any]:
        """
        Retrieves a list of user teams associated with the specified organization.

        Args:
            organization_id_or_slug (string): organization_id_or_slug

        Returns:
            list[Any]: API response data.

        Tags:
            Teams
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        url = (
            f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/user-teams/"
        )
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_a_project(
        self, organization_id_or_slug, project_id_or_slug
    ) -> dict[str, Any]:
        """
        Retrieves details about a specific project within an organization using the organization ID or slug and project ID or slug.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_a_project(
        self,
        organization_id_or_slug,
        project_id_or_slug,
        isBookmarked=None,
        name=None,
        slug=None,
        platform=None,
        subjectPrefix=None,
        subjectTemplate=None,
        resolveAge=None,
        highlightContext=None,
        highlightTags=None,
    ) -> dict[str, Any]:
        """
        Updates a project specified by organization ID or slug and project ID or slug using JSON data in the request body, requiring appropriate authentication.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            isBookmarked (boolean): Enables starring the project within the projects tab. Can be updated with **`project:read`** permission.
            name (string): The name for the project
            slug (string): Uniquely identifies a project and is used for the interface.
            platform (string): The platform for the project
            subjectPrefix (string): Custom prefix for emails from this project.
            subjectTemplate (string): The email subject to use (excluding the prefix) for individual alerts. Here are the list of variables you can use:
        - `$title`
        - `$shortID`
        - `$projectID`
        - `$orgID`
        - `${tag:key}` - such as `${tag:environment}` or `${tag:release}`.
            resolveAge (integer): Automatically resolve an issue if it hasn't been seen for this many hours. Set to `0` to disable auto-resolve.
            highlightContext (object): A JSON mapping of context types to lists of strings for their keys.
        E.g. `{'user': ['id', 'email']}`
            highlightTags (array): A list of strings with tag keys to highlight on this project's issues.
        E.g. `['release', 'environment']`

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        request_body = {
            "isBookmarked": isBookmarked,
            "name": name,
            "slug": slug,
            "platform": platform,
            "subjectPrefix": subjectPrefix,
            "subjectTemplate": subjectTemplate,
            "resolveAge": resolveAge,
            "highlightContext": highlightContext,
            "highlightTags": highlightTags,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_a_project(self, organization_id_or_slug, project_id_or_slug) -> Any:
        """
        Deletes a project identified by the specified organization ID or slug and project ID or slug using the DELETE method, requiring admin authentication.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug

        Returns:
            Any: No Content

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_a_project_s_environments(
        self, organization_id_or_slug, project_id_or_slug, visibility=None
    ) -> list[Any]:
        """
        Get a list of environments for a specified project within an organization, optionally filtered by visibility.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            visibility (string): Filter environments by visibility, with options for all, hidden, or visible environments.

        Returns:
            list[Any]: API response data.

        Tags:
            Environments
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/environments/"
        query_params = {k: v for k, v in [("visibility", visibility)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_a_project_environment(
        self, organization_id_or_slug, project_id_or_slug, environment
    ) -> dict[str, Any]:
        """
        Retrieves details for a specific environment within a project using the organization ID or slug, project ID or slug, and environment name.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            environment (string): environment

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Environments
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        if environment is None:
            raise ValueError("Missing required parameter 'environment'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/environments/{environment}/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_a_project_environment(
        self, organization_id_or_slug, project_id_or_slug, environment, isHidden
    ) -> dict[str, Any]:
        """
        Updates the environment settings for a specific project using the provided JSON data and returns a status message.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            environment (string): environment
            isHidden (boolean): Specify `true` to make the environment visible or `false` to make the environment hidden.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Environments
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        if environment is None:
            raise ValueError("Missing required parameter 'environment'")
        request_body = {
            "isHidden": isHidden,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/environments/{environment}/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_a_project_s_error_events(
        self,
        organization_id_or_slug,
        project_id_or_slug,
        cursor=None,
        full=None,
        sample=None,
    ) -> list[Any]:
        """
        Retrieves a list of events for a specific project in an organization using the provided identifiers and optional query parameters for pagination and data filtering.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            cursor (string): A string token used for cursor-based pagination to specify the position in the event list from which to continue fetching results.
            full (boolean): When set to true, returns the full event data; defaults to false for a summarized response.
            sample (boolean): Whether to return only a sample of events, rather than all events (default: false).

        Returns:
            list[Any]: API response data.

        Tags:
            Events
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/events/"
        query_params = {
            k: v
            for k, v in [("cursor", cursor), ("full", full), ("sample", sample)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def debug_event_source_maps(
        self,
        organization_id_or_slug,
        project_id_or_slug,
        event_id,
        frame_idx,
        exception_idx,
    ) -> dict[str, Any]:
        """
        Retrieves source map debug information for a specific event within a project, using the `GET` method and requiring an organization ID or slug, project ID or slug, event ID, frame index, and exception index.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            event_id (string): event_id
            frame_idx (integer): Index of the frame to retrieve debug information for within the event's source map.
            exception_idx (integer): The zero-based index of the exception to retrieve source map debug information for in the event.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Events
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        if event_id is None:
            raise ValueError("Missing required parameter 'event_id'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/events/{event_id}/source-map-debug/"
        query_params = {
            k: v
            for k, v in [("frame_idx", frame_idx), ("exception_idx", exception_idx)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_a_project_s_data_filters(
        self, organization_id_or_slug, project_id_or_slug
    ) -> list[Any]:
        """
        Retrieves a list of filters for a project in a specified organization using the provided organization ID or slug and project ID or slug.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug

        Returns:
            list[Any]: API response data.

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/filters/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_an_inbound_data_filter(
        self,
        organization_id_or_slug,
        project_id_or_slug,
        filter_id,
        active=None,
        subfilters=None,
    ) -> Any:
        """
        Updates a filter in a project using the organization ID or slug, project ID or slug, and filter ID, with the new filter details provided in the JSON body, requiring appropriate authentication for project administration or writing permissions.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            filter_id (string): filter_id
            active (boolean): Toggle the browser-extensions, localhost, filtered-transaction, or web-crawlers filter on or off.
            subfilters (array):
        Specifies which legacy browser filters should be active. Anything excluded from the list will be
        disabled. The options are:
        - `ie` - Internet Explorer Version 11 and lower
        - `edge` - Edge Version 18 and lower
        - `safari` - Safari Version 11 and lower
        - `firefox` - Firefox Version 66 and lower
        - `chrome` - Chrome Version 62 and lower
        - `opera` - Opera Version 50 and lower
        - `android` - Android Version 3 and lower
        - `opera_mini` - Opera Mini Version 34 and lower

        Deprecated options:
        - `ie_pre_9` - Internet Explorer Version 8 and lower
        - `ie9` - Internet Explorer Version 9
        - `ie10` - Internet Explorer Version 10
        - `ie11` - Internet Explorer Version 11
        - `safari_pre_6` - Safari Version 5 and lower
        - `opera_pre_15` - Opera Version 14 and lower
        - `opera_mini_pre_8` - Opera Mini Version 8 and lower
        - `android_pre_4` - Android Version 3 and lower
        - `edge_pre_79` - Edge Version 18 and lower (non Chromium based)


        Returns:
            Any: No Content

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        if filter_id is None:
            raise ValueError("Missing required parameter 'filter_id'")
        request_body = {
            "active": active,
            "subfilters": subfilters,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/filters/{filter_id}/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_a_project_s_client_keys(
        self, organization_id_or_slug, project_id_or_slug, cursor=None, status=None
    ) -> list[Any]:
        """
        Retrieves a list of keys for a project, allowing optional filtering by status and pagination with a cursor.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            cursor (string): A cursor string used for cursor-based pagination to specify the position from which to continue fetching key data in the project.
            status (string): A string parameter to filter the keys based on their status, used in the GET operation to retrieve keys for a specific project within an organization.

        Returns:
            list[Any]: API response data.

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/keys/"
        query_params = {
            k: v for k, v in [("cursor", cursor), ("status", status)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_a_new_client_key(
        self, organization_id_or_slug, project_id_or_slug, name=None, rateLimit=None
    ) -> dict[str, Any]:
        """
        Create a new key for a specific project within an organization by providing the necessary details in the request body.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            name (string): The optional name of the key. If not provided it will be automatically generated.
            rateLimit (object): Applies a rate limit to cap the number of errors accepted during a given time window. To
        disable entirely set `rateLimit` to null.
        ```json
        {
            "rateLimit": {
                "window": 7200, // time in seconds
                "count": 1000 // error cap
            }
        }
        ```

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        request_body = {
            "name": name,
            "rateLimit": rateLimit,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/keys/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_a_client_key(
        self, organization_id_or_slug, project_id_or_slug, key_id
    ) -> dict[str, Any]:
        """
        Retrieves details about a specific project key using the organization ID or slug and project ID or slug.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            key_id (string): key_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        if key_id is None:
            raise ValueError("Missing required parameter 'key_id'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/keys/{key_id}/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_a_client_key(
        self,
        organization_id_or_slug,
        project_id_or_slug,
        key_id,
        name=None,
        isActive=None,
        rateLimit=None,
        browserSdkVersion=None,
        dynamicSdkLoaderOptions=None,
    ) -> dict[str, Any]:
        """
        Updates a project key using the PUT method, requiring the organization ID or slug, project ID or slug, and key ID, with authentication for project admin or write permissions.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            key_id (string): key_id
            name (string): The name for the client key
            isActive (boolean): Activate or deactivate the client key.
            rateLimit (object): Applies a rate limit to cap the number of errors accepted during a given time window. To
        disable entirely set `rateLimit` to null.
        ```json
        {
            "rateLimit": {
                "window": 7200, // time in seconds
                "count": 1000 // error cap
            }
        }
        ```
            browserSdkVersion (string): The Sentry Javascript SDK version to use. The currently supported options are:

        * `latest` - Most recent version
        * `7.x` - Version 7 releases
            dynamicSdkLoaderOptions (object): Configures multiple options for the Javascript Loader Script.
        - `Performance Monitoring`
        - `Debug Bundles & Logging`
        - `Session Replay` - Note that the loader will load the ES6 bundle instead of the ES5 bundle.
        ```json
        {
            "dynamicSdkLoaderOptions": {
                "hasReplay": true,
                "hasPerformance": true,
                "hasDebug": true
            }
        }
        ```

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        if key_id is None:
            raise ValueError("Missing required parameter 'key_id'")
        request_body = {
            "name": name,
            "isActive": isActive,
            "rateLimit": rateLimit,
            "browserSdkVersion": browserSdkVersion,
            "dynamicSdkLoaderOptions": dynamicSdkLoaderOptions,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/keys/{key_id}/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_a_client_key(
        self, organization_id_or_slug, project_id_or_slug, key_id
    ) -> Any:
        """
        Deletes a specified API key within a project under an organization, requiring project admin authorization.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            key_id (string): key_id

        Returns:
            Any: No Content

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        if key_id is None:
            raise ValueError("Missing required parameter 'key_id'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/keys/{key_id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_a_project_s_organization_members(
        self, organization_id_or_slug, project_id_or_slug
    ) -> list[Any]:
        """
        Retrieves a list of members for a specific project within an organization using the provided organization ID or slug and project ID or slug.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug

        Returns:
            list[Any]: API response data.

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/members/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_a_monitor_for_a_project(
        self, organization_id_or_slug, project_id_or_slug, monitor_id_or_slug
    ) -> dict[str, Any]:
        """
        Retrieves details for a specific monitor within a project and organization using their respective IDs or slugs.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            monitor_id_or_slug (string): monitor_id_or_slug

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Crons
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        if monitor_id_or_slug is None:
            raise ValueError("Missing required parameter 'monitor_id_or_slug'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/monitors/{monitor_id_or_slug}/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_a_monitor_for_a_project(
        self,
        organization_id_or_slug,
        project_id_or_slug,
        monitor_id_or_slug,
        name,
        type,
        slug=None,
        status=None,
        owner=None,
        is_muted=None,
    ) -> dict[str, Any]:
        """
        Updates a monitor in a project using the organization and project identifiers.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            monitor_id_or_slug (string): monitor_id_or_slug
            name (string): Name of the monitor. Used for notifications.
            type (string): * `cron_job`
            slug (string): Uniquely identifies your monitor within your organization. Changing this slug will require updates to any instrumented check-in calls.
            status (string): Status of the monitor. Disabled monitors will not accept events and will not count towards the monitor quota.

        * `active`
        * `disabled`
            owner (string): The ID of the team or user that owns the monitor. (eg. user:51 or team:6)
            is_muted (boolean): Disable creation of monitor incidents

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Crons
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        if monitor_id_or_slug is None:
            raise ValueError("Missing required parameter 'monitor_id_or_slug'")
        request_body = {
            "name": name,
            "type": type,
            "slug": slug,
            "status": status,
            "owner": owner,
            "is_muted": is_muted,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/monitors/{monitor_id_or_slug}/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_project_monitor_or_environments(
        self,
        organization_id_or_slug,
        project_id_or_slug,
        monitor_id_or_slug,
        environment=None,
    ) -> Any:
        """
        Deletes a specific monitor from a project in an organization and returns an HTTP status indicating the outcome.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            monitor_id_or_slug (string): monitor_id_or_slug
            environment (array): Specifies the environment names or IDs as an array to filter which monitors to delete; if omitted, the operation applies to all environments.

        Returns:
            Any: Accepted

        Tags:
            Crons
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        if monitor_id_or_slug is None:
            raise ValueError("Missing required parameter 'monitor_id_or_slug'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/monitors/{monitor_id_or_slug}/"
        query_params = {
            k: v for k, v in [("environment", environment)] if v is not None
        }
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_check_ins_for_a_monitor_by_project(
        self, organization_id_or_slug, project_id_or_slug, monitor_id_or_slug
    ) -> list[Any]:
        """
        Retrieves checkin data for a specific monitor in a project, identified by the organization ID or slug, project ID or slug, and monitor ID or slug.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            monitor_id_or_slug (string): monitor_id_or_slug

        Returns:
            list[Any]: API response data.

        Tags:
            Crons
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        if monitor_id_or_slug is None:
            raise ValueError("Missing required parameter 'monitor_id_or_slug'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/monitors/{monitor_id_or_slug}/checkins/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_project_ownership_config(
        self, organization_id_or_slug, project_id_or_slug
    ) -> dict[str, Any]:
        """
        Retrieves project ownership details for a specific project within an organization using the provided organization ID or slug and project ID or slug.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/ownership/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_project_ownership_config(
        self,
        organization_id_or_slug,
        project_id_or_slug,
        raw=None,
        fallthrough=None,
        autoAssignment=None,
        codeownersAutoSync=None,
    ) -> dict[str, Any]:
        """
        Updates the ownership configuration for a specific project, allowing modification of ownership rules, fallthrough assignment, auto-assignment settings, and CODEOWNERS synchronization[1].

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            raw (string): Raw input for ownership configuration. See the [Ownership Rules Documentation](/product/issues/ownership-rules/) to learn more.
            fallthrough (boolean): A boolean determining who to assign ownership to when an ownership rule has no match. If set to `True`, all project members are made owners. Otherwise, no owners are set.
            autoAssignment (string): Auto-assignment settings. The available options are:
        - Auto Assign to Issue Owner
        - Auto Assign to Suspect Commits
        - Turn off Auto-Assignment
            codeownersAutoSync (boolean): Set to `True` to sync issue owners with CODEOWNERS updates in a release.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        request_body = {
            "raw": raw,
            "fallthrough": fallthrough,
            "autoAssignment": autoAssignment,
            "codeownersAutoSync": codeownersAutoSync,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/ownership/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_a_replay_instance(
        self, organization_id_or_slug, project_id_or_slug, replay_id
    ) -> Any:
        """
        Deletes a specified replay associated with a project and organization using its unique identifier.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            replay_id (string): replay_id

        Returns:
            Any: No Content

        Tags:
            Replays
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        if replay_id is None:
            raise ValueError("Missing required parameter 'replay_id'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/replays/{replay_id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_clicked_nodes(
        self,
        organization_id_or_slug,
        project_id_or_slug,
        replay_id,
        cursor=None,
        environment=None,
        per_page=None,
        query=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of user click events recorded during a specific replay session within a project and organization, with optional filtering and pagination.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            replay_id (string): replay_id
            cursor (string): A string parameter used in cursor-based pagination to specify the unique identifier of the last fetched record, allowing retrieval of the next page of data.
            environment (array): Filters replay click events by one or more environment names, returning only those that match the specified environments.
            per_page (integer): Specifies the number of click records to return per page.
            query (string): A string filter to search for specific click events within the specified replay.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Replays
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        if replay_id is None:
            raise ValueError("Missing required parameter 'replay_id'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/replays/{replay_id}/clicks/"
        query_params = {
            k: v
            for k, v in [
                ("cursor", cursor),
                ("environment", environment),
                ("per_page", per_page),
                ("query", query),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_recording_segments(
        self,
        organization_id_or_slug,
        project_id_or_slug,
        replay_id,
        cursor=None,
        per_page=None,
    ) -> list[Any]:
        """
        Retrieves a paginated list of recording segments for a specified replay within a project and organization.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            replay_id (string): replay_id
            cursor (string): An opaque string token used for pagination, indicating the position in the dataset from which to return results for subsequent requests.
            per_page (integer): The number of items to return per page for listing recording segments.

        Returns:
            list[Any]: API response data.

        Tags:
            Replays
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        if replay_id is None:
            raise ValueError("Missing required parameter 'replay_id'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/replays/{replay_id}/recording-segments/"
        query_params = {
            k: v
            for k, v in [("cursor", cursor), ("per_page", per_page)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_a_recording_segment(
        self, organization_id_or_slug, project_id_or_slug, replay_id, segment_id
    ) -> list[Any]:
        """
        Retrieves a specific recording segment from a replay within a project using the organization ID or slug and project ID or slug.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            replay_id (string): replay_id
            segment_id (string): segment_id

        Returns:
            list[Any]: API response data.

        Tags:
            Replays
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        if replay_id is None:
            raise ValueError("Missing required parameter 'replay_id'")
        if segment_id is None:
            raise ValueError("Missing required parameter 'segment_id'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/replays/{replay_id}/recording-segments/{segment_id}/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_users_who_have_viewed_a_replay(
        self, organization_id_or_slug, project_id_or_slug, replay_id
    ) -> dict[str, Any]:
        """
        Get a list of users who have viewed a specific replay in a project within an organization.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            replay_id (string): replay_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Replays
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        if replay_id is None:
            raise ValueError("Missing required parameter 'replay_id'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/replays/{replay_id}/viewed-by/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_a_project_s_issue_alert_rules(
        self, organization_id_or_slug, project_id_or_slug
    ) -> list[Any]:
        """
        Retrieves the list of rules configured for a specified project within an organization.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug

        Returns:
            list[Any]: API response data.

        Tags:
            Alerts
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/rules/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_an_issue_alert_rule_for_a_project(
        self,
        organization_id_or_slug,
        project_id_or_slug,
        name,
        frequency,
        actionMatch,
        conditions,
        actions,
        environment=None,
        owner=None,
        filterMatch=None,
        filters=None,
    ) -> dict[str, Any]:
        """
        Creates a new rule for a project within an organization using the provided JSON data and returns a success status upon creation.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            name (string): The name for the rule.
            frequency (integer): How often to perform the actions once for an issue, in minutes. The valid range is `5` to `43200`.
            actionMatch (string): A string determining which of the conditions need to be true before any filters are evaluated.

        * `all` - All conditions must evaluate to true.
        * `any` - At least one of the conditions must evaluate to true.
        * `none` - All conditions must evaluate to false.
            conditions (array):
        A list of triggers that determine when the rule fires. See below for a list of possible conditions.

        **A new issue is created**
        ```json
        {
            "id": "sentry.rules.conditions.first_seen_event.FirstSeenEventCondition"
        }
        ```

        **The issue changes state from resolved to unresolved**
        ```json
        {
            "id": "sentry.rules.conditions.regression_event.RegressionEventCondition"
        }
        ```

        **The issue is seen more than `value` times in `interval`**
        - `value` - An integer
        - `interval` - Valid values are `1m`, `5m`, `15m`, `1h`, `1d`, `1w` and `30d` (`m` for minutes, `h` for hours, `d` for days, and `w` for weeks).
        ```json
        {
            "id": "sentry.rules.conditions.event_frequency.EventFrequencyCondition",
            "value": 500,
            "interval": "1h"
        }
        ```

        **The issue is seen by more than `value` users in `interval`**
        - `value` - An integer
        - `interval` - Valid values are `1m`, `5m`, `15m`, `1h`, `1d`, `1w` and `30d` (`m` for minutes, `h` for hours, `d` for days, and `w` for weeks).
        ```json
        {
            "id": "sentry.rules.conditions.event_frequency.EventUniqueUserFrequencyCondition",
            "value": 1000,
            "interval": "15m"
        }
        ```

        **The issue affects more than `value` percent of sessions in `interval`**
        - `value` - A float
        - `interval` - Valid values are `5m`, `10m`, `30m`, and `1h` (`m` for minutes, `h` for hours).
        ```json
        {
            "id": "sentry.rules.conditions.event_frequency.EventFrequencyPercentCondition",
            "value": 50.0,
            "interval": "10m"
        }
        ```

            actions (array):
        A list of actions that take place when all required conditions and filters for the rule are met. See below for a list of possible actions.

        **Send a notification to Suggested Assignees**
        - `fallthroughType` - Who the notification should be sent to if there are no suggested assignees. Valid values are `ActiveMembers`, `AllMembers`, and `NoOne`.
        ```json
        {
            "id" - "sentry.mail.actions.NotifyEmailAction",
            "targetType" - "IssueOwners",
            "fallthroughType" - "ActiveMembers"
        }
        ```

        **Send a notification to a Member or a Team**
        - `targetType` - One of `Member` or `Team`.
        - `fallthroughType` - Who the notification should be sent to if it cannot be sent to the original target. Valid values are `ActiveMembers`, `AllMembers`, and `NoOne`.
        - `targetIdentifier` - The ID of the Member or Team the notification should be sent to.
        ```json
        {
            "id": "sentry.mail.actions.NotifyEmailAction",
            "targetType": "Team"
            "fallthroughType": "AllMembers"
            "targetIdentifier": 4524986223
        }
        ```

        **Send a Slack notification**
        - `workspace` - The integration ID associated with the Slack workspace.
        - `channel` - The name of the channel to send the notification to (e.g., #critical, Jane Schmidt).
        - `channel_id` (optional) - The ID of the channel to send the notification to.
        - `tags` (optional) - A string of tags to show in the notification, separated by commas (e.g., "environment, user, my_tag").
        - `notes` (optional) - Text to show alongside the notification. To @ a user, include their user id like `@<USER_ID>`. To include a clickable link, format the link and title like `<http://example.com|Click Here>`.
        ```json
        {
            "id": "sentry.integrations.slack.notify_action.SlackNotifyServiceAction",
            "workspace": 293854098,
            "channel": "#warning",
            "tags": "environment,level"
            "notes": "Please <http://example.com|click here> for triage information"
        }
        ```

        **Send a Microsoft Teams notification**
        - `team` - The integration ID associated with the Microsoft Teams team.
        - `channel` - The name of the channel to send the notification to.
        ```json
        {
            "id": "sentry.integrations.msteams.notify_action.MsTeamsNotifyServiceAction",
            "team": 23465424,
            "channel": "General"
        }
        ```

        **Send a Discord notification**
        - `server` - The integration ID associated with the Discord server.
        - `channel_id` - The ID of the channel to send the notification to.
        - `tags` (optional) - A string of tags to show in the notification, separated by commas (e.g., "environment, user, my_tag").
        ```json
        {
            "id": "sentry.integrations.discord.notify_action.DiscordNotifyServiceAction",
            "server": 63408298,
            "channel_id": 94732897,
            "tags": "browser,user"
        }
        ```

        **Create a Jira Ticket**
        - `integration` - The integration ID associated with Jira.
        - `project` - The ID of the Jira project.
        - `issuetype` - The ID of the type of issue that the ticket should be created as.
        - `dynamic_form_fields` (optional) - A list of any custom fields you want to include in the ticket as objects.
        ```json
        {
            "id": "sentry.integrations.jira.notify_action.JiraCreateTicketAction",
            "integration": 321424,
            "project": "349719"
            "issueType": "1"
        }
        ```

        **Create a Jira Server Ticket**
        - `integration` - The integration ID associated with Jira Server.
        - `project` - The ID of the Jira Server project.
        - `issuetype` - The ID of the type of issue that the ticket should be created as.
        - `dynamic_form_fields` (optional) - A list of any custom fields you want to include in the ticket as objects.
        ```json
        {
            "id": "sentry.integrations.jira_server.notify_action.JiraServerCreateTicketAction",
            "integration": 321424,
            "project": "349719"
            "issueType": "1"
        }
        ```

        **Create a GitHub Issue**
        - `integration` - The integration ID associated with GitHub.
        - `repo` - The name of the repository to create the issue in.
        - `title` - The title of the issue.
        - `body` (optional) - The contents of the issue.
        - `assignee` (optional) - The GitHub user to assign the issue to.
        - `labels` (optional) - A list of labels to assign to the issue.
        ```json
        {
            "id": "sentry.integrations.github.notify_action.GitHubCreateTicketAction",
            "integration": 93749,
            "repo": default,
            "title": "My Test Issue",
            "assignee": "Baxter the Hacker",
            "labels": ["bug", "p1"]
            ""
        }
        ```

        **Create a GitHub Enterprise Issue**
        - `integration` - The integration ID associated with GitHub Enterprise.
        - `repo` - The name of the repository to create the issue in.
        - `title` - The title of the issue.
        - `body` (optional) - The contents of the issue.
        - `assignee` (optional) - The GitHub user to assign the issue to.
        - `labels` (optional) - A list of labels to assign to the issue.
        ```json
        {
            "id": "sentry.integrations.github_enterprise.notify_action.GitHubEnterpriseCreateTicketAction",
            "integration": 93749,
            "repo": default,
            "title": "My Test Issue",
            "assignee": "Baxter the Hacker",
            "labels": ["bug", "p1"]
            ""
        }
        ```

        **Create an Azure DevOps work item**
        - `integration` - The integration ID.
        - `project` - The ID of the Azure DevOps project.
        - `work_item_type` - The type of work item to create.
        - `dynamic_form_fields` (optional) - A list of any custom fields you want to include in the work item as objects.
        ```json
        {
            "id": "sentry.integrations.vsts.notify_action.AzureDevopsCreateTicketAction",
            "integration": 294838,
            "project": "0389485",
            "work_item_type": "Microsoft.VSTS.WorkItemTypes.Task",
        }
        ```

        **Send a PagerDuty notification**
        - `account` - The integration ID associated with the PagerDuty account.
        - `service` - The ID of the service to send the notification to.
        - `severity` - The severity of the Pagerduty alert. This is optional, the default is `critical` for fatal issues, `error` for error issues, `warning` for warning issues, and `info` for info and debug issues.
        ```json
        {
            "id": "sentry.integrations.pagerduty.notify_action.PagerDutyNotifyServiceAction",
            "account": 92385907,
            "service": 9823924,
            "severity": "critical"
        }
        ```

        **Send an Opsgenie notification**
        - `account` - The integration ID associated with the Opsgenie account.
        - `team` - The ID of the Opsgenie team to send the notification to.
        - `priority` - The priority of the Opsgenie alert. This is optional, the default is `P3`.
        ```json
        {
            "id": "sentry.integrations.opsgenie.notify_action.OpsgenieNotifyTeamAction",
            "account": 8723897589,
            "team": "9438930258-fairy",
            "priority": "P1"
        }
        ```

        **Send a notification to a service**
        - `service` - The plugin slug.
        ```json
        {
            "id": "sentry.rules.actions.notify_event_service.NotifyEventServiceAction",
            "service": "mail"
        }
        ```

        **Send a notification to a Sentry app with a custom webhook payload**
        - `settings` - A list of objects denoting the settings each action will be created with. All required fields must be included.
        - `sentryAppInstallationUuid` - The ID for the Sentry app
        ```json
        {
            "id": "sentry.rules.actions.notify_event_sentry_app.NotifyEventSentryAppAction",
            "settings": [
                {"name": "title", "value": "Team Rocket"},
                {"name": "summary", "value": "We're blasting off again."},
            ],
            "sentryAppInstallationUuid": 643522
            "hasSchemaFormConfig": true
        }
        ```

        **Send a notification (for all legacy integrations)**
        ```json
        {
            "id": "sentry.rules.actions.notify_event.NotifyEventAction"
        }
        ```

            environment (string): The name of the environment to filter by.
            owner (string): The ID of the team or user that owns the rule.
            filterMatch (string): A string determining which filters need to be true before any actions take place. Required when a value is provided for `filters`.

        * `all` - All filters must evaluate to true.
        * `any` - At least one of the filters must evaluate to true.
        * `none` - All filters must evaluate to false.
            filters (array):
        A list of filters that determine if a rule fires after the necessary conditions have been met. See below for a list of possible filters.

        **The issue is `comparison_type` than `value` `time`**
        - `comparison_type` - One of `older` or `newer`
        - `value` - An integer
        - `time` - The unit of time. Valid values are `minute`, `hour`, `day`, and `week`.
        ```json
        {
            "id": "sentry.rules.filters.age_comparison.AgeComparisonFilter",
            "comparison_type": "older",
            "value": 3,
            "time": "week"
        }
        ```

        **The issue has happened at least `value` times**
        - `value` - An integer
        ```json
        {
            "id": "sentry.rules.filters.issue_occurrences.IssueOccurrencesFilter",
            "value": 120
        }
        ```

        **The issue is assigned to No One**
        ```json
        {
            "id": "sentry.rules.filters.assigned_to.AssignedToFilter",
            "targetType": "Unassigned"
        }
        ```

        **The issue is assigned to `targetType`**
        - `targetType` - One of `Team` or `Member`
        - `targetIdentifier` - The target's ID
        ```json
        {
            "id": "sentry.rules.filters.assigned_to.AssignedToFilter",
            "targetType": "Member",
            "targetIdentifier": 895329789
        }
        ```

        **The event is from the latest release**
        ```json
        {
            "id": "sentry.rules.filters.latest_release.LatestReleaseFilter"
        }
        ```

        **The issue's category is equal to `value`**
        - `value` - An integer correlated with a category. Valid values are `1` (Error), `2` (Performance), `3` (Profile), `4` (Cron), and `5` (Replay).
        ```json
        {
            "id": "sentry.rules.filters.issue_category.IssueCategoryFilter",
            "value": 2
        }
        ```

        **The event's `attribute` value `match` `value`**
        - `attribute` - Valid values are `message`, `platform`, `environment`, `type`, `error.handled`, `error.unhandled`, `error.main_thread`, `exception.type`, `exception.value`, `user.id`, `user.email`, `user.username`, `user.ip_address`, `http.method`, `http.url`, `http.status_code`, `sdk.name`, `stacktrace.code`, `stacktrace.module`, `stacktrace.filename`, `stacktrace.abs_path`, `stacktrace.package`, `unreal.crashtype`, and `app.in_foreground`.
        - `match` - The comparison operator. Valid values are `eq` (equals), `ne` (does not equal), `sw` (starts with), `ew` (ends with), `co` (contains), `nc` (does not contain), `is` (is set), and `ns` (is not set).
        - `value` - A string. Not required when `match` is `is` or `ns`.
        ```json
        {
            "id": "sentry.rules.conditions.event_attribute.EventAttributeCondition",
            "attribute": "http.url",
            "match": "nc",
            "value": "localhost"
        }
        ```

        **The event's tags match `key` `match` `value`**
        - `key` - The tag
        - `match` - The comparison operator. Valid values are `eq` (equals), `ne` (does not equal), `sw` (starts with), `ew` (ends with), `co` (contains), `nc` (does not contain), `is` (is set), and `ns` (is not set).
        - `value` - A string. Not required when `match` is `is` or `ns`.
        ```json
        {
            "id": "sentry.rules.filters.tagged_event.TaggedEventFilter",
            "key": "level",
            "match": "eq"
            "value": "error"
        }
        ```

        **The event's level is `match` `level`**
        - `match` - Valid values are `eq`, `gte`, and `lte`.
        - `level` - Valid values are `50` (fatal), `40` (error), `30` (warning), `20` (info), `10` (debug), `0` (sample).
        ```json
        {
            "id": "sentry.rules.filters.level.LevelFilter",
            "match": "gte"
            "level": "50"
        }
        ```


        Returns:
            dict[str, Any]: API response data.

        Tags:
            Alerts
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        request_body = {
            "name": name,
            "frequency": frequency,
            "actionMatch": actionMatch,
            "conditions": conditions,
            "actions": actions,
            "environment": environment,
            "owner": owner,
            "filterMatch": filterMatch,
            "filters": filters,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/rules/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_an_issue_alert_rule_for_a_project(
        self, organization_id_or_slug, project_id_or_slug, rule_id
    ) -> dict[str, Any]:
        """
        Retrieves information about a specific rule in a project using the organization ID or slug, project ID or slug, and rule ID.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            rule_id (string): rule_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Alerts
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        if rule_id is None:
            raise ValueError("Missing required parameter 'rule_id'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/rules/{rule_id}/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_an_issue_alert_rule(
        self,
        organization_id_or_slug,
        project_id_or_slug,
        rule_id,
        name,
        actionMatch,
        conditions,
        actions,
        frequency,
        environment=None,
        filterMatch=None,
        filters=None,
        owner=None,
    ) -> dict[str, Any]:
        """
        Updates a specific rule in a project by replacing its current state with new values provided in the request body, requiring authentication with the necessary permissions.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            rule_id (string): rule_id
            name (string): The name for the rule.
            actionMatch (string): A string determining which of the conditions need to be true before any filters are evaluated.

        * `all` - All conditions must evaluate to true.
        * `any` - At least one of the conditions must evaluate to true.
        * `none` - All conditions must evaluate to false.
            conditions (array): A list of triggers that determine when the rule fires. See [Create an Issue Alert Rule](/api/alerts/create-an-issue-alert-rule-for-a-project) for valid conditions.
            actions (array): A list of actions that take place when all required conditions and filters for the rule are met. See [Create an Issue Alert Rule](/api/alerts/create-an-issue-alert-rule-for-a-project) for valid actions.
            frequency (integer): How often to perform the actions once for an issue, in minutes. The valid range is `5` to `43200`.
            environment (string): The name of the environment to filter by.
            filterMatch (string): A string determining which filters need to be true before any actions take place.

        * `all` - All filters must evaluate to true.
        * `any` - At least one of the filters must evaluate to true.
        * `none` - All filters must evaluate to false.
            filters (array): A list of filters that determine if a rule fires after the necessary conditions have been met. See [Create an Issue Alert Rule](/api/alerts/create-an-issue-alert-rule-for-a-project) for valid filters.
            owner (string): The ID of the team or user that owns the rule.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Alerts
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        if rule_id is None:
            raise ValueError("Missing required parameter 'rule_id'")
        request_body = {
            "name": name,
            "actionMatch": actionMatch,
            "conditions": conditions,
            "actions": actions,
            "frequency": frequency,
            "environment": environment,
            "filterMatch": filterMatch,
            "filters": filters,
            "owner": owner,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/rules/{rule_id}/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_an_issue_alert_rule(
        self, organization_id_or_slug, project_id_or_slug, rule_id
    ) -> Any:
        """
        Deletes a specific rule from a project within an organization by rule ID.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            rule_id (string): rule_id

        Returns:
            Any: Accepted

        Tags:
            Alerts
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        if rule_id is None:
            raise ValueError("Missing required parameter 'rule_id'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/rules/{rule_id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_a_project_s_symbol_sources(
        self, organization_id_or_slug, project_id_or_slug, id=None
    ) -> list[Any]:
        """
        Retrieves a list of symbol sources for a specified project within an organization using the provided organization and project identifiers.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            id (string): Optional string identifier to filter symbol sources by a specific ID.

        Returns:
            list[Any]: API response data.

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/symbol-sources/"
        query_params = {k: v for k, v in [("id", id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_a_symbol_source_to_a_project(
        self,
        organization_id_or_slug,
        project_id_or_slug,
        type,
        name,
        id=None,
        layout=None,
        url=None,
        username=None,
        password=None,
        bucket=None,
        region=None,
        access_key=None,
        secret_key=None,
        prefix=None,
        client_email=None,
        private_key=None,
    ) -> Any:
        """
        Creates a new symbol source for a specified project within an organization using the provided JSON data and returns a 201 status on success.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            type (string): The type of the source.

        * `http` - SymbolServer (HTTP)
        * `gcs` - Google Cloud Storage
        * `s3` - Amazon S3
            name (string): The human-readable name of the source.
            id (string): The internal ID of the source. Must be distinct from all other source IDs and cannot start with '`sentry:`'. If this is not provided, a new UUID will be generated.
            layout (object): Layout settings for the source. This is required for HTTP, GCS, and S3 sources.

        **`type`** ***(string)*** - The layout of the folder structure. The options are:
        - `native` - Platform-Specific (SymStore / GDB / LLVM)
        - `symstore` - Microsoft SymStore
        - `symstore_index2` - Microsoft SymStore (with index2.txt)
        - `ssqp` - Microsoft SSQP
        - `unified` - Unified Symbol Server Layout
        - `debuginfod` - debuginfod

        **`casing`** ***(string)*** - The layout of the folder structure. The options are:
        - `default` - Default (mixed case)
        - `uppercase` - Uppercase
        - `lowercase` - Lowercase

        ```json
        {
            "layout": {
                "type": "native"
                "casing": "default"
            }
        }
        ```
            url (string): The source's URL. Optional for HTTP sources, invalid for all others.
            username (string): The user name for accessing the source. Optional for HTTP sources, invalid for all others.
            password (string): The password for accessing the source. Optional for HTTP sources, invalid for all others.
            bucket (string): The GCS or S3 bucket where the source resides. Required for GCS and S3 source, invalid for HTTP sources.
            region (string): The source's [S3 region](https://docs.aws.amazon.com/general/latest/gr/s3.html). Required for S3 sources, invalid for all others.

        * `us-east-2` - US East (Ohio)
        * `us-east-1` - US East (N. Virginia)
        * `us-west-1` - US West (N. California)
        * `us-west-2` - US West (Oregon)
        * `ap-east-1` - Asia Pacific (Hong Kong)
        * `ap-south-1` - Asia Pacific (Mumbai)
        * `ap-northeast-2` - Asia Pacific (Seoul)
        * `ap-southeast-1` - Asia Pacific (Singapore)
        * `ap-southeast-2` - Asia Pacific (Sydney)
        * `ap-northeast-1` - Asia Pacific (Tokyo)
        * `ca-central-1` - Canada (Central)
        * `cn-north-1` - China (Beijing)
        * `cn-northwest-1` - China (Ningxia)
        * `eu-central-1` - EU (Frankfurt)
        * `eu-west-1` - EU (Ireland)
        * `eu-west-2` - EU (London)
        * `eu-west-3` - EU (Paris)
        * `eu-north-1` - EU (Stockholm)
        * `sa-east-1` - South America (São Paulo)
        * `us-gov-east-1` - AWS GovCloud (US-East)
        * `us-gov-west-1` - AWS GovCloud (US)
            access_key (string): The [AWS Access Key](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html#access-keys-and-secret-access-keys).Required for S3 sources, invalid for all others.
            secret_key (string): The [AWS Secret Access Key](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html#access-keys-and-secret-access-keys).Required for S3 sources, invalid for all others.
            prefix (string): The GCS or [S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html) prefix. Optional for GCS and S3 sourcse, invalid for HTTP.
            client_email (string): The GCS email address for authentication. Required for GCS sources, invalid for all others.
            private_key (string): The GCS private key. Required for GCS sources, invalid for all others.

        Returns:
            Any: API response data.

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        request_body = {
            "type": type,
            "name": name,
            "id": id,
            "layout": layout,
            "url": url,
            "username": username,
            "password": password,
            "bucket": bucket,
            "region": region,
            "access_key": access_key,
            "secret_key": secret_key,
            "prefix": prefix,
            "client_email": client_email,
            "private_key": private_key,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/symbol-sources/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_a_project_s_symbol_source(
        self,
        organization_id_or_slug,
        project_id_or_slug,
        id,
        type,
        name,
        id_body=None,
        layout=None,
        url=None,
        username=None,
        password=None,
        bucket=None,
        region=None,
        access_key=None,
        secret_key=None,
        prefix=None,
        client_email=None,
        private_key=None,
    ) -> Any:
        """
        Updates or replaces a symbol source configuration for a specified project within an organization using the provided JSON data.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            id (string): The unique identifier of the symbol source to update, provided as a required query parameter.
            type (string): The type of the source.

        * `http` - SymbolServer (HTTP)
        * `gcs` - Google Cloud Storage
        * `s3` - Amazon S3
            name (string): The human-readable name of the source.
            id_body (string): The internal ID of the source. Must be distinct from all other source IDs and cannot start with '`sentry:`'. If this is not provided, a new UUID will be generated.
            layout (object): Layout settings for the source. This is required for HTTP, GCS, and S3 sources.

        **`type`** ***(string)*** - The layout of the folder structure. The options are:
        - `native` - Platform-Specific (SymStore / GDB / LLVM)
        - `symstore` - Microsoft SymStore
        - `symstore_index2` - Microsoft SymStore (with index2.txt)
        - `ssqp` - Microsoft SSQP
        - `unified` - Unified Symbol Server Layout
        - `debuginfod` - debuginfod

        **`casing`** ***(string)*** - The layout of the folder structure. The options are:
        - `default` - Default (mixed case)
        - `uppercase` - Uppercase
        - `lowercase` - Lowercase

        ```json
        {
            "layout": {
                "type": "native"
                "casing": "default"
            }
        }
        ```
            url (string): The source's URL. Optional for HTTP sources, invalid for all others.
            username (string): The user name for accessing the source. Optional for HTTP sources, invalid for all others.
            password (string): The password for accessing the source. Optional for HTTP sources, invalid for all others.
            bucket (string): The GCS or S3 bucket where the source resides. Required for GCS and S3 source, invalid for HTTP sources.
            region (string): The source's [S3 region](https://docs.aws.amazon.com/general/latest/gr/s3.html). Required for S3 sources, invalid for all others.

        * `us-east-2` - US East (Ohio)
        * `us-east-1` - US East (N. Virginia)
        * `us-west-1` - US West (N. California)
        * `us-west-2` - US West (Oregon)
        * `ap-east-1` - Asia Pacific (Hong Kong)
        * `ap-south-1` - Asia Pacific (Mumbai)
        * `ap-northeast-2` - Asia Pacific (Seoul)
        * `ap-southeast-1` - Asia Pacific (Singapore)
        * `ap-southeast-2` - Asia Pacific (Sydney)
        * `ap-northeast-1` - Asia Pacific (Tokyo)
        * `ca-central-1` - Canada (Central)
        * `cn-north-1` - China (Beijing)
        * `cn-northwest-1` - China (Ningxia)
        * `eu-central-1` - EU (Frankfurt)
        * `eu-west-1` - EU (Ireland)
        * `eu-west-2` - EU (London)
        * `eu-west-3` - EU (Paris)
        * `eu-north-1` - EU (Stockholm)
        * `sa-east-1` - South America (São Paulo)
        * `us-gov-east-1` - AWS GovCloud (US-East)
        * `us-gov-west-1` - AWS GovCloud (US)
            access_key (string): The [AWS Access Key](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html#access-keys-and-secret-access-keys).Required for S3 sources, invalid for all others.
            secret_key (string): The [AWS Secret Access Key](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html#access-keys-and-secret-access-keys).Required for S3 sources, invalid for all others.
            prefix (string): The GCS or [S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html) prefix. Optional for GCS and S3 sourcse, invalid for HTTP.
            client_email (string): The GCS email address for authentication. Required for GCS sources, invalid for all others.
            private_key (string): The GCS private key. Required for GCS sources, invalid for all others.

        Returns:
            Any: API response data.

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        request_body = {
            "type": type,
            "name": name,
            "id": id_body,
            "layout": layout,
            "url": url,
            "username": username,
            "password": password,
            "bucket": bucket,
            "region": region,
            "access_key": access_key,
            "secret_key": secret_key,
            "prefix": prefix,
            "client_email": client_email,
            "private_key": private_key,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/symbol-sources/"
        query_params = {k: v for k, v in [("id", id)] if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_a_symbol_source_from_a_project(
        self, organization_id_or_slug, project_id_or_slug, id
    ) -> Any:
        """
        Deletes symbol sources from a specific project identified by organization ID or slug and project ID or slug using the provided ID, requiring project admin authentication.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            id (string): Required string identifier for the symbol source to delete.

        Returns:
            Any: No Content

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/symbol-sources/"
        query_params = {k: v for k, v in [("id", id)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_a_project_s_teams(
        self, organization_id_or_slug, project_id_or_slug
    ) -> list[Any]:
        """
        Retrieves a list of teams within a specified project using the provided organization and project identifiers.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug

        Returns:
            list[Any]: API response data.

        Tags:
            Teams
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/teams/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_a_team_to_a_project(
        self, organization_id_or_slug, project_id_or_slug, team_id_or_slug
    ) -> dict[str, Any]:
        """
        Adds a specified team to a project within an organization and returns a response indicating successful creation.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            team_id_or_slug (string): team_id_or_slug

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        if team_id_or_slug is None:
            raise ValueError("Missing required parameter 'team_id_or_slug'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/teams/{team_id_or_slug}/"
        query_params = {}
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_a_team_from_a_project(
        self, organization_id_or_slug, project_id_or_slug, team_id_or_slug
    ) -> dict[str, Any]:
        """
        Deletes a team from a project within a specified organization using the API with appropriate permissions.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            team_id_or_slug (string): team_id_or_slug

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        if team_id_or_slug is None:
            raise ValueError("Missing required parameter 'team_id_or_slug'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/teams/{team_id_or_slug}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_a_team(
        self, organization_id_or_slug, team_id_or_slug, expand=None, collapse=None
    ) -> dict[str, Any]:
        """
        Retrieves information about a team within an organization using the provided organization ID or slug and team ID or slug, allowing optional expansion or collapse of additional details.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            team_id_or_slug (string): team_id_or_slug
            expand (string): The "expand" query parameter allows you to include additional related data in the response for a GET request, enabling the retrieval of multiple types of objects in a single call.
            collapse (string): The "collapse" parameter is a string query parameter that determines how to handle data grouping for the team data returned by the API operation.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Teams, important
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if team_id_or_slug is None:
            raise ValueError("Missing required parameter 'team_id_or_slug'")
        url = (
            f"{self.base_url}/api/0/teams/{organization_id_or_slug}/{team_id_or_slug}/"
        )
        query_params = {
            k: v
            for k, v in [("expand", expand), ("collapse", collapse)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_a_team(
        self, organization_id_or_slug, team_id_or_slug, slug
    ) -> dict[str, Any]:
        """
        Updates the details of a specified team within a given organization using the provided data and requires administrative or write permissions.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            team_id_or_slug (string): team_id_or_slug
            slug (string): Uniquely identifies a team. This is must be available.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Teams, important
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if team_id_or_slug is None:
            raise ValueError("Missing required parameter 'team_id_or_slug'")
        request_body = {
            "slug": slug,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = (
            f"{self.base_url}/api/0/teams/{organization_id_or_slug}/{team_id_or_slug}/"
        )
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_a_team(self, organization_id_or_slug, team_id_or_slug) -> Any:
        """
        Deletes a team from an organization using the provided organization ID or slug and team ID or slug, requiring the team admin authentication token for authorization.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            team_id_or_slug (string): team_id_or_slug

        Returns:
            Any: No Content

        Tags:
            Teams
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if team_id_or_slug is None:
            raise ValueError("Missing required parameter 'team_id_or_slug'")
        url = (
            f"{self.base_url}/api/0/teams/{organization_id_or_slug}/{team_id_or_slug}/"
        )
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_an_external_team(
        self,
        organization_id_or_slug,
        team_id_or_slug,
        external_name,
        provider,
        integration_id,
        external_id=None,
    ) -> dict[str, Any]:
        """
        Create a new external team associated with a specified organization and team using the provided JSON data.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            team_id_or_slug (string): team_id_or_slug
            external_name (string): The associated name for the provider.
            provider (string): The provider of the external actor.

        * `github`
        * `github_enterprise`
        * `slack`
        * `gitlab`
        * `msteams`
        * `custom_scm`
            integration_id (integer): The Integration ID.
            external_id (string): The associated user ID for provider.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Integrations
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if team_id_or_slug is None:
            raise ValueError("Missing required parameter 'team_id_or_slug'")
        request_body = {
            "external_name": external_name,
            "provider": provider,
            "integration_id": integration_id,
            "external_id": external_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/teams/{organization_id_or_slug}/{team_id_or_slug}/external-teams/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_an_external_team(
        self,
        organization_id_or_slug,
        team_id_or_slug,
        external_team_id,
        external_name,
        provider,
        integration_id,
        external_id=None,
    ) -> dict[str, Any]:
        """
        Updates an external team's details for a specified team and organization, requiring admin or write permissions, with the request body containing the updated data.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            team_id_or_slug (string): team_id_or_slug
            external_team_id (string): external_team_id
            external_name (string): The associated name for the provider.
            provider (string): The provider of the external actor.

        * `github`
        * `github_enterprise`
        * `slack`
        * `gitlab`
        * `msteams`
        * `custom_scm`
            integration_id (integer): The Integration ID.
            external_id (string): The associated user ID for provider.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Integrations
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if team_id_or_slug is None:
            raise ValueError("Missing required parameter 'team_id_or_slug'")
        if external_team_id is None:
            raise ValueError("Missing required parameter 'external_team_id'")
        request_body = {
            "external_name": external_name,
            "provider": provider,
            "integration_id": integration_id,
            "external_id": external_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/teams/{organization_id_or_slug}/{team_id_or_slug}/external-teams/{external_team_id}/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_an_external_team(
        self, organization_id_or_slug, team_id_or_slug, external_team_id
    ) -> Any:
        """
        Deletes an external team association with the specified team in an organization using the provided organization identifier, team identifier, and external team ID.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            team_id_or_slug (string): team_id_or_slug
            external_team_id (string): external_team_id

        Returns:
            Any: No Content

        Tags:
            Integrations
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if team_id_or_slug is None:
            raise ValueError("Missing required parameter 'team_id_or_slug'")
        if external_team_id is None:
            raise ValueError("Missing required parameter 'external_team_id'")
        url = f"{self.base_url}/api/0/teams/{organization_id_or_slug}/{team_id_or_slug}/external-teams/{external_team_id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_a_team_s_members(
        self, organization_id_or_slug, team_id_or_slug, cursor=None
    ) -> list[Any]:
        """
        Retrieves a list of members belonging to the specified team within the given organization, supporting pagination via a cursor parameter.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            team_id_or_slug (string): team_id_or_slug
            cursor (string): A string token used to retrieve the next or previous page of members, marking the current position in the paginated result set.

        Returns:
            list[Any]: API response data.

        Tags:
            Teams
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if team_id_or_slug is None:
            raise ValueError("Missing required parameter 'team_id_or_slug'")
        url = f"{self.base_url}/api/0/teams/{organization_id_or_slug}/{team_id_or_slug}/members/"
        query_params = {k: v for k, v in [("cursor", cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_a_team_s_projects(
        self, organization_id_or_slug, team_id_or_slug, cursor=None
    ) -> list[Any]:
        """
        Retrieves a paginated list of projects associated with a specific team within an organization, using optional cursor-based pagination.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            team_id_or_slug (string): team_id_or_slug
            cursor (string): A string parameter used for cursor-based pagination, allowing clients to fetch the next page of projects by specifying a unique identifier or token from previous responses.

        Returns:
            list[Any]: API response data.

        Tags:
            Teams
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if team_id_or_slug is None:
            raise ValueError("Missing required parameter 'team_id_or_slug'")
        url = f"{self.base_url}/api/0/teams/{organization_id_or_slug}/{team_id_or_slug}/projects/"
        query_params = {k: v for k, v in [("cursor", cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_a_new_project(
        self,
        organization_id_or_slug,
        team_id_or_slug,
        name,
        slug=None,
        platform=None,
        default_rules=None,
    ) -> dict[str, Any]:
        """
        Creates a new project within the specified team and organization using provided details and returns the project resource upon success.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            team_id_or_slug (string): team_id_or_slug
            name (string): The name for the project.
            slug (string): Uniquely identifies a project and is used for the interface.
                If not provided, it is automatically generated from the name.
            platform (string): The platform for the project.
            default_rules (boolean):
        Defaults to true where the behavior is to alert the user on every new
        issue. Setting this to false will turn this off and the user must create
        their own alerts to be notified of new issues.


        Returns:
            dict[str, Any]: API response data.

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if team_id_or_slug is None:
            raise ValueError("Missing required parameter 'team_id_or_slug'")
        request_body = {
            "name": name,
            "slug": slug,
            "platform": platform,
            "default_rules": default_rules,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/teams/{organization_id_or_slug}/{team_id_or_slug}/projects/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_user_emails(self, user_id) -> list[Any]:
        """
        Retrieves a list of email addresses associated with the specified user ID, requiring authentication.

        Args:
            user_id (string): user_id

        Returns:
            list[Any]: API response data.

        Tags:
            Users
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user_id'")
        url = f"{self.base_url}/api/0/users/{user_id}/emails/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_a_secondary_email_address(self, user_id, email) -> list[Any]:
        """
        Adds a new email address for a specified user using the provided JSON data and returns a success message.

        Args:
            user_id (string): user_id
            email (string): The email address to add/remove.

        Returns:
            list[Any]: API response data.

        Tags:
            Users
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user_id'")
        request_body = {
            "email": email,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/users/{user_id}/emails/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_a_primary_email_address(self, user_id, email) -> list[Any]:
        """
        Updates the email address of a user specified by the `user_id` using the provided JSON data in the request body.

        Args:
            user_id (string): user_id
            email (string): The email address to add/remove.

        Returns:
            list[Any]: API response data.

        Tags:
            Users
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user_id'")
        request_body = {
            "email": email,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/users/{user_id}/emails/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_an_email_address(self, user_id) -> Any:
        """
        Deletes a user's email configurations associated with the specified user ID using the DELETE method.

        Args:
            user_id (string): user_id

        Returns:
            Any: No Content

        Tags:
            Users
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user_id'")
        url = f"{self.base_url}/api/0/users/{user_id}/emails/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_event_counts_for_a_team(
        self,
        organization_id_or_slug,
        team_id_or_slug,
        stat=None,
        since=None,
        until=None,
        resolution=None,
    ) -> list[Any]:
        """
        Retrieves team statistics for a specified organization and team, allowing filtering by specific stat, date range, and resolution.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            team_id_or_slug (string): team_id_or_slug
            stat (string): The "stat" parameter is a query string parameter that specifies the type of statistic to retrieve, accepting values "received" or "rejected" for filtering team statistics.
            since (string): Specifies the timestamp or date from which to start including statistics in the response.
            until (string): The "until" parameter specifies the end date or time for retrieving team statistics, formatted as a string.
            resolution (string): Defines the time resolution for retrieving team statistics, available options include 10-second, 1-hour, and 1-day intervals.

        Returns:
            list[Any]: Success

        Tags:
            Teams
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if team_id_or_slug is None:
            raise ValueError("Missing required parameter 'team_id_or_slug'")
        url = f"{self.base_url}/api/0/teams/{organization_id_or_slug}/{team_id_or_slug}/stats/"
        query_params = {
            k: v
            for k, v in [
                ("stat", stat),
                ("since", since),
                ("until", until),
                ("resolution", resolution),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def resolve_an_event_id(self, organization_id_or_slug, event_id) -> dict[str, Any]:
        """
        Retrieves event details for a specific event within an organization identified by the provided organization ID or slug and event ID.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            event_id (string): event_id

        Returns:
            dict[str, Any]: Success

        Tags:
            Organizations
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if event_id is None:
            raise ValueError("Missing required parameter 'event_id'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/eventids/{event_id}/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_an_organization_s_repositories(self, organization_id_or_slug) -> list[Any]:
        """
        Retrieves a list of repositories for the specified organization identified by its ID or slug, requiring organization read authorization.

        Args:
            organization_id_or_slug (string): organization_id_or_slug

        Returns:
            list[Any]: Success

        Tags:
            Organizations
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/repos/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_a_repository_s_commits(
        self, organization_id_or_slug, repo_id
    ) -> list[Any]:
        """
        Retrieves a list of commits from a specified repository within an organization, requiring read access for authentication.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            repo_id (string): repo_id

        Returns:
            list[Any]: Success

        Tags:
            Organizations
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if repo_id is None:
            raise ValueError("Missing required parameter 'repo_id'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/repos/{repo_id}/commits/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def resolve_a_short_id(self, organization_id_or_slug, short_id) -> dict[str, Any]:
        """
        Retrieves information for a specific short ID within an organization using the provided organization ID or slug.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            short_id (string): short_id

        Returns:
            dict[str, Any]: Success

        Tags:
            Organizations
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if short_id is None:
            raise ValueError("Missing required parameter 'short_id'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/shortids/{short_id}/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_your_projects(self, cursor=None) -> list[Any]:
        """
        Get a list of projects accessible to the user, optionally paginated using a cursor.

        Args:
            cursor (string): This parameter is used for cursor-based pagination, providing a unique identifier to fetch the next page of data in a specific order, typically based on a unique identifier like a timestamp or record ID.

        Returns:
            list[Any]: Success

        Tags:
            Projects
        """
        url = f"{self.base_url}/api/0/projects/"
        query_params = {k: v for k, v in [("cursor", cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_project_debug_files(
        self, organization_id_or_slug, project_id_or_slug
    ) -> Any:
        """
        Retrieves a list of dSYM files for a specific project within an organization using the provided organization ID or slug and project ID or slug.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug

        Returns:
            Any: Success

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/files/dsyms/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_project_debug_file(
        self, organization_id_or_slug, project_id_or_slug, id
    ) -> Any:
        """
        Deletes a dSYM file from a project using its ID, requiring a write authorization token for the project.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            id (string): Required string identifier for the file to be deleted.

        Returns:
            Any: Success

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/files/dsyms/"
        query_params = {k: v for k, v in [("id", id)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_a_project_s_users(
        self, organization_id_or_slug, project_id_or_slug, query=None
    ) -> list[Any]:
        """
        Retrieves a list of users associated with a specified project within an organization, optionally filtered by a query parameter.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            query (string): A string parameter used to filter or search for specific users within the specified project.

        Returns:
            list[Any]: Success

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/users/"
        query_params = {k: v for k, v in [("query", query)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_a_tag_s_values(
        self, organization_id_or_slug, project_id_or_slug, key
    ) -> list[Any]:
        """
        Retrieves a list of values for a specific tag key within a project, using the organization ID or slug and project ID or slug.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            key (string): key

        Returns:
            list[Any]: Success

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        if key is None:
            raise ValueError("Missing required parameter 'key'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/tags/{key}/values/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_event_counts_for_a_project(
        self,
        organization_id_or_slug,
        project_id_or_slug,
        stat=None,
        since=None,
        until=None,
        resolution=None,
    ) -> list[Any]:
        """
        Retrieves statistics for a specific project within an organization, optionally filtered by stat type, time range, and resolution.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            stat (string): Specifies the type of statistics to retrieve, which must be one of: "received", "rejected", "blacklisted", or "generated".
            since (string): The "since" parameter filters the returned statistics to include only data from the specified date or time onwards.
            until (string): Specifies the timestamp or date up to which to retrieve statistics for the project.
            resolution (string): Specifies the time aggregation interval for the stats data, with possible values of "10s", "1h", or "1d".

        Returns:
            list[Any]: Success

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/stats/"
        query_params = {
            k: v
            for k, v in [
                ("stat", stat),
                ("since", since),
                ("until", until),
                ("resolution", resolution),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_a_project_s_user_feedback(
        self, organization_id_or_slug, project_id_or_slug
    ) -> list[Any]:
        """
        Retrieves a list of user feedback items for a specified project within an organization.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug

        Returns:
            list[Any]: Success

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/user-feedback/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def submit_user_feedback(
        self,
        organization_id_or_slug,
        project_id_or_slug,
        event_id=None,
        name=None,
        email=None,
        comments=None,
    ) -> dict[str, Any]:
        """
        Submits user feedback for a specific project within an organization using the provided JSON body and authenticates via an authentication token with project write permissions.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            event_id (string): The event ID. This can be retrieved from the [beforeSend callback](https://docs.sentry.io/platforms/javascript/configuration/filtering/#using-beforesend).
            name (string): User's name.
            email (string): User's email address.
            comments (string): Comments supplied by user.
                Example:
                ```json
                {
                  "event_id": "14bad9a2e3774046977a21440ddb39b2",
                  "name": "Jane Schmidt",
                  "email": "jane@empowerplant.io",
                  "comments": "It broke!"
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        request_body = {
            "event_id": event_id,
            "name": name,
            "email": email,
            "comments": comments,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/user-feedback/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_a_project_s_service_hooks(
        self, organization_id_or_slug, project_id_or_slug, cursor=None
    ) -> list[Any]:
        """
        Retrieves a list of hooks for a specific project within an organization using the project and organization identifiers.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            cursor (string): A token that marks the current position in paginated results, used to fetch the next or previous page of data.

        Returns:
            list[Any]: Success

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/hooks/"
        query_params = {k: v for k, v in [("cursor", cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def register_a_new_service_hook(
        self, organization_id_or_slug, project_id_or_slug, url, events
    ) -> dict[str, Any]:
        """
        Creates a new webhook for the specified project within an organization and returns a success status upon creation.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            url (string): The URL for the webhook.
            events (array): The events to subscribe to.
                Example:
                ```json
                {
                  "url": "https://empowerplant.io/sentry-hook",
                  "events": [
                    "event.alert",
                    "event.created"
                  ]
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        request_body = {
            "url": url,
            "events": events,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/hooks/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_a_service_hook(
        self, organization_id_or_slug, project_id_or_slug, hook_id
    ) -> dict[str, Any]:
        """
        Retrieves a specific hook from a project using organization and project identifiers.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            hook_id (string): hook_id

        Returns:
            dict[str, Any]: Success

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        if hook_id is None:
            raise ValueError("Missing required parameter 'hook_id'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/hooks/{hook_id}/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_a_service_hook(
        self,
        organization_id_or_slug,
        project_id_or_slug,
        hook_id,
        url=None,
        events=None,
    ) -> dict[str, Any]:
        """
        Updates a specific hook in a project using the provided JSON payload and returns a success response upon completion.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            hook_id (string): hook_id
            url (string): The URL for the webhook.
            events (array): The events to subscribe to.
                Example:
                ```json
                {
                  "url": "https://empowerplant.io/sentry-hook",
                  "events": [
                    "event.alert",
                    "event.created"
                  ]
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        if hook_id is None:
            raise ValueError("Missing required parameter 'hook_id'")
        request_body = {
            "url": url,
            "events": events,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/hooks/{hook_id}/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_a_service_hook(
        self, organization_id_or_slug, project_id_or_slug, hook_id
    ) -> Any:
        """
        Deletes a webhook hook identified by the specified hook ID within a project, requiring administrative privileges for the project.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            hook_id (string): hook_id

        Returns:
            Any: Success

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        if hook_id is None:
            raise ValueError("Missing required parameter 'hook_id'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/hooks/{hook_id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_an_event_for_a_project(
        self, organization_id_or_slug, project_id_or_slug, event_id
    ) -> dict[str, Any]:
        """
        Retrieves details for a specific event within a project using the organization ID or slug and project ID or slug.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            event_id (string): event_id

        Returns:
            dict[str, Any]: Success

        Tags:
            Events
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        if event_id is None:
            raise ValueError("Missing required parameter 'event_id'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/events/{event_id}/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_project_issues(
        self,
        organization_id_or_slug,
        project_id_or_slug,
        statsPeriod=None,
        shortIdLookup=None,
        query=None,
        hashes=None,
        cursor=None,
    ) -> list[Any]:
        """
        Get a list of issues for a specified project within an organization, with optional filters for query, stats period, short ID lookup, hashes, and pagination.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            statsPeriod (string): An optional string parameter specifying the time range for statistics, such as "24h" or "14d", to filter issue data within that period.
            shortIdLookup (boolean): When true, enables lookup of issues by their short ID in the query.
            query (string): The search query string to filter or search issues within the specified project and organization.
            hashes (string): Optional string parameter to specify hashes for filtering issues.
            cursor (string): A string parameter used for cursor-based pagination, indicating the position in the dataset from which to retrieve the next set of issues.

        Returns:
            list[Any]: Success

        Tags:
            Events
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/issues/"
        query_params = {
            k: v
            for k, v in [
                ("statsPeriod", statsPeriod),
                ("shortIdLookup", shortIdLookup),
                ("query", query),
                ("hashes", hashes),
                ("cursor", cursor),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_mutate_a_list_of_issues(
        self,
        organization_id_or_slug,
        project_id_or_slug,
        id=None,
        status=None,
        status_body=None,
        statusDetails=None,
        ignoreDuration=None,
        isPublic=None,
        merge=None,
        assignedTo=None,
        hasSeen=None,
        isBookmarked=None,
    ) -> dict[str, Any]:
        """
        Updates an issue in a specific project within an organization using the provided JSON body and returns a status code indicating the outcome of the update.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            id (integer): Optional integer query parameter specifying the ID to further filter or identify issues within the project.
            status (string): Specifies the desired issue status to update (e.g., "open", "closed") when modifying an issue via the PUT operation; optional.
            status_body (string): The new status for the issues. Valid values are `"resolved"`, `"resolvedInNextRelease"`, `"unresolved"`, and `"ignored"`.
            statusDetails (object): Additional details about the resolution. Valid values are `"inRelease"`, `"inNextRelease"`, `"inCommit"`, `"ignoreDuration"`, `"ignoreCount"`, `"ignoreWindow"`, `"ignoreUserCount"`, and `"ignoreUserWindow"`.
            ignoreDuration (integer): The number of minutes to ignore this issue.
            isPublic (boolean): Sets the issue to public or private.
            merge (boolean): Allows to merge or unmerge different issues.
            assignedTo (string): The actor ID (or username) of the user or team that should be assigned to this issue.
            hasSeen (boolean): In case this API call is invoked with a user context this allows changing of the flag that indicates if the user has seen the event.
            isBookmarked (boolean): In case this API call is invoked with a user context this allows changing of the bookmark flag.
                Example:
                ```json
                {
                  "isPublic": false,
                  "status": "unresolved"
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Events
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        request_body = {
            "status": status_body,
            "statusDetails": statusDetails,
            "ignoreDuration": ignoreDuration,
            "isPublic": isPublic,
            "merge": merge,
            "assignedTo": assignedTo,
            "hasSeen": hasSeen,
            "isBookmarked": isBookmarked,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/issues/"
        query_params = {
            k: v for k, v in [("id", id), ("status", status)] if v is not None
        }
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_remove_a_list_of_issues(
        self, organization_id_or_slug, project_id_or_slug, id=None
    ) -> Any:
        """
        Deletes issues from a project by organization or project identifier using the "DELETE" method, requiring authentication as an event administrator.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            id (integer): The `id` parameter is an integer specifying the issue ID to be deleted, passed as a query parameter in the DELETE operation.

        Returns:
            Any: Success

        Tags:
            Events
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/issues/"
        query_params = {k: v for k, v in [("id", id)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_a_tag_s_values_related_to_an_issue(
        self, organization_id_or_slug, issue_id, key
    ) -> list[Any]:
        """
        Retrieves the available values for a specific tag key associated with an issue within the specified organization.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            issue_id (string): issue_id
            key (string): key

        Returns:
            list[Any]: Success

        Tags:
            Events
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if issue_id is None:
            raise ValueError("Missing required parameter 'issue_id'")
        if key is None:
            raise ValueError("Missing required parameter 'key'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/issues/{issue_id}/tags/{key}/values/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_an_issue_s_hashes(
        self, organization_id_or_slug, issue_id, full=None, cursor=None
    ) -> list[Any]:
        """
        Retrieves hashes for a specific issue in an organization using the provided organization ID or slug and issue ID, optionally including additional details if the "full" query parameter is set.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            issue_id (string): issue_id
            full (boolean): Returns detailed information if set to true; otherwise, returns a limited view of the hashes. Default is true.
            cursor (string): A unique identifier (or token) used for cursor-based pagination to fetch the next or previous page of hash records; if provided, results will start after (or before, depending on implementation) the specified position in the dataset.

        Returns:
            list[Any]: Success

        Tags:
            Events
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if issue_id is None:
            raise ValueError("Missing required parameter 'issue_id'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/issues/{issue_id}/hashes/"
        query_params = {
            k: v for k, v in [("full", full), ("cursor", cursor)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_an_issue(self, organization_id_or_slug, issue_id) -> dict[str, Any]:
        """
        Retrieves details about a specific issue within an organization using the provided organization ID or slug and issue ID.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            issue_id (string): issue_id

        Returns:
            dict[str, Any]: Success

        Tags:
            Events, important
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if issue_id is None:
            raise ValueError("Missing required parameter 'issue_id'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/issues/{issue_id}/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_an_issue(
        self,
        organization_id_or_slug,
        issue_id,
        status=None,
        statusDetails=None,
        assignedTo=None,
        hasSeen=None,
        isBookmarked=None,
        isSubscribed=None,
        isPublic=None,
    ) -> dict[str, Any]:
        """
        Updates an existing issue within an organization by modifying its details using the provided JSON payload.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            issue_id (string): issue_id
            status (string): The new status for the issues. Valid values are `"resolved"`, `"resolvedInNextRelease"`, `"unresolved"`, and `"ignored"`.
            statusDetails (object): Additional details about the resolution. Supported values are `"inRelease"`, `"inNextRelease"`, `"inCommit"`, `"ignoreDuration"`, `"ignoreCount"`, `"ignoreWindow"`, `"ignoreUserCount"`, and `"ignoreUserWindow"`.
            assignedTo (string): The actor id (or username) of the user or team that should be assigned to this issue.
            hasSeen (boolean): In case this API call is invoked with a user context this allows changing of the flag that indicates if the user has seen the event.
            isBookmarked (boolean): In case this API call is invoked with a user context this allows changing of the bookmark flag.
            isSubscribed (boolean): In case this API call is invoked with a user context this allows the user to subscribe to workflow notications for this issue.
            isPublic (boolean): Sets the issue to public or private.
                Example:
                ```json
                {
                  "status": "unresolved"
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Events
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if issue_id is None:
            raise ValueError("Missing required parameter 'issue_id'")
        request_body = {
            "status": status,
            "statusDetails": statusDetails,
            "assignedTo": assignedTo,
            "hasSeen": hasSeen,
            "isBookmarked": isBookmarked,
            "isSubscribed": isSubscribed,
            "isPublic": isPublic,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/issues/{issue_id}/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_an_issue(self, organization_id_or_slug, issue_id) -> Any:
        """
        Deletes an issue identified by `{issue_id}` within an organization specified by `{organization_id_or_slug}` using the DELETE method.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            issue_id (string): issue_id

        Returns:
            Any: Success

        Tags:
            Events
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if issue_id is None:
            raise ValueError("Missing required parameter 'issue_id'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/issues/{issue_id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_an_organization_s_releases(
        self, organization_id_or_slug, query=None
    ) -> list[Any]:
        """
        Retrieves a list of releases for a specified organization using the provided organization ID or slug, with optional query filtering.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            query (string): A string parameter used to filter or search releases within the specified organization.

        Returns:
            list[Any]: Success

        Tags:
            Releases
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/releases/"
        query_params = {k: v for k, v in [("query", query)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_a_new_release_for_an_organization(
        self,
        organization_id_or_slug,
        version=None,
        projects=None,
        ref=None,
        url=None,
        dateReleased=None,
        commits=None,
        refs=None,
    ) -> dict[str, Any]:
        """
        Creates a new release for the specified organization using the provided release data.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            version (string): A version identifier for this release. Can be a version number, a commit hash, etc.
            projects (array): A list of project slugs that are involved in this release.
            ref (string): An optional commit reference. This is useful if a tagged version has been provided.
            url (string): A URL that points to the release. This can be the path to an online interface to the source code for instance
            dateReleased (string): An optional date that indicates when the release went live. If not provided the current time is assumed.
            commits (array): An optional list of commit data to be associated with the release. Commits must include parameters `id` (the SHA of the commit), and can optionally include `repository`, `message`, `patch_set`, `author_name`, `author_email`, and `timestamp`.
            refs (array): An optional way to indicate the start and end commits for each repository included in a release. Head commits must include parameters `repository` and `commit` (the HEAD sha). They can optionally include `previousCommit` (the sha of the HEAD of the previous release), which should be specified if this is the first time you've sent commit data. `commit` may contain a range in the form of `previousCommit..commit`.
                Example:
                ```json
                {
                  "version": "2.0rc2",
                  "ref": "6ba09a7c53235ee8a8fa5ee4c1ca8ca886e7fdbb",
                  "projects": [
                    "pump-station"
                  ]
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Releases
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        request_body = {
            "version": version,
            "projects": projects,
            "ref": ref,
            "url": url,
            "dateReleased": dateReleased,
            "commits": commits,
            "refs": refs,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/releases/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_an_organization_s_release_files(
        self, organization_id_or_slug, version
    ) -> list[Any]:
        """
        Retrieves a list of files associated with a specific release version within an organization using the provided organization ID or slug and version number.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            version (string): version

        Returns:
            list[Any]: Success

        Tags:
            Releases
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if version is None:
            raise ValueError("Missing required parameter 'version'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/releases/{version}/files/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_a_project_s_release_files(
        self, organization_id_or_slug, project_id_or_slug, version
    ) -> list[Any]:
        """
        Get a list of files associated with a specific release version for a project within an organization.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            version (string): version

        Returns:
            list[Any]: Success

        Tags:
            Releases
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        if version is None:
            raise ValueError("Missing required parameter 'version'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/releases/{version}/files/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_an_organization_release_s_file(
        self, organization_id_or_slug, version, file_id, download=None
    ) -> dict[str, Any]:
        """
        Retrieves a file from a release in an organization using the provided organization ID or slug, version, and file ID, optionally allowing for file download.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            version (string): version
            file_id (string): file_id
            download (boolean): Indicates whether to initiate a file download when the request is made; set to true to enable download, false otherwise.

        Returns:
            dict[str, Any]: Success

        Tags:
            Releases
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if version is None:
            raise ValueError("Missing required parameter 'version'")
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/releases/{version}/files/{file_id}/"
        query_params = {k: v for k, v in [("download", download)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_an_organization_release_file(
        self, organization_id_or_slug, version, file_id, name=None, dist=None
    ) -> dict[str, Any]:
        """
        Updates a file with the specified ID in a release of an organization using the provided JSON data.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            version (string): version
            file_id (string): file_id
            name (string): The new name (full path) of the file.
            dist (string): The new name of the dist.
                Example:
                ```json
                {
                  "name": "/demo/goodbye.txt"
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Releases
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if version is None:
            raise ValueError("Missing required parameter 'version'")
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'")
        request_body = {
            "name": name,
            "dist": dist,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/releases/{version}/files/{file_id}/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_an_organization_release_s_file(
        self, organization_id_or_slug, version, file_id
    ) -> Any:
        """
        Deletes a specific file associated with a release in an organization using the provided organization ID or slug, version, and file ID.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            version (string): version
            file_id (string): file_id

        Returns:
            Any: Success

        Tags:
            Releases
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if version is None:
            raise ValueError("Missing required parameter 'version'")
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/releases/{version}/files/{file_id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_a_project_release_s_file(
        self,
        organization_id_or_slug,
        project_id_or_slug,
        version,
        file_id,
        download=None,
    ) -> dict[str, Any]:
        """
        Retrieves a specific file from a project release using the "GET" method, requiring organization ID or slug, project ID or slug, version, and file ID, and optionally allows for a download option via query parameter.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            version (string): version
            file_id (string): file_id
            download (boolean): Indicates whether the file should be returned as a downloadable resource or not.

        Returns:
            dict[str, Any]: Success

        Tags:
            Releases
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        if version is None:
            raise ValueError("Missing required parameter 'version'")
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/releases/{version}/files/{file_id}/"
        query_params = {k: v for k, v in [("download", download)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_a_project_release_file(
        self,
        organization_id_or_slug,
        project_id_or_slug,
        version,
        file_id,
        name=None,
        dist=None,
    ) -> dict[str, Any]:
        """
        Updates a specific file associated with a project release using the provided JSON data.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            version (string): version
            file_id (string): file_id
            name (string): The new name (full path) of the file.
            dist (string): The new name of the dist.
                Example:
                ```json
                {
                  "name": "/demo/goodbye.txt"
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Releases
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        if version is None:
            raise ValueError("Missing required parameter 'version'")
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'")
        request_body = {
            "name": name,
            "dist": dist,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/releases/{version}/files/{file_id}/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_a_project_release_s_file(
        self, organization_id_or_slug, project_id_or_slug, version, file_id
    ) -> Any:
        """
        Deletes a specific file from a release version in a project using the organization and project identifiers.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            version (string): version
            file_id (string): file_id

        Returns:
            Any: Success

        Tags:
            Releases
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        if version is None:
            raise ValueError("Missing required parameter 'version'")
        if file_id is None:
            raise ValueError("Missing required parameter 'file_id'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/releases/{version}/files/{file_id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_an_organization_release_s_commits(
        self, organization_id_or_slug, version
    ) -> list[Any]:
        """
        Retrieves a list of commits for a specific version within an organization using the provided organization ID or slug and version number.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            version (string): version

        Returns:
            list[Any]: Success

        Tags:
            Releases
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if version is None:
            raise ValueError("Missing required parameter 'version'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/releases/{version}/commits/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_a_project_release_s_commits(
        self, organization_id_or_slug, project_id_or_slug, version
    ) -> list[Any]:
        """
        Get the list of commits associated with a specific release version in a project within an organization.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            project_id_or_slug (string): project_id_or_slug
            version (string): version

        Returns:
            list[Any]: Success

        Tags:
            Releases
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if project_id_or_slug is None:
            raise ValueError("Missing required parameter 'project_id_or_slug'")
        if version is None:
            raise ValueError("Missing required parameter 'version'")
        url = f"{self.base_url}/api/0/projects/{organization_id_or_slug}/{project_id_or_slug}/releases/{version}/commits/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_files_changed_in_a_release_s_commits(
        self, organization_id_or_slug, version
    ) -> Any:
        """
        Retrieves a list of commit files for a specific release version within an organization, identified by its ID or slug.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            version (string): version

        Returns:
            Any: Success

        Tags:
            Releases
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if version is None:
            raise ValueError("Missing required parameter 'version'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/releases/{version}/commitfiles/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_a_release_s_deploys(self, organization_id_or_slug, version) -> list[Any]:
        """
        Retrieves deployment information for a specific release version within an organization.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            version (string): version

        Returns:
            list[Any]: Success

        Tags:
            Releases
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if version is None:
            raise ValueError("Missing required parameter 'version'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/releases/{version}/deploys/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_a_new_deploy_for_an_organization(
        self,
        organization_id_or_slug,
        version,
        environment=None,
        url=None,
        name=None,
        projects=None,
        dateStarted=None,
        dateFinished=None,
    ) -> dict[str, Any]:
        """
        Records a new deployment of a specific release version for an organization identified by its ID or slug and returns status codes indicating success, conflict, or error.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            version (string): version
            environment (string): The environment you're deploying to.
            url (string): The optional URL that points to the deploy.
            name (string): The optional name of the deploy.
            projects (array): The optional list of projects to deploy.
            dateStarted (string): An optional date that indicates when the deploy started.
            dateFinished (string): An optional date that indicates when the deploy ended. If not provided, the current time is used.
                Example:
                ```json
                {
                  "environment": "prod"
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Releases
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        if version is None:
            raise ValueError("Missing required parameter 'version'")
        request_body = {
            "environment": environment,
            "url": url,
            "name": name,
            "projects": projects,
            "dateStarted": dateStarted,
            "dateFinished": dateFinished,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/releases/{version}/deploys/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_organization_integration_installations(
        self, organization_id_or_slug
    ) -> list[Any]:
        """
        Retrieves a list of Sentry app installations for a specified organization using the organization ID or slug.

        Args:
            organization_id_or_slug (string): organization_id_or_slug

        Returns:
            list[Any]: Success

        Tags:
            Integration
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/sentry-app-installations/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_or_update_an_external_issue(
        self, uuid, issueId, webUrl, project, identifier
    ) -> dict[str, Any]:
        """
        Creates or updates an external issue linked to a Sentry issue using the integration platform integration specified by the `uuid` path parameter, requiring authentication with a token having the `event:write` scope.

        Args:
            uuid (string): uuid
            issueId (integer): The ID of the Sentry issue to link the external issue to.
            webUrl (string): The URL of the external service to link the issue to.
            project (string): The external service's project.
            identifier (string): A unique identifier of the external issue.
                Example:
                ```json
                {
                  "issueId": 1,
                  "webUrl": "https://somerandom.io/project/issue-id",
                  "project": "ExternalProj",
                  "identifier": "issue-1"
                }
                ```

        Returns:
            dict[str, Any]: Success

        Tags:
            Integration
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        request_body = {
            "issueId": issueId,
            "webUrl": webUrl,
            "project": project,
            "identifier": identifier,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/sentry-app-installations/{uuid}/external-issues/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_an_external_issue(self, uuid, external_issue_id) -> Any:
        """
        Deletes an external issue associated with a specific integration installation in Sentry, requiring authentication with the `event:admin` scope.

        Args:
            uuid (string): uuid
            external_issue_id (string): external_issue_id

        Returns:
            Any: Success

        Tags:
            Integration
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        if external_issue_id is None:
            raise ValueError("Missing required parameter 'external_issue_id'")
        url = f"{self.base_url}/api/0/sentry-app-installations/{uuid}/external-issues/{external_issue_id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def enable_spike_protection(self, organization_id_or_slug, projects) -> Any:
        """
        Creates a new spike protection for an organization using the provided JSON data and returns a status message, requiring authentication with permissions to read, write, or administer projects.

        Args:
            organization_id_or_slug (string): organization_id_or_slug
            projects (array): Slugs of projects to enable Spike Protection for. Set to `$all` to enable Spike Protection for all the projects in the organization.

        Returns:
            Any: Success

        Tags:
            Projects
        """
        if organization_id_or_slug is None:
            raise ValueError("Missing required parameter 'organization_id_or_slug'")
        request_body = {
            "projects": projects,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/0/organizations/{organization_id_or_slug}/spike-protections/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_an_issue_s_events(
        self,
        issue_id,
        start=None,
        end=None,
        statsPeriod=None,
        environment=None,
        full=None,
        sample=None,
        query=None,
    ) -> list[Any]:
        """
        Retrieves a list of events associated with a specific issue, optionally filtered by date range, environment, and other query parameters.

        Args:
            issue_id (string): issue_id
            start (string): The "start" query parameter is a string used to specify the starting point or cursor for paginating through the list of events for a given issue.
            end (string): Specifies the end timestamp for filtering events, typically used in combination with other query parameters to limit the range of events returned.
            statsPeriod (string): Specifies the time period for which to retrieve event statistics, with possible values such as "24h", "14d", or an empty string; defaults to "24h" if not provided[2][3][5].
            environment (array): Specifies the environments to filter the events for a given issue, allowing multiple values as an array.
            full (boolean): Indicates whether to retrieve a full set of events for the specified issue, with true including additional details and false returning a basic set.
            sample (boolean): Indicates whether to sample events, accepting true or false values.
            query (string): A free-text string used to filter events for a specific issue by applying a custom query.

        Returns:
            list[Any]: API response data.

        Tags:
            Events
        """
        if issue_id is None:
            raise ValueError("Missing required parameter 'issue_id'")
        url = f"{self.base_url}/api/0/issues/{issue_id}/events/"
        query_params = {
            k: v
            for k, v in [
                ("start", start),
                ("end", end),
                ("statsPeriod", statsPeriod),
                ("environment", environment),
                ("full", full),
                ("sample", sample),
                ("query", query),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_an_issue_event(
        self, issue_id, event_id, environment=None
    ) -> dict[str, Any]:
        """
        Retrieves event details for a specific event within an issue using the provided issue ID and event ID, optionally filtered by environment.

        Args:
            issue_id (string): issue_id
            event_id (string): event_id
            environment (array): Array of environment identifiers to filter events by specific environments.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Events
        """
        if issue_id is None:
            raise ValueError("Missing required parameter 'issue_id'")
        if event_id is None:
            raise ValueError("Missing required parameter 'event_id'")
        url = f"{self.base_url}/api/0/issues/{issue_id}/events/{event_id}/"
        query_params = {
            k: v for k, v in [("environment", environment)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_tag_details(self, issue_id, key, environment=None) -> dict[str, Any]:
        """
        Retrieves a tag for a specific issue based on the provided key, with optional filtering by environment.

        Args:
            issue_id (string): issue_id
            key (string): key
            environment (array): A list of environment contexts where the tag should be applied, typically used to filter or specify the relevant settings for the tag linked to the issue.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            Events
        """
        if issue_id is None:
            raise ValueError("Missing required parameter 'issue_id'")
        if key is None:
            raise ValueError("Missing required parameter 'key'")
        url = f"{self.base_url}/api/0/issues/{issue_id}/tags/{key}/"
        query_params = {
            k: v for k, v in [("environment", environment)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_a_tag_s_values_for_an_issue(
        self, issue_id, key, sort=None, environment=None
    ) -> list[Any]:
        """
        Retrieves a list of values for a specific tag key associated with an issue, allowing optional sorting and filtering by environment.

        Args:
            issue_id (string): issue_id
            key (string): key
            sort (string): Sorts the API response by a specified attribute, which can be one of the following: age, count, date, or id.
            environment (array): A list of environment names to filter the tag values for the specified issue.

        Returns:
            list[Any]: API response data.

        Tags:
            Events
        """
        if issue_id is None:
            raise ValueError("Missing required parameter 'issue_id'")
        if key is None:
            raise ValueError("Missing required parameter 'key'")
        url = f"{self.base_url}/api/0/issues/{issue_id}/tags/{key}/values/"
        query_params = {
            k: v
            for k, v in [("sort", sort), ("environment", environment)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [
            self.list_your_organizations,
            self.retrieve_an_organization,
            self.update_an_organization,
            self.list_an_organization_s_metric_alert_rules,
            self.create_organization_metric_alert_rule,
            self.get_organization_metric_alert_rule,
            self.update_a_metric_alert_rule,
            self.delete_a_metric_alert_rule,
            self.get_metric_alert_rule_activations,
            self.get_integration_provider_information,
            self.list_an_organization_s_custom_dashboards,
            self.create_a_new_dashboard_for_an_organization,
            self.retrieve_an_organization_s_custom_dashboard,
            self.edit_an_organization_s_custom_dashboard,
            self.delete_an_organization_s_custom_dashboard,
            self.list_an_organization_s_discover_saved_queries,
            self.create_a_new_saved_query,
            self.retrieve_an_organization_s_discover_saved_query,
            self.edit_organization_discover_saved_query,
            self.delete_organization_discover_saved_query,
            self.list_an_organization_s_environments,
            self.query_discover_events_in_table_format,
            self.create_an_external_user,
            self.update_an_external_user,
            self.delete_an_external_user,
            self.list_organization_available_integrations,
            self.get_organization_integration,
            self.delete_organization_integration,
            self.list_an_organization_s_members,
            self.add_a_member_to_an_organization,
            self.retrieve_an_organization_member,
            self.update_an_organization_member_s_roles,
            self.delete_an_organization_member,
            self.add_an_organization_member_to_a_team,
            self.update_an_organization_member_s_team_role,
            self.delete_an_organization_member_from_a_team,
            self.retrieve_monitors_for_an_organization,
            self.create_a_monitor,
            self.retrieve_a_monitor,
            self.update_a_monitor,
            self.delete_a_monitor_or_monitor_environments,
            self.retrieve_check_ins_for_a_monitor,
            self.list_spike_protection_notifications,
            self.create_spike_protection_notification,
            self.retrieve_a_spike_protection_notification_action,
            self.update_a_spike_protection_notification_action,
            self.delete_a_spike_protection_notification_action,
            self.list_an_organization_s_projects,
            self.list_an_organization_s_trusted_relays,
            self.get_release_threshold_statuses,
            self.retrieve_an_organization_s_release,
            self.update_an_organization_s_release,
            self.delete_an_organization_s_release,
            self.retrieve_a_count_of_replays,
            self.list_an_organization_s_selectors,
            self.list_an_organization_s_replays,
            self.retrieve_a_replay_instance,
            self.list_an_organization_s_paginated_teams,
            self.provision_a_new_team,
            self.query_an_individual_team,
            self.update_a_team_s_attributes,
            self.delete_an_individual_team,
            self.list_an_organization_s_scim_members,
            self.provision_a_new_organization_member,
            self.query_an_individual_organization_member,
            self.update_an_organization_member_s_attributes,
            self.delete_an_organization_member_via_scim,
            self.retrieve_release_health_session_statistics,
            self.get_organization_events_count_by_project,
            self.get_organization_event_counts_v2,
            self.list_an_organization_s_teams,
            self.create_a_new_team,
            self.list_a_user_s_teams_for_an_organization,
            self.retrieve_a_project,
            self.update_a_project,
            self.delete_a_project,
            self.list_a_project_s_environments,
            self.retrieve_a_project_environment,
            self.update_a_project_environment,
            self.list_a_project_s_error_events,
            self.debug_event_source_maps,
            self.list_a_project_s_data_filters,
            self.update_an_inbound_data_filter,
            self.list_a_project_s_client_keys,
            self.create_a_new_client_key,
            self.retrieve_a_client_key,
            self.update_a_client_key,
            self.delete_a_client_key,
            self.list_a_project_s_organization_members,
            self.retrieve_a_monitor_for_a_project,
            self.update_a_monitor_for_a_project,
            self.delete_project_monitor_or_environments,
            self.retrieve_check_ins_for_a_monitor_by_project,
            self.get_project_ownership_config,
            self.update_project_ownership_config,
            self.delete_a_replay_instance,
            self.list_clicked_nodes,
            self.list_recording_segments,
            self.retrieve_a_recording_segment,
            self.list_users_who_have_viewed_a_replay,
            self.list_a_project_s_issue_alert_rules,
            self.create_an_issue_alert_rule_for_a_project,
            self.retrieve_an_issue_alert_rule_for_a_project,
            self.update_an_issue_alert_rule,
            self.delete_an_issue_alert_rule,
            self.retrieve_a_project_s_symbol_sources,
            self.add_a_symbol_source_to_a_project,
            self.update_a_project_s_symbol_source,
            self.delete_a_symbol_source_from_a_project,
            self.list_a_project_s_teams,
            self.add_a_team_to_a_project,
            self.delete_a_team_from_a_project,
            self.retrieve_a_team,
            self.update_a_team,
            self.delete_a_team,
            self.create_an_external_team,
            self.update_an_external_team,
            self.delete_an_external_team,
            self.list_a_team_s_members,
            self.list_a_team_s_projects,
            self.create_a_new_project,
            self.list_user_emails,
            self.add_a_secondary_email_address,
            self.update_a_primary_email_address,
            self.remove_an_email_address,
            self.retrieve_event_counts_for_a_team,
            self.resolve_an_event_id,
            self.list_an_organization_s_repositories,
            self.list_a_repository_s_commits,
            self.resolve_a_short_id,
            self.list_your_projects,
            self.list_project_debug_files,
            self.delete_project_debug_file,
            self.list_a_project_s_users,
            self.list_a_tag_s_values,
            self.retrieve_event_counts_for_a_project,
            self.list_a_project_s_user_feedback,
            self.submit_user_feedback,
            self.list_a_project_s_service_hooks,
            self.register_a_new_service_hook,
            self.retrieve_a_service_hook,
            self.update_a_service_hook,
            self.remove_a_service_hook,
            self.retrieve_an_event_for_a_project,
            self.list_project_issues,
            self.bulk_mutate_a_list_of_issues,
            self.bulk_remove_a_list_of_issues,
            self.list_a_tag_s_values_related_to_an_issue,
            self.list_an_issue_s_hashes,
            self.retrieve_an_issue,
            self.update_an_issue,
            self.remove_an_issue,
            self.list_an_organization_s_releases,
            self.create_a_new_release_for_an_organization,
            self.list_an_organization_s_release_files,
            self.list_a_project_s_release_files,
            self.retrieve_an_organization_release_s_file,
            self.update_an_organization_release_file,
            self.delete_an_organization_release_s_file,
            self.retrieve_a_project_release_s_file,
            self.update_a_project_release_file,
            self.delete_a_project_release_s_file,
            self.list_an_organization_release_s_commits,
            self.list_a_project_release_s_commits,
            self.retrieve_files_changed_in_a_release_s_commits,
            self.list_a_release_s_deploys,
            self.create_a_new_deploy_for_an_organization,
            self.list_organization_integration_installations,
            self.create_or_update_an_external_issue,
            self.delete_an_external_issue,
            self.enable_spike_protection,
            self.list_an_issue_s_events,
            self.retrieve_an_issue_event,
            self.retrieve_tag_details,
            self.list_a_tag_s_values_for_an_issue,
        ]
