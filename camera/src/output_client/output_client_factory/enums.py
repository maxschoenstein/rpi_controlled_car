from enum import IntEnum


class OutputClientInterface(IntEnum):
    MOCK = 0
    SOCKETIO = 1
    MQTT = 2
