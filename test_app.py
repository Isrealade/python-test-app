import unittest
from app import add, subtract

class TestAppFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(5, 9), -4)

if __name__ == "__main__":
    unittest.main()
