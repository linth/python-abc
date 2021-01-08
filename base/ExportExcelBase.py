import xlwt
from django.http import HttpResponse
from abc import ABC, abstractmethod


class SetUpQuerySet(ABC):
    """ set up the queryset which is a result by searching. """
    def __init__(self):
        self.queryset = None

    def set_queryset(self, qs) -> None:
        """
        set up the queryset.
        :param qs: the data is a result by searching. (IeSearch class)
        :return:
        """
        self.queryset = qs


class SetUpCellStyle(ABC):
    """ set up the style of cell. """
    @abstractmethod
    def set_cell_style(self):
        """
        example:
            for i in range(0, 20):
                ws.col(i).width = 256 * 20
        :return:
        """
        pass


class WriteDataIntoExcel(ABC):
    """ write data into the excel. """
    @abstractmethod
    def write_title(self):
        """
        write the title of first row in the excel.
        example:
            for index, row in enumerate(rows):
                ws.write(0, index, row)
        :return:
        """
        pass

    @abstractmethod
    def write_data(self):
        """
        write queryset data into the excel.
        :return:
        """
        return NotImplementedError('write_data() must be overridden.')


class SetUpRows(ABC):
    """ set up the parameter of rows. """
    def __init__(self):
        self.rows = []

    def set_rows(self, rows) -> None:
        """
        the rows denotes the content of array.
        :param rows:
        :return:
        """
        self.rows = rows


class ExportExcelBase(ABC):
    def __init__(self) -> None:
        self.wb = xlwt.Workbook()
        self.response = HttpResponse(content_type='application/ms-excel')

    def set_workbook(self):
        return self.wb # encoding='utf-8'

    def set_worksheet(self, sheet_name):
        # cell_overwrite_ok=True
        return self.wb.add_sheet(sheet_name)


class ExportExcel(ExportExcelBase,
                  SetUpRows,
                  SetUpCellStyle,
                  SetUpQuerySet,
                  WriteDataIntoExcel):
    """ the abstract class of exporting excel. """
    pass


