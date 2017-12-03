import csv
import itertools

from aoc.shared import open_file


class Sheet:

    def __init__(self, raw_data):
        self.rows = self._parse(raw_data)

    @property
    def checksum(self):
        return sum(
            self._row_checksum(row)
            for row in self.rows
        )

    def _parse(self, raw_data):
        rows = [
            self._convert_row_to_ints(row)
            for row in csv.reader(
                raw_data,
                delimiter="\t"
            )
        ]
        return rows

    def _convert_row_to_ints(self, row):
        return [int(s) for s in row]

    def _row_checksum(self, row):
        raise NotImplementedError()


class MaxMinSheet(Sheet):

    def _row_checksum(self, row):
        return max(row) - min(row)


class EvenDivisorsSheet(Sheet):

    def _row_checksum(self, row):
        pairs = itertools.combinations(row, 2)
        for pair in pairs:
            high, low = max(pair), min(pair)
            if high % low == 0:
                return int(high / low)



if __name__ == '__main__':
    input_file = open_file("day2")
    sheet = MaxMinSheet(input_file)
    print(sheet.checksum)

    input_file = open_file("day2")
    sheet = EvenDivisorsSheet(input_file)
    print(sheet.checksum)
