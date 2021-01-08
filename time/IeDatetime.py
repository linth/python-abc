"""
Reference
    -

Keyword:
    - strftime: convert to string from datetime (format the format of time).
    - strptime: convert to datetime format from string.
"""
import time
import datetime


class IeDateTime:
    """ usually used function for datetime. """
    @staticmethod
    def datetime_to_str(dt: datetime, format_dt: str = '%Y-%m-%d %H:%M:%S') -> str:
        """
        convert to string from datetime.
        :return:
        """
        return datetime.datetime.strftime(dt, format_dt)

    @staticmethod
    def str_to_datetime(str_dt: str, format_dt: str = '%Y-%m-%d %H:%M:%S') -> datetime:
        """
        convert to datetime from string.
        :return:
        """
        return datetime.datetime.strptime(str_dt, format_dt)

    @staticmethod
    def diff(start: datetime, end: datetime):
        """
        the diff between two days.
        :return:
        """
        return start - end


# now = datetime.datetime.today()
# one_day = '2020-09-23 11:00:00'
# od_dt = datetime.datetime.strptime(one_day, '%Y-%m-%d %H:%M:%S')
# print('od_dt', od_dt)
#
# res = IeDateTime().diff(now, od_dt)
# print(res, type(res))
