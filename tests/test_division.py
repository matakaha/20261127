import math
import unittest

from division import divide


class DivideTests(unittest.TestCase):
    def test_valid_results(self):
        cases = (
            (10, 2, 5.0),
            (5.0, 2.0, 2.5),
            (-9, 3, -3.0),
            (0, 2, 0.0),
            (1, 2, 0.5),
            (1e-300, 1e300, 0.0),
        )
        for dividend, divisor, expected in cases:
            with self.subTest(dividend=dividend, divisor=divisor):
                result = divide(dividend, divisor)
                self.assertEqual(result, expected)
                self.assertTrue(math.isfinite(result))

    def test_invalid_types(self):
        for dividend, divisor in (
            ("10", 2),
            (10, "2"),
            (True, 2),
            (10, False),
        ):
            with self.subTest(dividend=dividend, divisor=divisor):
                with self.assertRaises(TypeError):
                    divide(dividend, divisor)

    def test_type_validation_precedes_value_validation(self):
        with self.assertRaises(TypeError):
            divide(True, float("nan"))

    def test_non_finite_dividend(self):
        for dividend in (float("nan"), float("inf"), float("-inf")):
            with self.subTest(dividend=dividend):
                with self.assertRaises(ValueError):
                    divide(dividend, 2)

    def test_non_finite_divisor(self):
        for divisor in (float("nan"), float("inf"), float("-inf")):
            with self.subTest(divisor=divisor):
                with self.assertRaises(ValueError):
                    divide(10, divisor)

    def test_integer_conversion_overflow(self):
        with self.assertRaises(OverflowError):
            divide(10**400, 2)
        with self.assertRaises(OverflowError):
            divide(10, 10**400)

    def test_zero_divisor(self):
        for divisor in (0, 0.0, -0.0):
            with self.subTest(divisor=divisor):
                with self.assertRaises(ZeroDivisionError):
                    divide(10, divisor)

    def test_result_overflow(self):
        with self.assertRaises(OverflowError):
            divide(1e308, 1e-308)


if __name__ == "__main__":
    unittest.main()
