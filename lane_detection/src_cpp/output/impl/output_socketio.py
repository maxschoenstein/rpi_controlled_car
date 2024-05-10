import logging
import socketio

from controler.output import Output


class OutputSocketIO(Output):
    def __init__(self, ip: str, port: int, endpoint='frame'):
        self._server_url = f'http://{ip}:{port}'
        self._endpoint = endpoint

        self.sio = socketio.Client()

        @self.sio.event
        def connect():
            logging.info('Connected to server:', self._server_url)

        @self.sio.event
        def disconnect():
            logging.info('Disconnected from server')

        self.sio.connect(self._server_url)

    def emitMessage(self, data):
        self.sio.emit(self._endpoint, data)

    def disconnect(self):
        self.sio.disconnect()
