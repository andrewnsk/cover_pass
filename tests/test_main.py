import unittest
from main import *


class Test(unittest.TestCase):

    def test_print_me(self):
        self.assertEqual(print_me(5), 15)
        self.assertEqual(print_me(8), 18)
        self.assertEqual(print_me(20), 30)
        self.assertEqual(print_me(0), 10)

    def test_return_val(self):
        self.assertEqual(return_val(1), 2)

    def test_return_val2(self):
        self.assertEqual(return_val(1), 2)


if __name__ == "__main__":
    unittest.main()

