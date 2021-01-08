import xlwt
from xlwt import XFStyle
from xlwt import Borders
from xlwt import Pattern
from xlwt import Font

from base.ExcelStyleBase import ExcelStyleBase
from abc import ABC, abstractmethod


# TODO: need to find the rule for the style of excel cell.
# TODO: 1) setting up the attributes: font, pattern, borders, xfstyle.
#       2) using xlwt.easyxf() to setting up them.


class IeExcelStyle(ExcelStyleBase):
    pass


# TODO: 希望只能唯獨
# TODO: StudentDelegate當作一個interface去阻擋其他對資料亂寫
class StudentDelegate(ABC):
    def get_student_numberr(self) -> str:
        pass

    def get_grade(self) -> int:
        pass


class StudentImpl(StudentDelegate):
    def __init__(self, number: str, grade: int):
        self.number = number
        self.grade = grade

    def get_student_number(self) -> str:
        return self.number

    def get_grade(self) -> int:
        return self.grade()


eee = StudentImpl("abc", 99)

ddd: StudentDelegate = eee
# ddd. -> cannot show number or grade.
ddd.get_grade()
ddd.get_student_numberr()


# TODO: title, date, week, content, summary, product, and so on.
class Title(ExcelStyleBase):
    def __init__(self) -> None:
        self.borders = Borders()
        self.pattern = Pattern()
        self.font = Font()
        self.xf_style = XFStyle()

    def config_font(self, color: str) -> object:
        self.font.height = 250
        self.font.colour_index = xlwt.Style.colour_map[color]
        self.font.bold = True
        return self

    def config_pattern(self, color: str) -> object:
        self.pattern.pattern = Pattern.SOLID_PATTERN
        self.pattern.pattern_fore_colour = xlwt.Style.colour_map[color]
        return self

    def config_borders(self) -> object:
        self.borders.left = 0x01
        self.borders.right = 0x01
        self.borders.top = 0x01
        self.borders.bottom = 0x01
        return self

    def config_alignment(self) -> object:
        self.xf_style.alignment.vert = 0x01
        self.xf_style.alignment.horz = 0x02
        return self

    def config_xf_style(self) -> object:
        self.config_font('white')
        self.config_borders()
        self.config_pattern('black')
        self.config_alignment()

        self.xf_style.num_format_str = 'YYYY-MM-DD'
        self.xf_style.font = self.font
        self.xf_style.borders = self.borders
        self.xf_style.pattern = self.pattern
        return self.xf_style
