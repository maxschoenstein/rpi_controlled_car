import logging

from image_processor.impl.image_processor_impl import ImageProcessorImpl
from image_processor.image_processor_factory.enums import ImageProcessorImplementation

from utils.loadConfig import loadConfig

CONFIG = loadConfig('config.json')


class ImageProcessorFactory():
    def createImageProcessor(self):
        if CONFIG['imageProcessorImplementation'] == ImageProcessorImplementation.IMG_PROC:
            imageProcessor = ImageProcessorImpl()

        else:
            raise ValueError(
                f'{__class__.__name__}: OutputImplementation - Choose from {list(ImageProcessorImplementation)}')

        logging.info(
            f'{__class__.__name__} - Created ImageProcessor: {imageProcessor.__class__.__name__}')

        return imageProcessor
