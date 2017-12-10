from aoc.shared import open_file

OPEN_GROUP = '{'
CLOSE_GROUP = '}'
OPEN_GARBAGE = '<'
CLOSE_GARBAGE = '>'
NEGATE = '!'


class State:

    def __init__(self):
        self.negate = False
        self.in_garbage = False
        self._group_depth = 0
        self.group_score = 0
        self.garbage_count = 0

    def flip_negate(self):
        self.negate = not self.negate

    def open_group(self):
        self._group_depth += 1
        self.group_score += self._group_depth

    def close_group(self):
        self._group_depth -= 1


def groups(data, state):

    for c in data:
        if state.negate:
            state.flip_negate()
            continue
        if c == NEGATE:
            state.flip_negate()
            continue
        elif c == OPEN_GROUP and not state.in_garbage:
            state.open_group()
        elif c == CLOSE_GROUP and not state.in_garbage:
            state.close_group()
        elif c == OPEN_GARBAGE and not state.in_garbage:
            state.in_garbage = True
        elif c == CLOSE_GARBAGE and state.in_garbage:
            state.in_garbage = False
        elif state.in_garbage:
            state.garbage_count += 1


if __name__ == '__main__':
    data = open_file("day9").read()
    state = State()
    groups(data, state)
    print(state.group_score)
    print(state.garbage_count)
