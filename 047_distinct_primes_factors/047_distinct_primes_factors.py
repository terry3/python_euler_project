#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
"""
prime_size = 4

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
        while self.n < n_2:       # find the right self.n
            self.next()

        for prime_a in self.q:
            if prime_a > n_2:
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


def exec_main():
    print "Tata~!"

if __name__ == '__main__':
    exec_main()
