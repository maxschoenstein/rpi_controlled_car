from enum import IntEnum


class InputImplementation(IntEnum):
    MQTT = 0
    SOCKETIO = 1
    MOCK = 2
