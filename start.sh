#!/bin/bash

# Start camera
python ./camera/src/main.py &

# Start hmi
node ./hmi/src/server.js &

# Start control
python ./control/src/main.py &

echo "Started all files."
