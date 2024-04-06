
import logging

from utils.loadConfig import loadConfig

CONFIG = loadConfig('config.json')

from pwm_output.factory.enum import PwmOutputSteerImplementation  # noqa

if CONFIG["steerOutputImplementation"] == PwmOutputSteerImplementation.ABS:
    from pwm_output.factory.impl.pwm_output_absolute import PwmOutputAbsolute
elif CONFIG["steerOutputImplementation"] == PwmOutputSteerImplementation.STEP_STEER:
    from pwm_output.factory.impl.pwm_output_steer_step import PwmoutputSteerStep
elif CONFIG["steerOutputImplementation"] == PwmOutputSteerImplementation.MOCK:
    from pwm_output.factory.impl.pwm_output_mock import PwmOutputMock


class PwmOutputSteerFactory():
    def createPwmOutoutSteer(self):
        if CONFIG["steerOutputImplementation"] == PwmOutputSteerImplementation.ABS:
            pwmOutputDrive = PwmOutputAbsolute(
                CONFIG["steerPwmPin"], CONFIG["steerPwmFrequency"], CONFIG["steerMaxPwmDutyCycle"], CONFIG["steerMinPwmDutyCycle"],
                CONFIG["steerNeutralPwmDutyCycle"])
        elif CONFIG["steerOutputImplementation"] == PwmOutputSteerImplementation.STEP_STEER:
            pwmOutputDrive = PwmoutputSteerStep(
                CONFIG["steerPwmPin"], CONFIG["steerPwmFrequency"], CONFIG["steerMaxPwmDutyCycle"], CONFIG["steerMinPwmDutyCycle"],
                CONFIG["steerNeutralPwmDutyCycle"], CONFIG["steerPwmDutyCycleStep"])
        elif CONFIG["steerOutputImplementation"] == PwmOutputSteerImplementation.MOCK:
            pwmOutputDrive = PwmOutputMock()
        else:
            raise ValueError(
                f'{__class__.__name__} - steerOutputImplementation: Select values from {list(PwmOutputSteerImplementation)}')

        logging.info(
            f'{__class__.__name__} - Created PwmOutputDrive: {pwmOutputDrive.__class__.__name__}')

        return pwmOutputDrive
