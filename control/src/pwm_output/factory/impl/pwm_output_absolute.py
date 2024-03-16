import time
import logging

import RPi.GPIO as GPIO

from control_handler.pwm_output import PwmOutput


class PwmOutputAbsolute(PwmOutput):
    def __init__(self, pin, frequency, max, min, neutral):
        self.pin = pin
        self.frequency = frequency
        self.neutral = neutral
        self.min = min
        self.max = max
        self.duty_cycle = neutral

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)

        self.pwm = GPIO.PWM(pin, frequency)

        self.pwm.start(neutral)
        time.sleep(1.5)
        self.pwm.ChangeDutyCycle(0)

        logging.info(f'{self._class__.__name__} initalized\n \
        Pin: {self.pin}\n \
        PWM-Frequency: {self.frequency}\n\
        PWM-Max: {self.max}\n \
        PWM-Min: {self.min}\n \
        PWM-Neutral: {self.neutral}')

    def setDutyCycle(self, percentage):
        if percentage >= 0:
            scale = self.max
        elif percentage < 0:
            scale = self.min
        scaledDutyCycle = self._scaleDutyCycle(percentage, scale)
        self.pwm.ChangeDutyCycle(scaledDutyCycle)

    def _scaleDutyCycle(self, percentage, scale):
        scaled = (scale-self.neutral) * abs(percentage)
        scaled_final = scaled + self.neutral
        return round(scaled_final, 1)

    def exit(self):
        logging.info('exit')
        self.pwm.ChangeDutyCycle(self.neutral)
        time.sleep(1.5)
        self.pwm.stop()
        GPIO.cleanup()
        return

    def neutralize(self):
        self.pwm.ChangeDutyCycle(self.neutral)
