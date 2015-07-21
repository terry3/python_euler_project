#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""
class Prime_Num(object):
    def __init__(self):
        self.n = 1
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
        self.n += 1
        while not self.is_prime():
            self.n += 1
        return int(self.n)

    def reset(self):
        self.n = 1

def dict_new_or_incre(dict, key):
    if dict.has_key(key):
        dict[key] += 1
    else:
        dict[key] = 1

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

def generate_list(number=20):
    for i in range(2,number + 1):
        list.append({})
        n = i
        p = Prime_Num()
        while True:
            if is_prime(n):
                dict_new_or_incre(list[i], n)
                break
            pn = p.next()
            if n % pn == 0:
                dict_new_or_incre(list[i], pn)
                n = n/pn
                p.reset()

def analyse_list(number=20):
    t_max = 0
    for i in range(2,number + 1):
        t_max = 0
        for j in range(2, number + 1):
            if list[j].has_key(i):
                t_max = max(list[j][i], t_max)
            target_dict[i] = t_max

def calculate_dict(number=20):
    sum = 1
    for (k, v) in target_dict.items():
        for i in range(v):
            sum *= k
    return sum

list = []
target_dict = {}
list.append({})
list.append({})
list[1][1] = 1

def exec_main():
    generate_list()
    analyse_list()
    # print list
    # print target_dict
    print calculate_dict()

if __name__ == '__main__':
    exec_main()
