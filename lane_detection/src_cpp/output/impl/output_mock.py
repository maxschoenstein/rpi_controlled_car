import logging

from controler.output import Output


class OutputMock(Output):
    def __init__(self, endpoint):
        self._endpoint = endpoint

    def emitMessage(self, data):
        logging.info(
            f'{__class__.__name__}: emitMessage to {self._endpoint}')

    def disconnect(self):
        logging.info(f'{__class__.__name__}: disconnect')
