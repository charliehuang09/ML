from pytube import YouTube, Playlist
import os
from pathlib import Path

# p = Playlist('https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr')
# for url in p.video_urls:
#     print(url)
#     url = YouTube(url)
#     video = url.streams.get_highest_resolution()
#     path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))
#     video.download(path_to_download_folder)

link = "https://www.youtube.com/watch?v=qv6UVOQ0F44"

url = YouTube(link)

print("downloading....")

video = url.streams.get_highest_resolution()

path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))

video.download(path_to_download_folder)
print("Downloaded! :)")
