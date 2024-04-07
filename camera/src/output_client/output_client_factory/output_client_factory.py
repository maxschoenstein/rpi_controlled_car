import logging

from output_client.impl.output_client_socketio import OutputClientSocketIO
from output_client.impl.output_client_mqtt import OutputClientMQTT
from output_client.impl.output_client_mock import OutputClientMock

from output_client.output_client_factory.enums import OutputClientInterface

from utils.loadConfig import loadConfig

CONFIG = loadConfig('config.json')


class OutputClientFactory():
    def createOutputClient(self):
        if CONFIG['outputImplementation'] == OutputClientInterface.MOCK:
            outputClient = OutputClientMock(endpoint='frame')

        elif CONFIG['outputImplementation'] == OutputClientInterface.SOCKETIO:
            outputClient = OutputClientSocketIO(
                ip=CONFIG["messangerIp"], port=CONFIG["messangerPort"], endpoint='frame')

        elif CONFIG['outputImplementation'] == OutputClientInterface.MQTT:
            outputClient = OutputClientMQTT(
                ip=CONFIG["messangerIp"], port=CONFIG["messangerPort"], endpoint='frame')

        else:
            raise ValueError(
                f'{__class__.__name__}: outputImplementation - Choose from {list(OutputClientInterface)}')

        logging.info(
            f'{__class__.__name__} - Created OuputClient: {outputClient.__class__.__name__}')

        return outputClient
