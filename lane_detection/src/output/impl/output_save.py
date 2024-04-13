import os

from controler.output import Output


class OutputSave(Output):
    def __init__(self):
        self._directorypath = os.path.join("data", "lane_detection_output")

    def emitMessage(self, outputFrame):
        with open(os.path.join(self._directorypath, "processedImage.jpg"), "wb") as f:
            f.write(outputFrame)

    def disconnect(self):
        pass
