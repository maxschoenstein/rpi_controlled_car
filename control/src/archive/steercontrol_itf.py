# import RPi.GPIO as GPIO
from flask import Flask, render_template
from flask_socketio import SocketIO
import logging

from steercontrol import SteerControl

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Beispiel GPIO Pins (anpassen je nach Verkabelung)
# FORWARD_PIN = 17
# BACKWARD_PIN = 18
# LEFT_PIN = 22
# RIGHT_PIN = 23

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(FORWARD_PIN, GPIO.OUT)
# GPIO.setup(BACKWARD_PIN, GPIO.OUT)
# GPIO.setup(LEFT_PIN, GPIO.OUT)
# GPIO.setup(RIGHT_PIN, GPIO.OUT)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('control')
def handle_control(direction):
    if direction == "forward":
        print("forward")
        # GPIO.output(FORWARD_PIN, True)
    elif direction == "backward":
        print("backward")
        # GPIO.output(BACKWARD_PIN, True)
    elif direction == "left":
        print("left")
        logging.info("left")
        servocontrol.decrease_duty_cycle()
        # GPIO.output(LEFT_PIN, True)
    elif direction == "right":
        print("right")
        logging.info("right")
        servocontrol.increase_duty_cycle()
        # GPIO.output(RIGHT_PIN, True)
    elif direction == "exit":
        servocontrol.exit()


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)

    servocontrol = ServoControl()
    servocontrol.increase_duty_cycle()
    logging.info("Socket started")
    socketio.run(app, host='0.0.0.0', port=5000)
