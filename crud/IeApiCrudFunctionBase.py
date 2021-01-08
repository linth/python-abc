from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# Function-based API.
@csrf_exempt
def api_create_object(request) -> JsonResponse:
    """
    provide an API to create object.
    :param request:
    :return:
    """
    try:
        res = dict()
        data = json.loads(request.body.decode('utf-8'))['params']

        if data['modal_product_profile'] == '':
            raise Exception('資料不能為空')

        # using django ORM to create object.
        # Product_profile.objects.create()
        res['result'] = 'successful'
        res['message'] = '成功建立資料'
    except IntegrityError:
        res['result'] = 'failure'
        res['message'] = '資料重複'
        return JsonResponse(res, safe=False)
    except Exception as e:
        res['result'] = 'failure'
        res['message'] = str(e)
    return JsonResponse(res, safe=False)


@csrf_exempt
def api_update_object(request) -> JsonResponse:
    """
    provide an API to update object.
    :param request:
    :return:
    """
    try:
        res = dict()
        data = json.loads(request.body.decode('utf-8'))['params']

        if data['product_profile'] == '':
            raise Exception('資料不能為空')

        # using django ORM to update object.
        # p = Product_profile.objects.get(), ...
        res['result'] = 'successful'
        res['message'] = '成功更新資料'
    except IntegrityError:
        res['result'] = 'failure'
        res['message'] = '資料重複'
    except ObjectDoesNotExist:
        res['result'] = 'failure'
        res['message'] = '資料不存在'
    except Exception as e:
        res['result'] = 'failure'
        res['message'] = str(e)
    return JsonResponse(res, safe=False)


@csrf_exempt
def api_delete_object(request) -> JsonResponse:
    """
    provide an API to update object.
    :param request:
    :return:
    """
    try:
        res = dict()
        data = json.loads(request.body.decode('utf-8'))['params']

        # using django ORM to delete object.
        # p = Product_profile.objects.get(), ...
        res['result'] = 'successful'
        res['message'] = '成功刪除資料'
    except ObjectDoesNotExist:
        res['result'] = 'failure'
        res['message'] = '資料不存在'
    except Exception as e:
        res['result'] = 'failure'
        res['message'] = str(e)
    return JsonResponse(res, safe=False)




