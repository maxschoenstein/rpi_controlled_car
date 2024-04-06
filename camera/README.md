
# Camera
## Config
Please rename the ``config.dist.json`` to ``config.json`` and insert your individual values for those parameters marked with ``Individual == True``

| Parameters | Individual | Type | Description |
| - | - | - | - |
| **GENERAL**
| raspberryPiIp | True | str | IP adress of RaspberyPi |
| messangerPort | False | int | Port adress of the messanger service |
| **CAMERA**
| frameRate | False | int | Frame rate of the Raspberry Pi camera module |
| resolutionX | False | int | Resolution of x-axis of the Raspberry Pi camera module |
| resolutionY | False | int | Resolution of y-axis of the Raspberry Pi camera module |
| **IMPLEMENTATIONS**
| outputImplementation | False | int | 0: MOCK - Logging of output without sending anything <br> 1: SOCKETIO - Sending the output to an SocketIo server <br> 2: Sending the output to an MQTT broker |
| cameraProcessorImplementation | False | int | 0: MOCK - Loading predefined images <br> 1: RASPI - Streaming the captured images of the Rapberry Pi camera module |
