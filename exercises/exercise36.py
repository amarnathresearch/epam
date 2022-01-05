from amar.exercise35 import Calc
import unittest

class TestCalc(unittest.TestCase):
    def test_add(self):
        c = Calc()
        self.assertEqual(c.add(10, 20), 30)

    def test_sub(self):
        c = Calc()
        self.assertEqual(c.sub(0, 0), 0)
        self.assertEqual(c.sub(1, -1), 2)

    def test_mul(self):
        c = Calc()
        self.assertEqual(c.mul(0, 0), 0)
        self.assertEqual(c.mul(0, 2), 0)
    def test_div(self):
        c = Calc()
        self.assertEqual(c.div(10, 2), 5)
        self.assertEqual(c.div(10, 0), -1)
# raise
if __name__ == '__main__':
    unittest.main()