from steer_control import SteerControl
from drive_control import DriveControl


class ControlHandler():
    def __init__(self):
        self.__steer_control = SteerControl(18, 50, 9, 3.5, 6.25, 0.25)
        self.__drive_control = DriveControl(19, 50, 7.6, 6.1, 6.5, 0.5, 8, 5.8)

    def handle_drive(self, data):
        self.__drive_control.set_drive(data)
        return

    def handle_steer(self, data):
        self.__steer_control.set_steering(data)
        return
