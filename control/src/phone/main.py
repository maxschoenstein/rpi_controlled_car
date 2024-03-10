import socketio

from control_handler import ControlHandler

# Create a new Socket.IO client
sio = socketio.Client()

control_handler_ = ControlHandler()


@sio.event
def connect():
    print('Connected to the server')


@sio.on('drive')
def drive(data):
    data = int(data)
    control_handler_.handle_drive(data/100)


@sio.on('steer')
def steer(data):
    data = int(data)
    control_handler_.handle_steer(data/100)


@sio.on('exit')
def exit(data):
    control_handler_.exit()
    sio.disconnect()


@sio.on('neutral')
def neutral(data):
    control_handler_.neutralize()


@sio.event
def disconnect():
    print('Disconnected from the server')


if __name__ == "__main__":
    server_url = 'http://127.0.0.1:5001'
    sio.connect(server_url)

    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass
    finally:
        # Disconnect from the server when done
        sio.disconnect()
