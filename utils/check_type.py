

def check_type(func):
    def warp():
        print(f'check_type(), {func.__name__}')
        func()
    return warp()


@check_type
def add(a: int, b: int):
    print(f'a: {a}')
    print(f'b: {b}')
    return a+b


if __name__ == '__main__':
    add(1, 2)
