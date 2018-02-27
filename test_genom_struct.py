"""
test_genom_struct.py: to test genom structure class.

"""

import unittest
from genom_struct import GenomStruct


__author__ = "Mostafa Rafaie"
__license__ = "APLv2"


class GenomStructTest(unittest.TestCase):

    def test_genom_struct(self):
        path = 'sample_genom_struct.csv'

        gs = GenomStruct(path)

        # print(gs.cs[5])
        self.assertEqual(len(gs.cs), 8)
        self.assertAlmostEqual(gs.cs[3].name, 'q4')
        self.assertAlmostEqual(gs.cs[3].min_value, 1)
        self.assertAlmostEqual(gs.cs[3].max_value, 8)
        self.assertAlmostEqual(gs.cs[5].is_fixed, False)

        r = gs.rand(2)
        self.assertGreaterEqual(r, gs.cs[2].min_value)
        self.assertLessEqual(r, gs.cs[2].max_value)
