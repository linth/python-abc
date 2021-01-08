from typing import Generic, TypeVar
from chain.chain_operations import IeAbsConverter
from chain.chain_operations import IeAbsCallable
# TODO: general interface to design backend API.

T = TypeVar("T")


class BaseAjaxConverter(IeAbsConverter):
    """ general ABC class provides JSON data for front-end. """
    def execute_conversion(self, item: T) -> T:
        pass


class BaseAjaxCallable(IeAbsCallable):
    """ general ABC class provides JSON data for front-end. """
    def execute_generation(self) -> T:
        pass

