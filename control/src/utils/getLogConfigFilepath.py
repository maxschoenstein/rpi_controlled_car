import os


def getLogConfigFilepath():
    """Get the file path of the log configuration file.

    Returns
    -------
    Path
        Path to log configuration file
    """
    return os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), '.config', 'logs.json')
