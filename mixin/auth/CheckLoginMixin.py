

class CheckAuthMixin:
    """ this is a mixin class. """
    def check_acc_and_pwd(self):
        """
        check the account and password have value or not.
        :return:
        """
        if self.account is None and self.password is None or \
                self.account == '' and self.password == '':
            # No content.
            self.context['error_msg'] = ''
        elif self.account is None or \
                self.password is None or \
                self.password == '' or \
                self.password == '':
            # miss or loss content partially.
            self.context['error_msg'] = 'Please fill in.'
        else:
            # others situation.
            self.context['error_msg'] = ''
        return self

    def check_some_rules(self):
        # TODO: account is email, regex.
        pass



