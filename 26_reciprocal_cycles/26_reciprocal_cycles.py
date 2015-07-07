#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

def calc_division_result(d=3):
    remainder = 1
    strr = ""
    d_list = []
    d_ret = 0
    while True:
        remainder *= 10
        if 0 == remainder % d:
            return "0";
        else:
            if remainder in d_list:
                # find the curring cycle
                first_r = d_list.index(remainder)
                return strr[first_r:]
            d_list.append(remainder)
            d_ret = str(remainder / d)
            strr += d_ret
            remainder = remainder % d

def find_max_curring_cycles(n=10):
    t_max = 0
    t_strr = ""
    t_num = 0
    for var in range(1, n):
        strr = calc_division_result(d=var)
        sum = len(strr)
        if t_max < sum:
            t_max = sum
            t_strr = strr
            t_num = var
    print t_num, t_max, t_strr

find_max_curring_cycles(n=1000)
