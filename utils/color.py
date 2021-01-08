

class IeColor:
    """ the class is for printing information with color. """
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

    """
    examples:
        - add font color.
            30 ~ 37, i.e., \033[30m ~ \033[37m
        - add background color.
            40 ~ 47, i.e., \033[40;37m ~ \033[47;37m
    others:
        \33[0m 關閉所有屬性
        \33[1m 設置高亮度
        \33[4m 下劃線
        \33[5m 閃爍
        \33[7m 反顯
        \33[8m 消隱
        \33[30m -- \33[37m 設置前景色
        \33[40m -- \33[47m 設置背景色
        \33[nA 光標上移n行
        \33[nB 光標下移n行
        \33[nC 光標右移n行
        \33[nD 光標左移n行
        \33[y;xH設置光標位置
        \33[2J 清屏
        \33[K 清除從光標到行尾的內容
        \33[s 保存光標位置
        \33[u 恢復光標位置
        \33[?25l 隱藏光標
        \33[?25h 顯示光標 
    """


class A:
    def show_info(self):
        print('info')

    def add(self, x, y):
        res = {}
        try:
            res['value'] = x+y
            res['result'] = 'successful'
        except TypeError as e:
            # raise e
            B().error_msg('class A: add(), ' + str(e))
        except Exception as e:
            # print('error of add().')
            # res['result'] = '[Error] ' + str(e)
            # raise e
            B().error_msg('class A: add(), ' + str(e))
        return res


class B:
    def error_msg(self, msg: str):
        print('[Error] ', msg)


class Foo(object):
    def bar(self):
        print("Foo.bar called")
        return self

    def baz(self):
        print("Foo.baz called")
        return self


if __name__ == '__main__':
    # TODO: more examples for training.
    # a = A()
    # res = a.add(1, '3')
    # print('res', res)
    foo = Foo()
    foo2 = foo.bar().baz()

    print('id(foo): ', id(foo))
    print('id(foo2): ', id(foo2))
