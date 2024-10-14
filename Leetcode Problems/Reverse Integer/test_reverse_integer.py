import unittest
from reverse_integer import reverse_integer

class TestReverseInteger(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(reverse_integer(123), 321)  # Normal case
        self.assertEqual(reverse_integer(120), 21)   # Trailing zero case

    def test_negative_integer(self):
        self.assertEqual(reverse_integer(-123), -321)  # Normal case
        self.assertEqual(reverse_integer(-120), -21)    # Trailing zero case

    def test_zero(self):
        self.assertEqual(reverse_integer(0), 0)  # Edge case

    def test_overflow(self):
        self.assertEqual(reverse_integer(1534236469), 0)  # Overflow case
        self.assertEqual(reverse_integer(-1534236469), 0)  # Negative overflow case

    def test_boundary_values(self):
        self.assertEqual(reverse_integer(2147483647), 0)  # Upper boundary overflow
        self.assertEqual(reverse_integer(-2147483648), 0)  # Lower boundary overflow

if __name__ == "__main__":
    unittest.main()
