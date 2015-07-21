#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

max 300,000
"""

def calc_fifth_powers(n):
    tmp = 0
    ori_n = n
    ret = 0
    while True:
        tmp = n % 10
        if 0 != tmp:
            ret += tmp ** 5
        n /= 10
        if 0 == n:
            break
    if(ori_n == ret):
        return True
    return False

def find_max_sum_fifth_powers():
    ret = 0
    sum = 0
    for var in range(2, 300000):
        if calc_fifth_powers(var):
            print var
            sum += var
    return sum

print find_max_sum_fifth_powers()
