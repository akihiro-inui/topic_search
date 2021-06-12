import os
from src.downloaders.base import BaseDownloader
from src.utils.common_logger import logger
from pytube import YouTube


class YoutubeDownloader(BaseDownloader):
    """
    Class to download Youtube video from URL
    """
    def download_one_video(self, url: str, output_file_path: str):
        try:
            # Download Youtube video with ID
            video_id = os.path.split(url)[-1]
            video = YouTube(url)
            video.streams.filter(file_extension="mp4").all()
            video.streams.get_by_itag(18).download(filename=video_id)
        except Exception as err:
            logger.error(f"Failed to download YouTube video: {err}")

