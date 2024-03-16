from control_handler.pwm_output import PwmOutput


class ControlHandler():
    def handle_drive(self, data, pwmOutputDrive: PwmOutput):
        pwmOutputDrive.setDutyCycle(data)
        return

    def handle_steer(self, data, pwmOutputSteer: PwmOutput):
        pwmOutputSteer.setDutyCycle(data)
        return

    def neutralize(self, pwmOutputDrive: PwmOutput,
                   pwmOutputSteer: PwmOutput):
        pwmOutputDrive.neutralize()
        pwmOutputSteer.neutralize()

    def exit(self, pwmOutputDrive: PwmOutput,
             pwmOutputSteer: PwmOutput):
        pwmOutputDrive.exit()
        pwmOutputSteer.exit()
