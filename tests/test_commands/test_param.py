import unittest
from sful.interpreter import Interpreter


class TestParamCommands(unittest.TestCase):
    def test_column(self):
        interpreter = Interpreter("10><&", ":test:")
        interpreter.run()
        self.assertEqual(interpreter.param, 9)
    
    def test_row(self):
        interpreter = Interpreter("10v^%", ":test:")
        interpreter.run()
        self.assertEqual(interpreter.param, 9)
    
    def test_cell(self):
        interpreter = Interpreter("10=!", ":test:")
        interpreter.run()
        self.assertEqual(interpreter.param, 10)


if __name__ == "__main__":
    unittest.main()
