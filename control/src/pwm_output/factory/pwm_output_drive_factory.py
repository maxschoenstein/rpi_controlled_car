
import logging

from utils.loadConfig import loadConfig

CONFIG = loadConfig('config.json')


from pwm_output.factory.enum import PwmOutputDriveImplementation  # noqa

if CONFIG["driveOutputImplementation"] == PwmOutputDriveImplementation.ABS:
    from pwm_output.factory.impl.pwm_output_absolute import PwmOutputAbsolute
elif CONFIG["driveOutputImplementation"] == PwmOutputDriveImplementation.DRV_MODES:
    from pwm_output.factory.impl.pwm_output_drive_modes import PwmOutputDriveModes
elif CONFIG["driveOutputImplementation"] == PwmOutputDriveImplementation.MOCK:
    from pwm_output.factory.impl.pwm_output_mock import PwmOutputMock


class PwmOutputDriveFactory():
    def createPwmOutoutDrive(self):
        if CONFIG["driveOutputImplementation"] == PwmOutputDriveImplementation.ABS:
            pwmOutputDrive = PwmOutputAbsolute(
                CONFIG["drivePwmPin"], CONFIG["drivePwmFrequency"], CONFIG["driveMaxPwmDutyCycle"], CONFIG["driveMinPwmDutyCycle"],
                CONFIG["driveNeutralPwmDutyCycle"])
        elif CONFIG["driveOutputImplementation"] == PwmOutputDriveImplementation.DRV_MODES:
            pwmOutputDrive = PwmOutputDriveModes(
                CONFIG["drivePwmPin"], CONFIG["drivePwmFrequency"], CONFIG["driveMaxPwmDutyCycle"], CONFIG["driveMinPwmDutyCycle"],
                CONFIG["driveNeutralPwmDutyCycle"], CONFIG["driveAccPwmDutyCycle"], CONFIG["driveDecPwmDutyCycle"])
        elif CONFIG["driveOutputImplementation"] == PwmOutputDriveImplementation.MOCK:
            pwmOutputDrive = PwmOutputMock()
        else:
            raise ValueError(
                f'{__class__.__name__} - driveOutputImplementation: {CONFIG["driveOutputImplementation"]} - Select values from {list(PwmOutputDriveImplementation)}')

        logging.info(
            f'{__class__.__name__} - Created PwmOutputDrive: {pwmOutputDrive.__class__.__name__}')

        return pwmOutputDrive
