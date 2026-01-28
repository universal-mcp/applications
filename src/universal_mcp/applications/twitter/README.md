# Twitter MCP Application

A streamlined Twitter API integration with essential day-to-day functions for interacting with Twitter/X.

## Features

This application provides a focused set of the most commonly used Twitter API functions, organized by category:

### Tweet Operations
- **create_tweet** - Post tweets with text, media, polls, or as replies/quotes
- **delete_tweet** - Permanently delete a tweet
- **get_tweet** - Retrieve detailed tweet information
- **search_recent_tweets** - Search tweets from the past 7 days

### User Operations
- **get_authenticated_user** - Get the authenticated user's profile
- **get_user_by_username** - Look up user by username/handle
- **get_user_by_id** - Look up user by ID
- **search_users** - Search for users by query

### Timeline Operations
- **get_user_tweets** - Get tweets from a user's timeline
- **get_user_mentions** - Get tweets mentioning a user

### Social Interactions
- **like_tweet** / **unlike_tweet** - Like/unlike tweets
- **retweet** / **unretweet** - Retweet/unretweet tweets
- **get_liked_tweets** - Get tweets liked by a user
- **get_liking_users** - Get users who liked a tweet
- **get_retweeters** - Get users who retweeted a tweet

### Follow Operations
- **follow_user** / **unfollow_user** - Follow/unfollow users
- **get_followers** - Get a user's followers
- **get_following** - Get users a user is following

### Direct Messages
- **send_dm** - Send a direct message
- **get_dm_events** - Get DM conversations

### Bookmarks
- **bookmark_tweet** / **remove_bookmark** - Bookmark/unbookmark tweets
- **get_bookmarks** - Get bookmarked tweets

### Lists
- **create_list** - Create a new list
- **get_list** - Get list details
- **get_list_tweets** - Get tweets from a list

## Authentication

Requires Twitter API credentials configured through the integration system.

## Design Philosophy

This application focuses on the most common day-to-day Twitter operations, excluding:
- Streaming endpoints (firehose, compliance streams)
- Advanced analytics and metrics
- Spaces operations
- Trend tracking
- Compliance and batch operations

The goal is to provide a clean, focused API for typical Twitter interactions without the complexity of the full API surface.
