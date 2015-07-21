#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""
n9 =  999 * 999
ls = str(n9)[:3]
ln = int(ls)


def find_max_p_number(number=998):
    while number > 0:
        a = 100
        ls = str(number)
        rs = ls[::-1]
        n = int(ls + rs)
        while a < 1000:
            if n % a == 0 and n/a < 1000:
                return [a, n/a, n]
            a += 1
        number -= 1
print find_max_p_number(ln)
