# Universal MCP Applications

**A collection of 80+ installable application wrappers for the Universal MCP framework.**

This package provides a unified collection of all individual Universal MCP applications. It allows you to install every available tool at once and use them either as Python libraries in your own code.

## Installation

It is recommended to use `uv` for faster installation.

```bash
# Recommended using uv
uv pip install universal-mcp-applications

# Or using standard pip
pip install universal-mcp-applications
```

## Usage

The primary way to use the tools in this package is give below :-

### 1. As a Library

Each application can be imported and used directly in your Python projects. This is useful for integrating with other scripts or building more complex workflows.

**Example:**

```python
from universal_mcp_applications.falai import FalaiApp
from universal_mcp.utils import process_output

# Instantiate the application
# You may need to provide credentials via an integration
app = FalaiApp() 

# Call a method
result = app.some_method(param1="value1")

# Process and print the output
process_output(result)
```

## Included Applications

This package includes the following 82 applications:

- `ahrefs`
- `airtable`
- `apollo`
- `asana`
- `aws-s3`
- `bill`
- `box`
- `braze`
- `cal-com-v2`
- `calendly`
- `canva`
- `clickup`
- `coda`
- `confluence`
- `contentful`
- `crustdata`
- `dialpad`
- `digitalocean`
- `domain-checker`
- `e2b`
- `elevenlabs`
- `exa`
- `falai`
- `figma`
- `firecrawl`
- `fireflies`
- `fpl`
- `ghost-content`
- `github`
- `gong`
- `google-ads`
- `google-calendar`
- `google-docs`
- `google-drive`
- `google-gemini`
- `google-mail`
- `google-searchconsole`
- `google-sheet`
- `hashnode`
- `heygen`
- `http-tools`
- `hubspot`
- `jira`
- `klaviyo`
- `linkedin`
- `mailchimp`
- `markitdown`
- `miro`
- `ms-teams`
- `neon`
- `notion`
- `openai`
- `outlook`
- `perplexity`
- `pipedrive`
- `posthog`
- `reddit`
- `replicate`
- `resend`
- `retell`
- `rocketlane`
- `semanticscholar`
- `semrush`
- `sendgrid`
- `sentry`
- `serpapi`
- `sharepoint`
- `shopify`
- `shortcut`
- `slack`
- `spotify`
- `supabase`
- `tavily`
- `trello`
- `twillo`
- `twitter`
- `unipile`
- `whatsapp`
- `whatsapp-business`
- `wrike`
- `youtube`
- `zenquotes`
