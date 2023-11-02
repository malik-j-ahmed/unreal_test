"""Author: Japa
   Organization: Umlaut Part of Accenture
   Project: Metaverese Launcher

   This module initialize the logger objects to log essential trace information
   """

import logging
from logging.handlers import RotatingFileHandler


def get_logger_service():
    """

    :return: logger object
    """
    log_obj = logging.getLogger('metaverse_launcher')
    logging.basicConfig(level=logging.INFO)
    fh = RotatingFileHandler('logs.log', mode='a', maxBytes=5 * 1024 * 1024)
    fh.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    log_obj.addHandler(fh)
    for log_name, log_obj in logging.Logger.manager.loggerDict.items():
        if log_name != 'Metaverse Launcher':
            log_obj.disabled = True
    log_obj.info('Initialized logger')

    return log_obj

"""---------------------------------------------------------------------Unit Testing Mudule START----------------------------------------------------------------------------------------------"""
if __name__ == '__main__':
    logger = get_logger_service()
    logger.info('this is a test')

"""---------------------------------------------------------------------Unit Testing Mudule END----------------------------------------------------------------------------------------------"""
