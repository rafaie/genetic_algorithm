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

        self.assertEqual(len(gs.cs), 5)
        self.assertAlmostEqual(gs.cs[3].name, 'v4')
        self.assertAlmostEqual(gs.cs[3].min_value, -100)
        self.assertAlmostEqual(gs.cs[3].max_value, 100)
        self.assertAlmostEqual(gs.cs[2].is_fixed, False)

        r = gs.rand(2)
        self.assertGreaterEqual(r, gs.cs[2].min_value)
        self.assertLessEqual(r, gs.cs[2].max_value)

        genom = gs.random_genom()
        self.assertGreaterEqual(len(genom), len(gs.cs))
        self.assertGreaterEqual(genom[2], gs.cs[2].min_value)
        self.assertLessEqual(genom[4], gs.cs[4].max_value)

    def test_genom_struct_fixed_value(self):
        path = 'sample_genom_struct.csv'

        gs = GenomStruct(path)
        gs.cs[1].is_fixed = True

        r = gs.rand(1)
        self.assertEqual(r, gs.cs[1].value)

        r = gs.rand(1)
        self.assertEqual(r, gs.cs[1].value)

        r = gs.random_genom()
        self.assertEqual(r[1], gs.cs[1].value)

        l = gs.rand_c_options()
        self.assertTrue(1 not in l)
