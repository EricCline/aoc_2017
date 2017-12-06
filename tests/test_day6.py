import unittest

from aoc.days.day6 import Memory


class TestMemory(unittest.TestCase):

    def test_remove_max_bank(self):
        m = Memory([0, 2, 7, 0])
        max_bank, max_index = m._remove_max_bank()
        self.assertEqual([0, 2, 0, 0], m.banks)
        self.assertEqual(7, max_bank)
        self.assertEqual(2, max_index)

    def test_remove_max_bank_selects_lowest_index_when_tie(self):
        m = Memory([2, 2, 0, 0])
        max_bank, max_index = m._remove_max_bank()
        self.assertEqual([0, 2, 0, 0], m.banks)
        self.assertEqual(2, max_bank)
        self.assertEqual(0, max_index)

    def test_redistribution_indices(self):
        m = Memory([0, 2, 7, 0])
        indices = m._redistribution_indices(7, 2)
        self.assertEqual([3, 0, 1, 2, 3, 0, 1], indices)

    def test_add_snapshot(self):
        m = Memory([0, 2, 7, 0])
        self.assertEqual([[0, 2, 7, 0]], m._snapshots)
        m._add_snapshot()
        self.assertEqual([[0, 2, 7, 0], [0, 2, 7, 0]], m._snapshots)

    def test_redistribute_multiple(self):
        m = Memory([0, 2, 7, 0])
        m._redistribute()
        self.assertEqual([2, 4, 1, 2], m.banks)
        m._redistribute()
        self.assertEqual([3, 1, 2, 3], m.banks)
        m._redistribute()
        self.assertEqual([0, 2, 3, 4], m.banks)
        m._redistribute()
        self.assertEqual([1, 3, 4, 1], m.banks)
        m._redistribute()
        self.assertEqual([2, 4, 1, 2], m.banks)

    def test_redistribute(self):
        m = Memory([0, 2, 7, 0])
        m.redistribute()
        self.assertEqual(5, m.redistribution_count)

    def test_loop_size(self):
        m = Memory([0, 2, 7, 0])
        m.redistribute()
        self.assertEqual(4, m.infinite_loop_size)
