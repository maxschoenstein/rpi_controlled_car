import logging

from camera_processor.output_client import OutputClient


class OutputClientMock(OutputClient):
    def __init__(self):
        pass

    def emitMessage(self, event, data):
        logging.info(f'{__class__.__name__}: emitMessage - event: {event}')

    def disconnect(self):
        logging.info(f'{__class__.__name__}: disconnect')
