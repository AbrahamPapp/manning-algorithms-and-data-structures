import csv
import sys


class SpreadsheetReader:
    def __init__(self, csvfile_path: str) -> None:
        self.csvfile_path = csvfile_path

    def read_csv(self) -> None:
        contents = []
        with open(self.csvfile_path, encoding="latin-1") as csv_file:
            csv_contents = csv.reader(csv_file)
            for row in list(csv_contents)[1:]:
                contents.append(row)
            


def main():
    csvfile_path = sys.argv[1]

    SpreadsheetReader(csvfile_path=csvfile_path).read_csv()


main()
