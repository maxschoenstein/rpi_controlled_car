import cv2
import numpy as np

from controler.image_processor import ImageProcessor


class ImageProcessorImpl(ImageProcessor):
    def __init__(self):
        pass

    def processImage(self, frame):
        frame_array = np.frombuffer(frame, dtype=np.uint8)
        frame_image = cv2.imdecode(frame_array, flags=cv2.IMREAD_COLOR)

        edged = cv2.Canny(frame_image, 50, 150)
        edged_bytes = cv2.imencode('.jpg', edged)[1].tobytes()
        return edged_bytes
