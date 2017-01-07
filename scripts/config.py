import os
import yaml

CONFIG_FILE_PATH = 'conf.yml'
DEFAULT_BACKUP_COUNT = 30


def exists_config_file():
    return os.path.exists(CONFIG_FILE_PATH)


def get_slack_token():
    with open(CONFIG_FILE_PATH, "r") as conf_file:
        data = yaml.load(conf_file)
        return data.get("slack").get("token")


def get_mongodb_conf():
    with open(CONFIG_FILE_PATH, "r") as conf_file:
        data = yaml.load(conf_file)
        return data.get("mongodb")


def get_logging_backup_count():
    with open(CONFIG_FILE_PATH, "r") as conf_file:
        data = yaml.load(conf_file)
        backup_count = data.get("logging", dict()).get("backup_count")
        if backup_count is None:
            backup_count = DEFAULT_BACKUP_COUNT

        return backup_count
