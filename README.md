# Facebook MCP Server

MCP server for managing a Facebook Page via the Graph API. Exposes tools for creating posts, moderating comments, fetching post insights, and filtering negative feedback — ready for Claude Desktop, Claude Code, or any MCP-compatible client.

[![Trust Score](https://archestra.ai/mcp-catalog/api/badge/quality/HagaiHen/facebook-mcp-server)](https://archestra.ai/mcp-catalog/hagaihen__facebook-mcp-server)
<a href="https://glama.ai/mcp/servers/@HagaiHen/facebook-mcp-server">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/@HagaiHen/facebook-mcp-server/badge" />
</a>

---

## What Is This?

An MCP server providing AI-callable tools that connect directly to a Facebook Page, abstracting Graph API operations as LLM-friendly functions.

### Benefits

- Automates **social media moderation and analytics** for Page managers
- Integrates with **Claude Desktop, Claude Code CLI, or any MCP client**
- Fine-grained control over Facebook content via natural language

---

## Features (33 tools)

| Tool | Description |
|------|-------------|
| `post_to_facebook` | Create a new text post on the Page |
| `reply_to_comment` | Reply to a specific comment |
| `get_page_posts` | Fetch recent posts from the Page |
| `get_post_comments` | Get all comments for a post |
| `delete_post` | Delete a post by ID |
| `delete_comment` | Delete a comment by ID |
| `hide_comment` | Hide a comment from public view |
| `unhide_comment` | Unhide a previously hidden comment |
| `filter_negative_comments` | Filter comments by negative sentiment keywords |
| `get_number_of_comments` | Count comments on a post |
| `get_number_of_likes` | Count likes on a post |
| `get_post_insights` | Get all insights metrics for a post |
| `get_post_impressions` | Total impressions |
| `get_post_impressions_unique` | Unique impressions (reach) |
| `get_post_impressions_paid` | Paid impressions |
| `get_post_impressions_organic` | Organic impressions |
| `get_post_engaged_users` | Unique engaged users |
| `get_post_clicks` | Total post clicks |
| `get_post_reactions_like_total` | Like reaction count |
| `get_post_reactions_love_total` | Love reaction count |
| `get_post_reactions_wow_total` | Wow reaction count |
| `get_post_reactions_haha_total` | Haha reaction count |
| `get_post_reactions_sorry_total` | Sorry/Sad reaction count |
| `get_post_reactions_anger_total` | Angry reaction count |
| `get_post_reactions_breakdown` | All reaction counts in one call |
| `get_post_top_commenters` | Top commenters sorted by count |
| `post_image_to_facebook` | Post an image with caption |
| `send_dm_to_user` | Send a DM via Messenger |
| `update_post` | Update an existing post's text |
| `schedule_post` | Schedule a post for future publication |
| `get_page_fan_count` | Total Page fan/follower count |
| `get_post_share_count` | Number of shares for a post |
| `bulk_delete_comments` | Delete multiple comments by ID |
| `bulk_hide_comments` | Hide multiple comments by ID |

---

## Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/gacabartosz/facebook-mcp-server.git
cd facebook-mcp-server
```

### 2. Install Dependencies

Using [uv](https://docs.astral.sh/uv/) (recommended):

```bash
uv pip install -r requirements.txt
```

Or with pip:

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

Copy the example env file and add your Facebook credentials:

```bash
cp .env.example .env
```

Edit `.env` with your values:

```
FACEBOOK_ACCESS_TOKEN=your_page_access_token
FACEBOOK_PAGE_ID=your_page_id
```

Get these from [Facebook Graph API Explorer](https://developers.facebook.com/tools/explorer).

---

## Usage

### Claude Desktop

Go to **Settings > Developer > Edit Config** and add:

```json
{
  "mcpServers": {
    "facebook-pages": {
      "command": "uv",
      "args": [
        "run",
        "--with", "mcp[cli]",
        "--with", "requests",
        "--with", "python-dotenv",
        "mcp", "run",
        "/absolute/path/to/facebook-mcp-server/server.py"
      ],
      "env": {
        "FACEBOOK_ACCESS_TOKEN": "your_token",
        "FACEBOOK_PAGE_ID": "your_page_id"
      }
    }
  }
}
```

### Claude Code CLI

Add to your project's `.claude/settings.json` or user settings:

```json
{
  "mcpServers": {
    "facebook-pages": {
      "command": "uv",
      "args": [
        "run",
        "/path/to/facebook-mcp-server/server.py"
      ],
      "env": {
        "FACEBOOK_ACCESS_TOKEN": "your_token",
        "FACEBOOK_PAGE_ID": "your_page_id"
      }
    }
  }
}
```

### Direct Execution

```bash
cd facebook-mcp-server
python server.py
```

The server communicates over stdio using the MCP protocol.

---

## Architecture

```
server.py          MCP tool definitions (FastMCP decorators)
  ├── manager.py   Business logic layer
  │   └── facebook_api.py   Facebook Graph API HTTP client
  └── config.py    Environment config & validation
```

- **Auth**: Uses `Authorization: Bearer` header (not URL params)
- **Error handling**: HTTP errors raise `FacebookAPIError` with status code and message
- **Startup validation**: Missing env vars fail fast with clear error message
- **Graph API**: v22.0

---

## Required Facebook Permissions

- `pages_manage_posts` — Create, update, delete posts
- `pages_read_engagement` — Read comments, likes, shares
- `pages_manage_engagement` — Reply to/delete/hide comments
- `pages_messaging` — Send DMs via Messenger
- `pages_read_user_content` — Read user comments
- `read_insights` — Access post insights/metrics

---

## Contributing

Contributions welcome! Fork the repo and submit a pull request.

```bash
git checkout -b feature/YourFeature
git commit -m 'feat: add new feature'
git push origin feature/YourFeature
```

---

## License

MIT License. Originally by [Hagai Hen](https://github.com/HagaiHen).
