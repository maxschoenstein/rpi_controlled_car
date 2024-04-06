
# Camera
## Config
Please rename the ``config.dist.json`` to ``config.json`` and insert your individual values for those parameters marked with ``Individual == True``

| Parameters | Individual | Type | Description |
| - | - | - | - |
| **GENERAL**
| raspberryPiIp | True | str | IP adress of RaspberyPi |
| messangerPort | False | int | Port adress of the messanger service |
| **DRIVE**
| drivePwmPin | False | int | Used GPIO PWM Pin from Raspberry Pi for drive motor |
| drivePwmFrequency | False | int | Frequency of PWM for drive control |
| driveMaxPwmDutyCycle | False | float | Maximal possible duty cycle of PWM for drive control |
| driveMinPwmDutyCycle | False | float | Minimal possible duty cycle of PWM for drive control |
| driveNeutralPwmDutyCycle | False | float | Neutral duty cycle (motor speed: 0 rpm) of PWM for drive control |
| driveAccPwmDutyCycle | False | float | Duty cycle for PWM during acceleration (Only for PwmOutputDriveModes (driveOutputImplementation==2)) |
| driveDecPwmDutyCycle | False | float | Duty cycle for PWM during deceleration (Only for PwmOutputDriveModes (driveOutputImplementation==2)) |
| **STEER**
| steerPwmPin | False | int | Used GPIO PWM Pin from Raspberry Pi for steer motor |
| steerPwmFrequency | False | int | Frequency of PWM for steer control |
| steerMaxPwmDutyCycle | False | float | Maximal possible duty cycle of PWM for steer control |
| steerMinPwmDutyCycle | False | float | Minimal possible duty cycle of PWM for steer control |
| steerNeutralPwmDutyCycle | False | float | Neutral duty cycle (steer angle: 0 °) of PWM for steer control |
| steerPwmDutyCycleStep | False | float | Step size of duty cycle for PwmoutputSteerStep (steerOutputImplementation == 2) |
| **IMPLEMENTATIONS**
| inputImplementation | False | int | 0: MQTT - <br> 1: SOCKETIO - |
| driveOutputImplementation | False | int | 0: MOCK - Logging outputs but not sending data <br> 1: ABS - Converting received values from -100 to 100 into PWM <br> 3: DRV_MODES - Control by drive mode |
| steerOutputImplementation | False | int | 0: MOCK - Logging outputs but not sending data <br> 1: ABS - Converting received values from -100 to 100 into PWM <br> 3: STEP_STEER - Increase or decrease duty cycle by step size for every input |
