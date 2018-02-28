"""
test_genetic_algorithm.py.py: to test Genetic Algorithem class.

"""

import unittest
import numpy as np
from genetic_algorithm import GeneticAlgorithm


__author__ = "Mostafa Rafaie"
__license__ = "APLv2"


class GeneticAlgorithmTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(GeneticAlgorithmTest, self).__init__(*args, **kwargs)

        self.path = 'sample_genom_struct.csv'
        self.ga = GeneticAlgorithm(self.path)

    def test_functions(self):
        init_population_size = 10

        population = self.ga.init_ga(init_population_size)

        self.assertEqual(len(population), init_population_size)
        self.assertEqual(len(np.unique(population, axis=0)),
                         init_population_size)
        self.assertEqual(population[1, 5], 0)

    def test_crossovers(self):
        g1 = [1, 2, 3, 4, 5, 0.0]
        g2 = [15, 16, 17, 18, 19, 1.0]

        g3 = self.ga.do_crossover(GeneticAlgorithm.SINGLE_POINT_CROSSOVER,
                                  g1, g2)
        # print(g3)
        self.assertEqual(len(g3), 6)

        g3 = self.ga.do_crossover(GeneticAlgorithm.TWO_POINT_CROSSOVER,
                                  g1, g2)
        # print(g3)
        self.assertEqual(len(g3), 6)

        g3 = self.ga.do_crossover(GeneticAlgorithm.CUT_SLICE_CROSSOVER,
                                  g1, g2)
        # print(g3)
        self.assertEqual(len(g3), 6)

        g3 = self.ga.do_crossover(GeneticAlgorithm.UNIFORM_CROSSOVER,
                                  g1, g2)
        # print(g3)
        self.assertEqual(len(g3), 6)
