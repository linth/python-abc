from abc import ABC, abstractmethod


class IeAuthBase(ABC):
    def __init__(self):
        self.resp_result = dict()

    @abstractmethod
    def auth(self) -> dict:
        return NotImplementedError('auth() must be overridden.')


class IeAbsAuth(ABC, IeAuthBase):
    """ abstract class with django default authentication. """
    def __init__(self, account: str, password):
        self.account = account
        self.password = password


class IeAbsLdap(ABC, IeAuthBase):
    """ ldap abstract base class. """
    def __init__(self, host: str, user: str, password):
        self.host = host
        self.user = user
        self.password = password


class IeAbsGoogle(ABC, IeAuthBase):
    """ google abstract base class. """
    pass


class IeAbsFacebook(ABC, IeAuthBase):
    """ facebook abstract base class. """
    pass




