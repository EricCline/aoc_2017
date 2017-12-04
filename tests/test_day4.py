import unittest

from aoc.days.day4 import (
    count_valids,
    unique_words,
    split_to_words,
    no_anagrams
)


class TestDay4(unittest.TestCase):

    def test_unique_words(self):
        self.assertTrue(unique_words(["aa", "bb", "cc", "dd", "ee"]))
        self.assertFalse(unique_words(["aa", "bb", "cc", "dd", "aa"]))
        self.assertTrue(unique_words(["aa", "bb", "cc", "dd", "aaa"]))

    def test_count_valids_unique_words(self):
        phrases = [
            ["aa", "bb", "cc", "dd", "ee"],
            ["aa", "bb", "cc", "dd", "aa"],
            ["aa", "bb", "cc", "dd", "aaa"]
        ]
        self.assertEqual(2, count_valids(phrases, unique_words))

    def test_split_to_words(self):
        self.assertEqual(["aa", "bb", "cc"], split_to_words("aa bb cc"))

    def test_no_anagrams(self):
        self.assertTrue(no_anagrams(["abcde", "fghij"]))
        self.assertFalse(no_anagrams(["abcde", "xyz", "ecdab"]))
        self.assertTrue(no_anagrams(["a", "ab", "abc", "abd", "abf", "abj"]))
        self.assertTrue(no_anagrams(["iiii", "oiii", "ooii", "oooi", "oooo"]))
        self.assertFalse(no_anagrams(["oiii", "ioii", "iioi", "iiio"]))

    def test_count_valids_no_anagrams(self):
        phrases = [
            ["abcde", "fghij"],
            ["abcde", "xyz", "ecdab"],
            ["a", "ab", "abc", "abd", "abf", "abj"],
            ["iiii", "oiii", "ooii", "oooi", "oooo"],
            ["oiii", "ioii", "iioi", "iiio"]
        ]
        self.assertEqual(3, count_valids(phrases, no_anagrams))
