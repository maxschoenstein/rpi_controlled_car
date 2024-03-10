
import time

import paho.mqtt.client as mqttClient

from control_handler import ControlHandler

control_handler_ = ControlHandler()


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        client.subscribe("drive")
        client.subscribe("steer")
        client.subscribe("exit")
        client.subscribe("neutral")
    else:
        print("Connection failed")


def on_message(client, userdata, message):
    if message.topic == 'drive':
        data = int(data)
        control_handler_.handle_drive(data/100)

    elif message.topic == 'steer':
        data = int(data)
        control_handler_.handle_steer(data/100)

    elif message.topic == 'exit':
        control_handler_.exit()
        client.disconnect()

    elif message.topic == 'neutral':
        control_handler_.neutralize()


if __name__ == "__main__":
    broker_address = "192.168.0.170"
    port = 9001

    client = mqttClient.Client(transport="websockets")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker_address, port=port)
    client.loop_start()

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("exiting")
        client.disconnect()
        client.loop_stop()
