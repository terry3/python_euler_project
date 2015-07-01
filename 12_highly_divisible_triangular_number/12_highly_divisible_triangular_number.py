#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""
import time
import math

def find_triangualr_number_first_over_n_divisors(n=5):
    tri_number = 0
    divisors   = 0
    tmp        = 0
    t_tmp      = 0
    seed       = 0
    while True:
        seed += 1
        tri_number += seed
        divisors = 0
        t_tmp = math.sqrt(tri_number) # performance key!!!
        tmp = 1
        # print tri_number
        while tmp < t_tmp:      # performance key also!!!
            if tri_number % tmp == 0:
                divisors += 2
            tmp += 1
        # print divisors
        if divisors + 1 > n:    # plus 1 means add self
            break
    print tri_number

begin = time.time()
find_triangualr_number_first_over_n_divisors(n=500)
print time.time() - begin
