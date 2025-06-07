import os
import requests


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
    """
    print("Immich search photos query: ##############")
    print(query)

    immich_url = os.getenv("IMMICH_URL")
    search_photos_url = immich_url + "/api/search/smart"
    search_photos_api_key = os.getenv("IMMICH_API_KEY")

    headers = {
      "x-api-key": search_photos_api_key
    }

    response = requests.post(search_photos_url, headers=headers, json={"query": query, "limit": 10})
    if (response.status_code == 200):
      response_data = response.json()
      assets = response_data["assets"]["items"]

      cleaned_photos_data = []
      for photo in assets:
        cleaned_photos_data.append({
          "id": photo["id"],
          "originalFileName": photo["originalFileName"],
          "url": immich_url + "/photos/" + photo["id"],
        })
        
      assets_data_markdown = "Here are the photos that match your search query:\n\n" 
      for photo in cleaned_photos_data:
        assets_data_markdown += f"### {photo['originalFileName']}\n\n"
        assets_data_markdown += f"[{photo['originalFileName']}]({photo['url']})\n\n"

      return {"status": "success", "result": assets_data_markdown}
    else:
        print("Immich search photos response: ##############")
        return {"status": "error", "error_message": response.text}