import unittest
from sful.interpreter import Interpreter


class TestProcCommands(unittest.TestCase):
    def test_define(self):
        interpreter = Interpreter("@a{$+} 10a", ":test:")
        interpreter.run()
        self.assertEqual(interpreter.env.procedures["a"]["code"], "$+")
        self.assertEqual(interpreter.env.get(), 10)

    def test_anon(self):
        interpreter = Interpreter("10{$+}", ":test:")
        interpreter.run()
        self.assertEqual(interpreter.env.get(), 10)

    def test_proc_param(self):
        interpreter = Interpreter("2$", ":test:")
        self.assertRaises(Exception, interpreter.run)

    def test_quit(self):
        interpreter = Interpreter("{10+q10-}5+", ":test:")
        interpreter.run()
        self.assertEqual(interpreter.env.get(), 15)

if __name__ == "__main__":
    unittest.main()
