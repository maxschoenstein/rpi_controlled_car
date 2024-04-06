import json

from utils.getConfigFilePath import getConfigFilePath


def loadConfig(config: str):
    """Load a camera configuration file.

    Parameters
    ----------
    config : str
        Name of configuration file

    Returns
    -------
    Dict
        Dictionary containing the configuration
    """
    configFilePath = getConfigFilePath(config)

    with open(configFilePath, 'r') as f:
        return json.load(f)
