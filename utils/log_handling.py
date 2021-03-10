import logging
import sys

FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s")


def _get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


logger = logging.getLogger('Logger')
logger.setLevel(logging.DEBUG)
logger.addHandler(_get_console_handler())
logger.propagate = False
