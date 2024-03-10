from abc import ABC, abstractmethod


class CameraProcessor(ABC):
    @abstractmethod
    def sendStream(self):
        pass
