import csv
import os

from script import data_header_const

RESULT_HEADER = {data_header_const.ID: "id", data_header_const.NAME: "name", data_header_const.COUNT: "count", data_header_const.DATE: "date"}
RESULT_FILE_PATH = 'result.csv'
LATEST_INFO_HEADER = {data_header_const.ID: "id", data_header_const.LATEST_TS: "latest_ts"}
LATEST_INFO_PATH = 'latest_info.csv'


def save_result(results):
    with open(RESULT_FILE_PATH, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, RESULT_HEADER)
        writer.writerow(RESULT_HEADER)

        for result in results:
            writer.writerow(result)


def load_result():
    if not os.path.exists(RESULT_FILE_PATH):
        return []

    with open(RESULT_FILE_PATH, 'r') as csvfile:
        result = list(csv.DictReader(csvfile))

        return result


def save_latest_info(latest_infos):
    with open(LATEST_INFO_PATH, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, LATEST_INFO_HEADER)
        writer.writerow(LATEST_INFO_HEADER)

        for latest_info in latest_infos:
            writer.writerow(latest_info)


def load_latest_info():
    if not os.path.exists(LATEST_INFO_PATH):
        return []

    with open(LATEST_INFO_PATH, 'r') as csvfile:
        result = list(csv.DictReader(csvfile))

        return result
