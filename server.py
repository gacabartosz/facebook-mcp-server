import logging
from mcp.server.fastmcp import FastMCP
from manager import Manager
from config import validate_config
from typing import Any

logging.basicConfig(level=logging.INFO, format="%(name)s %(levelname)s: %(message)s")

validate_config()

mcp = FastMCP("FacebookMCP")
manager = Manager()


@mcp.tool()
def post_to_facebook(message: str) -> dict[str, Any]:
    """Create a new text post on the Facebook Page."""
    return manager.post_to_facebook(message)


@mcp.tool()
def reply_to_comment(comment_id: str, message: str) -> dict[str, Any]:
    """Reply to a specific comment on a Facebook post."""
    return manager.reply_to_comment(comment_id, message)


@mcp.tool()
def get_page_posts() -> dict[str, Any]:
    """Fetch the most recent posts from the Page."""
    return manager.get_page_posts()


@mcp.tool()
def get_post_comments(post_id: str) -> dict[str, Any]:
    """Retrieve all comments for a given post."""
    return manager.get_post_comments(post_id)


@mcp.tool()
def delete_post(post_id: str) -> dict[str, Any]:
    """Delete a specific post from the Facebook Page."""
    return manager.delete_post(post_id)


@mcp.tool()
def delete_comment(comment_id: str) -> dict[str, Any]:
    """Delete a specific comment by its ID."""
    return manager.delete_comment(comment_id)


@mcp.tool()
def hide_comment(comment_id: str) -> dict[str, Any]:
    """Hide a comment from public view."""
    return manager.hide_comment(comment_id)


@mcp.tool()
def unhide_comment(comment_id: str) -> dict[str, Any]:
    """Unhide a previously hidden comment."""
    return manager.unhide_comment(comment_id)


@mcp.tool()
def filter_negative_comments(comments: dict[str, Any]) -> list[dict[str, Any]]:
    """Filter comments for basic negative sentiment using keyword matching."""
    return manager.filter_negative_comments(comments)


@mcp.tool()
def get_number_of_comments(post_id: str) -> int:
    """Count the number of comments on a given post."""
    return manager.get_number_of_comments(post_id)


@mcp.tool()
def get_number_of_likes(post_id: str) -> int:
    """Return the total number of likes on a post."""
    return manager.get_number_of_likes(post_id)


@mcp.tool()
def get_post_insights(post_id: str) -> dict[str, Any]:
    """Fetch all insights metrics (impressions, reactions, clicks, engagement) for a post."""
    return manager.get_post_insights(post_id)


@mcp.tool()
def get_post_impressions(post_id: str) -> dict[str, Any]:
    """Fetch total impressions of a post."""
    return manager.get_post_impressions(post_id)


@mcp.tool()
def get_post_impressions_unique(post_id: str) -> dict[str, Any]:
    """Fetch unique impressions (reach) of a post."""
    return manager.get_post_impressions_unique(post_id)


@mcp.tool()
def get_post_impressions_paid(post_id: str) -> dict[str, Any]:
    """Fetch paid impressions of a post."""
    return manager.get_post_impressions_paid(post_id)


@mcp.tool()
def get_post_impressions_organic(post_id: str) -> dict[str, Any]:
    """Fetch organic impressions of a post."""
    return manager.get_post_impressions_organic(post_id)


@mcp.tool()
def get_post_engaged_users(post_id: str) -> dict[str, Any]:
    """Fetch number of unique users who engaged with a post."""
    return manager.get_post_engaged_users(post_id)


@mcp.tool()
def get_post_clicks(post_id: str) -> dict[str, Any]:
    """Fetch total number of clicks on a post."""
    return manager.get_post_clicks(post_id)


@mcp.tool()
def get_post_reactions_like_total(post_id: str) -> dict[str, Any]:
    """Fetch total 'Like' reactions on a post."""
    return manager.get_post_reactions_like_total(post_id)


@mcp.tool()
def get_post_reactions_love_total(post_id: str) -> dict[str, Any]:
    """Fetch total 'Love' reactions on a post."""
    return manager.get_post_reactions_love_total(post_id)


@mcp.tool()
def get_post_reactions_wow_total(post_id: str) -> dict[str, Any]:
    """Fetch total 'Wow' reactions on a post."""
    return manager.get_post_reactions_wow_total(post_id)


@mcp.tool()
def get_post_reactions_haha_total(post_id: str) -> dict[str, Any]:
    """Fetch total 'Haha' reactions on a post."""
    return manager.get_post_reactions_haha_total(post_id)


@mcp.tool()
def get_post_reactions_sorry_total(post_id: str) -> dict[str, Any]:
    """Fetch total 'Sorry/Sad' reactions on a post."""
    return manager.get_post_reactions_sorry_total(post_id)


@mcp.tool()
def get_post_reactions_anger_total(post_id: str) -> dict[str, Any]:
    """Fetch total 'Angry' reactions on a post."""
    return manager.get_post_reactions_anger_total(post_id)


@mcp.tool()
def get_post_top_commenters(post_id: str) -> list[dict[str, Any]]:
    """Get the most active commenters on a post, sorted by comment count."""
    return manager.get_post_top_commenters(post_id)


@mcp.tool()
def post_image_to_facebook(image_url: str, caption: str) -> dict[str, Any]:
    """Post an image with a caption to the Facebook Page."""
    return manager.post_image_to_facebook(image_url, caption)


@mcp.tool()
def send_dm_to_user(user_id: str, message: str) -> dict[str, Any]:
    """Send a direct message to a user via Messenger."""
    return manager.send_dm_to_user(user_id, message)


@mcp.tool()
def update_post(post_id: str, new_message: str) -> dict[str, Any]:
    """Update the message text of an existing post."""
    return manager.update_post(post_id, new_message)


@mcp.tool()
def schedule_post(message: str, publish_time: int) -> dict[str, Any]:
    """Schedule a post for future publication. publish_time is a Unix timestamp."""
    return manager.schedule_post(message, publish_time)


@mcp.tool()
def get_page_fan_count() -> int:
    """Get the Page's total fan/follower count."""
    return manager.get_page_fan_count()


@mcp.tool()
def get_post_share_count(post_id: str) -> int:
    """Get the number of shares for a post."""
    return manager.get_post_share_count(post_id)


@mcp.tool()
def get_post_reactions_breakdown(post_id: str) -> dict[str, Any]:
    """Get all reaction type counts for a post in a single call."""
    return manager.get_post_reactions_breakdown(post_id)


@mcp.tool()
def bulk_delete_comments(comment_ids: list[str]) -> list[dict[str, Any]]:
    """Delete multiple comments by their IDs. Returns per-comment success/failure."""
    return manager.bulk_delete_comments(comment_ids)


@mcp.tool()
def bulk_hide_comments(comment_ids: list[str]) -> list[dict[str, Any]]:
    """Hide multiple comments by their IDs. Returns per-comment success/failure."""
    return manager.bulk_hide_comments(comment_ids)


if __name__ == "__main__":
    mcp.run()
