#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

"""
def formula_1(n):
    return n*n
def formula_2(n):
    return n * n - n + 1
def formula_3(n):
    return n * n -3 * (n - 1)
def formula_4(n):
    return (n - 1) * (n - 1) + 1

# analyse the 5 formula
def calc_diagonals(n=5):
    t_sum = 1
    t_n = 3
    while t_n <= n:
        t_sum += formula_1(t_n)
        t_sum += formula_2(t_n)
        t_sum += formula_3(t_n)
        t_sum += formula_4(t_n)
        t_n += 2
    print t_sum


def exec_main():
    calc_diagonals(n=1001)

if __name__ == '__main__':
    exec_main()
