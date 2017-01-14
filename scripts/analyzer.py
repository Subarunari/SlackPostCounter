from collections import defaultdict
from datetime import datetime

from logbook import Logger

from scripts import data_header_const

DEFAULT_LATEST_TS = 0
log = Logger(__name__)


def get_message_count(response, slack_client, now_latest_infos):
    results = []
    latest_info = []

    for channel in response.body["channels"]:
        latest_ts = get_latest_ts(now_latest_infos, channel["id"])

        saving_latest_ts = latest_ts
        ts_offset = datetime.now().timestamp()
        result_per_day, saving_latest_ts = _get_message_count(slack_client, channel, saving_latest_ts, latest_ts, ts_offset)

        for key, value in result_per_day.items():
            results.append({data_header_const.ID: channel["id"], data_header_const.NAME: channel["name"], data_header_const.COUNT: value, data_header_const.DATE: key})

        latest_info.append({data_header_const.ID: channel["id"], data_header_const.LATEST_TS: saving_latest_ts})

    if len(results) == 0:
        log.info("Nothing new message.")

    return results, latest_info


def get_latest_ts(now_latest_infos, channel_id):
    latest_ts = DEFAULT_LATEST_TS
    for now_latest in now_latest_infos:
        if now_latest["id"] == channel_id and now_latest["latest_ts"] != '0':
            latest_ts = float(now_latest["latest_ts"])
            break

    return latest_ts


def _get_message_count(slack_client, channel, saving_latest_ts, latest_ts, ts_offset):
    has_more = True
    result_per_day = defaultdict(int)
    while has_more and ts_offset >= latest_ts:
        histories = slack_client.channels.history(channel["id"], oldest=latest_ts, latest=ts_offset, count=10)
        for history in histories.body["messages"]:
            ts = float(history["ts"])
            now_datetime = datetime.fromtimestamp(ts)
            if saving_latest_ts < ts:
                saving_latest_ts = ts

            if ts_offset > ts:
                ts_offset = ts
                ts_offset += 0.0000001

            result_per_day[now_datetime.date()] += 1

        has_more = histories.body["has_more"]

    return result_per_day, saving_latest_ts
