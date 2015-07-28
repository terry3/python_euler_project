#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
"""
import sys
sys.path.append("./000_misc")
from t_prime import Prime_Num

chk_prime = Prime_Num()

def formula_1(n):
    return n*n
def formula_2(n):
    return n * n - n + 1
def formula_3(n):
    return n * n -3 * (n - 1)
def formula_4(n):
    return (n - 1) * (n - 1) + 1

def calc_spiral_primes(n):
    t_index = 3
    t_tmp = 0
    t_sum = 1
    t_prime = 0
    while True:
        t_tmp =  formula_2(t_index)
        if chk_prime.is_prime_o(t_tmp):
            t_prime += 1
        t_tmp =  formula_3(t_index)
        if chk_prime.is_prime_o(t_tmp):
            t_prime += 1
        t_tmp =  formula_4(t_index)
        if chk_prime.is_prime_o(t_tmp):
            t_prime += 1
        t_sum += 4
        # print t_prime, t_sum, t_index
        print float(t_prime) / t_sum
        if float(t_prime) / t_sum < 0.1:
            return t_index
        t_index += 2

def exec_main():
    print "58"
    print calc_spiral_primes(n=10)

if __name__ == '__main__':
    exec_main()
