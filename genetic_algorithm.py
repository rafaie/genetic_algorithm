"""
genetic_algorithm.py: the base genetic_algorithm class.

"""

from genom_struct import GenomStruct


__author__ = "Mostafa Rafaie"
__license__ = "APLv2"


class GeneticAlgorithm:

    # Cross Over Types
    SINGLE_POINT_CROSSOVER = 1
    TWO_POINT_CROSSOVER = 2
    CUT_SLICE_CROSSOVER = 3
    UNIFORM_CROSSOVER = 4

    def __init__(self, path):
        self.path = path
        self.gs = GenomStruct(path)

        pass

    # Cross Over functions
    def do_crossover_single_point(self, type, genom1, genom2):
        pass

    def do_crossover_two_point(self, type, genom1, genom2):
        pass

    def do_crossover_cut_slice(self, type, genom1, genom2):
        pass

    def do_crossover_uniform(self, type, genom1, genom2):
        pass

    def do_crossover(self, type, genom1, genom2):
        pass

    # Run the GA Algorithem
    def reset(self, init_population_size, path=None):
        pass

    def run(self, dataset, fitness, cuncurrency, init_population_size,
            population_size, mutation_rate, num_iteratitions, crossover_type):
        pass
