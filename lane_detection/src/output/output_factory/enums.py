from enum import IntEnum


class OutputImplementation(IntEnum):
    MOCK = 0
    SOCKETIO = 1
    MQTT = 2
    SAVE = 3
