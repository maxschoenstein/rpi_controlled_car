import os
import logging

from camera_processor.enums import CameraProcessorImplementation

CAMERA_PROCESSOR_IMPL = int(os.getenv('CAMERA_PROCESSOR_IMPL'))


class CameraProcessorFactory():
    def createCameraProcessor(self):
        if CAMERA_PROCESSOR_IMPL == CameraProcessorImplementation.MOCK:
            from camera_processor.impl.camera_processor_mock import CameraProcessorMock
            cameraProcessor = CameraProcessorMock()

        elif CAMERA_PROCESSOR_IMPL == CameraProcessorImplementation.RASPI:
            from camera_processor.impl.camera_processor_raspi import CameraProcessorRaspi
            cameraProcessor = CameraProcessorRaspi()
        else:
            raise ValueError(
                f'{__class__.__name__}: CAMERA_PROCESSOR_IMPL - Choose from {list(CameraProcessorImplementation)}')

        logging.info(
            f'{self.__class__.__name__} - Created CameraProcessor: {cameraProcessor.__class__.__name__}')
        return cameraProcessor
