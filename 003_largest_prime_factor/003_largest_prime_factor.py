#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
number = 600851475143
relist = []
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

def is_prime(n):
    if n == 1:
        return True
    n2 = n / 2
    while n % n2 != 0:
        n2 -= 1
        if n2 == 1:
            return True
        else:
            return False


def find_largest_prime(number = 15):
    p = Prime_Num()
    prime = p.next()
    t_number = number
    while True:
        if is_prime(t_number):
            break
        prime = p.next()
        if t_number % prime == 0:
            relist.append(prime)
            t_number = t_number / prime


def exec_main():
    find_largest_prime(number)
    relist.sort()
    print relist[-1]

if __name__ == '__main__':
    exec_main()
