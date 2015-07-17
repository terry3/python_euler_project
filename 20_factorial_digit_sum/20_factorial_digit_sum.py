#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

def calc_factorial(n=1):
    t_ret = 1
    while n != 1:
        t_ret *= n
        n -= 1
    return t_ret

def calc_factorial_digit_sum(n=100):
    t_ret = 0
    t_factorial = calc_factorial(n)
    s_factorial = str(t_factorial)
    for t_char in s_factorial:
        t_ret += int(t_char)

    return t_ret

print calc_factorial_digit_sum()
