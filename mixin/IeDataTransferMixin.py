from utils.json_utils import obj_to_json
from abc import ABC


# TODO: two main transfer data:
#  1) Data type, i.e., JSON, YAML, TOML.
#  2) File type, i.e., excel, csv, pdf, xml, and so on.
#  3) others, i.e., bin file.


class IeAbsConvertDataMixin(ABC):
    pass


class IeAbsExportFileMixin(ABC):
    pass


class IeConvert2JsonMixin(IeAbsConvertDataMixin):
    """ Mixin class: convert to data type from object. """
    def obj_to_json(self) -> str:
        """
        convert to json from object.
        :return:
        """
        return obj_to_json(self.object)


class IeConvert2YamlMixin(IeAbsConvertDataMixin):
    """ Mixin class: convert to yaml from object. """
    def obj_to_yaml(self):
        """
        convert to yaml from object.
        :return:
        """
        pass


class IeConvert2TomlMixin(IeAbsConvertDataMixin):
    """ Mixin class: convert to toml from object. """
    def obj_to_toml(self):
        """
        convert to toml from object.
        :return:
        """
        pass


class IeExport2CsvFileMixin(IeAbsExportFileMixin):
    """ Mixin class: export to csv file. """
    def to_csv(self):
        pass


class IeExport2ExcelFileMixin(IeAbsExportFileMixin):
    """ Mixin class: export to excel file. """
    def to_excel(self):
        pass


class IeExport2PdfFileMixin(IeAbsExportFileMixin):
    """ Mixin class: export to pdf file. """
    def to_pdf(self):
        pass


class IeExport2XmlFileMixin(IeAbsExportFileMixin):
    """ Mixin class: export to xml file. """
    def to_xml(self):
        pass


