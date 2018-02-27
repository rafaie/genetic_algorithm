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

        self.assertEqual(len(gs.cs), 8)
        self.assertAlmostEqual(gs.cs[3].name, 'q4')
        self.assertAlmostEqual(gs.cs[3].min_value, 1)
        self.assertAlmostEqual(gs.cs[3].max_value, 8)
        self.assertAlmostEqual(gs.cs[5].is_fixed, False)

        r = gs.rand(2)
        self.assertGreaterEqual(r, gs.cs[2].min_value)
        self.assertLessEqual(r, gs.cs[2].max_value)

        genom = gs.random_genom()
        self.assertGreaterEqual(len(genom), len(gs.cs))
        self.assertGreaterEqual(genom[2], gs.cs[2].min_value)
        self.assertLessEqual(genom[4], gs.cs[4].max_value)
