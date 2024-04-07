#!/bin/bash
# Start camera and log output
/usr/bin/python3.7 /home/maxscho/rpi_controlled_car/camera/src/main.py &
# Start hmi and log output
node /home/maxscho/rpi_controlled_car/hmi/src/server.js &
# Start control and log output
/usr/bin/python3.7  /home/maxscho/rpi_controlled_car/control/src/main.py