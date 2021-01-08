"""
References:
    - http://tdongsi.github.io/blog/2016/05/21/convert-python-objects-to-json/
"""
import json


def obj_to_json(given: object) -> str:
    """
    convert to json from object.
    :param given:
    :return:
    """
    try:
        return json.dumps(given, default=vars, indent=4)
    except Exception as e:
        print(f'error on obj_to_json: {e}')
        return ''


# TODO: try this function.
#  using dumps(), loads(),
