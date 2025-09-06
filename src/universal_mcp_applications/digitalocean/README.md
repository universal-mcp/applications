# DigitaloceanApp MCP Server

An MCP Server for the DigitaloceanApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the DigitaloceanApp API.


| Tool | Description |
|------|-------------|
| `one_clicks_list` | List 1-Click Applications |
| `one_clicks_install_kubernetes` | Install Kubernetes 1-Click Applications |
| `account_get` | Get User Information |
| `ssh_keys_list` | List All SSH Keys |
| `ssh_keys_create` | Create a New SSH Key |
| `ssh_keys_get` | Retrieve an Existing SSH Key |
| `ssh_keys_update` | Update an SSH Key's Name |
| `ssh_keys_delete` | Delete an SSH Key |
| `actions_list` | List All Actions |
| `actions_get` | Retrieve an Existing Action |
| `apps_list` | List All Apps |
| `apps_create` | Create a New App |
| `apps_delete` | Delete an App |
| `apps_get` | Retrieve an Existing App |
| `apps_update` | Update an App |
| `apps_restart` | Restart an App |
| `get_app_component_logs` | Retrieve Active Deployment Logs |
| `get_component_execution_details` | Retrieve Exec URL |
| `apps_get_instances` | Retrieve App Instances |
| `apps_list_deployments` | List App Deployments |
| `apps_create_deployment` | Create an App Deployment |
| `apps_get_deployment` | Retrieve an App Deployment |
| `apps_cancel_deployment` | Cancel a Deployment |
| `apps_get_logs` | Retrieve Deployment Logs |
| `apps_get_logs_aggregate` | Retrieve Aggregate Deployment Logs |
| `apps_get_exec` | Retrieve Exec URL for Deployment |
| `get_app_logs` | Retrieve Active Deployment Aggregate Logs |
| `apps_list_instance_sizes` | List Instance Sizes |
| `apps_get_instance_size` | Retrieve an Instance Size |
| `apps_list_regions` | List App Regions |
| `apps_validate_app_spec` | Propose an App Spec |
| `apps_list_alerts` | List all app alerts |
| `apps_assign_alert_destinations` | Update destinations for alerts |
| `apps_create_rollback` | Rollback App |
| `apps_validate_rollback` | Validate App Rollback |
| `apps_commit_rollback` | Commit App Rollback |
| `apps_revert_rollback` | Revert App Rollback |
| `get_app_bandwidth_daily` | Retrieve App Daily Bandwidth Metrics |
| `create_daily_bandwidth_metrics` | Retrieve Multiple Apps' Daily Bandwidth Metrics |
| `apps_get_health` | Retrieve App Health |
| `cdn_list_endpoints` | List All CDN Endpoints |
| `cdn_create_endpoint` | Create a New CDN Endpoint |
| `cdn_get_endpoint` | Retrieve an Existing CDN Endpoint |
| `cdn_update_endpoints` | Update a CDN Endpoint |
| `cdn_delete_endpoint` | Delete a CDN Endpoint |
| `cdn_purge_cache` | Purge the Cache for an Existing CDN Endpoint |
| `certificates_list` | List All Certificates |
| `certificates_create` | Create a New Certificate |
| `certificates_get` | Retrieve an Existing Certificate |
| `certificates_delete` | Delete a Certificate |
| `balance_get` | Get Customer Balance |
| `billing_history_list` | List Billing History |
| `invoices_list` | List All Invoices |
| `invoices_get_by_uuid` | Retrieve an Invoice by UUID |
| `invoices_get_csv_by_uuid` | Retrieve an Invoice CSV by UUID |
| `invoices_get_pdf_by_uuid` | Retrieve an Invoice PDF by UUID |
| `invoices_get_summary_by_uuid` | Retrieve an Invoice Summary by UUID |
| `databases_list_options` | List Database Options |
| `databases_list_clusters` | List All Database Clusters |
| `databases_create_cluster` | Create a New Database Cluster |
| `databases_get_cluster` | Retrieve an Existing Database Cluster |
| `databases_destroy_cluster` | Destroy a Database Cluster |
| `databases_get_config` | Retrieve an Existing Database Cluster Configuration |
| `databases_patch_config` | Update the Database Configuration for an Existing Database |
| `databases_get_ca` | Retrieve the Public Certificate |
| `databases_get_migration_status` | Retrieve the Status of an Online Migration |
| `start_online_migration` | Start an Online Migration |
| `delete_online_migration_by_id` | Stop an Online Migration |
| `databases_update_region` | Migrate a Database Cluster to a New Region |
| `databases_update_cluster_size` | Resize a Database Cluster |
| `databases_list_firewall_rules` | List Firewall Rules (Trusted Sources) for a Database Cluster |
| `update_database_cluster_firewall` | Update Firewall Rules (Trusted Sources) for a Database |
| `update_database_maintenance` | Configure a Database Cluster's Maintenance Window |
| `databases_install_update` | Start Database Maintenance |
| `databases_list_backups` | List Backups for a Database Cluster |
| `databases_list_replicas` | List All Read-only Replicas |
| `databases_create_replica` | Create a Read-only Replica |
| `databases_list_events_logs` | List all Events Logs |
| `databases_get_replica` | Retrieve an Existing Read-only Replica |
| `databases_destroy_replica` | Destroy a Read-only Replica |
| `databases_promote_replica` | Promote a Read-only Replica to become a Primary Cluster |
| `databases_list_users` | List all Database Users |
| `databases_add_user` | Add a Database User |
| `databases_get_user` | Retrieve an Existing Database User |
| `databases_delete_user` | Remove a Database User |
| `databases_update_user` | Update a Database User |
| `databases_reset_auth` | Reset a Database User's Password or Authentication Method |
| `databases_list` | List All Databases |
| `databases_add` | Add a New Database |
| `databases_get` | Retrieve an Existing Database |
| `databases_delete` | Delete a Database |
| `databases_list_connection_pools` | List Connection Pools (PostgreSQL) |
| `databases_add_connection_pool` | Add a New Connection Pool (PostgreSQL) |
| `databases_get_connection_pool` | Retrieve Existing Connection Pool (PostgreSQL) |
| `update_database_pool` | Update Connection Pools (PostgreSQL) |
| `delete_pool` | Delete a Connection Pool (PostgreSQL) |
| `databases_get_eviction_policy` | Retrieve the Eviction Policy for a Redis or Valkey Cluster |
| `update_eviction_policy` | Configure the Eviction Policy for a Redis or Valkey Cluster |
| `databases_get_sql_mode` | Retrieve the SQL Modes for a MySQL Cluster |
| `databases_update_sql_mode` | Update SQL Mode for a Cluster |
| `databases_update_major_version` | Upgrade Major Version for a Database |
| `databases_list_kafka_topics` | List Topics for a Kafka Cluster |
| `databases_create_kafka_topic` | Create Topic for a Kafka Cluster |
| `databases_get_kafka_topic` | Get Topic for a Kafka Cluster |
| `databases_update_kafka_topic` | Update Topic for a Kafka Cluster |
| `databases_delete_kafka_topic` | Delete Topic for a Kafka Cluster |
| `databases_list_logsink` | List Logsinks for a Database Cluster |
| `databases_create_logsink` | Create Logsink for a Database Cluster |
| `databases_get_logsink` | Get Logsink for a Database Cluster |
| `databases_update_logsink` | Update Logsink for a Database Cluster |
| `databases_delete_logsink` | Delete Logsink for a Database Cluster |
| `get_database_metrics_credentials` | Retrieve Database Clusters' Metrics Endpoint Credentials |
| `update_database_credentials` | Update Database Clusters' Metrics Endpoint Credentials |
| `list_database_indexes` | List Indexes for a OpenSearch Cluster |
| `delete_database_index_by_name` | Delete Index for OpenSearch Cluster |
| `domains_list` | List All Domains |
| `domains_create` | Create a New Domain |
| `domains_get` | Retrieve an Existing Domain |
| `domains_delete` | Delete a Domain |
| `domains_list_records` | List All Domain Records |
| `domains_create_record` | Create a New Domain Record |
| `domains_get_record` | Retrieve an Existing Domain Record |
| `domains_patch_record` | Update a Domain Record |
| `domains_update_record` | Update a Domain Record |
| `domains_delete_record` | Delete a Domain Record |
| `droplets_list` | List All Droplets |
| `droplets_create` | Create a New Droplet |
| `droplets_destroy_by_tag` | Deleting Droplets by Tag |
| `droplets_get` | Retrieve an Existing Droplet |
| `droplets_destroy` | Delete an Existing Droplet |
| `droplets_list_backups` | List Backups for a Droplet |
| `droplets_get_backup_policy` | Retrieve the Backup Policy for an Existing Droplet |
| `droplets_list_backup_policies` | List Backup Policies for All Existing Droplets |
| `list_supported_policies` | List Supported Droplet Backup Policies |
| `droplets_list_snapshots` | List Snapshots for a Droplet |
| `droplet_actions_list` | List Actions for a Droplet |
| `droplet_actions_post` | Initiate a Droplet Action |
| `droplet_actions_post_by_tag` | Acting on Tagged Droplets |
| `droplet_actions_get` | Retrieve a Droplet Action |
| `droplets_list_kernels` | List All Available Kernels for a Droplet |
| `droplets_list_firewalls` | List all Firewalls Applied to a Droplet |
| `droplets_list_neighbors` | List Neighbors for a Droplet |
| `destroy_droplet_with_resources` | List Associated Resources for a Droplet |
| `destroy_select` | Selectively Destroy a Droplet and its Associated Resources |
| `delete_droplet_resources` | Destroy a Droplet and All of its Associated Resources (Dangerous) |
| `get_droplet_status` | Check Status of a Droplet Destroy with Associated Resources Request |
| `retry_droplet_with_resources` | Retry a Droplet Destroy with Associated Resources Request |
| `autoscalepools_list` | List All Autoscale Pools |
| `autoscalepools_create` | Create a New Autoscale Pool |
| `autoscalepools_get` | Retrieve an Existing Autoscale Pool |
| `autoscalepools_update` | Update Autoscale Pool |
| `autoscalepools_delete` | Delete autoscale pool |
| `delete_autoscale_pool_dangerously` | Delete autoscale pool and resources |
| `autoscalepools_list_members` | List members |
| `autoscalepools_list_history` | List history events |
| `firewalls_list` | List All Firewalls |
| `firewalls_create` | Create a New Firewall |
| `firewalls_get` | Retrieve an Existing Firewall |
| `firewalls_update` | Update a Firewall |
| `firewalls_delete` | Delete a Firewall |
| `firewalls_assign_droplets` | Add Droplets to a Firewall |
| `firewalls_delete_droplets` | Remove Droplets from a Firewall |
| `firewalls_add_tags` | Add Tags to a Firewall |
| `firewalls_delete_tags` | Remove Tags from a Firewall |
| `firewalls_add_rules` | Add Rules to a Firewall |
| `firewalls_delete_rules` | Remove Rules from a Firewall |
| `floating_ips_list` | List All Floating IPs |
| `floating_ips_create` | Create a New Floating IP |
| `floating_ips_get` | Retrieve an Existing Floating IP |
| `floating_ips_delete` | Delete a Floating IP |
| `floating_ips_action_list` | List All Actions for a Floating IP |
| `floating_ips_action_post` | Initiate a Floating IP Action |
| `floating_ips_action_get` | Retrieve an Existing Floating IP Action |
| `functions_list_namespaces` | List Namespaces |
| `functions_create_namespace` | Create Namespace |
| `functions_get_namespace` | Get Namespace |
| `functions_delete_namespace` | Delete Namespace |
| `functions_list_triggers` | List Triggers |
| `functions_create_trigger` | Create Trigger |
| `functions_get_trigger` | Get Trigger |
| `functions_update_trigger` | Update Trigger |
| `functions_delete_trigger` | Delete Trigger |
| `images_list` | List All Images |
| `images_create_custom` | Create a Custom Image |
| `images_get` | Retrieve an Existing Image |
| `images_update` | Update an Image |
| `images_delete` | Delete an Image |
| `image_actions_list` | List All Actions for an Image |
| `image_actions_post` | Initiate an Image Action |
| `image_actions_get` | Retrieve an Existing Action |
| `kubernetes_list_clusters` | List All Kubernetes Clusters |
| `kubernetes_create_cluster` | Create a New Kubernetes Cluster |
| `kubernetes_get_cluster` | Retrieve an Existing Kubernetes Cluster |
| `kubernetes_update_cluster` | Update a Kubernetes Cluster |
| `kubernetes_delete_cluster` | Delete a Kubernetes Cluster |
| `destroy_cluster_resources` | List Associated Resources for Cluster Deletion |
| `delete_cluster_resources` | Selectively Delete a Cluster and its Associated Resources |
| `destroy_cluster_with_resources` | Delete a Cluster and All of its Associated Resources (Dangerous) |
| `kubernetes_get_kubeconfig` | Retrieve the kubeconfig for a Kubernetes Cluster |
| `kubernetes_get_credentials` | Retrieve Credentials for a Kubernetes Cluster |
| `get_cluster_upgrades` | Retrieve Available Upgrades for an Existing Kubernetes Cluster |
| `kubernetes_upgrade_cluster` | Upgrade a Kubernetes Cluster |
| `kubernetes_list_node_pools` | List All Node Pools in a Kubernetes Clusters |
| `kubernetes_add_node_pool` | Add a Node Pool to a Kubernetes Cluster |
| `kubernetes_get_node_pool` | Retrieve a Node Pool for a Kubernetes Cluster |
| `kubernetes_update_node_pool` | Update a Node Pool in a Kubernetes Cluster |
| `kubernetes_delete_node_pool` | Delete a Node Pool in a Kubernetes Cluster |
| `kubernetes_delete_node` | Delete a Node in a Kubernetes Cluster |
| `kubernetes_recycle_node_pool` | Recycle a Kubernetes Node Pool |
| `kubernetes_get_cluster_user` | Retrieve User Information for a Kubernetes Cluster |
| `kubernetes_list_options` | List Available Regions, Node Sizes, and Versions of Kubernetes |
| `kubernetes_run_cluster_lint` | Run Clusterlint Checks on a Kubernetes Cluster |
| `get_cluster_lint` | Fetch Clusterlint Diagnostics for a Kubernetes Cluster |
| `kubernetes_add_registry` | Add Container Registry to Kubernetes Clusters |
| `kubernetes_remove_registry` | Remove Container Registry from Kubernetes Clusters |
| `kubernetes_get_status_messages` | Fetch Status Messages for a Kubernetes Cluster |
| `load_balancers_create` | Create a New Load Balancer |
| `load_balancers_list` | List All Load Balancers |
| `load_balancers_get` | Retrieve an Existing Load Balancer |
| `load_balancers_update` | Update a Load Balancer |
| `load_balancers_delete` | Delete a Load Balancer |
| `load_balancers_delete_cache` | Delete a Global Load Balancer CDN Cache |
| `load_balancers_add_droplets` | Add Droplets to a Load Balancer |
| `load_balancers_remove_droplets` | Remove Droplets from a Load Balancer |
| `add_forwarding_rule` | Add Forwarding Rules to a Load Balancer |
| `delete_lb_forwarding_rules` | Remove Forwarding Rules from a Load Balancer |
| `monitoring_list_alert_policy` | List Alert Policies |
| `monitoring_create_alert_policy` | Create Alert Policy |
| `monitoring_get_alert_policy` | Retrieve an Existing Alert Policy |
| `monitoring_update_alert_policy` | Update an Alert Policy |
| `monitoring_delete_alert_policy` | Delete an Alert Policy |
| `get_droplet_bandwidth_metrics` | Get Droplet Bandwidth Metrics |
| `get_droplet_cpu_metrics` | Get Droplet CPU Metrics |
| `get_droplet_filesystem_free` | Get Droplet Filesystem Free Metrics |
| `get_droplet_filesystem_size` | Get Droplet Filesystem Size Metrics |
| `get_droplet_load_metrics` | Get Droplet Load1 Metrics |
| `get_droplet_load5_metrics` | Get Droplet Load5 Metrics |
| `get_droplet_load_metric` | Get Droplet Load15 Metrics |
| `get_droplet_memory_cached` | Get Droplet Cached Memory Metrics |
| `get_droplet_memory_free` | Get Droplet Free Memory Metrics |
| `get_droplet_memory_total` | Get Droplet Total Memory Metrics |
| `get_droplet_memory_available` | Get Droplet Available Memory Metrics |
| `get_app_memory_percentage` | Get App Memory Percentage Metrics |
| `get_app_cpu_metrics` | Get App CPU Percentage Metrics |
| `get_app_restart_count` | Get App Restart Count Metrics |
| `get_frontend_connections` | Get Load Balancer Frontend Total Current Active Connections Metrics |
| `get_lb_frontend_connections_limit` | Get Load Balancer Frontend Max Connections Limit Metrics |
| `get_frontend_cpu_utilization` | Get Load Balancer Frontend Average Percentage CPU Utilization Metrics |
| `get_frontend_firewall_bytes` | Get Load Balancer Frontend Firewall Dropped Bytes Metrics |
| `get_lb_frontend_fw_dropped_pkts` | Get Load Balancer Frontend Firewall Dropped Packets Metrics |
| `get_load_balancer_responses` | Get Load Balancer Frontend HTTP Rate Of Response Code Metrics |
| `fetch_frontend_request_rate` | Get Load Balancer Frontend HTTP Requests Metrics |
| `get_frontend_network_throughput` | Get Load Balancer Frontend HTTP Throughput Metrics |
| `get_frontend_udp_throughput` | Get Load Balancer Frontend UDP Throughput Metrics |
| `get_frontend_tcp_throughput` | Get Load Balancer Frontend TCP Throughput Metrics |
| `get_frontend_nlb_tcp_throughput` | Get Network Load Balancer Frontend TCP Throughput Metrics |
| `get_nlb_udp_throughput` | Get Network Load Balancer Frontend UDP Throughput Metrics |
| `get_frontend_tls_connections` | Get Load Balancer Frontend Current TLS Connections Rate Metrics |
| `get_frontend_tls_connections_limit` | Get Load Balancer Frontend Max TLS Connections Limit Metrics |
| `get_tls_exceeding_rate_limit` | Get Load Balancer Frontend Closed TLS Connections For Exceeded Rate Limit Metrics |
| `get_droplet_session_duration_avg` | Get Load Balancer Droplets Average HTTP Session Duration Metrics |
| `get_droplet_session_duration_50p` | Get Load Balancer Droplets 50th Percentile HTTP Session Duration Metrics |
| `get_droplet_session_duration_95p` | Get Load Balancer Droplets 95th Percentile HTTP Session Duration Metrics |
| `get_droplet_response_time` | Get Load Balancer Droplets Average HTTP Response Time Metrics |
| `get_droplet_http_response_time` | Get Load Balancer Droplets 50th Percentile HTTP Response Time Metrics |
| `get_droplets_http_response_timep_95p` | Get Load Balancer Droplets 95th Percentile HTTP Response Time Metrics |
| `get_droplets_http_response_timep_99p` | Get Load Balancer Droplets 99th Percentile HTTP Response Time Metrics |
| `get_droplet_queue_size` | Get Load Balancer Droplets Queue Size Metrics |
| `get_droplet_responses` | Get Load Balancer Droplets HTTP Rate Of Response Code Metrics |
| `get_droplet_connections` | Get Load Balancer Droplets Active Connections Metrics |
| `get_droplet_health_checks` | Get Load Balancer Droplets Health Check Status Metrics |
| `get_load_balancer_downtime` | Get Load Balancer Droplets Downtime Status Metrics |
| `get_current_autoscale_instances` | Get Droplet Autoscale Pool Current Size |
| `list_target_instances` | Get Droplet Autoscale Pool Target Size |
| `get_droplet_cpu_utilization` | Get Droplet Autoscale Pool Current Average CPU utilization |
| `get_droplet_target_cpu_utilization` | Get Droplet Autoscale Pool Target Average CPU utilization |
| `get_droplet_memory_utilization` | Get Droplet Autoscale Pool Current Average Memory utilization |
| `get_autoscale_memory_target` | Get Droplet Autoscale Pool Target Average Memory utilization |
| `monitoring_create_destination` | Create Logging Destination |
| `monitoring_list_destinations` | List Logging Destinations |
| `monitoring_get_destination` | Get Logging Destination |
| `monitoring_update_destination` | Update Logging Destination |
| `monitoring_delete_destination` | Delete Logging Destination |
| `monitoring_create_sink` | Create Sink |
| `monitoring_list_sinks` | Lists all sinks |
| `monitoring_get_sink` | Get Sink |
| `monitoring_delete_sink` | Delete Sink |
| `partner_attachments_list` | List all partner attachments |
| `partner_attachments_create` | Create a new partner attachment |
| `partner_attachments_get` | Retrieve an existing partner attachment |
| `partner_attachments_patch` | Update an existing partner attachment |
| `partner_attachments_delete` | Delete an existing partner attachment |
| `get_bgp_auth_key_by_pa_id` | Get current BGP auth key for the partner attachment |
| `get_partner_network_remote_routes` | List remote routes for a partner attachment |
| `update_remote_routes` | Set remote routes for a partner attachment |
| `get_partner_service_key` | Get the current service key for the partner attachment |
| `create_service_key` | Regenerate the service key for the partner attachment |
| `projects_list` | List All Projects |
| `projects_create` | Create a Project |
| `projects_get_default` | Retrieve the Default Project |
| `projects_update_default` | Update the Default Project |
| `projects_patch_default` | Patch the Default Project |
| `projects_get` | Retrieve an Existing Project |
| `projects_update` | Update a Project |
| `projects_patch` | Patch a Project |
| `projects_delete` | Delete an Existing Project |
| `projects_list_resources` | List Project Resources |
| `projects_assign_resources` | Assign Resources to a Project |
| `list_project_resources` | List Default Project Resources |
| `create_default_project_resource` | Assign Resources to Default Project |
| `regions_list` | List All Data Center Regions |
| `registry_get` | Get Container Registry Information |
| `registry_create` | Create Container Registry |
| `registry_delete` | Delete Container Registry |
| `registry_get_subscription` | Get Subscription Information |
| `registry_update_subscription` | Update Subscription Tier |
| `registry_get_docker_credentials` | Get Docker Credentials for Container Registry |
| `registry_validate_name` | Validate a Container Registry Name |
| `registry_list_repositories` | List All Container Registry Repositories |
| `registry_list_repositories_v` | List All Container Registry Repositories (V2) |
| `registry_list_repository_tags` | List All Container Registry Repository Tags |
| `registry_delete_repository_tag` | Delete Container Registry Repository Tag |
| `get_repository_digests` | List All Container Registry Repository Manifests |
| `delete_manifest_digest` | Delete Container Registry Repository Manifest |
| `registry_run_garbage_collection` | Start Garbage Collection |
| `registry_get_garbage_collection` | Get Active Garbage Collection |
| `list_registry_garbage_collections` | List Garbage Collections |
| `update_garbage_collection` | Update Garbage Collection |
| `registry_get_options` | List Registry Options (Subscription Tiers and Available Regions) |
| `droplets_list_neighbors_ids` | List All Droplet Neighbors |
| `reserved_ips_list` | List All Reserved IPs |
| `reserved_ips_create` | Create a New Reserved IP |
| `reserved_ips_get` | Retrieve an Existing Reserved IP |
| `reserved_ips_delete` | Delete a Reserved IP |
| `reserved_ips_actions_list` | List All Actions for a Reserved IP |
| `reserved_ips_actions_post` | Initiate a Reserved IP Action |
| `reserved_ips_actions_get` | Retrieve an Existing Reserved IP Action |
| `reserved_ipv_list` | [Public Preview] List All Reserved IPv6s |
| `reserved_ipv_create` | [Public Preview] Create a New Reserved IPv6 |
| `reserved_ipv_get` | [Public Preview] Retrieve an Existing Reserved IPv6 |
| `reserved_ipv_delete` | [Public Preview] Delete a Reserved IPv6 |
| `reserved_ipv_actions_post` | [Public Preview] Initiate a Reserved IPv6 Action |
| `sizes_list` | List All Droplet Sizes |
| `snapshots_list` | List All Snapshots |
| `snapshots_get` | Retrieve an Existing Snapshot |
| `snapshots_delete` | Delete a Snapshot |
| `spaces_key_list` | List Spaces Access Keys |
| `spaces_key_create` | Create a New Spaces Access Key |
| `spaces_key_get` | Get a Spaces Access Key |
| `spaces_key_delete` | Delete a Spaces Access Key |
| `spaces_key_update` | Update Spaces Access Keys |
| `spaces_key_patch` | Update Spaces Access Keys |
| `tags_list` | List All Tags |
| `tags_create` | Create a New Tag |
| `tags_get` | Retrieve a Tag |
| `tags_delete` | Delete a Tag |
| `tags_assign_resources` | Tag a Resource |
| `tags_unassign_resources` | Untag a Resource |
| `volumes_list` | List All Block Storage Volumes |
| `volumes_create` | Create a New Block Storage Volume |
| `volumes_delete_by_name` | Delete a Block Storage Volume by Name |
| `volume_actions_post` | Initiate A Block Storage Action By Volume Name |
| `volume_snapshots_get_by_id` | Retrieve an Existing Volume Snapshot |
| `volume_snapshots_delete_by_id` | Delete a Volume Snapshot |
| `volumes_get` | Retrieve an Existing Block Storage Volume |
| `volumes_delete` | Delete a Block Storage Volume |
| `volume_actions_list` | List All Actions for a Volume |
| `volume_actions_post_by_id` | Initiate A Block Storage Action By Volume Id |
| `volume_actions_get` | Retrieve an Existing Volume Action |
| `volume_snapshots_list` | List Snapshots for a Volume |
| `volume_snapshots_create` | Create Snapshot from a Volume |
| `vpcs_list` | List All VPCs |
| `vpcs_create` | Create a New VPC |
| `vpcs_get` | Retrieve an Existing VPC |
| `vpcs_update` | Update a VPC |
| `vpcs_patch` | Partially Update a VPC |
| `vpcs_delete` | Delete a VPC |
| `vpcs_list_members` | List the Member Resources of a VPC |
| `vpcs_list_peerings` | List the Peerings of a VPC |
| `vpcs_create_peerings` | Create a Peering with a VPC |
| `vpcs_patch_peerings` | Update a VPC Peering |
| `vpc_peerings_list` | List All VPC Peerings |
| `vpc_peerings_create` | Create a New VPC Peering |
| `vpc_peerings_get` | Retrieve an Existing VPC Peering |
| `vpc_peerings_patch` | Update a VPC peering |
| `vpc_peerings_delete` | Delete a VPC peering |
| `uptime_list_checks` | List All Checks |
| `uptime_create_check` | Create a New Check |
| `uptime_get_check` | Retrieve an Existing Check |
| `uptime_update_check` | Update a Check |
| `uptime_delete_check` | Delete a Check |
| `uptime_get_check_state` | Retrieve Check State |
| `uptime_list_alerts` | List All Alerts |
| `uptime_create_alert` | Create a New Alert |
| `uptime_get_alert` | Retrieve an Existing Alert |
| `uptime_update_alert` | Update an Alert |
| `uptime_delete_alert` | Delete an Alert |
| `genai_list_agents` | List Agents |
| `genai_create_agent` | Create an Agent |
| `genai_list_agent_api_keys` | List Agent API Keys |
| `genai_create_agent_api_key` | Create an Agent API Key |
| `genai_update_agent_api_key` | Update API Key for an Agent |
| `genai_delete_agent_api_key` | Delete API Key for an Agent |
| `genai_regenerate_agent_api_key` | Regenerate API Key for an Agent |
| `genai_attach_agent_function` | Add Function Route to an Agent |
| `genai_update_agent_function` | Update Function Route for an Agent |
| `genai_detach_agent_function` | Delete Function Route for an Agent |
| `genai_attach_knowledge_bases` | Attach Knowledge Bases to an Agent |
| `genai_attach_knowledge_base` | Attach Knowledge Base to an Agent |
| `genai_detach_knowledge_base` | Detach Knowledge Base from an Agent |
| `genai_attach_agent` | Add Agent Route to an Agent |
| `genai_update_attached_agent` | Update Agent Route for an Agent |
| `genai_detach_agent` | Delete Agent Route for an Agent |
| `genai_get_agent` | Retrieve an Existing Agent |
| `genai_update_agent` | Update an Agent |
| `genai_delete_agent` | Delete an Agent |
| `genai_get_agent_children` | View Agent Routes |
| `update_deployment_visibility` | Update Agent Status |
| `genai_list_agent_versions` | List Agent Versions |
| `update_agent_version_by_uuid` | Rollback to Agent Version |
| `genai_list_anthropic_api_keys` | List Anthropic API Keys |
| `genai_create_anthropic_api_key` | Create Anthropic API Key |
| `genai_get_anthropic_api_key` | Get Anthropic API Key |
| `genai_update_anthropic_api_key` | Update Anthropic API Key |
| `genai_delete_anthropic_api_key` | Delete Anthropic API Key |
| `list_agents_by_key_uuid` | List agents by Anthropic key |
| `genai_list_indexing_jobs` | List Indexing Jobs for a Knowledge Base |
| `genai_create_indexing_job` | Start Indexing Job for a Knowledge Base |
| `list_job_data_sources` | List Data Sources for Indexing Job for a Knowledge Base |
| `genai_get_indexing_job` | Retrieve Status of Indexing Job for a Knowledge Base |
| `genai_cancel_indexing_job` | Cancel Indexing Job for a Knowledge Base |
| `genai_list_knowledge_bases` | List Knowledge Bases |
| `genai_create_knowledge_base` | Create a Knowledge Base |
| `list_data_source_by_knowledge_base` | List Data Sources for a Knowledge Base |
| `add_data_source` | Add Data Source to a Knowledge Base |
| `delete_data_source_by_uuid` | Delete a Data Source from a Knowledge Base |
| `genai_get_knowledge_base` | Retrieve Information About an Existing Knowledge Base |
| `genai_update_knowledge_base` | Update a Knowledge Base |
| `genai_delete_knowledge_base` | Delete a Knowledge Base |
| `genai_list_models` | List Available Models |
| `genai_list_model_api_keys` | List Model API Keys |
| `genai_create_model_api_key` | Create a Model API Key |
| `genai_update_model_api_key` | Update API Key for a Model |
| `genai_delete_model_api_key` | Delete API Key for a Model |
| `genai_regenerate_model_api_key` | Regenerate API Key for a Model |
| `genai_list_openai_api_keys` | List OpenAI API Keys |
| `genai_create_openai_api_key` | Create OpenAI API Key |
| `genai_get_openai_api_key` | Get OpenAI API Key |
| `genai_update_openai_api_key` | Update OpenAI API Key |
| `genai_delete_openai_api_key` | Delete OpenAI API Key |
| `get_agents_by_key_uuid` | List agents by OpenAI key |
| `genai_list_datacenter_regions` | List Datacenter Regions |
