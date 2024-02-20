import os.path
from pathlib import Path
from abc import ABC, abstractmethod


class CheckFile(ABC):

    def __init__(self, filename: str):
        if not isinstance(filename, str):
            raise ValueError

        self.filename = filename
        self.path = str(Path(__file__).parent / self.filename)
        self.extension = os.path.splitext(self.filename)[1][1::]

        if not os.path.exists(self.path):
            raise FileNotFoundError

    @abstractmethod
    def reader(self):
        pass

    def __str__(self):
        return f"CheckFile('{self.filename}')"


class TxtFileReader(CheckFile):
    def __init__(self, filename):
        super().__init__(filename)

    def reader(self):
        pass


class TxtFileConverter(TxtFileReader):
    def __init__(self, filename):
        super().__init__(filename)

    def txt_to_csv(self):
        pass

    def txt_to_xls(self):
        pass

    def txt_to_txt(self, recipient_file):
        pass


class CsvFileReader(CheckFile):
    def __init__(self, filename):
        super().__init__(filename)

    def reader(self):
        pass


class CsvFileConverter(CsvFileReader):
    def __init__(self, filename):
        super().__init__(filename)

    def csv_to_txt(self):
        pass

    def csv_to_xls(self):
        pass

    def csv_to_csv(self):
        pass


class XlsFileReader(CheckFile):
    def __init__(self, filename):
        super().__init__(filename)

    def reader(self):
        pass


class XlsFileConverter(XlsFileReader):
    def __init__(self, filename):
        super().__init__(filename)

    def xls_to_txt(self):
        pass

    def xls_to_csv(self):
        pass

    def xls_to_xls(self):
        pass


if __name__ == '__main__':
    pass
