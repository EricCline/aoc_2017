from collections import defaultdict
import operator

from aoc.shared import open_file


class Instruction:

    def __init__(self, raw_line):
        self._parse(raw_line)

    def _parse(self, raw_line):
        (self.change_register,
         self.operation,
         self.change_value,
         _,
         self.check_register,
         self.condition,
         self.check_value) = raw_line.split()
        self.change_value = int(self.change_value)
        self.check_value = int(self.check_value)


class Registers:

    operation_lookup = {
        'inc': operator.add,
        'dec': operator.sub
    }
    comparison_lookup = {
        '==': operator.eq,
        '!=': operator.ne,
        '>=': operator.ge,
        '<=': operator.le,
        '>': operator.gt,
        '<': operator.lt,
    }

    def __init__(self, instructions):
        self._instructions = instructions
        self._registers = defaultdict(lambda: 0)
        self.max_register = 0

    def apply_instructions(self):
        for instruction in self._instructions:
            self._apply_instruction(instruction)

    @property
    def current_max_register(self):
        return max(list(self._registers.values()))

    def _update_max_register(self):
        if self.current_max_register > self.max_register:
            self.max_register = self.current_max_register

    def _apply_instruction(self, instruction):
        value1 = self._registers[instruction.check_register]
        value2 = instruction.check_value
        if self._check(value1, value2, instruction.condition):
            self._update_register(
                instruction.change_register,
                instruction.change_value,
                instruction.operation
            )
            self._update_max_register()

    def _check(self, a, b, op):
        return self.comparison_lookup[op](a, b)

    def _update_register(self, register, change, op):
        result = self.operation_lookup[op](self._registers[register], change)
        self._registers[register] = result


if __name__ == '__main__':
    raw_lines = open_file("day8").read().splitlines()
    instructions = [Instruction(line) for line in raw_lines]
    reg = Registers(instructions)
    reg.apply_instructions()
    print(reg.current_max_register)
    print(reg.max_register)
