
import unittest
from shipping import calculate_shipping

class TestShipping(unittest.TestCase):

    def test_small_package(self):
        self.assertEqual(calculate_shipping(1), 5)

    def test_large_express(self):
        self.assertEqual(calculate_shipping(5, True), 18)

    def test_member(self):
        self.assertEqual(calculate_shipping(1, False, True), 4.5)

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            calculate_shipping(-1)

if __name__ == "__main__":
    unittest.main()
