from abc import ABC
from chain_operations import *


# TODO: which things should be checked.
#  1) model.
#  2) each attr in certain model.
#  3) for unittest.
#  4) others ?


class CheckModel(IeAbsConverter):
    """ check the data of model. """
    def execute_conversion(self, item: T) -> T:
        pass


class CheckAttr(IeAbsConverter):
    """ check the attribute of modal. """
    def execute_conversion(self, item: T) -> T:
        pass
