from pytube import YouTube, Playlist
import os
from pathlib import Path

link = "https://www.youtube.com/watch?v=I-sH53vXP2A"

url = YouTube(link)

print("downloading....")

video = url.streams.get_highest_resolution()

path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))

video.download(path_to_download_folder)
print("Downloaded! :)")
