
import logging
import os

from pwm_output.factory.pwm_output_drive_factory import PwmOutputDriveFactory
from pwm_output.factory.pwm_output_steer_factory import PwmOutputSteerFactory
from pwm_output.factory.pwm_outputs import PwmOutputs


class PwmOutputFactory():
    def createPwmOutout(self):
        pwmOutoutDrive = PwmOutputDriveFactory().createPwmOutoutDrive()
        pwmOutoutSteer = PwmOutputSteerFactory().createPwmOutoutSteer()

        pwmOutputs = PwmOutputs(pwmOutoutDrive, pwmOutoutSteer)

        logging.info(
            f'{__class__.__name__} - {pwmOutputs.__class__.__name__} - Created')

        return pwmOutputs
