# Web streaming example
# Source code from the official PiCamera package
# http://picamera.readthedocs.io/en/latest/recipes2.html#web-streaming

import io
import logging
import os
from threading import Condition

from http import server
import socketserver
import threading
# import picamera

with open(os.path.join(os.path.dirname(__file__), 'templates', 'index_phone.html'), 'r') as f:
    PAGE = f.read()


class StreamingOutput(object):
    def __init__(self, default_image_path):
        self.default_image_path = default_image_path
        self.frame = None
        self.load_default_image()

    def load_default_image(self):
        self.frame = self.default_image_path

    def write(self, buf):
        # No need to write anything if using a predefined image
        pass


class StreamingHandler(server.BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.output = kwargs.pop('output', None)
        super().__init__(*args, **kwargs)

    def do_GET(self):
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index_phone.html')
            self.end_headers()
        elif self.path == '/index_phone.html':
            content = PAGE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header(
                'Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            try:
                while True:
                    with self.output.condition:
                        self.output.condition.wait()
                        frame = self.output.frame
                    self.wfile.write(b'--FRAME\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length', len(frame))
                    self.end_headers()
                    self.wfile.write(frame)
                    self.wfile.write(b'\r\n')
            except Exception as e:
                logging.warning(
                    'Removed streaming client %s: %s',
                    self.client_address, str(e))
        else:
            self.send_error(404)
            self.end_headers()


class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True


class StreamServer():
    def __init__(self, output):
        self.output = output

    def serve(self):
        try:
            address = ('127.0.0.1', 8000)
            server = StreamingServer(address, StreamingHandler, {
                                     'output': self.output})
            server.serve_forever()
        finally:
            logging.info('Stream server closed.')


class Frontend():
    def __init__(self):
        # Replace 'default_image.jpg' with the path to your default image file
        with open(os.path.join(os.path.dirname(__file__), 'default_image.jpg'), 'rb') as f:
            self.default_image = f.read()
        self.output = StreamingOutput(self.default_image)
        self.stream_server = StreamServer(self.output)
        self.stream_server_thread = threading.Thread(
            target=self.stream_server.serve)
        self.stream_server_thread.start()


if __name__ == '__main__':
    Frontend()
