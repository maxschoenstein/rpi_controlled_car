import socketio
from camera_processor.output_client import OutputClient


class OutputClientSocketIO(OutputClient):
    def __init__(self, ip: str, port: int, endpoint='frame'):
        self.__server_url = f'http://{ip}:{port}'
        self.__endpoint = endpoint

        self.sio = socketio.Client()

        @self.sio.event
        def connect():
            print('Connected to server:', self.__server_url)

        @self.sio.event
        def disconnect():
            print('Disconnected from server')

        self.sio.connect(self.__server_url)

    def emitMessage(self, data):
        self.sio.emit(self.__endpoint, data)

    def disconnect(self):
        self.sio.disconnect()
