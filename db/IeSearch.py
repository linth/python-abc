"""
Reference:
    - https://www.python-course.eu/python3_abstract_classes.php
"""
from base.SearchBase import SearchBase
from abc import ABC, abstractmethod
from django.db import models


class IeSearch(SearchBase):

    def __init__(self):
        self.data = None
        self.params_conditions = None

    def set_params(self, input_params) -> None:
        self.params_conditions = input_params

    def set_data(self, qs) -> None:
        self.data = qs

    def process(self):
        for i in self.data:
            if i['name'] == self.params_conditions['name']:
                print(i)


# TODO: combine SQLAlchemy and python.
# TODO: abstractmethod class problems.


if __name__ == '__main__':
    data = [
        {'name': 'george', 'age': 20},
        {'name': 'peter', 'age': 32},
        {'name': 'JJ', 'age': 46},
    ]

    res = IeSearch()
    res.set_params({'name': 'george'}, )
    res.set_data(data)
    res.process()

    print(res.data)
    print(res.params_conditions)
