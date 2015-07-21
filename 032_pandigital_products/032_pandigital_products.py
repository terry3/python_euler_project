#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

def is_pandigital_string(d_str):
    if len(d_str) != 9:
        return False
    for var in range(1,10):
        if 1 != d_str.count(str(var)):
            return False
    return True

def find_all_pandigital_string():
    sum_list = []
    sum = 0
    d_str = ""
    for x in range(0, 100):
        for y in range(0, 10000):
            d_str = ""
            d_str += str(x)
            d_str += str(y)
            tmp = x * y
            d_str += str(tmp)
            if is_pandigital_string(d_str):
                # print d_str
                sum_list.append(tmp)
    # check is there have same product
    d_set = set(sum_list)
    for var in d_set:
        sum += var
    return sum


def exec_main():
    print find_all_pandigital_string()

if __name__ == '__main__':
    exec_main()
