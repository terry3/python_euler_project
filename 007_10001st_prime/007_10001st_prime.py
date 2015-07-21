#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import time
class Prime_Num(object):
    def __init__(self):
        self.n = 1
        self.q = []
        self.q.append(2)
        pass

    def is_prime(self):
        n_2 = self.n / 2 + 1
        for prime_a in self.q:
            if prime_a > n_2:
                break
            if self.n % prime_a == 0:
                return False
            n_2 = self.n / prime_a + 1
        self.q.append(self.n)
        return True

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



def exec_main():
    print get_prime(n=10001)

if __name__ == '__main__':
    exec_main()
