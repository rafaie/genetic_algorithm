"""
test_genetic_algorithm.py.py: to test Genetic Algorithem class.

"""

import unittest
import numpy as np
from genetic_algorithm import GeneticAlgorithm


__author__ = "Mostafa Rafaie"
__license__ = "APLv2"


class GeneticAlgorithmTest(unittest.TestCase):

    def test_functions(self):
        path = 'sample_genom_struct.csv'
        init_population_size = 10

        ga = GeneticAlgorithm(path)
        population = ga.init_ga(init_population_size)

        self.assertEqual(len(population), init_population_size)
        self.assertEqual(len(np.unique(population, axis=0)),
                         init_population_size)
        self.assertEqual(population[1, 5], 0)
