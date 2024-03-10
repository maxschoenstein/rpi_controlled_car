import tkinter as tk
import socketio
import os

from dotenv import load_dotenv
load_dotenv('./src/.env')


STEERING_ANGLE_MAX = int(os.getenv('STEERING_ANGLE_MAX'))
STEERING_ANGLE_MIN = int(os.getenv('STEERING_ANGLE_MIN'))
STEERING_ANGLE_STEP = int(os.getenv('STEERING_ANGLE_STEP'))

GAS_MAX = int(os.getenv('GAS_MAX'))
GAS_MIN = int(os.getenv('GAS_MIN'))
GAS_STEP = int(os.getenv('GAS_STEP'))


class RemoteControl(tk.Tk):
    def __init__(self):
        super().__init__()

        self.sio = socketio.Client()

        self.steering_angle = 0
        self.gas = 0

        self.title("Einfaches HMI")
        self.geometry('400x200')

        self.label = tk.Label(
            self, text=self.write_text(), font=("Arial", 24))
        self.label.pack(pady=20)

        self.bind("<Up>", self.increase_steering_angle)
        self.bind("<Down>", self.decrease_steering_angle)

        self.bind("<Right>", self.increase_gas)
        self.bind("<Left>", self.decrease_gas)

        self.bind("<d>", self.disconnect_from_server)
        self.bind("<c>", self.connect_to_server)

    def increase_steering_angle(self, event):
        if self.sio.connected:
            self.steering_angle += STEERING_ANGLE_STEP
            self.limit_steering_angle()

            self.sio.emit('my_message', [self.gas, self.steering_angle])
            self.label.config(text=self.write_text())

    def decrease_steering_angle(self, event):
        if self.sio.connected:
            self.steering_angle -= STEERING_ANGLE_STEP
            self.limit_steering_angle()
            self.sio.emit('my_message', [self.gas, self.steering_angle])
            self.label.config(text=self.write_text())

    def increase_gas(self, event):
        if self.sio.connected:
            self.gas += GAS_STEP
            self.limit_gas()
            self.sio.emit('my_message', [self.gas, self.steering_angle])
            self.label.config(text=self.write_text())

    def decrease_gas(self, event):
        if self.sio.connected:
            self.gas -= GAS_STEP
            self.limit_gas()
            self.sio.emit('my_message', [self.gas, self.steering_angle])
            self.label.config(text=self.write_text())

    def write_text(self):
        return f"steering angle: {self.steering_angle} \n gas pedal: {self.gas} \n Connected: {self.sio.connected}"

    def limit_steering_angle(self):
        if self.steering_angle > STEERING_ANGLE_MAX:
            self.steering_angle = STEERING_ANGLE_MAX
        elif self.steering_angle < STEERING_ANGLE_MIN:
            self.steering_angle = STEERING_ANGLE_MIN
        return

    def limit_gas(self):
        if self.gas > GAS_MAX:
            self.gas = GAS_MAX
        elif self.gas < GAS_MIN:
            self.gas = GAS_MIN
        return

    def disconnect_from_server(self, event):
        if self.sio.connected:
            self.sio.disconnect()
            self.label.config(text=self.write_text())

    def connect_to_server(self, event):
        if not self.sio.connected:
            self.sio.connect('http://localhost:5000')
            self.label.config(text=self.write_text())


if __name__ == "__main__":
    app = RemoteControl()
    app.mainloop()
