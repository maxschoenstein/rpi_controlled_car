import logging

import paho.mqtt.client as mqttClient

from control_handler.control_handler import ControlHandler
from input.input import Input
from pwm_output.factory.pwm_outputs import PwmOutputs


class InputMqtt(Input):
    def __init__(self, brokerIp, brokerPort, controlHandler: ControlHandler,
                 pwmOutputs: PwmOutputs):
        self._brokerIp = brokerIp
        self._brokerPort = brokerPort

        self.client = mqttClient.Client(transport="websockets")
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            logging.info(f"{__class__.__name__}: Connected to broker")
            self.client.subscribe("drive")
            self.client.subscribe("steer")
            self.client.subscribe("exit")
            self.client.subscribe("neutral")
        else:
            logging.info(f"{__class__.__name__}: Connection failed")

    def on_message(self, client, userdata, message):
        if message.topic == 'drive':
            data = int(message.payload)
            controlHandler.handle_drive(data/100, pwmOutputs.drive)

        elif message.topic == 'steer':
            data = int(message.payload)
            controlHandler.handle_steer(data/100, pwmOutputs.steer)

        elif message.topic == 'exit':
            controlHandler.exit(pwmOutputs.drive, pwmOutputs.steer)
            self.client.disconnect()

        elif message.topic == 'neutral':
            controlHandler.neutralize(pwmOutputs.drive, pwmOutputs.steer)

    def connect(self):
        self.client.connect(self._brokerIp, port=self._brokerPort)
        self.client.loop_start()

    def disconnect(self):
        self.client.disconnect()
        self.client.loop_stop()
