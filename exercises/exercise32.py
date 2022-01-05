import unittest
class Amar(unittest.TestCase):
    
    def test(self):
        print("Hello")
    
    def test_amar(self):
        print("testing amar function")

    def test_add(self):
        print("addition")

    def test_sub(self):
        print("subtraction")

if __name__ == '__main__':
    print("starting")
    unittest.main()