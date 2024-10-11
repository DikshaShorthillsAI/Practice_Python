import unittest
from Main import add, subtract, multiply, divide

class TestMathOperations(unittest.TestCase):
    
    # Test for the add function
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    # Test for the subtract function
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(2, 5), -3)
        self.assertEqual(subtract(0, 0), 0)

    # Test for the multiply function
    def test_multiply(self):
        self.assertEqual(multiply(3, 7), 21)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 10), 0)

    # Test for the divide function
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)  # Valid division

        # Test division by zero using assertRaises
        with self.assertRaises(ZeroDivisionError) as context:
            divide(5, 0)  # This should raise ZeroDivisionError

        # Check the error message
        self.assertEqual(str(context.exception), "division by zero")

if __name__ == "__main__":
    unittest.main()
