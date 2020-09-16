class IeColor:
    # color
    pink = '\033[95m'
    blue = '\033[94m'
    success = '\033[92m'
    warning = '\033[93m'
    red = '\033[91m'

    # style
    end = '\033[0m'
    bold = '\033[1m'
    under_line = '\033[4m'


if __name__ == '__main__':
    print(IeColor.red + 'Hello world.' + IeColor.end)