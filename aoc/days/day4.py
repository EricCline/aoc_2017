from aoc.shared import open_file


def split_to_words(passphrase):
    return passphrase.split(' ')


def unique_words(words):
    return sorted(list(set(words))) == sorted(words)


def no_anagrams(words):
    reduced = sorted(set("".join(sorted(word)) for word in words))
    original = sorted("".join(sorted(word)) for word in words)
    return reduced == original


def count_valids(passphrases, comparison_function):
    valids = [
        p for p in passphrases
        if comparison_function(p)
    ]
    return len(valids)


if __name__ == '__main__':
     passphrases = [
         split_to_words(line) for line in open_file("day4").read().splitlines()
     ]
     print(count_valids(passphrases, unique_words))
     print(count_valids(passphrases, no_anagrams))
