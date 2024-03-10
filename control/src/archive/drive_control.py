import RPi.GPIO as GPIO
import time
import logging

logging.basicConfig(level=logging.DEBUG)

from pwm_control import PWMControl

class DriveControl(PWMControl):
    def __init__(self, pin, frequency, max, min, neutral, step):
        super().__init__(pin, frequency, max, min, neutral, step)

    def decrease_duty_cycle(self):
        if self.duty_cycle == self.neutral:
            self._engage_reverse()
        if self.duty_cycle <= self.min:
            pass
        else:
            self.duty_cycle -= self.step
            self.pwm.ChangeDutyCycle(self.duty_cycle) 
        logging.info('decrease')
        logging.info(self.duty_cycle)
        return
    
    def _engage_reverse(self):
        self.pwm.ChangeDutyCycle(self.min)
        time.sleep(1.5)
        self.pwm.ChangeDutyCycle(self.neutral)
        return
    