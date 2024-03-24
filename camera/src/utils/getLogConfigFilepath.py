import os

def getLogConfigFilepath():
    return os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) , '.config', 'logs', 'logs.json')