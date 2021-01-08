"""
    use django listview to create a template backend.
"""
from django.views.generic import ListView
from abc import ABC, abstractmethod


class IeDelegateList(ABC, ListView):
    def get_context_data(self, *args, **kwargs) -> dict:
        """
        get some parameters or data from backend.
        :param args:
        :param kwargs:
        :return:
        """
        # context = super().get_context_data(*args, **kwargs)
        # return context
        pass

    def get_queryset(self) -> None:
        """
        get the queryset from database.
        :return:
        """
        pass


class ExampleList(IeDelegateList):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # context['msg'] = 'hi, everyone.'
        print(f'type: {context}, {dir(context)}')
        return context

    def get_queryset(self):
        return []


if __name__ == '__main__':
    idl = IeDelegateList()
    print(idl.get_queryset())

    el = ExampleList()
    res = el.get_context_data()

    # print(res['msg'])




