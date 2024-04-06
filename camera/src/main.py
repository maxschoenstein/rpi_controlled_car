import threading
import logging
import logging.config
import json


from utils.getLogConfigFilepath import getLogConfigFilepath

with open(getLogConfigFilepath(), 'r') as f:
    logging_config = json.load(f)

# Apply logging configuration
logging.config.dictConfig(logging_config)

from camera_processor.camera_processor_factory import CameraProcessorFactory  # noqa
from output_client.output_client_factory.output_client_factory import OutputClientFactory  # noqa


if __name__ == '__main__':
    cameraProcessor = CameraProcessorFactory().createCameraProcessor()
    outputClient = OutputClientFactory().createOutputClient()

    stream_thread = threading.Thread(
        target=cameraProcessor.sendStream, args=(outputClient,))
    stream_thread.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        outputClient.disconnect()
