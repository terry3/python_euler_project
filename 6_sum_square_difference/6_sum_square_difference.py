#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""

n = 100

# print range(1,n + 1)
def get_sum(n=10):
    sum = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                sum += i * j

    return sum

print get_sum(n=n)
