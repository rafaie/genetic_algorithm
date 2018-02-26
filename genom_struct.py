import os
import sys
import random

__author__ = "Mostafa Rafaie"
__license__ = "APLv2"


class ChromosomesStruct:
    def __init__(self, name, min_value, max_value, floating_point,
                 is_fixed=False):
        self.name = name
        self.min_value = min_value
        self.max_value = max_value
        self.floating_point = floating_point
        self.is_fixed = is_fixed


class GenomStruct:
    def __init__(self, path):
        if os.path.isfile(path) is not True:
            print ('The Genom File Structure "{}" is not avaliable'.
                   format(path))
            sys.exit(1)

        self.chromosomes_structs = []

        with open(path, 'r') as fi:
            lines = fi.readline()
            for i in range(len(lines)):
                l = lines[i].split(',')
                self.chromosomes_structs[i] = ChromosomesStruct(l[0], l[1],
                                                                l[2], l[3],
                                                                l[4])

    def rand(self, i):
        cs = self.chromosomes_structs[i]

        if cs.is_fixed is True:
            return None

        p = 1 if cs.floating_point == 0 else cs.floating_point * 10
        return random.randint(cs.min_value * p,
                              cs.max_value * p) / p
