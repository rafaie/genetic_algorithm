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

    def test_init_ga(self):
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

    def fitness(g):
        return sum(g)

    def test_scenario1(self):
        population = np.array([[1, 2, 3, 0],
                               [4, 5, 6, 0],
                               [7, 8, 9, 0],
                               [10, 11, 12, 0]])

        self.ga.evaluate_fitness(population, GeneticAlgorithmTest.fitness)
        self.assertEqual(population[0][-1], 6)
        self.assertEqual(population[2][-1], 24)

        new_population = self.ga.choose_best_population(population, 3)
        # print(new_population)
        self.assertEqual(len(new_population), 3)
        self.assertEqual(new_population[0][-1], 33)
        self.assertEqual(new_population[1][-1], 24)
