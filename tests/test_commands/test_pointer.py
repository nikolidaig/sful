import unittest
from sful.interpreter import Interpreter


class TestPointerCommands(unittest.TestCase):
    # Down, Up, Left, Right are tested in test_commands/test_param.py

    def test_row(self):
        interpreter = Interpreter("10r", ":test:")
        interpreter.run()
        self.assertEqual(interpreter.env.row, 10)
    

    def test_col(self):
        interpreter = Interpreter("10c", ":test:")
        interpreter.run()
        self.assertEqual(interpreter.env.col, 10)


if __name__ == "__main__":
    unittest.main()
