
import unittest
from shipping import (
    calculate_shipping,
    estimate_delivery_days,
    is_free_shipping_eligible,
)


class TestShipping(unittest.TestCase):
    def test_small_local_package(self):
        self.assertEqual(calculate_shipping(1), 5.0)

    def test_weight_boundary_two_kg(self):
        self.assertEqual(calculate_shipping(2), 5.0)

    def test_medium_national_package(self):
        self.assertEqual(calculate_shipping(5, "national"), 17.0)

    def test_heavy_international_package(self):
        self.assertEqual(calculate_shipping(12, "international"), 40.0)

    def test_express_shipping(self):
        self.assertEqual(calculate_shipping(1, express=True), 13.0)

    def test_insurance(self):
        self.assertEqual(calculate_shipping(1, insured=True), 10.0)

    def test_member_discount_and_extras(self):
        self.assertEqual(
            calculate_shipping(5, "national", True, True, True), 27.0
        )

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            calculate_shipping(-1)

    def test_non_numeric_weight(self):
        with self.assertRaises(TypeError):
            calculate_shipping("heavy")

    def test_invalid_destination(self):
        with self.assertRaises(ValueError):
            calculate_shipping(2, "moon")

    def test_local_delivery(self):
        self.assertEqual(estimate_delivery_days(), 2)

    def test_national_express_delivery(self):
        self.assertEqual(estimate_delivery_days("national", True), 3)

    def test_international_delivery(self):
        self.assertEqual(estimate_delivery_days("international"), 10)

    def test_local_express_minimum_day(self):
        self.assertEqual(estimate_delivery_days("local", True), 1)

    def test_invalid_delivery_destination(self):
        with self.assertRaises(ValueError):
            estimate_delivery_days("moon")

    def test_free_shipping_regular_customer(self):
        self.assertTrue(is_free_shipping_eligible(75))
        self.assertFalse(is_free_shipping_eligible(74))

    def test_free_shipping_member(self):
        self.assertTrue(is_free_shipping_eligible(50, True))
        self.assertFalse(is_free_shipping_eligible(49, True))

    def test_invalid_order_total(self):
        with self.assertRaises(ValueError):
            is_free_shipping_eligible(-1)


if __name__ == "__main__":
    unittest.main()
