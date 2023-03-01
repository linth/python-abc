'''
datetime custom class.
'''

import datetime



class MyCustomDateTime:
    def __init__(self, year, month, day, hour=0, minute=0, second=0, microsecond=0) -> None:
        self.dt = datetime.datetime(year, month, day, hour, minute, second, microsecond)
        self.now = None

    def __str__(self):
        return str(self.dt)

    def add_days(self, days):
        self.dt += datetime.timedelta(days=days)

    def add_hours(self, hours):
        self.dt += datetime.timedelta(hours=hours)

    def add_minutes(self, minutes):
        self.dt += datetime.timedelta(minutes=minutes)

    def add_seconds(self, seconds):
        self.dt += datetime.timedelta(seconds=seconds)

    def add_microseconds(self, microseconds):
        self.dt += datetime.timedelta(microseconds=microseconds)

    def get_date(self):
        return self.dt.date()

    def get_time(self):
        return self.dt.time()

    def get_datetime(self):
        return self.dt


class CalculateDateTime(MyCustomDateTime):
    def __init__(self):
        # get now.
        dt2 = datetime.datetime.now()
        super().__init__(dt2.year, dt2.month, dt2.day)
                
    def set_datetime_is_now(self):
        # set up the time is now.
        self.now = datetime.datetime.now()
        return self
    


if __name__ == '__main__':
    # 設定一天日期、時間
    one_day = MyCustomDateTime(2023, 1, 1, 0, 0, 0)
    print(one_day)
    
    # 增加一天
    one_day.add_days(1)
    print(one_day)
    
    # 增加兩個小時
    one_day.add_hours(2)
    print(one_day.get_time())
    
    # 增加三分鐘
    one_day.add_minutes(3)
    print(one_day.get_time())

    # 增加四秒
    one_day.add_seconds(4)
    print(one_day.get_time())

    # 增加五微秒
    one_day.add_microseconds(5)
    print(one_day.get_time())
    
    # 今日時間
    print(one_day.set_datetime_is_now())
    
    cdt = CalculateDateTime()
    print('get_now', cdt.get_now())
    
    print('set_datetime_is_now', cdt.set_datetime_is_now())
    
    