import os
import logging

from input.factory.enum import InputImplementation
from input.factory.impl.input_mqtt import InputMqtt
from input.factory.impl.input_socketio import InputSocketIo

from utils.loadConfig import loadConfig

CONFIG = loadConfig('config.json')


class InputFactory():
    def createInput(self, controlHandler, pwmOutput):
        if CONFIG["inputImplementation"] == InputImplementation.MQTT:
            input = InputMqtt(CONFIG["messangerIp"], CONFIG["messangerPort"],
                              controlHandler, pwmOutput)
        elif CONFIG["inputImplementation"] == InputImplementation.SOCKETIO:
            input = InputSocketIo(CONFIG["messangerIp"], CONFIG["messangerPort"],
                                  controlHandler, pwmOutput)
        else:
            raise ValueError(
                f'{__class__.__name__} - CONFIG["inputImplementation"]: Select values from {list(InputImplementation)}')

        logging.info(
            f'{__class__.__name__} - Created Input: {input.__class__.__name__}')

        return input
