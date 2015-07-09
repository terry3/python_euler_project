#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

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

    def is_prime_o(self, n):         # check if input n is prime number
        n_2 = n / 2 + 1
        if n == 1:
            return False
        while self.n < n_2:       # find the right self.n
            self.next()

        for prime_a in self.q:
            if prime_a >= n_2:
                break
            if n % prime_a == 0:
                return False
            n_2 = n / prime_a + 1 # resize the search scale
        return True

    def next(self):
        self.n += 2
        while not self.is_prime():
            self.n += 2
        return int(self.n)

chk_prime = Prime_Num()

def is_truncate_also_prime(n):
    d_len = len(str(n))
    d_tmp = 1
    s_n = str(n)
    if d_len == 1:
        return False
    # left to right
    while d_tmp < d_len:
        if not chk_prime.is_prime_o(int(s_n[d_tmp:])):
            return False
        d_tmp += 1
    # right to left
    d_tmp = 1
    while d_tmp < d_len:
        if not chk_prime.is_prime_o(int(s_n[:d_len - d_tmp])):
            return False
        d_tmp += 1
    return True

def find_all_truncate_prime(n=3):
    sum = 0
    find_n = 0
    n_prime = Prime_Num()
    while find_n < n:
        prime = n_prime.next()
        if is_truncate_also_prime(prime):
            print prime
            sum += prime
            find_n += 1
    return sum

print find_all_truncate_prime(n=11)
