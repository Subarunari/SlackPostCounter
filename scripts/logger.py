import os

from logbook import TimedRotatingFileHandler

from scripts import config

LOG_FILE_NAME = 'application.log'
LOG_FILE_DIR = os.path.realpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../logs'))
LOG_FILE_PATH = os.path.join(LOG_FILE_DIR, LOG_FILE_NAME)


def setup():
    if not os.path.exists(LOG_FILE_DIR):
        os.mkdir(LOG_FILE_DIR)

    handler = TimedRotatingFileHandler(
        filename=LOG_FILE_PATH,
        backup_count=config.get_logging_backup_count())

    handler.push_application()
