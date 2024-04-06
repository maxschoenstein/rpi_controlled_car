import logging

from camera_processor.enums import CameraProcessorImplementation

from utils.loadConfig import loadConfig

CONFIG = loadConfig('config.json')


class CameraProcessorFactory():
    def createCameraProcessor(self):
        if CONFIG['cameraProcessorImplementation'] == CameraProcessorImplementation.MOCK:
            from camera_processor.impl.camera_processor_mock import CameraProcessorMock
            cameraProcessor = CameraProcessorMock()

        elif CONFIG['cameraProcessorImplementation'] == CameraProcessorImplementation.RASPI:
            from camera_processor.impl.camera_processor_raspi import CameraProcessorRaspi
            cameraProcessor = CameraProcessorRaspi()
        else:
            raise ValueError(
                f'{__class__.__name__}: cameraProcessorImplementation - Choose from {list(CameraProcessorImplementation)}')

        logging.info(
            f'{self.__class__.__name__} - Created CameraProcessor: {cameraProcessor.__class__.__name__}')
        return cameraProcessor
