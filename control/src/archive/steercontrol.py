# import RPi.GPIO as GPIO
import time
import sys
import logging

DUTY_CYCLE_MAX = 9
DUTY_CYCLE_MIN = 4


class SteerControl():
    def __init__(self):
        #        self.sio = socketio.Client()

        self.duty_cycle = 7.5
        self.servo_pin = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.servo_pin, GPIO.OUT)

        self.p = GPIO.PWM(self.servo_pin, 50)  # GPIO 17 mit PWM 17 Hz
        self.p.start(self.duty_cycle)  # Init
        time.sleep(1.3)
        self.p.ChangeDutyCycle(0)

    def increase_duty_cycle(self):
        self.duty_cycle += 1
        self.limit_duty_cycle()
        print(self.duty_cycle)
        logging.info(self.duty_cycle)
        self.p.ChangeDutyCycle(duty_cycle)
        time.sleep(1.3)
        self.p.ChangeDutyCycle(0)

    def decrease_duty_cycle(self):
        self.duty_cycle -= 1
        self.limit_duty_cycle()
        print(self.duty_cycle)
        logging.info(self.duty_cycle)
        self.p.ChangeDutyCycle(duty_cycle)
        time.sleep(1.3)
        self.p.ChangeDutyCycle(0)

    def change_duty_cycle(self, duty_cycle):
        self.exit(duty_cycle)
        self.p.ChangeDutyCycle(duty_cycle)
        time.sleep(1.3)
        self.p.ChangeDutyCycle(0)

    def limit_duty_cycle(self):
        if self.duty_cycle > DUTY_CYCLE_MAX:
            self.duty_cycle = DUTY_CYCLE_MAX
        elif self.duty_cycle < DUTY_CYCLE_MIN:
            self.duty_cycle = DUTY_CYCLE_MIN
        return

    def exit(self, input):
        self.p.stop()
        GPIO.cleanup()
        print('Terminated')
        sys.exit()
        return
