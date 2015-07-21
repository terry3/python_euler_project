#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
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

d_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def is_all_digit_1_to_9(d_str):
    s_len = len(d_str)
    for var in range(1, s_len + 1):
        if not d_list[var] in d_str:
            return False
    return True

def find_max_pandigital_prime():
    tmp = 0
    prime = Prime_Num()
    ret = 0
    while tmp < 10000000:
        # Note: Nine numbers cannot be done (1+2+3+4+5+6+7+8+9=45 => always dividable by 3)
        # Note: Eight numbers cannot be done (1+2+3+4+5+6+7+8=36 => always dividable by 3)
        # haha
        tmp = prime.next()
        if is_all_digit_1_to_9(str(tmp)):
            ret = tmp
            print tmp
    return ret

def exec_main():
    print find_max_pandigital_prime()

if __name__ == '__main__':
    exec_main()
