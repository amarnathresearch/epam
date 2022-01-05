from amar.exercise37 import User
import unittest

class TestUser(unittest.TestCase):

    def setUp(self):
        print("im executed")
        self.user1 = User('amar', 'nath')
        self.user2 = User('robert', 'alvin')
        self.user1.setDesignation('trainer')
        self.user2.setDesignation('manager')

    def test_user(self):
        print("test_user")
        self.assertEqual(self.user1.getUserName(), 'amar nath')
        self.assertEqual(self.user2.getUserName(), 'robert alvin')

    def test_designation(self):
        print("test_designation")
        self.assertEqual(self.user1.getDesignation(), 'trainer')
        self.assertEqual(self.user2.getDesignation(), 'manager')

if __name__ == '__main__':
    unittest.main()