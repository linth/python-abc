from datetime import datetime, timedelta
from utils.color import IeColor


# TODO: should be implement them as follows:
def django_datetime_to_str():
    """
    example:
        orcd = Oven_record.objects.get(id=1)
        print(orcd.oven_start_time)
        str_time = orcd.oven_start_time.strftime('%Y-%m-%d %H:%M:%S')
        print(str_time)
    :return:
    """
    pass


if __name__ == '__main__':
    # str_time = '2020-09-07 14:53:03.182654'
    #
    # res = datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S.%f')
    # print('Time: ', res, '\n', 'Type: ', type(res))
    #
    # now_time = datetime.now()
    # print('Now Time: ', now_time, '\n', 'Type: ', type(now_time))
    #
    # # diff
    # diff = (now_time - res)
    # print('Diff Time: (diff) ', diff, type(diff))
    # diffs = diff.seconds / 60
    # print('Diff Time: (diffs) ', diffs, type(diffs))
    # print('.....', diff.seconds)
    # print('.....', diff.days)
    #
    # t = datetime.now()
    # y = t - timedelta(days=1) - timedelta(seconds=50)
    # print('---------------------')
    # print('t', t, type(t),
    #       'y', y, type(y))
    # print(IeColor.pink, t-y, IeColor.end)
    # print(IeColor.pink, (t - y).total_seconds(), type((t - y).total_seconds()), IeColor.end)
    # print(IeColor.red, (t - y).total_seconds() // 60 // 60 // 24)
    # print(IeColor.red, datetime.now(), type(datetime.now()))
    # print(IeColor.red, datetime.utcnow(), type(datetime.utcnow()))
    # diff2 = t - y
    # print(IeColor.blue, 'diff2', diff2, type(diff2))
    # print(IeColor.warning, 'second', diff2.seconds, type(diff2.seconds), IeColor.end)
    #
    # str_time2 = '2020-09-20 11:11:11.00'
    # res2 = datetime.strptime(str_time2, '%Y-%m-%d %H:%M:%S.%f')
    # print('res2', res2, type(res2))
    #
    # dt_time3 = datetime.today()
    # print(IeColor().success, 'today', IeColor().end, IeColor().pink, dt_time3, IeColor().end)
    # res3 = datetime.strftime(dt_time3, '%Y-%m-%d %H:%M:%S.%f')
    # print('res3', res3, type(res3))

    y = datetime(2020, 12, 28, 0, 0, 0)
    t = datetime.now()
    print(t, type(t))
    print(y, type(y))
    print(t - y, type(t-y))
