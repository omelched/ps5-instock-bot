import os
import configparser

from utils.log_handling import logger


class LoggedBaseException(BaseException):
    logger = logger

    def __init__(self, message: str = None):
        super().__init__(message)

        self.logger.error(str(self))

    def __str__(self):
        return str(self.__class__).split('\'')[1]


class Config(configparser.ConfigParser):

    def __init__(self):
        super().__init__()

        if os.path.exists(os.path.dirname('CONFIG.cfg')):
            self.read('CONFIG.cfg')

        for key in list(os.environ.keys()):
            setattr(self, key, os.environ[key])


config = Config()
