import threading
import logging
import os

from dotenv import load_dotenv


try:
    path = os.path.join(os.path.dirname(
        os.path.dirname(__file__)), 'env', '.env.dev')
    load_dotenv(path)
    print(f"{path} environment is loaded")
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
