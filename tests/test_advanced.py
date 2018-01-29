# -*- coding: utf-8 -*-

from .context import postcodes
import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_validate_correct(self):
        
        cases = ['AA9A 9AA',]
        for case in cases:
            self.assertEqual(postcodes.validate(case), True)

    def test_validate_incorrect(self):
        
        cases = ['AA9A 9AA']
        for case in cases:
            self.assertEqual(postcodes.validate(case), True)            
    def test_format_correct(self):
        
        cases = ['AA9A 9AA',]
        for case in cases:
            self.assertEqual(postcodes.validate(case), True)


    def test_format_incorrect(self):
        
        cases = ['AA9A 9AA',]
        for case in cases:
            self.assertRaises(postcodes.format(case), True)


if __name__ == '__main__':
    unittest.main()
