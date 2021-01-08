"""
extend the chain operations.
"""
from chain.chain_operations import *


class IeCombineConvertCallable(Generic[T], IeAbsConverter):
    """ combine convert and callable function. """
    def do_convert(self, item: T = None) -> T:
        try:
            if item is None:
                return self.execute_generation()    # for convert function.
            else:
                return self.execute_conversion(item)    # for callable function.
        except Exception as e:
            if isinstance(e, IeBaseException):
                raise e
            else:
                raise IeBaseException(__class__.__name__,
                                      'execute_conversion',
                                      'Error on involve execute_conversion()!',
                                      str(e),)

    # @abstractmethod
    def execute_conversion(self, item: T) -> T:
        """
        execute conversion function.
        :param item:
        :return:
        """
        raise NotImplementedError('execute_conversion() must be overridden.')

    # @abstractmethod
    def execute_generation(self) -> T:
        """
        execute callable function.
        :return:
        """
        raise NotImplementedError('execute_generation() must be overridden.')


# class IeSettingDelegate(ABC):
#     """ have input, but no output. """
#     @abstractmethod
#     def set(self, item: T) -> T:
#         """
#         for setting a self value.
#         :param item:
#         :return:
#         """
#         raise NotImplementedError('set() must be overridden.')


# class IeSetting(Generic[T], IeSettingDelegate):
#     """ it's for settings self variable. """
#     def __init__(self, item: dict):
#         """
#         if using dict() as argument, it still not understand the dictionary().
#         using for-loop to
#         :param item:
#         """
#         pass
#
#     def set(self, item: T):
#         try:
#             self.execute_setting()
#         except Exception as e:
#             if isinstance(e, IeSettingDelegate):
#                 raise e
#             else:
#                 raise IeBaseException(__class__.__name__,
#                                       'set',
#                                       'Error on involve execute_setting()!',
#                                       str(e),)
#
#     @abstractmethod
#     def execute_setting(self, item: T):
#         raise NotImplementedError('execute_setting() must be overridden.')
