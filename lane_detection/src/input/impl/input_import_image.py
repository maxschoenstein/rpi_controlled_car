import os

from input.input import Input
from controler.controler import Controler
from controler.image_processor import ImageProcessor
from controler.output import Output

from utils.open_jpeg_to_bytes import openJpegToBytes


class InputImportImage(Input):
    def __init__(self, controler: Controler, imageProcessor: ImageProcessor, output: Output):
        self._jpeg_directory = os.path.join(os.path.dirname(os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))))), "data", "rpi_camera")

        self._controler = controler
        self._imageProcessor = imageProcessor
        self._output = output

    def connect(self):
        while True:
            for filename in os.listdir(self._jpeg_directory):
                if filename.endswith(".jpg") or filename.endswith(".jpeg"):
                    file_path = os.path.join(self._jpeg_directory, filename)

                    jpeg_bytes = openJpegToBytes(file_path)

                self._controler.controlLaneDetection(
                    jpeg_bytes, self._imageProcessor, self._output)

    def disconnect(self):
        return
