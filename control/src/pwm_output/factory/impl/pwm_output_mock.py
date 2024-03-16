
import logging

from control_handler.pwm_output import PwmOutput


class PwmOutputMock(PwmOutput):
    def setDutyCycle(self, dutyCycle):
        logging.info(f'{__class__.__name__}: New DutyCycle: {dutyCycle}')

    def neutralize(self):
        logging.info(f'{__class__.__name__}: Neutralized')

    def exit(self):
        logging.info(f'{__class__.__name__}: Exited')
