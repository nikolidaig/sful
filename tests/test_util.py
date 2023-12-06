import unittest
import sful.util as util


class TestUtil(unittest.TestCase):
    def test_parse_param(self):
        lines = ["123abc"]
        self.assertEqual(util.parse_param(lines, 0, 0), 123)

    def test_match_delim(self):
        lines = ["{{[}", "}] "]

        self.assertEqual(util.match_delim(lines, 0, 0, "}"), (1, 0))
        self.assertEqual(util.match_delim(lines, 0, 0, "}", nestable=False), (0, 3))
        self.assertEqual(util.match_delim(lines, 1, 0, "{", forward=False), (0, 0))


if __name__ == "__main__":
    unittest.main()
