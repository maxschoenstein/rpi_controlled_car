import time
import logging

import paho.mqtt.client as mqtt

from camera_processor.output_client import OutputClient


class OutputClientMQTT(OutputClient):
    def __init__(self, ip: str, port: int, endpoint: str):
        self._endpoint = endpoint

        def on_connect(client, userdata, flags, rc):
            logging.info("Connected with result code "+str(rc))
            client.subscribe(self._endpoint)

        self.client = mqtt.Client()

        self.client.on_connect = on_connect

        self.client.connect(ip, port, 60)
        self.client.loop_start()

    def emitMessage(self, data):
        self.client.publish(self._endpoint, data)

    def disconnect(self):
        self.client.loop_stop()
