from aoc.shared import open_file


class OffsetReader:

    def __init__(self, offsets):
        self.offsets = offsets

    def run(self):
        current_position = 0
        moves = 0

        while True:
            try:
                offset = self.offsets[current_position]
            except IndexError:
                break
            self.increment_offset(current_position)
            current_position += offset
            moves += 1
        return moves

    def increment_offset(self, index):
        self.offsets[index] += 1


class ThreeOrMoreReader(OffsetReader):

    def increment_offset(self, index):
        value = self.offsets[index]
        if value >= 3:
            self.offsets[index] -= 1
        else:
            self.offsets[index] += 1



if __name__ == '__main__':
    offsets = [int(i) for i in open_file("day5").read().splitlines()]
    print(OffsetReader(offsets).run())
    offsets = [int(i) for i in open_file("day5").read().splitlines()]
    print(ThreeOrMoreReader(offsets).run())
