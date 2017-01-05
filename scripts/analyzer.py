from collections import defaultdict
from datetime import datetime

from scripts import data_header_const

DEFAULT_LATEST_TS = 0


def get_latest_ts(latest_ts):
    return latest_ts if latest_ts == "0" else float(latest_ts)


def get_message_count(response, slack_client, now_latest_infos):
    results = []
    latest_info = []

    for channel in response.body["channels"]:
        latest_ts = DEFAULT_LATEST_TS

        for now_latest in now_latest_infos:
            if now_latest["id"] == channel["id"]:
                latest_ts = get_latest_ts(now_latest["latest_ts"])

        saving_latest_ts = latest_ts
        ts_offset = datetime.now().timestamp()
        result_per_day = _get_message_count(slack_client, channel, saving_latest_ts, latest_ts, ts_offset)

        for key, value in result_per_day.items():
            results.append({data_header_const.ID: channel["id"], data_header_const.NAME: channel["name"], data_header_const.COUNT: value, data_header_const.DATE: key})

        latest_info.append({data_header_const.ID: channel["id"], data_header_const.LATEST_TS: saving_latest_ts})

    if len(results) == 0:
        print("Nothing new data")

    return results, latest_info


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

    return result_per_day
