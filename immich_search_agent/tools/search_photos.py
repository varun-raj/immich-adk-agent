import os
import requests
from ..helpers.call_immich import call_immich

def search_photos(query: str, filters: dict) -> dict:
    """Searches for photos in the Immich database.

    Possible Filters
    size, 
    rating, 
    takenAfter, 
    takenBefore, 
    type (IMAGE, VIDEO, AUDIO, OTHER), 
    updatedAfter, 
    uploadedBefore,
    uploadedAfter,
    uploadedBefore,
    make,
    model,
    city,
    state,
    country


    Args:
        query (str): The search query for the photos.

    Returns:
        dict: status and result or error msg.
        result: list of photos with id, originalFileName, url
    """
    print("Immich search photos query: ##############")
    response_data = call_immich("/api/search/smart", "POST", {"query": query, "limit": 10})
    if (response_data["status"] == "success"):
      assets = response_data["result"]["assets"]["items"]

      cleaned_photos_data = []
      for photo in assets:
        cleaned_photos_data.append({
          "id": photo["id"],
          "originalFileName": photo["originalFileName"],
          "url": os.getenv("IMMICH_URL") + "/photos/" + photo["id"],
        })
        
      # assets_data_markdown = "Here are the photos that match your search query:\n\n" 
      # for photo in cleaned_photos_data:
      #   assets_data_markdown += f"name: {photo['originalFileName']}\n"
      #   assets_data_markdown += f"url: {photo['url']}\n\n"
      #   assets_data_markdown += f"id: {photo['id']}\n\n"

      return {"status": "success", "result": cleaned_photos_data}
    else:
        print("Immich search photos response: ##############")
        return {"status": "error", "error_message": response_data["error_message"]}