from auth import token
import requests

# These methods get the infromation about the inputted spotify playlist
class Playlist_Methods:
    # Gets the end of the url, or in this case, the playlist link
    def extract_playlist_id(playlist_link):
        match = playlist_link.rsplit('/', 1)[-1]
        return match if match else None

    # The required authorization for Spotify authorization using their API
    def get_playlist_information(playlist_id, access_token):
        headers = {
            'Authorization': f'Bearer {access_token}',
        }
        playlist_url = f'https://api.spotify.com/v1/playlists/{playlist_id}'
        
        response = requests.get(playlist_url, headers=headers)
        if response.status_code == 200:
            playlist_data = response.json()
            playlist_name = playlist_data['name']
            total_tracks = playlist_data['tracks']['total']
            tracks = Playlist_Methods.extract_track_details(playlist_data['tracks']['items'])
            return playlist_name, total_tracks, tracks
        else:
            print(f"Error: Failed to fetch playlist information. Status code: {response.status_code}")
            return None, None, None

    # Gets the artist(s) and the name of the song
    def extract_track_details(tracks):
        track_details = {}
        for track in tracks:
            track_name = track['track']['name']
            artists = [artist['name'] for artist in track['track']['artists']]
            artist_names = ', '.join(artists)
            track_details[track_name] = artist_names
        return track_details
