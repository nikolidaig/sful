import unittest
from unittest.mock import patch
from sful.interpreter import Interpreter


@patch('builtins.print')
class TestCellCommands(unittest.TestCase):
    def test_space(self, mock_print):
        interpreter = Interpreter("5_", ":test:")
        interpreter.run()
        mock_print.assert_called_with("     ", end="")

    def test_line(self, mock_print):
        interpreter = Interpreter("5n", ":test:")
        interpreter.run()
        mock_print.assert_called_with("\n\n\n\n\n", end="")

    def test_char(self, mock_print):
        interpreter = Interpreter("100+.", ":test:")
        interpreter.run()
        mock_print.assert_called_with("d", end="")

    def test_number(self, mock_print):
        interpreter = Interpreter("100+#", ":test:")
        interpreter.run()
        mock_print.assert_called_with(100, end="")


if __name__ == "__main__":
    unittest.main()
