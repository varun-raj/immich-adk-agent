import os
import requests
from ..helpers.call_immich import call_immich

def get_statistics() -> dict:
    """Gets the statistics of the immich server.

    Example:
    Number of photos, Usage by user, Photo usage, Video user uage, 

    Returns:
        dict: status and result or error msg.
    """
    response_data = call_immich("/api/server/statistics", {})
    if (response_data["status"] == "success"):
        return {"status": "success", "result": response_data}
    else:
        return {"status": "error", "error_message": response_data["error_message"]}
