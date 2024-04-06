from abc import ABC, abstractmethod
import json


class OutputClient(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def emitMessage(self, message: json):
        '''Emitting a image encoded as a json string.

        Args:
        - message: json encoded message.        
        '''
        pass

    @abstractmethod
    def disconnect(self):
        '''Disconnect from server.'''
        pass
