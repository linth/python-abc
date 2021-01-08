from abc import ABC
from exception.basic_exception import IeBaseException

# TODO: list all thing should be saved.
#  1) Exception
#  2) Django model
#  3) Event


class SaveExceptionMixin:
    """ Mixin class: save exception error message. """
    def save_exception(self):
        try:
            if self.model is not None:
                self.model.objects\
                    .create_or_update()
            else:
                raise IeBaseException(__class__.__name__,
                                      'save',
                                      f'{self.model} isn\'t found.')
        except Exception as e:
            if isinstance(e, IeBaseException):
                raise e
            else:
                raise IeBaseException(__class__.__name__,
                                      'save',
                                      f'{self.model} cannot be saved.',
                                      str(e), )


class SaveModelMixin:
    """ Mixin class: save the data of model. """
    def save_model(self):
        pass

