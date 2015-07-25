#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
just calcute factorial.
"""

def calc_factorial(n):
    t_ret = 1
    while n != 1:
        t_ret *= n
        n -= 1
    return t_ret
