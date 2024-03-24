import threading
import logging
import logging.config
import os
import json

from dotenv import load_dotenv

from utils.getLogConfigFilepath import getLogConfigFilepath
from utils.getDevEnvFilePath import getDevEnvFilePath

with open(getLogConfigFilepath(), 'r') as f:
    logging_config = json.load(f)

# Apply logging configuration
logging.config.dictConfig(logging_config)

try:
    path = getDevEnvFilePath('camera')
    load_dotenv(path)
    logging.info(f"{path} environment is loaded")
except:
    logging.info("prod environment is loaded")

from output_client.output_client_factory.output_client_factory import OutputClientFactory  # noqa
from camera_processor.camera_processor_factory import CameraProcessorFactory  # noqa



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
