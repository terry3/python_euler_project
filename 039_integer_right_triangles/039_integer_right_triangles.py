#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
def find_max_right_angle_triangle_solutions(n):
    p = 2
    t_max = 0
    t_sum = 0
    t_p   = 0
    while p < n:
        p_2 = p / 2
        t_sum = 0
        for a in range(1, p_2):
            for b in range(1, p_2):
                if (p ** 2) / 2 == a * p + b * p - a * b:
                    t_sum += 1
        if t_sum > t_max:
            t_max = t_sum
            t_p = p
            print p, t_max
        p += 2                  # p always even
    return t_p

print find_max_right_angle_triangle_solutions(n=1000)
