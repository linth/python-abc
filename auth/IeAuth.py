from ldap3 import Server, Connection, ALL
# from django.contrib.auth.models import User, Group, Permission
from abc import ABC, abstractmethod
# from auth.IeAbsAuth import IeAbsAuth


# class AuthSettingDelegate(ABC):
#     def __init__(self, host, user, pwd):
#         self.host = host
#         self.user = user
#         self.pwd = pwd
#
#
# class IeAbsAuthSetting(AuthSettingDelegate):
#     def __init__(self, host, user, pwd):
#         host = 'ad1.goglobal.com.tw'
#         super().__init__(host, user, pwd)
#
#
class IeAuthAbc:
    def auth(self):
        return NotImplementedError('auth() must be overridden.')

    def is_user_existed(self):
        return NotImplementedError('is_user_existed() must be overridden.')


class IeAuthAbstract(IeAuthAbc):
    def __init__(self, host_address: str = None, user: str = None, pwd: str = None):
        self.host: str = host_address
        self.user: str = user
        self.pwd: str = pwd
        self.resp: dict = dict()


class IeAuth(IeAuthAbstract):
    def __init__(self, user: str = None, pwd: str = None, host_address: str = None):
        if host_address is None:
            host_address = 'ad1.goglobal.com.tw'
        super().__init__(host_address, user, pwd)

    def auth(self) -> dict:
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

            server = Server(self.host, get_info=ALL)
            Connection(server,
                       user=self.user,
                       password=self.pwd,
                       auto_bind=True)
            self.resp['result'] = 'connection successful.'
            self.resp['is_successful'] = True
            return self.resp
        except Exception as e:
            self.resp['result'] = 'connection fail.'
            self.resp['is_successful'] = False
            self.resp['error_msg'] = str(e)
            return self.resp

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
    # iaas = IeAbsAuthSetting('', 'george_lin', '1111')
    # print('host', iaas.host)
    # print('user', iaas.user)
    # print('password', iaas.pwd)
    # g = Group.objects.all()
    # print('g', g)

    ia = IeAuth('george_lin', '111') \
        .auth()
    print('the result of auth: ', ia)







