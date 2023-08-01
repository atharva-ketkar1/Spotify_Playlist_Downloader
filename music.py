from dotenv import load_dotenv
import os
from googleapiclient.discovery import build
import time

load_dotenv()

# Uses the Youtube API to search the playlist songs
class MusicApp:
    def __init__(self):
        self.youtube_key = os.getenv("YOUTUBE_KEY")
        self.cache = {}

    # Uses the specific required methods to fetch searches 
    def search_yt(self, query):
        if query in self.cache:
            return self.cache[query]

        youtube = build('youtube', 'v3', developerKey=self.youtube_key)

        request = youtube.search().list(
            part='snippet',
            q=query,
            type='video',
            maxResults='1',
            videoCategoryId='10'
        )

        response = request.execute()

        # Add a delay to avoid overwhelming the YouTube API with requests
        time.sleep(1)

        # Creates the link for each specific video and caches it to prevent 
        # duplicate calls if there are duplicate songs in the playlist
        if 'items' in response:
            link_suffix = response['items'][0]['id']['videoId']
            link = f'https://www.youtube.com/watch?v={link_suffix}'
            self.cache[query] = link
            return link
        else:
            self.cache[query] = None
            return None