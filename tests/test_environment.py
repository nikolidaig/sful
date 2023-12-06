import unittest
import sful.environment as environment


class TestEnvironment(unittest.TestCase):
    def setUp(self):
        self.env = environment.Environment()

    def test_get(self):
        self.env.memory["0,1"] = 123
        self.assertEqual(self.env.get(), 0)

        self.env.col = 1
        self.assertEqual(self.env.get(), 123)

    def test_set(self):
        self.env.set(123)
        self.assertEqual(self.env.memory["0,0"], 123)

        self.env.set(0)
        self.assertNotIn("0,0", self.env.memory)

        self.assertRaises(ValueError, lambda: self.env.set(-1))

    def test_inc(self):
        self.env.set(123)
        self.env.inc(456)
        self.assertEqual(self.env.get(), 579)

    def test_delete(self):
        self.env.set(123)

        self.env.delete()
        self.assertNotIn("0,0", self.env.memory)


if __name__ == "__main__":
    unittest.main()
