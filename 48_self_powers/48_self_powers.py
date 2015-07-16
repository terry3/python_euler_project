#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
"""
def calc_self_powers(n):
    sum = 0
    while n > 0:
        sum += n ** n
        n -= 1
    return sum

print str(calc_self_powers(1000))[-10:]
