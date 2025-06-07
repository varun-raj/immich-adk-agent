import os
import requests

def call_immich(path: str, params: dict):
    """
    Call the Immich API to get the photos or perform actions on the photos.
    """
    immich_url = os.getenv("IMMICH_URL")
    immich_api_key = os.getenv("IMMICH_API_KEY")

    headers = {
        "x-api-key": immich_api_key
    }

    response = requests.get(immich_url + path, headers=headers, params=params)
    if (response.status_code == 200):
        response_data = response.json()
        return {"status": "success", "result": response_data}
    else:
        return {"status": "error", "error_message": response.text}