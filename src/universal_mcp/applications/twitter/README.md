---
name: twitter
description: Twitter API integration with essential day-to-day functions.
---

# Twitter Integration

Twitter API integration with essential day-to-day functions.

## Available Tools

| Tool | Description |
|------|-------------|
| `create_tweet` | Posts a new tweet with text, media, polls, or as a reply/quote. Supports various tweet formats including replies, quotes, media attachments, and polls with customizable visibility settings. |
| `delete_tweet` | Permanently deletes a specific tweet by its unique ID on behalf of the authenticated user. This action cannot be undone and removes the tweet from all timelines. |
| `get_tweet` | Retrieves detailed information for a single tweet by its unique ID with customizable fields. Allows fetching tweet metrics, media details, author information, and more. |
| `search_recent_tweets` | Searches for tweets from the past seven days matching a specific query with filtering and pagination. Supports advanced Twitter search operators for precise results. NOTE: This endpoint requires elevated Twitter API access (Pro/Enterprise tier). |
| `get_authenticated_user` | Retrieves detailed information about the currently authenticated user making the API request. Returns profile data for the account whose credentials are being used. |
| `get_user_by_username` | Retrieves detailed profile information for a specific user by their username (handle). Fetches public profile data and optionally includes pinned tweets and metrics. |
| `get_user_by_id` | Retrieves detailed profile information for a specific user by their unique user ID. Fetches public profile data and optionally includes pinned tweets and metrics. |
| `get_user_tweets` | Retrieves tweets authored by a specific user in reverse chronological order with filtering options. Fetches original tweets, retweets, and replies based on exclude parameters. |
| `get_user_mentions` | Retrieves tweets mentioning a specific user in reverse chronological order with time-based filtering. Finds all tweets that mention the user's @username. |
| `get_liked_tweets` | Retrieves tweets liked by a specific user in reverse chronological order with pagination. Shows the user's like history with customizable field selections. |
| `retweet` | Causes the authenticated user to retweet a specific tweet by its ID. Shares the tweet to the user's followers and appears on their timeline. |
| `unretweet` | Removes a retweet from the authenticated user's timeline. Reverses a previous retweet action and removes it from the user's profile. |
| `get_retweeters` | Retrieves a list of users who retweeted a specific tweet with pagination support. Shows who amplified the tweet with customizable user field selections. |
| `get_liking_users` | Retrieves a list of users who liked a specific tweet with pagination support. Shows who engaged with the tweet through likes with customizable user fields. |
| `follow_user` | Causes the authenticated user to follow another user by their user ID. Creates a following relationship and adds the target to the user's following list. |
| `unfollow_user` | Causes the authenticated user to unfollow another user by their user ID. Removes the following relationship and stops seeing their tweets in the timeline. |
| `bookmark_tweet` | Bookmarks a specific tweet for the authenticated user for later reference. Saves the tweet to the user's private bookmarks collection. |
| `remove_bookmark` | Removes a bookmarked tweet from the authenticated user's bookmarks collection. Reverses a previous bookmark action and removes the saved tweet. |
| `get_bookmarks` | Retrieves all bookmarked tweets for the authenticated user with pagination support. Shows the user's saved tweets with customizable field selections. |
| `create_list` | Creates a new Twitter list with customizable name, description, and privacy settings. Allows organizing users into curated groups for focused timelines. |
| `get_list` | Retrieves detailed information for a specific Twitter list by its unique ID. Fetches list metadata including name, description, owner, and member count. |
| `get_list_tweets` | Retrieves tweets from a specific Twitter list's timeline in reverse chronological order. Shows tweets from all list members with pagination and customizable fields. |
