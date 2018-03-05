"""
ga_function_optimization.py: Using genetic_algorithm for Function Optimization
Function: F(x) = 12a + 24b -35c +7e -5c + 1

"""

import logging.config
import yaml
import time
from genetic_algorithm import GeneticAlgorithm

__author__ = "Mostafa Rafaie"
__license__ = "APLv2"


# F(x) = 12a + 24b -35c + 7e -5c + 1
FUNCTION = [12, 24, -35, 7, -5]
B = 1


# Using inverse function for fitness 1/F(x)
def calc_fitness(genom):
    return abs(sum([v * genom[i] for i, v in
               enumerate(FUNCTION)]) + B)


if __name__ == "__main__":
    logging.config.dictConfig(yaml.load(open('logging.yaml')))

    path = 'sample_genom_struct.csv'
    init_population_size = 10000
    population_size = 200
    mutation_rate = 0.15
    num_iteratitions = 400
    crossover_type = GeneticAlgorithm.TWO_POINT_CROSSOVER
    fitness_goal = 0.00001

    ga = GeneticAlgorithm(path)

    start_time = time.time()
    population = ga.run(init_population_size, population_size,
                        mutation_rate, num_iteratitions, crossover_type,
                        calc_fitness, fitness_goal,
                        cuncurrency=1,
                        reverse_fitness_order=False)
    end_time = time.time()
    print(population[:3].astype(float))
    print(population[:, -1].astype(float))
    print('Runtime :', end_time - start_time)

    # Runtime : 49.50081205368042, cuncurrency = 20
    # Runtime : 34.471755027770996, cuncurrency = 10
    # Runtime : 26.63480496406555, cuncurrency = 4
    # Runtime : 20.886075973510742, cuncurrency = 1
