#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

 For example,

 44 → 32 → 13 → 10 → 1 → 1
 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

 Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

t_hash = {}
t_cache = 0
t_non_cache = 0

def is_ended_with_89(n=89):
    """
    Every iteration will check the hash.
    """
    t_str = str(n)
    t_list = []
    t_list.append(n)
    t_sum = 0
    t_ret = n
    global t_cache
    global t_non_cache
    if t_hash.has_key(t_ret):
        t_cache += 1
        return t_hash[t_ret]
    while True:
        t_str = str(t_ret)
        t_ret = 0
        for var in t_str:
            t_ret += int(var) ** 2
        if t_hash.has_key(t_ret):
            t_cache += 1
            return t_hash[t_ret]
        t_list.append(t_ret)
        if t_ret == 89:
            for var in t_list:
                t_hash[var] = True
            t_non_cache += 1
            return True
        if t_ret == 1:
            for var in t_list:
                t_hash[var] = False
            t_non_cache += 1
            return False

def how_many_end_with_89(n=10000000):
    t_sum = 0
    global t_cache
    global t_non_cache
    for var in range(n, 0, -1):
        if var % 10000 == 0:
            print var, t_cache, t_non_cache, t_sum
        if is_ended_with_89(var):
            # print var
            t_sum += 1

    return t_sum

def exec_main():
    print "92"
    print how_many_end_with_89()
    # is_ended_with_89()

if __name__ == '__main__':
    exec_main()
