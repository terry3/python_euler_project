#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

sum = 1000

def find_pythagorean_triplet(max=12):
    for a in range(1, max-1):
        for b in range(a+1, max): # just fool loop
            if (a**2 + b**2) == (max - a - b) ** 2:
                print a, b, (max - a - b)
                print a*b*(max - a - b)

find_pythagorean_triplet(max=sum);


