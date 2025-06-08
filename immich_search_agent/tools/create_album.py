import os
from ..helpers.call_immich import call_immich

def create_album(name: str, description: str, photo_ids: list[str]):
    """
    Create an album in the Immich database.

    Args:
        name (str): The name of the album.
        description (str): The description of the album.
        photo_ids (list[str]): The IDs of the photos to add to the album.

    Returns:
        dict: status and result or error msg.
    """
    response_data = call_immich(
      "/api/albums", "POST", {"albumName": name, "description": description, "photoIds": photo_ids})
    if (response_data["status"] == "success"):
        return {"status": "success", "result": response_data}
    else:
        return {"status": "error", "error_message": response_data["error_message"]}
