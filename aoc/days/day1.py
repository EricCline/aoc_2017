from collections import deque

from aoc.shared import open_file


class Reducer:

    def __init__(self, digits, offset=1):
        self.digits = digits
        self.offset = offset

    def reduce(self):
        return sum(
            self._num_if_equal(a, b)
            for a, b in self._pairs()
        )

    def _pairs(self):
        rotated = deque(self.digits)
        rotated.rotate(self.offset)
        return zip(
            self.digits,
            rotated
        )

    def _num_if_equal(self, a, b):
        if a == b:
            return int(a)
        return 0


if __name__ == '__main__':
    input_data = open_file("day1").read().strip()
    reducer = Reducer(input_data)
    print(reducer.reduce())
    reducer = Reducer(
        input_data,
        offset=int(len(input_data) / 2))
    print(reducer.reduce())
