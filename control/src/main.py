
import time
import logging
import logging.config
import os
import json

from dotenv import load_dotenv

from utils.getLogConfigFilepath import getLogConfigFilepath
from utils.getDevEnvFilePath import getDevEnvFilePath

with open(getLogConfigFilepath(), 'r') as f:
    logging_config = json.load(f)

# Apply logging configuration
logging.config.dictConfig(logging_config)

try:
    path = getDevEnvFilePath('control')
    load_dotenv(path)
    logging.info(f"{path} environment is loaded")
except:
    logging.info("prod environment is loaded")

from control_handler.control_handler import ControlHandler  # noqa
from input.factory.input_factory import InputFactory  # noqa
from pwm_output.factory.pwm_output_factory import PwmOutputFactory  # noqa


if __name__ == "__main__":
    controlHandler = ControlHandler()
    pwmOutputs = PwmOutputFactory().createPwmOutout()
    input = InputFactory().createInput(controlHandler, pwmOutputs)

    try:
        input.connect()
    except Exception as e:
        raise Exception(f'{__file__}: {str(e)}')

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info(f"KeyboardInterrupt: {__file__}")
        input.disconnect()
