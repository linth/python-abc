from base.ExportExcelBase import ExportExcel


class IeExportExcel(ExportExcel):
    def set_cell_style(self) -> None:
        pass

    def write_title(self):
        pass

    def write_data(self):
        pass


if __name__ == '__main__':
    iee = IeExportExcel()
    print(iee.write_data())
