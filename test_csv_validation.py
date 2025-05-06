import unittest
from csv_validation import (
    is_valid_filename, validate_headers, validate_row_data
)

class TestCSVValidation(unittest.TestCase):
    
    def test_valid_filename(self):
        self.assertTrue(is_valid_filename("data_20250430.csv"))
        self.assertFalse(is_valid_filename("wrongfile.csv"))

    def test_validate_headers(self):
        expected = ["BatchID", "Value1", "Value2"]
        correct = ["BatchID", "Value1", "Value2"]
        incorrect = ["Wrong", "Headers"]
        self.assertTrue(validate_headers(correct, expected))
        self.assertFalse(validate_headers(incorrect, expected))

    def test_validate_row_data(self):
        valid = ["B001", "5.5", "7.8"]
        invalid_empty = ["B002", "", "4.5"]
        invalid_range = ["B003", "10.1", "8.5"]
        self.assertTrue(validate_row_data(valid))
        self.assertFalse(validate_row_data(invalid_empty))
        self.assertFalse(validate_row_data(invalid_range))

if __name__ == "__main__":
    unittest.main()
