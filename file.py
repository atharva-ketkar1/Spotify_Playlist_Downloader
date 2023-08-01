import os
from pytube import YouTube
from moviepy.editor import *
import subprocess
from playlist import Playlist_Methods as spotify, token
from music import MusicApp

# Function to remove possible illegal characters from the 
# playlist name which will be the folder name as well
def remove_illegal_characters(s):
    illegal_chars = r'<>:"/\|?*'
    substitutions = str.maketrans('', '', illegal_chars)
    name = s.translate(substitutions)

    return name

# Creates the folder that contains all the songs if the 
# folder doesn't already exist
def create_folder(path, playlist_name):
    folder_name = remove_illegal_characters(playlist_name)
    full_path = os.path.join(path, folder_name)

    if not os.path.exists(full_path):
        os.makedirs(full_path)

    return full_path

# Splits the audio in half due to imminent pytube download error
# where the first half of the file has sound and the second half 
# has no sound
def split_audio_in_half(input_file):
    audio_clip = AudioFileClip(input_file)
    audio_duration = audio_clip.duration
    audio_clip.close()

    midpoint = audio_duration 

    # Export the first half of the audio using ffmpeg
    first_half_output = os.path.splitext(input_file)[0] + "_first_half.mp4"
    subprocess.run(['ffmpeg', '-i', input_file, '-ss', '0', '-t', str(midpoint), '-c', 'copy', first_half_output])

    os.replace(first_half_output, input_file)

# Gets the audio file using pytube and downloads it to the folder
def get_audio(link, path):
    try:
        youtube = YouTube(link)
        audio_stream = youtube.streams.filter(only_audio=True, file_extension="mp4").first()
        mp4_file = audio_stream.download(output_path=path)

        # Split the audio file in half and delete the second half
        split_audio_in_half(mp4_file)

        print("Download and split complete!")
    except Exception as e: print(e)



if __name__ == '__main__':
    music_app = MusicApp()

    # Prompt the user to specify the folder path
    base_path = input("Enter the path where you want to create the folder: ")

    # Ensure the provided path is valid and exists
    while not os.path.exists(base_path):
        print("Invalid path or path does not exist. Please try again.")
        base_path = input("Enter the path where you want to create the folder: ")

    playlist_link = input("Enter your Spotify playlist link: ")

    playlist_id = spotify.extract_playlist_id(playlist_link)
    if playlist_id:
        playlist_name, total_tracks, tracks = spotify.get_playlist_information(playlist_id, token)
        if playlist_name and total_tracks:
            print(f"Playlist Name: {playlist_name}")
            print(f"Total Tracks: {total_tracks}")
            print("Tracks:")
            for track_name, artist_names in tracks.items():
                print(f"{track_name} - {artist_names}")

                youtube_query = f'{track_name} {artist_names} lyrics'
                youtube_link = music_app.search_yt(youtube_query)

                folder_path = create_folder(base_path, playlist_name)
                get_audio(youtube_link, folder_path)
        else:
            pass
    else:
        print("Invalid playlist link provided.")

