import unittest

from aoc.days.day1 import Reducer


class TestReducer(unittest.TestCase):

    def test_reducer_offset_1(self):
        self.assertEqual(3, Reducer("1122").reduce())
        self.assertEqual(4, Reducer("1111").reduce())
        self.assertEqual(0, Reducer("1234").reduce())
        self.assertEqual(9, Reducer("91212129").reduce())

    def test_reducer_offset_half(self):
        for expectation, input in (
            (6, "1212"),
            (0, "1221"),
            (4, "123425"),
            (12, "123123"),
            (4, "12131415")
        ):
            r = Reducer(input, offset=int(len(input) / 2))
            self.assertEqual(expectation, r.reduce())
