import unittest
from main import median_fits

class TestMedianFits_emptyList(unittest.TestCase):
    def test_error_raised_for_empty_input(self):
        with self.assertRaises(ValueError):
            median_fits([])

if __name__ == '__main__':
    unittest.main()