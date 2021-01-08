from abc import ABC, abstractmethod


class SetParams(ABC):
    @abstractmethod
    def set_params(self, input_params) -> None:
        """
        set up the conditions of searching.
        :return:
        """
        return NotImplementedError('set_params() must be overridden.')


class SetData(ABC):
    @abstractmethod
    def set_data(self, qs) -> None:
        """
        set up the data is result of queryset after searching.
        :return:
        """
        return NotImplementedError('set_data() must be overridden.')


class Process(ABC):
    @abstractmethod
    def process(self):
        """
        the process of searching.
        :return:
        """
        return NotImplementedError('process() must be overridden.')

    # TODO: convert(), callable(), ...


class SearchBase(SetParams, SetData, Process):
    """ the abstract class of searching. """
    pass


