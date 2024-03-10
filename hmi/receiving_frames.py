import socketio
import picamera
import threading
import base64
import time

# Connect to the Socket.IO server
sio = socketio.Client()
sio.connect('http://localhost:5001')  # Replace with the actual server address


@sio.event
def connect():
    print('Connected to server')


@sio.event
def disconnect():
    print('Disconnected from server')


@sio.event
def frame(sid, data):
    print(f'frame: {data}')


def convert_base64_to_jpg(base64_string, output_file):
    # Decode base64 string to bytes
    image_bytes = base64.b64decode(base64_string)

    # Write the bytes to a JPEG file
    with open(output_file, 'wb') as f:
        f.write(image_bytes)
