import os
import importlib
import inspect

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


def app_from_slug(slug: str):
    """
    Load an app class from its slug.

    Args:
        slug: The app slug (e.g., "google_mail")

    Returns:
        The app class or None if not found
    """
    try:
        # Convert slug to class name (e.g., google_mail -> GoogleMailApp)
        class_name = ''.join(word.capitalize() for word in slug.split('_')) + 'App'

        # Import the module
        module = importlib.import_module(f'universal_mcp.applications.{slug}')

        # Get the class
        app_class = getattr(module, class_name)
        return app_class
    except Exception as e:
        print(f"Error loading app {slug}: {e}")
        return None


def extract_class_docstring(app_class) -> str | None:
    """
    Extract the class docstring and normalize it for YAML.
    Gets the docstring from the class itself, not inherited.

    Returns:
        Single-line description or None
    """
    try:
        # Get docstring directly from __doc__ to avoid inheritance
        docstring = app_class.__doc__
        if docstring:
            # Clean up and join into single line for YAML
            docstring = inspect.cleandoc(docstring)
            docstring = ' '.join(docstring.split())
            return docstring
        return None
    except Exception as e:
        print(f"Error extracting class docstring: {e}")
        return None


def extract_tool_methods(app_instance) -> list[dict[str, str]]:
    """
    Extract tool methods by calling list_tools().

    Returns:
        List of dicts with 'name' and 'description' keys
    """
    try:
        # Get the list of tools
        tools_list = app_instance.list_tools()

        # Extract tool information
        tools = []
        for tool_method in tools_list:
            name = tool_method.__name__
            docstring = inspect.getdoc(tool_method)

            if docstring:
                # Extract first line/paragraph as description
                description = docstring.split('\n\n')[0].strip()
                # Remove extra whitespace
                description = ' '.join(description.split())
                tools.append({
                    'name': name,
                    'description': description
                })

        return tools
    except Exception as e:
        print(f"Error extracting tool methods: {e}")
        return []


def generate_readme(slug: str, output_path: str):
    """
    Generate README.md in agentskills format.
    """
    # Load app class
    app_class = app_from_slug(slug)
    if not app_class:
        print(f"Could not load app class for {slug}")
        return

    # Initialize app with integration=None
    app_instance = app_class(integration=None)

    # Extract class docstring for description
    description = extract_class_docstring(app_class)
    if not description:
        print(f"Could not extract docstring for {slug}")
        return

    # Extract tool methods
    tools = extract_tool_methods(app_instance)

    # Convert app slug to kebab-case for skill name
    skill_name = slug.replace('_', '-')

    # Get class name for title
    class_name = app_class.__name__

    # Generate README content
    readme_content = f"""---
name: {skill_name}
description: {description}
---

# {class_name.replace('App', ' Integration')}

{description}

## Available Tools

"""

    # Add tool reference table
    if tools:
        readme_content += "| Tool | Description |\n"
        readme_content += "|------|-------------|\n"
        for tool in tools:
            readme_content += f"| `{tool['name']}` | {tool['description']} |\n"
    else:
        readme_content += "No tools found.\n"

    # Write README.md
    with open(output_path, 'w') as f:
        f.write(readme_content)

    print(f"Generated README.md for {slug}")


def create_skill_symlink(readme_path: str):
    """
    Create SKILL.md as a symlink to README.md
    """
    skill_path = readme_path.replace('README.md', 'SKILL.md')

    # Remove existing symlink or file
    if os.path.exists(skill_path) or os.path.islink(skill_path):
        os.remove(skill_path)

    # Create symlink
    os.symlink('README.md', skill_path)
    print(f"Created symlink: SKILL.md -> README.md")


def main():
    """
    Runs the readme generation for a predefined list of applications.
    """
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "universal_mcp", "applications"))

    for app_slug in APPS:
        readme_path = os.path.join(base_path, app_slug, "README.md")

        try:
            # Generate README.md
            generate_readme(app_slug, readme_path)

            # Create SKILL.md symlink
            create_skill_symlink(readme_path)

        except Exception as e:
            print(f"Error processing {app_slug}: {e}")


if __name__ == "__main__":
    main()
