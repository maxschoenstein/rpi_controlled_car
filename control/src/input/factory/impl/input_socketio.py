import logging

import socketio

from control_handler.control_handler import ControlHandler
from input.input import Input
from pwm_output.factory.pwm_outputs import PwmOutputs


class InputSocketIo(Input):
    def __init__(self, brokerIp, brokerPort,
                 controlHandler: ControlHandler, pwmOutputs: PwmOutputs):
        self._server_url = f'http://{brokerIp}:{brokerPort}'
        self._sio = socketio.Client()

        self._sio.on('connect', on_connect)
        self._sio.on('drive', drive)
        self._sio.on('steer', steer)
        self._sio.on('exit', exit)
        self._sio.on('neutral', neutral)
        self._sio.on('disconnect', on_disconnect)

        def on_connect():
            logging.info(f'Connected to the server: {self._server_url}')

        def drive(data):
            data = int(data)
            controlHandler.handle_drive(data / 100, pwmOutputs.drive)

        def steer(data):
            data = int(data)
            controlHandler.handle_steer(data / 100, pwmOutputs.steer)

        def exit(data):
            controlHandler.exit(pwmOutputs.drive, pwmOutputs.steer)
            self._sio.disconnect()

        def neutral(data):
            controlHandler.neutralize(pwmOutputs.drive, pwmOutputs.steer)

        def on_disconnect():
            logging.info('Disconnected from the server')

    def connect(self):
        self._sio.connect(self._server_url)

    def disconnect(self):
        self._sio.disconnect()
