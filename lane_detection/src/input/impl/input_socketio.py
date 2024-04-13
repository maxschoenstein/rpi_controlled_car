import logging

import socketio

from input.input import Input
from controler.controler import Controler
from controler.image_processor import ImageProcessor
from controler.output import Output


class InputSocketIo(Input):
    def __init__(self, brokerIp, brokerPort,
                 controler: Controler, imageProcessor: ImageProcessor, output: Output):
        self._server_url = f'http://{brokerIp}:{brokerPort}'
        self._sio = socketio.Client()

        self._sio.on('connect', on_connect)
        self._sio.on('frame', frame)
        self._sio.on('disconnect', on_disconnect)

        def on_connect():
            logging.info(f'Connected to the server: {self._server_url}')

        def frame(frame):
            controler.controlLaneDetection(frame, imageProcessor, output)

        def on_disconnect():
            logging.info('Disconnected from the server')

    def connect(self):
        self._sio.connect(self._server_url)

    def disconnect(self):
        self._sio.disconnect()
