#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""
import sys
sys.path.append("..")
from t_base import exec_time


d_list = [200, 100, 40, 20, 10, 4,  2,   1]
n_list = [2,   5,  10, 20, 50, 100]
it_list = [0, 100, 40, 20, 10, 4, 2, 0]
d_sum  = 200

def calc_conis_list(run_list):
    ret = 0
    for var in range(0, len(run_list)):
        ret += run_list[var] * n_list[var]
    return ret <= 200

@exec_time
def calc_combination_conis():
    sum = 0
    for x_1 in range(0, it_list[1]):
        for x_2 in range(0, it_list[2]):
            for x_3 in range(0, it_list[3]):
                for x_4 in range(0, it_list[4]):
                    for x_5 in range(0, it_list[5]):
                        for x_6 in range(0, it_list[6]):
                            tmp = []
                            tmp.append(x_1)
                            tmp.append(x_2)
                            tmp.append(x_3)
                            tmp.append(x_4)
                            tmp.append(x_5)
                            tmp.append(x_6)
                            # print tmp
                            if calc_conis_list(tmp):
                                sum += 1

    return sum

print calc_combination_conis() + 7 # add the 7 all-same number

