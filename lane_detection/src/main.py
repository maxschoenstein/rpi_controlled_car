
import time
import logging
import logging.config
import json

from controler.controler import Controler
from output.output_factory.output_factory import OutputFactory
from image_processor.image_processor_factory.image_processor_factory import ImageProcessorFactory

from utils.getLogConfigFilepath import getLogConfigFilepath

with open(getLogConfigFilepath(), 'r') as f:
    logging_config = json.load(f)

# Apply logging configuration
logging.config.dictConfig(logging_config)

from input.factory.input_factory import InputFactory  # noqa


if __name__ == "__main__":
    controler = Controler()
    imageProcessor = ImageProcessorFactory().createImageProcessor()
    output = OutputFactory().createOutput()

    input = InputFactory().createInput(controler, imageProcessor, output)

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
