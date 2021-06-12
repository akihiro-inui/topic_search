from abc import ABC, abstractmethod


class BaseDownloader(ABC):
    """
    Base class for content downloader
    """
    def __init__(self):
        pass

    @abstractmethod
    def download_one_video(self, url: str, output_file_path: str):
        raise NotImplementedError
