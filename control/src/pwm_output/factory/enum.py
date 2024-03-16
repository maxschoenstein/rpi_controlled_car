from enum import IntEnum


class PwmOutputSteerImplementation(IntEnum):
    MOCK = 0
    ABS = 1
    STEP_STEER = 2


class PwmOutputDriveImplementation(IntEnum):
    MOCK = 0
    ABS = 1
    DRV_MODES = 2
