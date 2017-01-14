from datetime import datetime

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from logbook import Logger

from scripts import config
from scripts import data_header_const

log = Logger(__name__)


def _client_setup():
    mongodb_conf = config.get_mongodb_conf()
    mongo_client = MongoClient(mongodb_conf.get("server"), mongodb_conf.get("port"))
    try:
        mongo_client.server_info()
    except ConnectionFailure as error:
        log.critical("Mongodb exception occured: {0}".format(error))
        exit()

    db = mongo_client["slackUsageChecker"]
    return db


def save_result(results):
    db = _client_setup()

    for result in results:
        date_object = result[data_header_const.DATE]
        result[data_header_const.DATE] = datetime(date_object.year, date_object.month, date_object.day)
        inc = {"$inc": {data_header_const.COUNT: result[data_header_const.COUNT]}}
        result.pop(data_header_const.COUNT)

        db.results.update(result, inc, upsert=True)


def save_latest_info(latest_infos):
    db = _client_setup()

    for latest_info in latest_infos:
        db.latest_infos.update({data_header_const.ID: latest_info[data_header_const.ID]}, {"$set": {data_header_const.LATEST_TS: latest_info[data_header_const.LATEST_TS]}}, upsert=True)


def load_latest_info():
    db = _client_setup()

    return list(db.latest_infos.find())
