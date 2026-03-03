import os
import sys
from dotenv import load_dotenv

load_dotenv()

# Facebook Graph API setup
GRAPH_API_VERSION = "v22.0"
PAGE_ACCESS_TOKEN = os.getenv("FACEBOOK_ACCESS_TOKEN")
PAGE_ID = os.getenv("FACEBOOK_PAGE_ID")
GRAPH_API_BASE_URL = f"https://graph.facebook.com/{GRAPH_API_VERSION}"


def validate_config() -> None:
    """Validate required environment variables at startup."""
    missing = []
    if not PAGE_ACCESS_TOKEN:
        missing.append("FACEBOOK_ACCESS_TOKEN")
    if not PAGE_ID:
        missing.append("FACEBOOK_PAGE_ID")
    if missing:
        print(f"ERROR: Missing required environment variables: {', '.join(missing)}", file=sys.stderr)
        print("Create a .env file with FACEBOOK_ACCESS_TOKEN and FACEBOOK_PAGE_ID", file=sys.stderr)
        sys.exit(1)
