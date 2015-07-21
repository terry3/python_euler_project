#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
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

chk_prime = Prime_Num()

def rotate_number(n):
    d_str = str(n)
    d_ret = ""
    d_ret += d_str[len(d_str) - 1]
    d_ret += d_str[0:len(d_str) - 1]
    return int(d_ret)

def is_rotate_also_prime(n):
    ori_n = n
    if 1 == len(str(n)):
        return True
    if not chk_prime.is_prime_o(n):
        return False
    n = rotate_number(n)
    # print "hh", n
    while chk_prime.is_prime_o(n) and n != ori_n:
        n = rotate_number(n)
    if n != ori_n:
        return False
    return True

def find_circular_primes(n_in=100):
    dp  = Prime_Num()
    n   = 0
    sum = 0
    while n < n_in:
        n = dp.next()
        if is_rotate_also_prime(n):
            # print n
            sum += 1

    return sum + 1              # add the 2


def exec_main():
    print find_circular_primes(n_in=1000000)

if __name__ == '__main__':
    exec_main()
