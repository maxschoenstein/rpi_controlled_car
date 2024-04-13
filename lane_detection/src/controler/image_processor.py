from abc import ABC, abstractmethod


class ImageProcessor(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def processImage(self, frame):
        pass
