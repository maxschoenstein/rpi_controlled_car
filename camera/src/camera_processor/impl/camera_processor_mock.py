
import os
import base64
import time
from camera_processor.output_client import OutputClient


from camera_processor.camera_processor import CameraProcessor


class CameraProcessorMock(CameraProcessor):
    def sendStream(self, outputClient: OutputClient):
        i = 0
        imageDirectory = os.path.join(os.path.dirname(
            os.path.dirname(__file__)), 'mockFiles', 'img')

        num_files = len(os.listdir(imageDirectory))

        while True:
            time.sleep(0.1)
            imageNumber = i % num_files

            with open(os.path.join((imageDirectory), f'mockImage{imageNumber}.jpg'), 'rb') as f:
                imageData = f.read()
                # base64Image = base64.b64encode(imageData).decode('utf-8')
            outputClient.emitMessage(imageData)
            i += 1
