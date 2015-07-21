#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

HASH TABLE!!!
"""
import sys

class Collatz_seq:
    def __init__(self):
        self.n = 0
        self.sum = 1

    def next(self):
        # print self.n
        if self.is_even():
            self.n = self.n / 2
        else:
            self.n = 3 * self.n + 1
        self.sum += 1

    def is_term(self):
        if self.n == 1:
            return True
        return False

    def set_n(self, n):
        self.n = n
        self.sum = 1

    def get_sum(self):
        return self.sum

    def get_n(self):
        return self.n

    def is_even(self):
        return self.n % 2 == 0

    def is_odd(self):
        return self.n % 2 != 0

def find_max_Collatz_seq(n=13):
    cs = Collatz_seq()
    cs_max = 0
    cs_number = 0
    for i in range(n, 0, -1):
        cs.set_n(i)
        while not cs.is_term():
            cs.next()
        if cs.get_sum() > cs_max:
            cs_max = cs.get_sum()
            cs_number = i
            print cs_max
            print cs_number


def exec_main():
    find_max_Collatz_seq(1000000)

if __name__ == '__main__':
    exec_main()
