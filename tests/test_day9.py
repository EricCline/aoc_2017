import unittest

from aoc.days.day9 import groups, State


class TestNegation(unittest.TestCase):

    def test_groups_negates_properly(self):
        s = State()
        d = "!"
        groups(d, s)
        self.assertTrue(s.negate)
        s = State()
        d = "!!"
        groups(d, s)
        self.assertFalse(s.negate)
        s = State()
        d = "!!!"
        groups(d, s)
        self.assertTrue(s.negate)

    def test_groups_deals_with_groups(self):
        s = State()
        d = "{{{}}}"
        groups(d, s)
        self.assertEqual(6, s.group_score)
        s = State()
        d = "{{},{}}"
        groups(d, s)
        self.assertEqual(5, s.group_score)
        s = State()
        d = "{{{},{},{{}}}}"
        groups(d, s)
        self.assertEqual(16, s.group_score)
        s = State()
        d = "{<a>,<a>,<a>,<a>}"
        groups(d, s)
        self.assertEqual(1, s.group_score)
        s = State()
        d = "{{<ab>},{<ab>},{<ab>},{<ab>}}"
        groups(d, s)
        self.assertEqual(9, s.group_score)
        s = State()
        d = "{{<!!>},{<!!>},{<!!>},{<!!>}}"
        groups(d, s)
        self.assertEqual(9, s.group_score)
        s = State()
        d = "{{<a!>},{<a!>},{<a!>},{<ab>}}"
        groups(d, s)
        self.assertEqual(3, s.group_score)

    def test_counts_garbage(self):
        s = State()
        d = "<>"
        groups(d, s)
        self.assertEqual(0, s.garbage_count)
        s = State()
        d = "<random characters>"
        groups(d, s)
        self.assertEqual(17, s.garbage_count)
        s = State()
        d = "<<<<>"
        groups(d, s)
        self.assertEqual(3, s.garbage_count)
        s = State()
        d = "<{!>}>"
        groups(d, s)
        self.assertEqual(2, s.garbage_count)
        s = State()
        d = "<!!>"
        groups(d, s)
        self.assertEqual(0, s.garbage_count)
        s = State()
        d = "<!!!>>"
        groups(d, s)
        self.assertEqual(0, s.garbage_count)
        s = State()
        d = '<{o"i!a,<{i<a>'
        groups(d, s)
        self.assertEqual(10, s.garbage_count)
