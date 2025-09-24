import os
import subprocess

APPS = [
    "ahrefs",
    "airtable",
    "apollo",
    "asana",
    "aws_s3",
    "bill",
    "box",
    "braze",
    "cal_com_v2",
    "calendly",
    "canva",
    "clickup",
    "coda",
    "confluence",
    "contentful",
    "crustdata",
    "dialpad",
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
    "pipedrive",
    "posthog",
    "reddit",
    "replicate",
    "resend",
    "retell",
    "rocketlane",
    "scraper",
    "semanticscholar",
    "semrush",
    "sendgrid",
    "sentry",
    "serpapi",
    "sharepoint",
    "shopify",
    "shortcut",
    "slack",
    "spotify",
    "supabase",
    "tavily",
    "trello",
    "twilio",
    "twitter",
    "unipile",
    "whatsapp",
    "whatsapp_business",
    "wrike",
    "youtube",
    "zenquotes",
]


def main():
    """
    Runs the readme generation for a predefined list of applications.
    """
    base_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "universal_mcp", "applications")
    )

    for app in APPS:
        app_path = os.path.join(base_path, app, "app.py")
        command = ["universal_mcp", "codegen", "readme", app_path]

        try:
            # Using 'uv run' to ensure the command is executed in the correct environment
            subprocess.run(
                ["uv", "run"] + command, check=True, capture_output=True, text=True
            )
            # print(result.stdout) # Optional: print stdout for more details
        except subprocess.CalledProcessError:
            pass
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    main()
