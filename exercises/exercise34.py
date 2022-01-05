from amar.exercise33 import *
import unittest

class TestCal(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 20), 30)

    def test_sub(self):
        self.assertEqual(sub(0, 0), 0)
        self.assertEqual(sub(1, -1), 2)

    def test_div(self):
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(10, 0), -1)
# raise
if __name__ == '__main__':
    unittest.main()