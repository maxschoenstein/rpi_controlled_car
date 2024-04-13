from controler.image_processor import ImageProcessor
from controler.output import Output


class Controler():
    def controlLaneDetection(self, frame: bytes, imageProcessor: ImageProcessor, output: Output):
        processedImage = imageProcessor.processImage(frame)
        output.emitMessage(processedImage)
