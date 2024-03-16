import os
import logging

from input.factory.enum import InputImplementation
from input.factory.impl.input_mqtt import InputMqtt
from input.factory.impl.input_socketio import InputSocketIo


INPUT_IMPL = int(os.getenv('INPUT_IMPL'))
BROKER_IP = os.getenv('BROKER_IP')
BROKER_PORT = int(os.getenv('BROKER_PORT'))


class InputFactory():
    def createInput(self, controlHandler, pwmOutput):
        if INPUT_IMPL == InputImplementation.MQTT:
            input = InputMqtt(BROKER_IP, BROKER_PORT,
                              controlHandler, pwmOutput)
        elif INPUT_IMPL == InputImplementation.SOCKETIO:
            input = InputSocketIo(BROKER_IP, BROKER_PORT,
                                  controlHandler, pwmOutput)
        else:
            raise ValueError(
                f'{__class__.__name__} - INPUT_IMPL: Select values from {list(InputImplementation)}')

        logging.info(
            f'{__class__.__name__} - Created Input: {input.__class__.__name__}')

        return input
