import pytest
from universal_mcp.applications.utils import app_from_slug
from universal_mcp.utils.testing import check_application_instance

ALL_APPS = [
    "ahrefs",
    "airtable",
    "apollo",
    "asana",
    "aws_s3",
    "bill",  # not seeded
    "box",
    "braze",
    # "cal_com_v2",   # not seeded
    "calendly",
    "canva",
    "clickup",
    "coda",
    "confluence",  # not seeded
    "contentful",  # not seeded
    "crustdata",
    "dialpad",  # not seeded
    "digitalocean",
    "domain_checker",
    "e2b",
    "elevenlabs",
    "exa",
    "falai",
    "figma",
    "file_system",
    "firecrawl",
    "fireflies",
    "fpl",
    "ghost_content",
    "github",
    "gong",
    "google_calendar",
    "google_docs",
    "google_drive",
    "google_gemini",
    "google_mail",
    "google_searchconsole",
    "google_sheet",
    "hashnode",
    "heygen",
    "http_tools",
    "hubspot",
    "jira",
    "klaviyo",
    "linkedin",
    "mailchimp",
    "markitdown",
    "miro",
    "ms_teams",
    "neon",
    "notion",
    "openai",
    "outlook",
    "perplexity",
    "pipedrive",  # not seeded
    "posthog",
    "reddit",
    "resend",
    "retell",
    "rocketlane",
    "scraper",
    "semanticscholar",
    "semrush",  # not seeded
    "sendgrid",
    "sentry",
    "serpapi",
    "sharepoint",  # not seeded
    "shopify",
    "shortcut",
    "slack",  # not seeded
    "spotify",
    "supabase",
    "tavily",
    "trello",
    "twilio",
    "twitter",
    "unipile",
    "whatsapp",
    "whatsapp_business",
    "wrike",  # not seeded
    "yahoo_finance",
    "youtube",
    "zenquotes",
]


@pytest.mark.parametrize("app_name", ALL_APPS)
def test_application(app_name):
    app_class = app_from_slug(app_name)
    app_instance = app_class(integration=None)
    check_application_instance(app_instance, app_name)
