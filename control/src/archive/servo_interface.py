import socketio


class ServoInterface():
    def __init__(self):
        self._voltage: int = 0

    def main(self):
        sio = socketio.Client()

        @sio.event
        def connect():
            print('connection established')

        @sio.event
        def servo_receiver(data):
            self._voltage = data
            print('New voltage: ', self._voltage)
            print('type ', type(data))

        @sio.event
        def disconnect():
            print('disconnected from server')

        sio.connect('http://localhost:5000')
        sio.wait()


if __name__ == '__main__':
    servo_interface = ServoInterface()
    servo_interface.main()
