from pytube import YouTube
import requests
from io import BytesIO
from PIL import Image


class YTDownloader:
     def __init__(self, video_url: str):
          self.video_url = video_url
          self.video = YouTube(video_url)
          self.video_title = None
          self.video_description = None
          self.video_thumbnail = None
          self.video_duration = None
          self.available_resolutions = []

     def get_resolutions(self):
          # Filter progressive (includes video + audio)
          streams = self.video.streams.filter(progressive=True, file_extension='mp4')

          # Get available resolutions
          self.available_resolutions = sorted(set(stream.resolution for stream in streams if stream.resolution))
          return self.available_resolutions
     
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
