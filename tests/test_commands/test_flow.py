import unittest
from sful.interpreter import Interpreter

class TestFlowCommands(unittest.TestCase):
    def test_sq_brkt(self):
        interpreter = Interpreter("10=[+[-]][+]", ":test:")
        interpreter.run()
        self.assertEqual(interpreter.env.get(), 0)


    def test_paren(self):
        interpreter = Interpreter("(+(-)())", ":test:")
        interpreter.run()
        self.assertEqual(interpreter.env.get(), 1)


if __name__ == "__main__":
    unittest.main()
