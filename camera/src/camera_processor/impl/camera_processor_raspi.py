import io
import base64
import os

import picamera

from camera_processor.output_client import OutputClient
from camera_processor.camera_processor import CameraProcessor

RESOLUTION_X = int(os.getenv('RESOLUTION_X'))
RESOLUTION_Y = int(os.getenv('RESOLUTION_Y'))
FRAME_RATE = int(os.getenv('FRAME_RATE'))


class CameraProcessorRaspi(CameraProcessor):
    def sendStream(self, outputClient: OutputClient):
        with picamera.PiCamera() as camera:
            camera.resolution = (RESOLUTION_X, RESOLUTION_Y)
            camera.framerate = FRAME_RATE

            stream = io.BytesIO()

            for _ in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
                stream.seek(0)
                frame_bytes = stream.getvalue()

                # frame_base64 = base64.b64encode(frame_bytes).decode('utf-8')

                outputClient.emitMessage(frame_bytes)

                stream.seek(0)
                stream.truncate()
