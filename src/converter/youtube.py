import os
import logging

from pytube import YouTube as youtube
from abc import ABC, abstractmethod


"""
    TODO: implement video options properties
    itag = 18 - ["low", "360", "360p"]:
    itag = 22 - ["medium", "720", "720p", "hd"]:
    itag = 137 - ["high", "1080", "1080p", "fullhd", "full_hd", "full hd"]:
    itag = 313 - ["very high", "2160", "2160p", "4K", "4k"]:
"""

__all__ = ["YoutubeAudioConverter",
           "YoutubeVideoConverter",]

class __FileConverter(ABC):
    
    def __init__(self, url, video_format):
        self.video = youtube(url)
        self.video_format = video_format
    
    @abstractmethod
    def change_file_extension(self, filename):
        pass
    
    @abstractmethod
    def download_video(self, url):
        pass
    
    @abstractmethod
    def convert(self, url: str) -> str:
        pass
        

class YoutubeAudioConverter(__FileConverter):
    
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
            logging.error("Error during audio conversion: %s", e)
            return "Error parsing file/link"


class YoutubeVideoConverter(__FileConverter):
    
    def download_video(self):
        resolution = self.video_format
        stream = self.video.streams.get_by_itag(resolution)
        stream.download()
        return stream.default_filename

    def convert(self) -> str:
        try:
            if self.download_video():
                return "Successful video conversion"
            else:
                return "Error during downloading video file"
        except Exception as e:
            logging.error("Error during video conversion: %s", e)
            return "Error during video download"
    
    def change_file_extension(self, filename):
        pass