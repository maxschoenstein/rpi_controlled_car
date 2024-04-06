import io

import picamera

from camera_processor.output_client import OutputClient
from camera_processor.camera_processor import CameraProcessor

from utils.loadConfig import loadConfig

CONFIG = loadConfig('config.json')


class CameraProcessorRaspi(CameraProcessor):
    def sendStream(self, outputClient: OutputClient):
        with picamera.PiCamera() as camera:
            camera.resolution = (CONFIG["resolutionX"], CONFIG["resolutionY"])
            camera.framerate = CONFIG["frameRate"]

            stream = io.BytesIO()

            for _ in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
                stream.seek(0)
                frame_bytes = stream.getvalue()

                outputClient.emitMessage(frame_bytes)

                stream.seek(0)
                stream.truncate()
