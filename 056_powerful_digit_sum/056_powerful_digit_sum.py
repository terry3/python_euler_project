#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
"""

def calc_power(x, y):
    return x ** y

def calc_digital_sum(x, y):
    n = calc_power(x, y)
    t_sum = 0
    t_str = str(n)
    for var in t_str:
        t_sum += int(var)
    return t_sum

def find_max_power(n=100):
    t_max = 0
    t_tmp = 0
    t_max_x = 0
    t_max_y = 0
    for x in range(1, n):
        for y in range(1, n):
            t_tmp = calc_digital_sum(x, y)
            if t_tmp > t_max:
                t_max_x = x
                t_max_y = y
                t_max = t_tmp
    return [t_max_x, t_max_y, t_max]

def exec_main():
    print find_max_power(n=100)

if __name__ == '__main__':
    exec_main()
