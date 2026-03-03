import logging
import requests
from typing import Any
from config import GRAPH_API_BASE_URL, PAGE_ID, PAGE_ACCESS_TOKEN

logger = logging.getLogger("facebook-mcp")


class FacebookAPIError(Exception):
    """Raised when Facebook Graph API returns an error."""
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        super().__init__(f"Facebook API error ({status_code}): {message}")


class FacebookAPI:
    def _request(self, method: str, endpoint: str, params: dict[str, Any] | None = None, json: dict[str, Any] | None = None) -> dict[str, Any]:
        """Generic Graph API request with proper auth and error handling."""
        url = f"{GRAPH_API_BASE_URL}/{endpoint}"
        headers = {"Authorization": f"Bearer {PAGE_ACCESS_TOKEN}"}
        params = params or {}

        logger.debug("%s %s params=%s", method, endpoint, list(params.keys()))
        try:
            response = requests.request(method, url, params=params, json=json, headers=headers, timeout=30)
        except requests.RequestException as e:
            raise FacebookAPIError(0, f"Network error: {e}") from e

        if response.status_code >= 400:
            try:
                error_data = response.json().get("error", {})
                msg = error_data.get("message", response.text[:200])
            except ValueError:
                msg = response.text[:200]
            raise FacebookAPIError(response.status_code, msg)

        try:
            return response.json()
        except ValueError:
            raise FacebookAPIError(response.status_code, "Invalid JSON response")

    def post_message(self, message: str) -> dict[str, Any]:
        return self._request("POST", f"{PAGE_ID}/feed", {"message": message})

    def reply_to_comment(self, comment_id: str, message: str) -> dict[str, Any]:
        return self._request("POST", f"{comment_id}/comments", {"message": message})

    def get_posts(self) -> dict[str, Any]:
        return self._request("GET", f"{PAGE_ID}/posts", {"fields": "id,message,created_time,shares"})

    def get_comments(self, post_id: str) -> dict[str, Any]:
        return self._request("GET", f"{post_id}/comments", {"fields": "id,message,from,created_time"})

    def delete_post(self, post_id: str) -> dict[str, Any]:
        return self._request("DELETE", post_id)

    def delete_comment(self, comment_id: str) -> dict[str, Any]:
        return self._request("DELETE", comment_id)

    def hide_comment(self, comment_id: str) -> dict[str, Any]:
        return self._request("POST", comment_id, {"is_hidden": True})

    def unhide_comment(self, comment_id: str) -> dict[str, Any]:
        return self._request("POST", comment_id, {"is_hidden": False})

    def get_insights(self, post_id: str, metric: str, period: str = "lifetime") -> dict[str, Any]:
        return self._request("GET", f"{post_id}/insights", {"metric": metric, "period": period})

    def get_bulk_insights(self, post_id: str, metrics: list[str], period: str = "lifetime") -> dict[str, Any]:
        return self.get_insights(post_id, ",".join(metrics), period)

    def post_image_to_facebook(self, image_url: str, caption: str) -> dict[str, Any]:
        return self._request("POST", f"{PAGE_ID}/photos", {"url": image_url, "caption": caption})

    def send_dm_to_user(self, user_id: str, message: str) -> dict[str, Any]:
        payload = {
            "recipient": {"id": user_id},
            "message": {"text": message},
            "messaging_type": "RESPONSE",
        }
        return self._request("POST", "me/messages", json=payload)

    def update_post(self, post_id: str, new_message: str) -> dict[str, Any]:
        return self._request("POST", post_id, {"message": new_message})

    def schedule_post(self, message: str, publish_time: int) -> dict[str, Any]:
        return self._request("POST", f"{PAGE_ID}/feed", {
            "message": message,
            "published": False,
            "scheduled_publish_time": publish_time,
        })

    def get_page_fan_count(self) -> int:
        data = self._request("GET", PAGE_ID, {"fields": "fan_count"})
        return data.get("fan_count", 0)

    def get_post_share_count(self, post_id: str) -> int:
        data = self._request("GET", post_id, {"fields": "shares"})
        return data.get("shares", {}).get("count", 0)
