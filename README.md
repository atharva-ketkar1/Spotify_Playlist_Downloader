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

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/atharva-ketkar1/Spotify-Playlist-Downloader.git
cd Spotify-Playlist-Downloader


