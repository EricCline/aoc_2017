import unittest

from aoc.days.day7 import find_bottom_program, parse_line, build_program_data, get_complete_weight, find_unbalanced


class TestParseLine(unittest.TestCase):

    def parse_line_splits_line_with_children(self):
        l = 'fwft (72) -> ktlj, cntj, xhth'
        p = parse_line(l)
        self.assertEqual('fwft', p[0])
        self.assertEqual(72, p[1])
        self.assertEqual(['ktlj', 'cntj', 'xhth'], p[2])

    def test_program_splits_line_without_children(self):
        l = 'fwft (72)'
        p = parse_line(l)
        self.assertEqual('fwft', p[0])
        self.assertEqual(72, p[1])
        self.assertEqual([], p[2])


class TestDay7(unittest.TestCase):

    def setUp(self):
        lines = [
            "pbga (66)",
            "xhth (57)",
            "ebii (61)",
            "havc (66)",
            "ktlj (57)",
            "fwft (72) -> ktlj, cntj, xhth",
            "qoyq (66)",
            "padx (45) -> pbga, havc, qoyq",
            "tknk (41) -> ugml, padx, fwft",
            "jptl (61)",
            "ugml (68) -> gyxo, ebii, jptl",
            "gyxo (61)",
            "cntj (57)",
        ]

        self.programs = [Program(*parse_line(l)) for l in lines]
        self.program_data = build_program_data(lines)

    def test_find_bottom_returns_program_that_is_not_a_child(self):
        self.assertEqual('tknk', find_bottom_program(self.programs))

    def test_get_complete_weight_recurses(self):
        expected_weight = sum(p.weight for p in self.programs)
        weight = get_complete_weight('tknk', self.program_data)
        self.assertEqual(expected_weight, weight)

    def test_find_unbalanced(self):
        unbalanced = find_unbalanced('tknk', self.program_data)
        self.assertEqual({'ugml': 251, 'padx': 243, 'fwft': 243}, unbalanced)

    def test_find_unbalanced_recurse(self):

        program_data = {
            'a': {'weight': 0, 'children': ['aa', 'aaa', 'aaaa']},
            'aa': {'weight': 1, 'children': []},
            'aaa': {'weight': 1, 'children': []},
            'aaaa': {'weight': 1, 'children': ['b', 'bb']},
            'b': {'weight': 2, 'children': []},
            'bb': {'weight': 3, 'children': []},
        }
        unbalanced = find_unbalanced('a', program_data)
        self.assertEqual({'b': 2, 'bb': 3}, unbalanced)
