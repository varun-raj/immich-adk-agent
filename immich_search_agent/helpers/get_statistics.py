import os
import requests

def get_statistics() -> dict:
    """Gets the statistics of the immich server.

    Example:
    Number of photos, Usage by user, Photo usage, Video user uage, 

    Returns:
        dict: status and result or error msg.
    """
    immich_url = os.getenv("IMMICH_URL")
    get_statistics_url = immich_url + "/api/server/statistics"
    get_statistics_api_key = os.getenv("IMMICH_API_KEY")

    headers = {
        "x-api-key": get_statistics_api_key
    }

    response = requests.get(get_statistics_url, headers=headers)
    if (response.status_code == 200):
        response_data = response.json()
        return {"status": "success", "result": response_data}
    else:
        return {"status": "error", "error_message": response.text}
