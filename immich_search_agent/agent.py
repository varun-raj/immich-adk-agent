from dotenv import load_dotenv
from google.adk.agents import Agent

from .tools.search_photos import search_photos
from .tools.get_statistics import get_statistics
from .tools.create_album import create_album

# Dotenv
load_dotenv()

root_agent = Agent(
    name="immich_search_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to search for photos in the Immich database."
    ),
    instruction=(
        """
        You are a helpful agent who can search and find photos and perform actions on them in the Immich database.
        Do not send raw data or json data to the user.
        Be concise and to the point.
        Be funny and engaging.
        When you know the tools to be used, dont ask the user for confirmation.
        """ 
    ),
    tools=[search_photos, get_statistics, create_album],
)