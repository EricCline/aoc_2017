import unittest

from aoc.days.day5 import OffsetReader, ThreeOrMoreReader


class TestOffsetReader(unittest.TestCase):

    def test_increment_offset(self):
        r = OffsetReader([0, 1, 2, 3])
        r.increment_offset(0)
        self.assertEqual(1, r.offsets[0])

    def test_exits_if_offset_moves_outside_list(self):
        r = OffsetReader([1])
        self.assertEqual(1, r.run())

    def test_run_exits_in_correct_number_of_moves(self):
        r = OffsetReader([0, 3, 0, 1, -3])
        self.assertEqual(5, r.run())


class TestThreeOrdMoreReader(unittest.TestCase):

    def test_increment_offset_less_than_three(self):
        r = OffsetReader([0, 3, 4])
        r.increment_offset(0)
        self.assertEqual(1, r.offsets[0])

    def test_increment_offset_equal_three(self):
        r = OffsetReader([0, 3, 4])
        r.increment_offset(1)
        self.assertEqual(4, r.offsets[1])

    def test_increment_offset_greater_than_three(self):
        r = OffsetReader([0, 3, 4])
        r.increment_offset(2)
        self.assertEqual(5, r.offsets[2])

    def test_run_exits_in_correct_number_of_moves(self):
        r = ThreeOrMoreReader([0, 3, 0, 1, -3])
        self.assertEqual(10, r.run())
