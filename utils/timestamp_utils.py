from datetime import datetime


def timestamp2utc(ts):
    """
    timestamp convert to utc.
    :param ts: timestamp
    :return:
    """
    return datetime.utcfromtimestamp(ts)
