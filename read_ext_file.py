import os.path
from pathlib import Path
import pandas as pd


class TxtFile:
    def __init__(self, filename: str):
        if not isinstance(filename, str):
            raise ValueError

        self.filename = filename
        self.path = str(Path(__file__).parent / self.filename)
        self.extension = os.path.splitext(self.filename)[1][1::]

        if not os.path.exists(self.path):
            raise FileNotFoundError

    @property
    def reader(self):
        with open(self.path, 'r') as txt_file:
            reader = txt_file.read()
            return reader

    def txt_to_csv(self):
        pass

    def txt_to_xls(self):
        pass

    def txt_to_txt(self, recipient_file):
        pass

    def __str__(self):
        return f"TxtFile('{self.filename}')"


class CsvFile(TxtFile):
    def __init__(self, filename):
        super().__init__(filename)

    @property
    def reader(self):
        reader = pd.read_csv(self.path)
        return reader

    def csv_to_txt(self):
        pass

    def csv_to_xls(self):
        pass

    def csv_to_csv(self):
        pass

    def __str__(self):
        return f"CsvFile('{self.filename}')"


class XlsFile(TxtFile):
    def __init__(self, filename):
        super().__init__(filename)

    @property
    def reader(self):
        reader = pd.read_excel(self.path)
        return reader

    def xls_to_txt(self):
        pass

    def xls_to_csv(self):
        pass

    def xls_to_xls(self):
        pass

    def __str__(self):
        return f"XlsFile('{self.filename}')"


if __name__ == '__main__':
    pass
