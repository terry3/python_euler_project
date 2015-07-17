#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def calc_sum_of_divisors(n):
    t_ret = 1
    t_divisor = 2
    t_end = n / 2
    t_list = []
    if n == 1:
        return 0
    while t_divisor <= t_end:
        if n % t_divisor == 0 and t_divisor not in t_list:
            # print t_divisor
            t_ret += t_divisor
            t_end = n / t_divisor
            t_ret += t_end
            t_list.append(t_divisor)
            t_list.append(t_end)
        t_divisor += 1
    return t_ret

def find_amicable_numbers(n=10000):
    t_list = []
    t_ret = 0
    for var in range(4, n):     # begin from 4
        t_sum = calc_sum_of_divisors(var)
        t_sum_other = calc_sum_of_divisors(t_sum)
        if var == t_sum_other and var != t_sum and var not in t_list:
            # var can not in the t_list
            t_list.append(var)
            if t_sum != var:
                t_list.append(t_sum)
    for var in t_list:
        t_ret += var
    return t_ret

print find_amicable_numbers()
