"""
Reference
    -

Keyword:
    - strftime: convert to string from datetime (format the format of time).
    - strptime: convert to datetime format from string.
"""
import time
from datetime import datetime, timedelta
from mixin.DateTimeBaseMixin import DateTimeBaseMixin


class IeDateTimeMixin(DateTimeBaseMixin):
    """ the common calculation of datetime and usually used function for datetime. """
    @staticmethod
    def diff(start: datetime, end: datetime) -> datetime:
        """
        the diff between two days.
        :return:
        """
        return start - end





