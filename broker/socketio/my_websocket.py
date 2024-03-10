import sys
import datetime

import socketio
import eventlet
import eventlet.wsgi

# , max_http_buffer_size=100000000)
sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)


@sio.event
def connect(sid, environ):
    print(f"Client connected: {sid}")


@sio.event
def disconnect(sid):
    print(f"Client disconnected: {sid}")


@sio.event
def drive(sid, data):
    # print(f'drive: {data}')
    sio.emit('drive', data)


@sio.event
def steer(sid, data):
    print(f'steer: {data}')
    sio.emit('steer', data)


@sio.event
def exit(sid, data):
    print(f'exit: {data}')
    # sio.emit('exit', True)


@sio.event
def neutral(sid, data):
    print(f'neutral: {data}')
    # sio.emit('neutral', True)


@sio.event
def frame(sid, data):
    current_time = datetime.datetime.now().strftime(
        "%y-%m-%d:%H:%M:%S,%f")[:-3]
    print(f'[{current_time}] Frame received')
    sio.emit('frame', data)


@sio.event
def Escape(sid):
    sys.exit()


if __name__ == '__main__':
    your_ip_address = '0.0.0.0'
    your_port = 5001

    # Use eventlet to run the server with WebSocket support
    eventlet.wsgi.server(eventlet.listen((your_ip_address, your_port)), app)
