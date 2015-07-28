#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
just prime number class.
"""
class Prime_Num(object):
    def __init__(self):
        self.n = 1
        self.q = []
        self.hash = {}
        self.q.append(2)
        self.cache = 0
        self.non_cache = 0
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
        self.hash[self.n] = True
        return True

    def is_prime_o(self, n):         # check if input n is prime number
        # n_2 = n / 2 + 1
        if self.n < n:
            self.non_cache += 1
        else:
            self.cache += 1
        while self.n < n:       # find the right self.n
            self.next()
        # print self.non_cache, self.cache
        if self.hash.has_key(n):
            return True
        return False

        # for prime_a in self.q:
        #     if prime_a > n_2:
        #         break
        #     if n % prime_a == 0:
        #         return False
        #     n_2 = n / prime_a + 1 # resize the search scale
        # return True

    def next(self):
        self.n += 2
        while not self.is_prime():
            self.n += 2
        return int(self.n)

