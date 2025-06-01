from io import BytesIO

from yt_dlp import YoutubeDL
import requests
from PIL import Image


class YTDownloader:
     def __init__(self, video_url: str):
          self.video_url = video_url
          self.video = None
          self.video_title = None
          self.video_description = None
          self.video_thumbnail = None
          self.video_duration = None
          self.video_info = None

     def get_info(self):
          try:
               ydl_opts = {
                    "quiet": True,
                    "skip_download": True,
               }
               resolutions = set()
               with YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(self.video_url, download=False)
                    title = info.get("title")
                    print(title)
               
                    formats = info.get("formats", [])
                    for format in formats:
                         height = format.get("height")
                         if height:
                              resolutions.add(f"{height}p")
                              
                    resolutions = sorted(resolutions, key=lambda r: int(r.replace("p", "")))
                    
          except Exception as e:
               print("Failed to video info")
               print("Error:", e)
     
     def get_thumbnail(self):
          try:
               # Get the thumbnail URL
               response = requests.get(self.video.thumbnail_url)
               img_data = BytesIO(response.content)
               pil_img = Image.open(img_data)

               # Resize the image
               pil_img = pil_img.resize((480, 270), Image.ANTIALIAS)
               self.video_thumbnail = pil_img
               return self.video_thumbnail
          except Exception as e:
               print("Failed to load thumbnail")
               print("Error:", e)
