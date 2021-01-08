from abc import ABC, abstractmethod


# TODO: [template] a basic class has several methods.
class ExcelStyleBase(ABC):
    """
    Document:
        - https://xlwt.readthedocs.io/en/latest/

    Application Programming Interface (API)
        - https://xlwt.readthedocs.io/en/latest/api.html
    """
    def __init__(self) -> None:
        pass

    def config_styles(self) -> None:
        """
        Most elements of an Excel file can be formatted.
        For many elements including cells, rows and columns,
        this is done by assigning a style, known as an XF record,
        to that element.

        This is done by passing an xlwt.XFStyle instance to the
        optional last argument to the various write methods
        and specialist set_cell_ methods.

        xlwt.Row and xlwt.Column instances have set_style methods
        to which an xlwt.XFStyle instance can be passed.
        :return:
        """
        pass

    def config_xfstyle(self) -> None:
        """
        In xlwt, the XF record is represented by the XFStyle
        class and its related attribute classes.
        :return:
        """
        pass

    def config_easyxf(self) -> None:
        """
        xlwt provides the easyxf helper to create XFStyle
        instances from human readable text and an optional
        string containing a number format.
        :return:
        """
        pass

    def config_pattern(self) -> None:
        pass

    def config_borders(self) -> None:
        pass

    def config_alignment(self) -> None:
        pass

    def config_font(self) -> None:
        pass

    def config_protection(self) -> None:
        """
        The protection features of the Excel file format are
        only partially implemented in xlwt.
        Avoid them unless you plan on finishing their
        implementation.
        :return:
        """
        pass

    def config_formatting_sheets_and_workbooks(self) -> None:
        pass

    def config_formula(self) -> None:
        """
        Formulae can be written by xlwt by passing an xlwt.Formula
        instance to either of the write methods or by using the
        set_cell_formula method of Row instances, bugs allowing.
        :return:
        """
        pass
