import binascii
from collections import deque
import operator
from functools import reduce

from aoc.shared import open_file


class Hash:

    def __init__(self, lengths, numbers=None):
        self._lengths = self._parse_lengths(lengths)
        self._numbers = list(numbers or range(0, 256))
        self._skip = 0
        self._rotations = 0

    def _parse_lengths(self, lengths):
        return [int(i) for i in lengths.split(',')]

    def _process_length(self, length):
        self._numbers[:length] = reversed(self._numbers[:length])
        rotation = (length + self._skip) * -1
        self._rotate_numbers(rotation)
        self._skip += 1

    def hash(self):
        self._hash()
        self._undo_rotations()

    def _hash(self):
        for length in self._lengths:
            self._process_length(length)

    def _undo_rotations(self):
        self._rotate_numbers(self._rotations * -1)

    def _rotate_numbers(self, rotation):
        d = deque(self._numbers)
        d.rotate(rotation)
        self._numbers = list(d)
        self._rotations += rotation

    def product(self, index_a, index_b):
        return self._numbers[index_a] * self._numbers[index_b]


class AsciiHash(Hash):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._dense_hash = []
        self.hex = ''

    def _parse_lengths(self, lengths):
        return [ord(i) for i in lengths] + [17, 31, 73, 47, 23]

    def hash(self):
        for i in range(64):
            self._hash()
        self._undo_rotations()
        self._compact_hash()
        self._hexlify()
        return self._hex

    def _compact_hash(self):
        self._dense_hash = []
        for _ in range(16):
            block = [self._numbers.pop(0) for i in range(16)]
            self._dense_hash.append(reduce(operator.xor, block))

    def _hexlify(self):
        self._hex = binascii.hexlify(bytearray(self._dense_hash))


if __name__ == '__main__':
    lengths = open_file("day10").read().strip()
    h = Hash(lengths)
    h.hash()
    print(h.product(0, 1))
    h = AsciiHash(lengths)
    print(h.hash())
