"""
genetic_algorithm.py: the base genetic_algorithm class.

"""

import numpy as np
import multiprocessing as mp
import logging
import random
import os

if __package__ is '':
    from genom_struct import GenomStruct
else:
    from .genom_struct import GenomStruct


__author__ = "Mostafa Rafaie"
__license__ = "APLv2"


class GeneticAlgorithm:
    LOGGER_HANDLER_NAME = 'GA_LOG_HANDLER'

    # Cross Over Types
    SINGLE_POINT_CROSSOVER = 0
    TWO_POINT_CROSSOVER = 1
    CUT_SLICE_CROSSOVER = 2
    UNIFORM_CROSSOVER = 3

    TOURNAMENT_SIZE = 3

    def __init__(self, path, log_level=None):
        self.path = path
        self.gs = GenomStruct(path)
        self.logger = logging.getLogger(GeneticAlgorithm.LOGGER_HANDLER_NAME)
        self.log_level = log_level
        if log_level is not None:
            self.logger.setLevel(log_level)

        self.CROSSOVER_FUNCTIONS = {GeneticAlgorithm.SINGLE_POINT_CROSSOVER:
                                    self.do_crossover_single_point,
                                    GeneticAlgorithm.TWO_POINT_CROSSOVER:
                                    self.do_crossover_two_point,
                                    GeneticAlgorithm.CUT_SLICE_CROSSOVER:
                                    self.do_crossover_cut_slice,
                                    GeneticAlgorithm.UNIFORM_CROSSOVER:
                                    self.do_crossover_uniform}

    # Cross Over functions
    def do_crossover_single_point(self, genom1, genom2):
        c = random.randint(1, self.gs.size() - 2)
        return list(genom1[:c]) + list(genom2[c:-1]) + [0.0]

    def do_crossover_two_point(self, genom1, genom2):
        if self.gs.size() <= 3:
            return list(genom1[1]) + list(genom2[2]) + list(genom1[3]) + [0.0]

        c1 = random.randint(0, self.gs.size() - 2)
        c2 = random.randint(c1, self.gs.size() - 1)
        return list(genom1[:c1]) + list(genom2[c1:c2]) + list(genom1[c2:-1]) \
            + [0.0]

    def do_crossover_cut_slice(self, genom1, genom2):
        c1 = random.randrange(0, self.gs.size() - 1)
        c2 = random.randrange(0, self.gs.size() - 1)
        g = list(genom1[:c1]) + list(genom2[c2:])
        g = g[:self.gs.size() - 1]
        if len(g) < self.gs.size():
            g += self.gs.random_genom()[len(g):]
        return g + [0.0]

    def do_crossover_uniform(self, genom1, genom2):
        g = []
        for i in range(self.gs.size()):
            if random.randint(0, 1) == 1:
                g.append(genom1[i])
            else:
                g.append(genom2[i])

        return g + [0.0]

    def do_crossover(self, type, genom1, genom2):
        return self.CROSSOVER_FUNCTIONS[type](genom1, genom2)

    # Run the GA Algorithem
    def init_generation(self, init_population_size):
        self.logger.info('init_generation is started running')

        p = []
        counter = 0
        while counter < init_population_size:
            d = self.gs.random_genom() + [0.0]
            if d not in p:
                p.append(d)
                counter += 1

        population = np.array(p, dtype=np.float64)

        self.logger.info('initialize the genration with the size of {}'.
                         format(len(population)))

        return population

    def init_ga(self, init_population_size, path=None):
        if path is not None:
            self.gs = GenomStruct(path)

        return self.init_generation(init_population_size)

    def evaluate_fitness_partial(population, fitness, log_level):
        logger = logging.getLogger(GeneticAlgorithm.LOGGER_HANDLER_NAME)
        log_level = log_level
        logger.info('Start evaluating the partial fitness function ' +
                    'for population (size = {})'.format(len(population)))

        for g in population:
            g[-1] = fitness(g)
        return population

    def evaluate_fitness(self, population, fitness, cuncurrency=1):
        self.logger.info('Start evaluating the fitness function')
        sub_p = np.array_split(population, cuncurrency)
        pool = mp.Pool(processes=cuncurrency)
        results = [pool.apply_async(GeneticAlgorithm.evaluate_fitness_partial,
                                    args=(sub_p[i], fitness, self.log_level))
                   for i in range(cuncurrency)]

        output = [p.get() for p in results]
        pool.close()

        self.logger.info('Finish evaluating the fitness function')

        return np.concatenate(output)

    def check_stop_condition(self, population, num_iteratitions, iteratition,
                             fitness_goal, reverse_fitness_order):
        self.logger.info('Check stop Condition iterestion ' +
                         '{}'.format(iteratition))

        if iteratition > num_iteratitions:
            self.logger.info('Stop Condition: True. iteratitions>' +
                             'num_iteratitions({}>{})'.format(num_iteratitions,
                                                              iteratition))
            return False

        if population[0, -1] < fitness_goal and \
           reverse_fitness_order is False:
            self.logger.info('Stop Condition: True. Satisfied Fitness_goal!' +
                             'population[0, -1] < fitness_goal' +
                             '({}<{})'.format(population[0, -1], fitness_goal))
            return False

        if population[0, -1] > fitness_goal and \
           reverse_fitness_order is True:
            self.logger.info('Stop Condition: True. Satisfied Fitness_goal!' +
                             'population[0, -1] > fitness_goal' +
                             '({}>{})'.format(population[0, -1], fitness_goal))
            return False

        return True

    def choose_best_population(self, population, population_size,
                               reverse=False):
        if reverse is True:
            return population[(-population[:, -1]).argsort()][:population_size]
        return population[population[:, -1].argsort()][:population_size]

    def tournament_selection(self, population):
        g = random.choice(population)

        for i in range(GeneticAlgorithm.TOURNAMENT_SIZE):
            g1 = random.choice(population)
            if g1[-1] > g[-1]:
                g = g1

        return g

    def do_mutate(self, g):
        i = random.choice(self.gs.rand_c_options())
        g[i] = self.gs.rand(i)
        return g

    def gen_next_generation(self, population, population_size, mutation_rate,
                            crossover_type, fitness_func, fitness_goal,
                            cuncurrency=1):
        self.logger.info('Generate the next generation')

        new_p = []
        while len(new_p) != population_size:
            parent1 = self.tournament_selection(population)
            parent2 = self.tournament_selection(population)

            child = self.do_crossover(crossover_type, parent1, parent2)
            if random.uniform(0, 1) < mutation_rate:
                child = self.do_mutate(child)

                if child not in new_p:
                    new_p.append(child)

        new_population = np.array(new_p, dtype=np.float64)
        new_population = self.evaluate_fitness(new_population, fitness_func,
                                               cuncurrency)
        return new_population

    def reload_np_population(self, population, population_size,
                             population_np_path, reload_np_population_rate):
        if os.path.isfile(population_np_path) is not True:
            return population

        p = np.load(population_np_path)
        n = min(int(reload_np_population_rate * population_size), len(p))
        self.logger.info('reload_np_population ' +
                         'file "{}", '.format(population_np_path) +
                         'rate = {}, '.format(reload_np_population_rate) +
                         ', count = {}'.format(n))

        return np.concatenate((population, p[:n]), axis=0)

    def run(self, init_population_size, population_size,
            mutation_rate, num_iteratitions, crossover_type,
            fitness_func, fitness_goal,
            cuncurrency=1, reverse_fitness_order=False, path=None,
            population_np_path=None, reload_np_population_rate=0.1):

        iteratition = 1
        population = self.init_ga(init_population_size, path)

        if population_np_path is not None:
            population = self.reload_np_population(population,
                                                   population_size,
                                                   population_np_path,
                                                   reload_np_population_rate)

        population = self.evaluate_fitness(population, fitness_func,
                                           cuncurrency)

        population = self.choose_best_population(population,
                                                 population_size,
                                                 reverse_fitness_order)

        while self.check_stop_condition(population, num_iteratitions,
                                        iteratition, fitness_goal,
                                        reverse_fitness_order):
            self.logger.info('start iteration "{}" '.format(iteratition))

            new_population = self.gen_next_generation(population,
                                                      population_size,
                                                      mutation_rate,
                                                      crossover_type,
                                                      fitness_func,
                                                      fitness_goal,
                                                      cuncurrency)

            population = np.concatenate((population, new_population), axis=0)
            population = self.choose_best_population(population,
                                                     population_size,
                                                     reverse_fitness_order)
            iteratition += 1
            self.logger.info('population[:3].astype(float) : ' +
                             '{}'.format(population[:3].astype(float)))
            self.logger.info('fitness_value,{},{}'
                             .format(iteratition, ','.join(population[:, -1]
                                                           .astype(str))))

        return population
