import logging

from input.factory.enum import InputImplementation
from input.impl.input_mqtt import InputMqtt
from input.impl.input_socketio import InputSocketIo
from input.impl.input_import_image import InputImportImage

from utils.loadConfig import loadConfig

CONFIG = loadConfig('config.json')


class InputFactory():
    def createInput(self, controler, imageProcessor, output):
        if CONFIG["inputImplementation"] == InputImplementation.MQTT:
            input = InputMqtt(CONFIG["messangerIp"], CONFIG["messangerPort"],
                              controler, imageProcessor, output)

        elif CONFIG["inputImplementation"] == InputImplementation.SOCKETIO:
            input = InputSocketIo(CONFIG["messangerIp"], CONFIG["messangerPort"],
                                  controler, imageProcessor, output)

        elif CONFIG["inputImplementation"] == InputImplementation.MOCK:
            input = InputImportImage(controler, imageProcessor, output)
        else:
            raise ValueError(
                f'{__class__.__name__} - inputImplementation: Select values from {list(InputImplementation)}')

        logging.info(
            f'{__class__.__name__} - Created Input: {input.__class__.__name__}')

        return input
