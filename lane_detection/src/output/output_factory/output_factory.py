import logging

from output.impl.output_socketio import OutputSocketIO
from output.impl.output_mqtt import OutputMQTT
from output.impl.output_mock import OutputMock
from output.impl.output_save import OutputSave

from output.output_factory.enums import OutputImplementation

from utils.loadConfig import loadConfig

CONFIG = loadConfig('config.json')


class OutputFactory():
    def createOutput(self):
        if CONFIG['outputImplementation'] == OutputImplementation.MOCK:
            output = OutputMock(endpoint='frame')

        elif CONFIG['outputImplementation'] == OutputImplementation.SOCKETIO:
            output = OutputSocketIO(
                ip=CONFIG["messangerIp"], port=CONFIG["messangerPort"], endpoint='frame')

        elif CONFIG['outputImplementation'] == OutputImplementation.MQTT:
            output = OutputMQTT(
                ip=CONFIG["messangerIp"], port=CONFIG["messangerPort"], endpoint='frame')

        elif CONFIG['outputImplementation'] == OutputImplementation.SAVE:
            output = OutputSave()

        else:
            raise ValueError(
                f'{__class__.__name__}: OutputImplementation - Choose from {list(OutputImplementation)}')

        logging.info(
            f'{__class__.__name__} - Created Ouput: {output.__class__.__name__}')

        return output
