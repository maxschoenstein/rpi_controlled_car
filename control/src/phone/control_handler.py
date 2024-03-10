from pwm_control import PWMControl


class ControlHandler():
    def __init__(self):
        self.__steer_control = PWMControl(18, 50, 9, 3.5, 6.25)
        self.__drive_control = PWMControl(19, 50, 12, 4.5, 6.5)

    def handle_drive(self, data):
        self.__drive_control.setDutyCycle(data)
        return

    def handle_steer(self, data):
        self.__steer_control.setDutyCycle(data)
        return

    def neutralize(self):
        self.__steer_control.neutralize()
        self.__drive_control.neutralize()

    def exit(self):
        self.__steer_control.exit()
        self.__drive_control.exit()
