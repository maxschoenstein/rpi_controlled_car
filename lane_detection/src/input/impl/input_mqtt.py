import logging

import paho.mqtt.client as mqttClient

from input.input import Input
from controler.controler import Controler
from controler.image_processor import ImageProcessor
from controler.output import Output


class InputMqtt(Input):
    def __init__(self, brokerIp, brokerPort,
                 controler: Controler, imageProcessor: ImageProcessor, output: Output):
        self._brokerIp = brokerIp
        self._brokerPort = brokerPort

        self.client = mqttClient.Client(transport="websockets")

        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                logging.info(f"{__class__.__name__}: Connected to broker")
                self.client.subscribe("frame")
            else:
                logging.info(f"{__class__.__name__}: Connection failed")

        def on_message(client, userdata, message):
            if message.topic == 'frame':
                frame = str(message.payload)
                controler.controlLaneDetection(frame)

        self.client.on_connect = on_connect
        self.client.on_message = on_message

    def connect(self):
        self.client.connect(self._brokerIp, port=self._brokerPort)
        self.client.loop_start()

    def disconnect(self):
        self.client.disconnect()
        self.client.loop_stop()
