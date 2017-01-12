import os
import sys

from logbook import TimedRotatingFileHandler
from logbook import StreamHandler

from scripts import config

LOG_FILE_NAME = 'application.log'
LOG_FILE_DIR = os.path.realpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../logs'))
LOG_FILE_PATH = os.path.join(LOG_FILE_DIR, LOG_FILE_NAME)


def setup():
    if not os.path.exists(LOG_FILE_DIR):
        os.mkdir(LOG_FILE_DIR)

    file_handler = TimedRotatingFileHandler(
        filename=LOG_FILE_PATH,
        backup_count=config.get_logging_backup_count())

    stream_handler = StreamHandler(sys.stdout, level='CRITICAL')
    stream_handler.format_string = '{record.level_name}: {record.channel}: {record.message}'

    file_handler.push_application()
    stream_handler.push_application()
