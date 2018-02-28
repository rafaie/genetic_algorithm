"""
ga_function_optimization.py: Using genetic_algorithm for Function Optimization
Function: F(x) = 12a + 24b -35c +7e -5c + 1

"""

import logging.config
import yaml
from genetic_algorithm import GeneticAlgorithm

__author__ = "Mostafa Rafaie"
__license__ = "APLv2"


# F(x) = 12a + 24b -35c + 7e -5c + 1
FUNCTION = [12, 24, -35, 7, -5]
B = 1


# Using inverse function for fitness 1/F(x)
def calc_fitness(self, genom):
    return 1/(sum([v * genom[i] for i, v in enumerate(FUNCTION)]) + B)


if __name__ == "__main__":
    logging.config.dictConfig(yaml.load(open('logging.yaml')))

    path = 'sample_genom_struct.csv'
    ga = GeneticAlgorithm(path)
    ga.init_ga(100)
