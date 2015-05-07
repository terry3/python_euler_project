#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import time
class Prime_Num(object):
    def __init__(self):
        self.n = 3
        pass

    def is_prime(self):
        n2 = self.n / 2
        while self.n % n2 != 0:
            n2 -= 1
        if n2 == 1:
            return True
        else:
            return False

    def next(self):
        self.n += 2
        while not self.is_prime():
            self.n += 2
        return int(self.n)


def get_prime(n=6):
    p = Prime_Num()
    for i in range(n-2):
        re = p.next()
    return re

print "almost 2 min in 2.4Ghz CPU."
begin = time.time()
print get_prime(n=10001)
print time.time() - begin
