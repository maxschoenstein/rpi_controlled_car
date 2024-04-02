
import logging
import os

PIN_STEER = int(os.getenv('PIN_STEER'))
FREQENCY_STEER = int(os.getenv('FREQENCY_STEER'))
MAX_STEER = float(os.getenv('MAX_STEER'))
MIN_STEER = float(os.getenv('MIN_STEER'))
NEUTRAL_STEER = float(os.getenv('NEUTRAL_STEER'))
STEP_STEER = float(os.getenv('STEP_STEER'))

PWM_OUTPUT_STEER_IMPL = int(os.getenv('PWM_OUTPUT_STEER_IMPL'))

from pwm_output.factory.enum import PwmOutputSteerImplementation  # noqa

if PWM_OUTPUT_STEER_IMPL == PwmOutputSteerImplementation.ABS:
    from pwm_output.factory.impl.pwm_output_absolute import PwmOutputAbsolute
elif PWM_OUTPUT_STEER_IMPL == PwmOutputSteerImplementation.STEP_STEER:
    from pwm_output.factory.impl.pwm_output_steer_step import PwmoutputSteerStep
elif PWM_OUTPUT_STEER_IMPL == PwmOutputSteerImplementation.MOCK:
    from pwm_output.factory.impl.pwm_output_mock import PwmOutputMock


class PwmOutputSteerFactory():
    def createPwmOutoutSteer(self):
        if PWM_OUTPUT_STEER_IMPL == PwmOutputSteerImplementation.ABS:
            pwmOutputDrive = PwmOutputAbsolute(
                PIN_STEER, FREQENCY_STEER, MAX_STEER, MIN_STEER,
                NEUTRAL_STEER)
        elif PWM_OUTPUT_STEER_IMPL == PwmOutputSteerImplementation.STEP_STEER:
            pwmOutputDrive = PwmoutputSteerStep(
                PIN_STEER, FREQENCY_STEER, MAX_STEER, MIN_STEER,
                NEUTRAL_STEER, STEP_STEER)
        elif PWM_OUTPUT_STEER_IMPL == PwmOutputSteerImplementation.MOCK:
            pwmOutputDrive = PwmOutputMock()
        else:
            raise ValueError(
                f'{__class__.__name__} - PWM_OUTPUT_STEER_IMPL: Select values from {list(PwmOutputSteerImplementation)}')

        logging.info(
            f'{__class__.__name__} - Created PwmOutputDrive: {pwmOutputDrive.__class__.__name__}')

        return pwmOutputDrive
