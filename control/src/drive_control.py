import RPi.GPIO as GPIO
import time
import logging

from pwm_control import PWMControl

logging.basicConfig(level=logging.DEBUG)


class DriveControl(PWMControl):
    def __init__(self, pin, frequency, max, min, neutral, step, acc, dec):
        super().__init__(pin, frequency, max, min, neutral, step)
        self.__max_acceleration = acc
        self.__min_deceleration = dec

        self.__stop_time = 2
        self.__acceleration_time = 0.5
        self.__deceleration_time = 0.5

        self.__status = 'STOP'  # 'ACCELERATE', 'FORWARD', 'DECELERATE', 'BACKWARD'

    def set_drive(self, data):
        data = int(data)
        if data > 0:
            if self.__status == 'DECELERATE' or self.__status == 'BACKWARD':
                self.__stop()
            elif self.__status == 'STOP':
                self.__accelerate()
                self.__go_forward()
            elif self.__status == 'FORWARD' or self.__status == 'ACCELERATE':
                pass
        elif data < 0:
            if self.__status == 'ACCELERATE' or self.__status == 'FORWARD':
                self.__stop()
            elif self.__status == 'STOP':
                self.__decelerate()
                self.__go_backward()
            elif self.__status == 'BACKWARD' or self.__status == 'DECELERATE':
                pass
        logging.info(self.__status)
        return

    def __accelerate(self):
        self.__status = 'ACCELERATE'
        self.pwm.ChangeDutyCycle(self.__max_acceleration)
        time.sleep(self.__acceleration_time)
        self.__go_forward()
        return

    def __go_forward(self):
        self.__status = 'FORWARD'
        self.pwm.ChangeDutyCycle(self.max)
        return

    def __decelerate(self):
        self.__status = 'DECELERATE'
        self.pwm.ChangeDutyCycle(self.__min_deceleration)
        time.sleep(self.__deceleration_time)
        self.__go_backward()
        return

    def __go_backward(self):
        self.__status = 'BACKWARD'
        self.pwm.ChangeDutyCycle(self.min)
        return

    def __stop(self):
        self.__status = 'STOP'
        self.pwm.ChangeDutyCycle(self.neutral)
        time.sleep(self.__stop_time)
