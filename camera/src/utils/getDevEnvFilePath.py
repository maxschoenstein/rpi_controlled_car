import os

def getDevEnvFilePath(service):
    return os.path.join(os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), '.config', 'env', service, '.env.dev')