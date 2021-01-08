from abc import ABC, abstractmethod
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
import json

# TODO: 2020-12-04


class ApiCrudDelegate(ABC):
    # TODO: create CRUD class.
    """ delegate class for generic interface. """
    def __init__(self, request):
        self.request = request
        self.res = dict()
        self.data = None
        self.model = None

    def set_data(self):
        self.data = json.loads(self.request.body.decode('utf-8')['params'])

    def set_model(self, model):
        self.model = model

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass


class ApiAbsCrudBase(ApiCrudDelegate):
    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    @abstractmethod
    def action(self):
        pass

    def process(self):
        try:
            self.action()

            self.res['result'] = 'successful'
            self.res['message'] = '成功建立資料'
        except IntegrityError:
            self.res['result'] = 'failure'
            self.res['message'] = '資料重複'
        except ObjectDoesNotExist:
            self.res['result'] = 'failure'
            self.res['message'] = '資料不存在'
        except Exception as e:
            self.res['result'] = 'failure'
            self.res['message'] = str(e)
        return self.res


class ApiCreate(ApiAbsCrudBase):
    def action(self):
        """
        the action is to create an object.
        :return:
        """
        self.model.objects.create()


class ApiAbsCrudProductProfile(ApiCrudDelegate):
    # TODO: for the specific table, i.e., Product_profile.
    def create(self):
        try:
            # check the data cannot be empty.
            if self.data['modal_product_profile'] == '':
                raise Exception('資料不能為空')

            # using django ORM to create an object.
            # self.model.objects.create()

            self.res['result'] = 'successful'
            self.res['message'] = '成功建立資料'
        except IntegrityError:
            self.res['result'] = 'failure'
            self.res['message'] = '資料重複'
        except Exception as e:
            self.res['result'] = 'failure'
            self.res['message'] = str(e)
        return self.res

    def update(self):
        try:
            # check the data cannot be empty.
            if self.data['modal_product_profile'] == '':
                raise Exception('資料不能為空')

            # using django ORM to update an object.
            # p = self.model.objects.get(id=data['id'])
            # p.item_name = data['product_profile']
            # p.save()

            self.res['result'] = 'successful'
            self.res['message'] = '成功更新資料'
        except IntegrityError:
            self.res['result'] = 'failure'
            self.res['message'] = '資料重複'
        except ObjectDoesNotExist:
            self.res['result'] = 'failure'
            self.res['message'] = '資料不存在'
        except Exception as e:
            self.res['result'] = 'failure'
            self.res['message'] = str(e)
        return self.res

    def delete(self):
        try:
            # using django ORM to delete an object.
            # p = Product_profile.objects \
            #     .get(id=data['id'])
            # p.delet()
            self.res['result'] = 'successful'
            self.res['message'] = '成功刪除資料'
        except ObjectDoesNotExist:
            self.res['result'] = 'failure'
            self.res['message'] = '資料不存在'
        except Exception as e:
            self.res['result'] = 'failure'
            self.res['message'] = str(e)
        return self.res