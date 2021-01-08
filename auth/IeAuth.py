from django.contrib.auth.models import User, Group, Permission
from ldap3 import Server, Connection, ALL
from abc import ABC, abstractmethod
from auth.IeAbsAuth import IeAbsAuth


class AuthSettingDelegate(ABC):
    def __init__(self, host, user, pwd):
        self.host = host
        self.user = user
        self.pwd = pwd


class IeAbsAuthSetting(AuthSettingDelegate):
    def __init__(self, host, user, pwd):
        host = 'ad1.goglobal.com.tw'
        super().__init__(host, user, pwd)


class IeAuth(IeAbsAuth):
    def __init__(self, host_address=None, user=None, pwd=None):
        self.host = host_address
        self.user = user
        self.pwd = pwd

    def auth(self):
        """
        auth with AD server of microsoft.
        :return:
        """
        try:
            if self.user is None or \
                    self.user == '' or \
                    self.pwd is None or \
                    self.pwd == '':
                raise Exception('[錯誤] 帳密資料有誤!')

            if self.host is None:
                self.host = 'ad1.goglobal.com.tw'

            server = Server(self.host, get_info=ALL)
            Connection(server,
                       user=self.user,
                       password=self.pwd,
                       auto_bind=True)
            return True
        except Exception as e:
            return False

    def add_user(self):
        pass


if __name__ == '__main__':
    # res = IeAuth('ad1.goglobal.com.tw', 'george_lin', '1111')\
    #     .auth()
    #
    # if res is True:
    #     print('successful')
    # else:
    #     print('failure')
    iaas = IeAbsAuthSetting('', 'george_lin', '1111')
    print('host', iaas.host)
    print('user', iaas.user)
    print('password', iaas.pwd)
    g = Group.objects.all()
    print('g', g)







