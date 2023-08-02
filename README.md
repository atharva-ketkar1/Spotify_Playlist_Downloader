# Spotify_Playlist_Downloader

Spotify Playlist Downloader is a Python tool that allows you to download the songs from a Spotify playlist and save them as audio only mp4 files to your local machine.
The reason they are audio only mp4 files instead of mp3 files is because the conversion between mp4 and mp3 reduces audio quality. The script uses the Spotify API 
to fetch the track information from the given playlist and then searches for the corresponding songs on YouTube using the YouTube API. It then downloads the audio 
of those songs and saves them as MP4 files in a specified folder.

## Features

- Utilizes the Spotify API to retrieve track data from a specified Spotify playlist.
- Searches for the songs on YouTube using the YouTube API.
- Downloads the audio of the songs and saves them as audio only MP4 files.
- Utilizes a cache to store previously searched song queries, helping sustain the YouTube API quota by preventing duplicate searches for the same songs.
- handles any potential YouTube video problems to guarantee accurate song downloads.

## Prerequisites

- Python 3.x
- Spotify API credentials (Get the Client_Id and Client_Secret by creating a Spotify App on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications))
- YouTube API Key (Get it from the [Google Developers Console](https://console.developers.google.com/))
- A public spotify playlist link
- A valid download location

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/atharva-ketkar1/Spotify-Playlist-Downloader.git
cd Spotify-Playlist-Downloader
```
2. Download the requirements.txt file using pip:
```pip
pip install -r requirements.txt
```
3. Modify the .env_sample file by renaming it to .env and fill it in like this:
```markdown
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
YOUTUBE_KEY=your_youtube_api_key
```
- Make sure to rename the file to .env and upload your specific keys
4. You need a sustainable version of ffmpeg installed. This link shows how you can get ffmpeg: https://www.hostinger.com/tutorials/how-to-install-ffmpeg
Alternatively, you could install ffmpeg using “brew install ffmpeg” if you have homebrew installed. This link shows how you can install homebrew: https://docs.brew.sh/Installation

## Usage
1. First, run the file.py script using the command python file.py in the terminal(try python3 file.py if python file.py doesn't work)
2. You will be prompted to specify the path where you want to create the folder to store the downloaded audio tracks. Enter the desired path, and make sure the path exists and is accessible
3. Next, you will be asked to enter the Spotify playlist link you want to download. Provide the playlist link and press Enter
4. The script will fetch the details of the playlist from Spotify and display the name, total tracks, and individual track names along with their respective artists
5. The script will then search for each track on YouTube and download the audio files in the specified folder
6. If a song has already been downloaded (based on its name), the script will skip the download for that specific track to avoid duplicates

Please note that the YouTube API has a rate limit, so there might be a slight delay between each song download to avoid overwhelming the API with requests. This limit allows around 100 downloaded songs per day, and if you're playlist is longer than 100 songs, you might have to wait a day and then continue downloading it.

## Helpful Links

These are some helpful links that I used while building this project:

1. **Python Quickstart for YouTube API**:  
   This quickstart guide from Google provides step-by-step instructions on how to use the YouTube API with Python. It is a great resource to get started with integrating YouTube API functionalities into your project.
   [Link](https://developers.google.com/youtube/v3/quickstart/python)
2. **Python 2.7 or Python 3.5+**:  
   The project supports Python versions 2.7 or 3.5 and above. Make sure you have one of these versions installed on your system.
3. **pip install --upgrade google-api-python-client**:  
   To use the Google API client library for Python, you need to install it using pip. The command "pip install --upgrade google-api-python-client" will install the necessary library or update it to the latest version.   
4. **Background on the YouTube API for Python**:  
   This GitHub repository provides background information and documentation for using the Google API client library for YouTube in Python. It covers essential topics and details about the API.
   [Link](https://github.com/googleapis/google-api-python-client/blob/main/docs/start.md)
5. **Background on using YouTube v3 API**:  
   The official Google API client documentation provides a comprehensive guide to using the YouTube v3 API with Python. It includes details about different API methods and their usage.
   [Link](https://googleapis.github.io/google-api-python-client/docs/dyn/youtube_v3.html)
6. **Man page for the implemented search function**:  
   This documentation page provides a detailed explanation of the implemented search function using the YouTube v3 API. It covers parameters, response format, and usage examples.
   [Link](https://googleapis.github.io/google-api-python-client/docs/dyn/youtube_v3.search.html)
7. **Man page for the implemented search function**:  
   The official YouTube API documentation also includes information about the search function in the v3 API. It provides additional details and examples.
   [Link](https://developers.google.com/youtube/v3/docs/search)
8. **Implements caching and a delay to manage API quota**:  
   To avoid significant impact on the daily API quota, the project implements caching and a delay between requests. This approach helps optimize API usage while staying within the allowed quota.
   [Link](https://developers.google.com/youtube/v3/getting-started#quota)

These resources will provide you with valuable insights and guidance if you encounter an error


## Disclaimer
Only personal and educational use is intended for this project. Use of this script must adhere to all applicable copyright laws and platform terms of service. It's possible to break YouTube's terms of service or copyright laws in your country by downloading protected content from the site. Make sure you only use this script to download files that you have permission to access or that you own.
