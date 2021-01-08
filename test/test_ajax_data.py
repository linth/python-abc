from datetime import datetime
from datetime import timedelta


def check_all_params_have_received():
    """
    check all parameters have been received and value.
    :return:
    """
    pass


def check_magnitude_with_two_arg(first: datetime, second: datetime):
    """
    check the magnitude between two arguments, and make sure the second is larger than first.
    i.e., starting date and ending date.
    :param first:
    :param second:
    :return: True/False.
    """
    if isinstance(first, datetime) and isinstance(second, datetime):
        return second >= first
    else:
        return False


def add(first: (int), second: (int, float)):
    return first + second


if __name__ == '__main__':
    t = datetime.today()
    y = datetime.today() - timedelta(days=1)
    print(t, y)
    res = check_magnitude_with_two_arg(y, t)
    res2 = check_magnitude_with_two_arg(1, 2)

    print('res', res)
    print('res2', res2)

    res3 = add(1, 2)
    res4 = add(1.00000111, 2.2)
    print('res3', res3)
    print('res4', res4)


