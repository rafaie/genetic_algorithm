"""
genom_struct.py: the base structure to keep genom infrustructure.

"""
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

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "ChromosomesStruct, name={}, min_value={}, max_value={}" \
                .format(self.name, self.min_value, self.max_value) + \
               ", floating_point={}, is_fixed={}".format(self.floating_point,
                                                         self.is_fixed)


class GenomStruct:
    def __init__(self, path):
        if os.path.isfile(path) is not True:
            print ('The Genom File Structure "{}" is not avaliable'.
                   format(path))
            sys.exit(1)

        self.cs = []

        with open(path, 'r') as fi:
            for line in fi.readlines():
                l = line.strip().split(',')
                self.cs.append(ChromosomesStruct(l[0], float(l[1]),
                                                 float(l[2]), float(l[3]),
                                                 bool(int(l[4]))))

    def rand(self, i):
        cs_temp = self.cs[i]

        if cs_temp.is_fixed is True:
            return None

        p = 1 if cs_temp.floating_point == 0 else cs_temp.floating_point * 10
        return random.randint(cs_temp.min_value * p,
                              cs_temp.max_value * p) / p
