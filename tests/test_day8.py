import unittest

from aoc.days.day8 import Instruction, Registers


class TestInstruction(unittest.TestCase):

    def test_instruction_parses_input_line(self):
        line = "b inc 5 if a > 1"
        ins = Instruction(line)
        self.assertEqual("b", ins.change_register)
        self.assertEqual("inc", ins.operation)
        self.assertEqual(5, ins.change_value)
        self.assertEqual("a", ins.check_register)
        self.assertEqual(">", ins.condition)
        self.assertEqual(1, ins.check_value)


class TestRegisters(unittest.TestCase):

    def setUp(self):
        lines = [
            "b inc 5 if a > 1",
            "a inc 1 if b < 5",
            "c dec -10 if a >= 1",
            "c inc -20 if c == 10",
        ]
        instructions = [Instruction(line) for line in lines]
        self.registers = Registers(instructions)

    def test_current_max_register_returns_highest_value(self):
        self.registers._registers = {'asdf': 0, 'sdfg': 2, 'dfgh': 3}
        self.assertEqual(3, self.registers.current_max_register)

    def test_max_register_returns_highest_value_recorded(self):
        self.registers.apply_instructions()
        self.assertEqual(10, self.registers.max_register)

    def test_apply_instructions_updates_registers(self):
        self.registers.apply_instructions()
        self.assertEqual(
            {'a': 1, 'b': 0, 'c': -10},
            self.registers._registers
        )


