from abc import ABC, abstractmethod


class PwmOutput(ABC):
    @abstractmethod
    def setDutyCycle(self, percentage):
        pass

    @abstractmethod
    def exit(self):
        pass

    @abstractmethod
    def neutralize(self):
        pass
