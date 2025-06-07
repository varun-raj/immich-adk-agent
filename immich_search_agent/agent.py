from dotenv import load_dotenv
from google.adk.agents import Agent

from .tools.search_photos import search_photos
from .tools.get_statistics import get_statistics

# Dotenv
load_dotenv()

root_agent = Agent(
    name="immich_search_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to search for photos in the Immich database."
    ),
    instruction=(
        "You are a helpful agent who can search and find photos and perform actions on them in the Immich database." 
    ),
    tools=[search_photos, get_statistics],
)