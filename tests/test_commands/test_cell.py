import unittest
from sful.interpreter import Interpreter


class TestCellCommands(unittest.TestCase):
    def test_set(self):
        interpreter = Interpreter("123=", ":test:")
        interpreter.run()
        self.assertEqual(interpreter.env.get(), 123)


    def test_inc(self):
        interpreter = Interpreter("123+", ":test:")
        interpreter.run()
        self.assertEqual(interpreter.env.get(), 123)


    def test_dec(self):
        interpreter = Interpreter("123=123-", ":test:")
        interpreter.run()
        self.assertEqual(interpreter.env.get(), 0)


if __name__ == "__main__":
    unittest.main()
