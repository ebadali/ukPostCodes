# -*- coding: utf-8 -*-


from .context import sample


import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(sample.hmm())
        

    def test_validate_postcode(self):
        print(sample.validate('AA9A 9AA'))
        assert True


if __name__ == '__main__':
    unittest.main()
