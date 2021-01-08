from auth.IeAbsBaseAuth import IeAbsAuth
from auth.IeAbsBaseAuth import IeAbsLdap
from mixin.auth.CheckLoginMixin import CheckAuthMixin


# ***********************************************
# Single option authentication.
# ***********************************************
class IeInterfaceAuth(IeAbsAuth, CheckAuthMixin):
    """ interface class for django default authentication. """
    pass


class IeInterfaceLdapAuth(IeAbsLdap, CheckAuthMixin):
    """ interface class for ldap. """
    pass


# ***********************************************
# combination option authentication.
# ***********************************************
class IeInterfaceLdapAndAuth(IeAbsAuth, IeAbsLdap, CheckAuthMixin):
    """ interface class combines with ldap and django default authentication. """
    pass


if __name__ == '__main__':
    # i = IeAbsAuth(111, '3313')
    # print(i.account)
    # print(i.password)
    #
    # i.check_acc_and_pwd()
    # print(i.context['error_msg'])
    pass


