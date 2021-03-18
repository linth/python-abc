from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from exception.basic_exception import IeBaseException

"""
T = TypeVar('T')  # Can be anything
A = TypeVar('A', str, bytes)  # Must be str or bytes
"""
T = TypeVar("T")


class IeConversionDelegate(ABC):
    """ have input and output. """
    @abstractmethod
    def do_convert(self, input_data: T) -> T:
        """
        input and output are both existed.
        :param input_data:
        :return:
        """
        raise NotImplementedError('do_convert() must be overridden.')


class IeAbsConverter(Generic[T], IeConversionDelegate):
    def do_convert(self, item: T) -> T:
        try:
            return self.execute_conversion(item)
        except Exception as e:
            if isinstance(e, IeBaseException):
                raise e
            else:
                raise IeBaseException(__class__.__name__,
                                      'execute_conversion',
                                      'Error on involve execute_conversion()!',
                                      str(e),)

    @abstractmethod
    def execute_conversion(self, item: T) -> T:
        """
        execute conversion function.
        :param item:
        :return:
        """
        raise NotImplementedError('execute_conversion() must be overridden.')


class IeCallableDelegate(ABC):
    """ only have output. """
    @abstractmethod
    def call(self) -> T:
        """
        only output is existed without input.
        :return:
        """
        raise NotImplementedError('call() must be overridden.')


class IeAbsCallable(Generic[T], IeCallableDelegate):
    def call(self) -> T:
        try:
            return self.execute_generation()
        except Exception as e:
            if isinstance(e, IeBaseException):
                raise e
            else:
                raise IeBaseException(__class__.__name__,
                                      'execute_generation',
                                      'Error on involve execute_generation()!',
                                      str(e),)

    @abstractmethod
    def execute_generation(self) -> T:
        raise NotImplementedError('execute_generation() must be overridden.')


class IeFilterDelegate(ABC):
    """ have input and output, but output is belong to true/false. """
    @abstractmethod
    def predicate(self, item: T) -> bool:
        """
        for dealing with list. input and output are both existed.
        :param item:
        :return:
        """
        raise NotImplementedError('predicate() must be overridden.')


class IeFilter(Generic[T], IeFilterDelegate):
    def predicate(self, item: T) -> bool:
        try:
            return self
        except Exception as e:
            if isinstance(e, IeBaseException):
                return e
            else:
                raise IeBaseException(__class__.__name__,
                                      'execute_judgement',
                                      'Error on involve execute_judgement()!',
                                      str(e),)

    @abstractmethod
    def execute_judgement(self, item: T) -> bool:
        raise NotImplementedError('execute_judgement() must be overridden.')

# TODO: think about the situation as follows:
#  1) only have input.
#  2) not input and output.


class IeDataHolder(Generic[T]):
    def __init__(self, kept_data: T):
        self.kept_data = kept_data


class IeChain(Generic[T]):
    def __init__(self, data: T):
        self.ie_data_holder = IeDataHolder(data)

    def map(self, conversion: IeConversionDelegate):
        """
        chain function to get output from input class: IeConversionDelegate().
        :param conversion:
        :return:
        """
        input_data = self.ie_data_holder.kept_data
        print(f'Type of input: {type(input_data)}')
        output_data = conversion.do_convert(input_data)
        print(f'Type of output: {type(output_data)}')
        return IeChain(output_data)

    def on_complete(self) -> T:
        return self.ie_data_holder.kept_data
