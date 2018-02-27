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
    def do_crossover_single_point(self, type, genom1, genom2, verbose=False):
        pass

    def do_crossover_two_point(self, type, genom1, genom2, verbose=False):
        pass

    def do_crossover_cut_slice(self, type, genom1, genom2, verbose=False):
        pass

    def do_crossover_uniform(self, type, genom1, genom2, verbose=False):
        pass

    def do_crossover(self, type, genom1, genom2, verbose=False):
        pass

    # Run the GA Algorithem
    def init_generation(self, init_population_size, verbose=False):
        pass

    def init_ga(self, init_population_size, path=None, verbose=False):
        pass

    def calc_fitness(self, population, fitness, cuncurrency, verbose=False):
        pass

    def check_stop_condition(self, population, num_iteratitions, iteratition,
                             verbose=False):
        pass

    def choose_best_population(self, population, population_size, verbose):
        pass

    def run(self, fitness, cuncurrency, init_population_size, population_size,
            mutation_rate, num_iteratitions, crossover_type, path=None,
            verbose=False):

        iteratition = 0
        population = self.init_ga(init_population_size, path, verbose)
        self.calc_fitness(population, fitness, cuncurrency, verbose)

        population = self.choose_best_population(population,
                                                 population_size,
                                                 verbose)

        while self.check_stop_condition(population, num_iteratitions,
                                        iteratition, verbose):

            population = self.gen_next_population(population_size,
                                                  mutation_rate,
                                                  crossover_type,
                                                  cuncurrency,
                                                  fitness)

            population = self.choose_best_population(population,
                                                     population_size,
                                                     verbose)
        return population
