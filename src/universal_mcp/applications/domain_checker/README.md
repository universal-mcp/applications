---
name: domain-checker
description: Base class for Universal MCP Applications.
---

# DomainChecker Integration

Base class for Universal MCP Applications.

## Available Tools

| Tool | Description |
|------|-------------|
| `check_domain_registration` | Determines a domain's availability by querying DNS and RDAP servers. For registered domains, it returns details like registrar and key dates. This function provides a comprehensive analysis for a single, fully qualified domain name, unlike `check_keyword_across_tlds_tool` which checks a keyword across multiple domains. |
| `find_available_domains_for_keyword` | Checks a keyword's availability across a predefined list of popular TLDs. Using DNS and RDAP lookups, it generates a summary report of available and taken domains. This bulk-check differs from `check_domain_registration`, which deeply analyzes a single, fully-qualified domain. |
