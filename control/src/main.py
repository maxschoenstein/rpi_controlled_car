
import time
import logging
import os
from dotenv import load_dotenv

env_file_path = os.path.join(os.path.dirname(
    os.path.dirname(__file__)), '.env.dev')
load_dotenv(env_file_path)

from control_handler.control_handler import ControlHandler  # noqa
from input.factory.input_factory import InputFactory  # noqa
from pwm_output.factory.pwm_output_factory import PwmOutputFactory  # noqa

logging.basicConfig(level=logging.DEBUG)

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
