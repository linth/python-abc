from datetime import datetime, timedelta


class DateTimeBaseMixin:
    @staticmethod
    def generic_get_a_day(d: int = 0, t_hour: int = 0, t_minute: int = 0):
        return datetime.today() - timedelta(days=d,
                                            hours=t_hour,
                                            minutes=t_minute)

    @staticmethod
    def datetime_to_str(dt: datetime, format_dt: str = '%Y-%m-%d %H:%i:%S') -> str:
        """
        convert to string from datetime.
        :return:
        """
        return datetime.datetime.strftime(dt, format_dt)

    @staticmethod
    def str_to_datetime(str_dt: str, format_dt: str = '%Y-%m-%d %H:%i:%S') -> datetime:
        """
        convert to datetime from string.
        :return:
        """
        return datetime.datetime.strptime(str_dt, format_dt)

    @staticmethod
    def cal_diff_datetime(start: datetime, end: datetime) -> float:
        """
        difference between start of datetime and end of datetime.
        :param start:
        :param end:
        :return:
        """
        total_sec = (end - start).seconds
        t_hour = total_sec // 3600
        t_min = total_sec // 60 % 60
        return float(t_hour * 60 + t_min)


if __name__ == '__main__':
    idtm = DateTimeBaseMixin()
    res = idtm.generic_get_a_day()
    print('res', res)
