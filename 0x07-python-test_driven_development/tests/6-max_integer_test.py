"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_zero_number(self):
        """Test list with 0 number"""
        self.assertEqual(max_integer([0, 0]), 0)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

    def test_repeated_number(self):
        """Test repeated number"""
        self.assertEqual(max_integer([200, 200, 200]), 200)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_neg_numbers(self):
        """Test negative number"""
        self.assertEqual(max_integer([-7, -4, -6, -1]), -1)

    def test_tuple_in_a_list(self):
        """Test tuple inside a list """
        with self.assertRaises(TypeError):
            max_integer([11, (67, 21, 56)])

    def test_one_element_list(self):
        """Test a list with single value."""
        self.assertEqual(max_integer([5]), 5)

    def test_float(self):
        """Test a list of floats."""
        f = [1.1, 2.3, -3.2, 4.2, 5.2]
        self.assertEqual(max_integer(f), 5.2)

    def test_list_with_loop(self):
        """Test list with a loop"""
        my_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer([i * 5 for i in my_list]), 25)

    def test_int_and_float(self):
        """Test an int and float list."""
        values = [1.5, 20.1, 1, -12, 6]
        self.assertEqual(max_integer(values), 20.1)

    def test_string_number_in_list(self):
        """Test string in a list"""
        with self.assertRaises(TypeError):
            max_integer([0, 'L'])


if __name__ == '__main__':
    unittest.main()
