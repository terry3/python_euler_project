#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import time
class Prime_Num(object):
    def __init__(self):
        self.n = 1
        self.q = []
        self.q.append(2)
        pass

    def is_prime(self):         # check if self.n is prime number
        n_2 = self.n / 2 + 1
        for prime_a in self.q:
            if prime_a > n_2:
                break
            if self.n % prime_a == 0:
                return False
            n_2 = self.n / prime_a + 1 # resize the search scale
        self.q.append(self.n)
        return True

    def next(self):
        self.n += 2
        while not self.is_prime():
            self.n += 2
        return int(self.n)


def get_prime_sum(n=10):
    re = 0
    tmp = 0
    p = Prime_Num()
    while p.next() < n:
        # print p.n
        re += int(p.n)
    return re
sum = 2000000

begin = time.time()
print get_prime_sum(n=sum) + 2
print time.time() - begin
