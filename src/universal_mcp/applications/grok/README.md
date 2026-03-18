---
name: grok
description: Grok (xAI) integration for AI-powered X/Twitter search and structured tweet data extraction using Grok's real-time x_search tool.
---

# Grok Integration

Grok (xAI) integration for AI-powered X/Twitter search and structured data extraction. Fetches recent tweets from X users using Grok's real-time x_search tool and returns clean, structured tweet data including engagement metrics, media presence, and thread context.

## Available Tools

| Tool | Description |
|------|-------------|
| `get_user_tweets` | Fetches the most recent tweets from one or more X (Twitter) users using Grok's x_search tool. Accepts a list of usernames, a maximum tweet count per user, and a Grok model name. Returns structured per-user results containing tweet content, URL, engagement metrics (likes, reposts, views), media presence, and thread context. |
