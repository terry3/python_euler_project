#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

def factorial(x=1):
    ret = 1
    while x != 1:
        ret *= x
        x -= 1
    return ret

def combination_x_y(x=1, y=1):
    sum_x = 0
    sum_y = 0
    sum_z = 0
    sum_x = factorial(x)
    sum_y = factorial(y)
    sum_z = factorial(abs(x-y))
    return int(sum_x / (sum_z * sum_y))

print combination_x_y(40, 20)
