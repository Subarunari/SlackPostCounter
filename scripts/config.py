import os
import yaml

CONFIG_FILE_PATH = 'conf.yml'


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
