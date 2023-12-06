import unittest
from sful.interpreter import Interpreter


class TestInterpreter(unittest.TestCase):
    def test_delim_code(self):
        interpreter = Interpreter("{\n{\n}\n}", ":test:")
        code, line, index = interpreter.delim_code("}")
        self.assertEqual(code, "{\n{\n}\n}")


if __name__ == "__main__":
    unittest.main()
