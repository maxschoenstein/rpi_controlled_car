
import logging
import os

PIN_DRIVE = int(os.getenv('PIN_DRIVE'))
FREQENCY_DRIVE = int(os.getenv('FREQENCY_DRIVE'))
MAX_DRIVE = float(os.getenv('MAX_DRIVE'))
MIN_DRIVE = float(os.getenv('MIN_DRIVE'))
NEUTRAL_DRIVE = float(os.getenv('NEUTRAL_DRIVE'))
STEP_DRIVE = float(os.getenv('STEP_DRIVE'))
ACC_DRIVE = float(os.getenv('ACC_DRIVE'))
DEC_DRIVE = float(os.getenv('DEC_DRIVE'))

PWM_OUTPUT_DRIVE_IMPL = int(os.getenv('PWM_OUTPUT_DRIVE_IMPL'))

from pwm_output.factory.enum import PwmOutputDriveImplementation  # noqa

if PWM_OUTPUT_DRIVE_IMPL == PwmOutputDriveImplementation.ABS:
    from pwm_output.factory.impl.pwm_output_absolute import PwmOutputAbsolute
elif PWM_OUTPUT_DRIVE_IMPL == PwmOutputDriveImplementation.DRV_MODES:
    from pwm_output.factory.impl.pwm_output_drive_modes import PwmOutputDriveModes
elif PWM_OUTPUT_DRIVE_IMPL == PwmOutputDriveImplementation.MOCK:
    from pwm_output.factory.impl.pwm_output_mock import PwmOutputMock


class PwmOutputDriveFactory():
    def createPwmOutoutDrive(self):
        if PWM_OUTPUT_DRIVE_IMPL == PwmOutputDriveImplementation.ABS:
            pwmOutputDrive = PwmOutputAbsolute(
                PIN_DRIVE, FREQENCY_DRIVE, MAX_DRIVE, MIN_DRIVE,
                NEUTRAL_DRIVE, STEP_DRIVE)
        elif PWM_OUTPUT_DRIVE_IMPL == PwmOutputDriveImplementation.DRV_MODES:
            pwmOutputDrive = PwmOutputDriveModes(
                PIN_DRIVE, FREQENCY_DRIVE, MAX_DRIVE, MIN_DRIVE,
                NEUTRAL_DRIVE, STEP_DRIVE, ACC_DRIVE, DEC_DRIVE)
        elif PWM_OUTPUT_DRIVE_IMPL == PwmOutputDriveImplementation.MOCK:
            pwmOutputDrive = PwmOutputMock()
        else:
            raise ValueError(
                f'{__class__.__name__} - PWM_OUTPUT_DRIVE_IMPL: Select values from {list(PwmOutputDriveImplementation)}')

        logging.info(
            f'{__class__.__name__} - Created PwmOutputDrive: {pwmOutputDrive.__class__.__name__}')

        return pwmOutputDrive
