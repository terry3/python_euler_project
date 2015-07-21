#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

def generate_multiples(number=2, max=1000):
    n = 1
    sum = 0
    t_max = number
    while t_max < max:
        t_max = n * number
        if t_max >= max:
            break
        n += 1
        sum += t_max
    return sum

def exec_main():
    m3 = generate_multiples(number=3)
    m5 = generate_multiples(number=5)
    m15 = generate_multiples(number=15)
    print m3+m5-m15

if __name__ == '__main__':
    exec_main()
