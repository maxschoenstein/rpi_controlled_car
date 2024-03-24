# autonomous_rc_car
# MQTT
## Installation
TBD
## Start MQTT
* Type ``Service`` in windows Start
* Restart Mosquitto Broker

## Automatic startup 
Create Start up file in custom directory that is not the project directory:<br>
e.g. 
ust/bin/start_car.sh:
```
#!/bin/bash

# Log file paths
camera_log="/home/maxscho/rpi_controlled_car/logs/camera.log"
hmi_log="/home/maxscho/rpi_controlled_car/logs/hmi.log"
control_log="/home/maxscho/rpi_controlled_car/logs/control.log"

# Start camera and log output
/usr/bin/python3.7 /home/maxscho/rpi_controlled_car/camera/src/main.py >> "$camera_log" 2>&1 &

# Start hmi and log output
node /home/maxscho/rpi_controlled_car/hmi/src/server.js >> "$hmi_log" 2>&1 &

# Start control and log output
/usr/bin/python3.7  /home/maxscho/rpi_controlled_car/control/src/main.py >> "$control_log" 2>&1 &

echo "Started all files."

```
Add a crontab job executed at reboot:
```
sudo crontab -e -u <user_name>
```
Add at end of the file: 
```
@reboot sleep 20; /bin/bash  usr/bin/start.sh
```
