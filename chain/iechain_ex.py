from .chain_operations import IeAbsConverter
from .chain_operations import IeAbsCallable
from .chain_operations import IeFilter
from typing import Generic, TypeVar
from .chain_operations import IeChain

T = TypeVar("T")


class A(IeAbsConverter):
    def execute_conversion(self, item: T) -> T:
        print(f'A class execute_conversion.')
        print('item', item)
        item += 1
        print('item', item)
        return item


class B(IeFilter):
    def execute_judgement(self, arr):
        res = False
        for i in arr:
            if i == 1:
                res = True
        return res


class C(IeAbsCallable):
    def execute_generation(self) -> T:
        # for i in range(0, 10):
        #     print(f'--->, {i}')
        pass


# class D(IeSetting):
#     def __init__(self, item: T):
#         self.temp = item
#
#     def execute_setting(self, item: T):
#         if isinstance(item, (int, float)):
#             self.temp = item
#         else:
#             pass


# class E(IeCombineConvertCallable):
#     def execute_conversion(self, item: T) -> T:
#         for i in range(item):
#             print('->', i)
#
#
# class F(IeCombineConvertCallable):
#     def execute_generation(self) -> T:
#         print(f'class F: execute_generation()')


class G(IeAbsConverter):
    def execute_conversion(self, item: T) -> T:
        if isinstance(item, int):
            print(f'before: {item}, after: {item + 1}')
        else:
            print(f'the type of item isn\'t INT.')


if __name__ == '__main__':
    a = A()
    # b = A()
    # r = IeChain(2).map(a)
    # print(r)

    g = G()
    g2 = G()
    r2 = IeChain(2).map(g).on_complete()
    print('r2', r2)

    # arr = [1, 2, 3, 4]
    # b = B()
    # res = b.execute_judgement(arr)
    # # print('res', res)
    #
    # c = C()
    # c.call()

    # g = G()
    # g.execute_conversion(b)
    # r = IeChain(2).map(a)
    # print('r', r)

    # import random
    # # print(random.random())
    #
    # for i in range(0, 10):
    #     d = D()
    #     d.execute_setting(random.random()*i)
    #     print(d.temp)

    # e = E()
    # e.do_convert(10)
    #
    # f = F()
    # f.do_convert()


