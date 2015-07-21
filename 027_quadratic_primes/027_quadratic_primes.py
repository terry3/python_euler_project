#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n² + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
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

def calc_quadratic(n, x, y):
    return n * n + x * n + y

def find_quadratic_primes_result(ni=39):
    t_max = 0
    t_x = 0
    t_y = 0
    n = 0
    t_prime = Prime_Num()
    for x in range(-999, 1000):
        for y in range(-999, 1000):
            # print x, y
            n = 0
            while True:
                ret = calc_quadratic(n, x, y)
                if ret <= 0:
                    break
                if not t_prime.is_prime_o(ret):
                    if t_max < n:
                        print ret, n, x, y
                        t_max = n
                        t_x = x
                        t_y = y
                        # print ret, n, x, y
                    break
                n += 1
    print t_max, t_x, t_y, t_x * t_y


def exec_main():
    find_quadratic_primes_result()

if __name__ == '__main__':
    exec_main()
