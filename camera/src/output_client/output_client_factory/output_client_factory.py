import os
import logging

from output_client.impl.output_client_socketio import OutputClientSocketIO
from output_client.impl.output_client_mqtt import OutputClientMQTT
from output_client.impl.output_client_mock import OutputClientMock

from output_client.output_client_factory.enums import OutputClientInterface

OUTPUT_IMPL = int(os.getenv('OUTPUT_IMPL'))
IP_MSG = os.getenv('IP_MSG')
PORT_MSG = int(os.getenv('PORT_MSG'))


class OutputClientFactory():
    def createOutputClient(self):
        if OUTPUT_IMPL == OutputClientInterface.MOCK:
            outputClient = OutputClientMock()

        elif OUTPUT_IMPL == OutputClientInterface.SOCKETIO:
            outputClient = OutputClientSocketIO(
                ip=IP_MSG, port=PORT_MSG, endpoint='frame')

        elif OUTPUT_IMPL == OutputClientInterface.MQTT:
            outputClient = OutputClientMQTT(
                ip=IP_MSG, port=PORT_MSG, endpoint='frame')

        else:
            raise ValueError(
                f'{__class__.__name__}: OUTPUT_IMPL - Choose from {list(OutputClientInterface)}')

        logging.info(
            f'{__class__.__name__} - Created OuputClient: {outputClient.__class__.__name__}')

        return outputClient
