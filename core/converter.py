import os

from pytube import YouTube
from abc import ABC, abstractmethod

# from moviepy.editor import VideoFileClip

"""
    iitag = 18 - ["low", "360", "360p"]:
    itag = 22 - ["medium", "720", "720p", "hd"]:
    itag = 137 - ["high", "1080", "1080p", "fullhd", "full_hd", "full hd"]:
    itag = 313 - ["very high", "2160", "2160p", "4K", "4k"]:
"""

__all__ = ["YoutubeAudioConverter",
           "YoutubeVideoConverter",]

class __FileConverter(ABC):
    
    @abstractmethod
    def change_file_extension(self, filename):
        pass
    
    @abstractmethod
    def download_video(self, url):
        pass
    
    @abstractmethod
    def convert(self, url: str):
        pass
        

class YoutubeAudioConverter(__FileConverter):
    
    def __init__(self, url):
        self.video = YouTube(url)
    
    def change_file_extension(self, downloaded_filename):
        new_filename = downloaded_filename[:-4] + ".mp3"
        os.rename(downloaded_filename, new_filename)

    def download_video(self):
        stream = self.video.streams.get_audio_only()
        stream.download()
        return stream.default_filename
    
    
    def convert(self) -> str:
        try:
            self.change_file_extension(self.download_video())
            return "Successful audio conversion"
        except Exception as e:
            return "Error parsing file/link"


class YoutubeVideoConverter(__FileConverter):
    pass