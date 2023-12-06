import unittest
from sful.interpreter import Interpreter


class TestProcCommands(unittest.TestCase):
    def test_comment(self):
        interpreter = Interpreter("* 123+\n456+", ":test:")
        interpreter.run()
        self.assertEqual(interpreter.env.get(), 456)

if __name__ == "__main__":
    unittest.main()
