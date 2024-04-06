import logging

from camera_processor.output_client import OutputClient


class OutputClientMock(OutputClient):
    def __init__(self, endpoint):
        self._endpoint = endpoint

    def emitMessage(self, data):
        logging.info(
            f'{__class__.__name__}: emitMessage to {self._endpoint}')

    def disconnect(self):
        logging.info(f'{__class__.__name__}: disconnect')
