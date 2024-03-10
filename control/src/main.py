import socketio

from control_handler import ControlHandler

# Create a new Socket.IO client
sio = socketio.Client()


@sio.event
def connect():
    print('Connected to the server')


@sio.on('drive')
def drive(data):
    control_handler.handle_drive(data)


@sio.on('steer')
def steer(data):
    control_handler.handle_steer(data)


@sio.event
def disconnect():
    print('Disconnected from the server')


if __name__ == "__main__":
    server_url = 'http://127.0.0.1:5001'
    sio.connect(server_url)

    control_handler = ControlHandler()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass
    finally:
        # Disconnect from the server when done
        sio.disconnect()
