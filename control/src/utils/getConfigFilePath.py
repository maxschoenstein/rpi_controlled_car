import os


def getConfigFilePath(config: str):
    """Get the file path of a custom camera configuration file.

    Parameters
    ----------
    config : str
        Name of configuration file

    Returns
    -------
    Path
        Path to configuration file
    """
    return os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.config', config)
