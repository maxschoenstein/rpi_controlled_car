import RPi.GPIO as GPIO
import time
import logging

from control_handler.pwm_output import PwmOutput

logging.basicConfig(level=logging.DEBUG)


class PwmOutputDriveModes(PwmOutput):
    def __init__(self, pin, frequency, max, min, neutral, step, acc, dec):
        super().__init__(pin, frequency, max, min, neutral, step)
        self._max_acceleration = acc
        self._min_deceleration = dec

        self._stop_time = 2
        self._acceleration_time = 0.5
        self._deceleration_time = 0.5

        self._status = 'STOP'  # 'ACCELERATE', 'FORWARD', 'DECELERATE', 'BACKWARD'

    def setDutyCycle(self, data):
        data = int(data)
        if data > 0:
            if self._status == 'DECELERATE' or self._status == 'BACKWARD':
                self._stop()
            elif self._status == 'STOP':
                self._accelerate()
                self._go_forward()
            elif self._status == 'FORWARD' or self._status == 'ACCELERATE':
                pass
        elif data < 0:
            if self._status == 'ACCELERATE' or self._status == 'FORWARD':
                self._stop()
            elif self._status == 'STOP':
                self._decelerate()
                self._go_backward()
            elif self._status == 'BACKWARD' or self._status == 'DECELERATE':
                pass
        logging.info(self._status)
        return

    def _accelerate(self):
        self._status = 'ACCELERATE'
        self.pwm.ChangeDutyCycle(self._max_acceleration)
        time.sleep(self._acceleration_time)
        self._go_forward()
        return

    def _go_forward(self):
        self._status = 'FORWARD'
        self.pwm.ChangeDutyCycle(self.max)
        return

    def _decelerate(self):
        self._status = 'DECELERATE'
        self.pwm.ChangeDutyCycle(self._min_deceleration)
        time.sleep(self._deceleration_time)
        self._go_backward()
        return

    def _go_backward(self):
        self._status = 'BACKWARD'
        self.pwm.ChangeDutyCycle(self.min)
        return

    def _stop(self):
        self._status = 'STOP'
        self.pwm.ChangeDutyCycle(self.neutral)
        time.sleep(self._stop_time)

    def exit(self):
        logging.info('exit')

        self.pwm.ChangeDutyCycle(self.neutral)
        time.sleep(1.5)
        self.pwm.stop()
        GPIO.cleanup()
        return

    def neutralize(self):
        pass
