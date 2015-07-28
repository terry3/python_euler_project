#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
It is possible to show that the square root of two can be expressed as an infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
"""

# find some rule, numerator = p_denominator * 2 + p_numerator
#               denominator = p_denominator + p_numerator (p means prev item)

class Square_roor_number(object):
    def __init__(self):
        self.t_index = 0
        self.t_denominator = 1
        self.t_numerator   = 1
    def next(self):
        t_tmp_nu = self.t_denominator * 2 + self.t_numerator
        t_tmp_de = self.t_denominator + self.t_numerator
        self.t_denominator = t_tmp_de
        self.t_numerator   = t_tmp_nu
        self.t_index += 1
        return [self.t_numerator, self.t_denominator]               # [numerator, denominator]

def is_numerator_longer_than_denominator(nu, de):
    if len(str(nu)) > len(str(de)):
        return True
    return False

def calc_how_many_fractor(n=1000):
    t_index = 0
    square_number = Square_roor_number()
    t_list = []
    t_sum  = 0
    while t_index < n:
        t_list = []
        t_list = square_number.next()
        # print t_list
        if is_numerator_longer_than_denominator(t_list[0], t_list[1]):
            t_sum += 1
        t_index += 1
    return t_sum

def exec_main():
    print calc_how_many_fractor()

if __name__ == '__main__':
    exec_main()
