import unittest

from aoc.days.day10 import Hash


class TestHash(unittest.TestCase):

    def setUp(self):
        numbers = [0, 1, 2, 3, 4]
        self.lengths = "3, 4, 1, 5"
        self.h = Hash(self.lengths, numbers)

    def test_hash(self):
        self.h.hash()
        self.assertEqual([3, 4, 2, 1, 0], self.h._numbers)
