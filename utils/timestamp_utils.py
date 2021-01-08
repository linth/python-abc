from datetime import datetime


def timestamp2utc(ts):
    """
    timestamp convert to utc.
    :param ts: timestamp
    :return:
    """
    return datetime.utcfromtimestamp(ts)


def string_time_to_specific_format(string_time: str) -> datetime:
    return datetime.strptime(string_time, '%Y-%m-%d %H:%M:%S')


# TODO: for time function, several functions should be created as follows:
#  1) the diffence between two days.
#  2) the format of string time need to previous split before use it.
