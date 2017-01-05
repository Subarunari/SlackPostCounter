import importlib

from slacker import Slacker
from slacker import Error as SlackError

from scripts import analyzer
from scripts import argument
from scripts import config

DRIVER_MODULE_DIR = 'scripts.driver.{}'


def pre():
    if not config.exists_config_file():
        print("config file not exist")
        exit()

    return vars(argument.parse(argument.create())).get(argument.ARG_NAME)


def main(driver_name):
    driver_module = importlib.import_module(DRIVER_MODULE_DIR.format(driver_name))
    slack_client = Slacker(config.get_slack_token())

    try:
        response = slack_client.channels.list()
    except SlackError:
        exit()

    if not response.body["ok"]:
        return

    now_latest_infos = driver_module.load_latest_info()
    results, latest_infos = analyzer.get_message_count(response, slack_client, now_latest_infos)

    driver_module.save_result(results)
    driver_module.save_latest_info(latest_infos)
