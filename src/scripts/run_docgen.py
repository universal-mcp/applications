
import os
import subprocess

APPS = [
    "aws_s3",
    "calendly",
    "canva",
    "domain_checker",
    "e2b",
    "elevenlabs",
    "exa",
    "falai",
    "file_system",
    "firecrawl",
    "fireflies",
    "fpl",
    "google_calendar",
    "google_docs",
    "google_drive",
    "google_searchconsole",
    "google_sheet",
    "http_tools",
    "linkedin",
    "ms_teams",
    "openai",
    "outlook",
    "replicate",
    "resend",
    "scraper",
    "serpapi",
    "sharepoint",
    "slack",
    "tavily",
    "twitter",
    "unipile",
    "whatsapp",
    "whatsapp_business",
    "youtube",
    "zenquotes",
]

def main():
    """
    Runs the docgen.py script for a predefined list of applications.
    """
    script_path = "src/scripts/docgen.py"
    base_path = "/Users/ankitranjan/Work/applications/src/universal_mcp/applications"
    
    for app in APPS:
        app_path = os.path.join(base_path, app, "app.py")
        command = ["python", script_path, app_path]
        
        print(f"Running docgen for: {app}")
        try:
            subprocess.run(command, check=True)
            print(f"Successfully generated docs for: {app}")
        except subprocess.CalledProcessError as e:
            print(f"Error generating docs for {app}: {e}")
        except FileNotFoundError:
            print(f"Error: Could not find app file for {app} at {app_path}")
        print("-" * 20)

if __name__ == "__main__":
    main()
