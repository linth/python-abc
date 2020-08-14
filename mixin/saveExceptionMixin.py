from abc import ABC
from exception.basic_exception import IeBaseException


class SaveExceptionMixin(ABC):
    """ save exception error message. """
    model = None

    # TODO: must be modified with django and exception.
    def save(self):
        try:
            if self.model is not None:
                self.model.objects\
                    .create_or_update()
            else:
                raise IeBaseException(__class__.__name__,
                                      'save',
                                      f'{self.model} is None.')
        except Exception as e:
            raise IeBaseException(__class__.__name__,
                                  'save',
                                  f'{self.model} cannot be saved.')
