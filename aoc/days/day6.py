import copy
import itertools
from collections import deque

from aoc.shared import open_file


class Memory:

    def __init__(self, banks):
        self.banks = banks
        self._indices = self._reset_indices()
        self._snapshots = []
        self._add_snapshot()

    @property
    def redistribution_count(self):
        return len(self._snapshots) - 1

    @property
    def infinite_loop_size(self):
        first = self._snapshots.index(self._snapshots[-1])
        return len(self._snapshots) - 1 - first

    def redistribute(self):
        distribution_repeated = False
        while not distribution_repeated:
            self._redistribute()
            if self._saw_current_distribution():
                distribution_repeated = True
            self._add_snapshot()

    def _redistribute(self):
        max_bank, max_bank_index = self._remove_max_bank()
        for i in self._redistribution_indices(max_bank, max_bank_index):
            self.banks[i] += 1

    def _saw_current_distribution(self):
        return self.banks in self._snapshots

    def _add_snapshot(self):
        self._snapshots.append(copy.copy(self.banks))

    def _remove_max_bank(self):
        max_bank = max(self.banks)
        max_index = self.banks.index(max_bank)
        self.banks[max_index] = 0
        return max_bank, max_index

    def _redistribution_indices(self, bank_value, bank_index):
        self._reset_indices()
        # rotate left and don't include bank_index
        rotation = (bank_index + 1) * -1
        self._indices.rotate(rotation)
        index_gen = itertools.cycle(self._indices)
        return [next(index_gen) for _ in range(bank_value)]

    def _reset_indices(self):
        self._indices = deque(range(0, len(self.banks)))


if __name__ == '__main__':
    banks = [int(i) for i in open_file("day6").read().strip().split()]
    m = Memory(banks)
    m.redistribute()
    print(m.redistribution_count)
    print(m.infinite_loop_size)
