#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

t_abundant_hash = {}
def calc_sum_of_divisors(n):
    t_ret = 1
    t_divisor = 2
    t_end = n / 2
    t_list = []
    if n == 1:
        return 0
    while t_divisor < t_end:
        if n % t_divisor == 0 and t_divisor not in t_list:
            # print t_divisor
            t_ret += t_divisor
            t_end = n / t_divisor
            t_ret += t_end
            t_list.append(t_divisor)
            t_list.append(t_end)
        t_divisor += 1
    return t_ret

def is_abundant_number(n):
    t_sum = calc_sum_of_divisors(n)
    if t_sum > n:
        return True
    return False

def generate_abundant_number_list(max_in):
    for var in range(1, max_in + 1):
        if is_abundant_number(var):
            t_abundant_hash[var] = 1

def find_all_not_sum_of_two_abundant_number(max_in):
    t_sum = 0
    bad_toogle = False
    for var in range(0, 23+1):
        t_sum += var
    generate_abundant_number_list(max_in)
    for var in range(24, max_in + 1):
        bad_toggle = False
        for t_node in t_abundant_hash.keys():
            t_tmp = var - t_node
            if t_tmp < 12:
                break
            if t_abundant_hash.has_key(t_tmp):
                bad_toggle = True
                break
        if not bad_toggle:
            # print var
            t_sum += var
    return t_sum


def exec_main():
    print "!!!HAS PROBLEM!!!"
    print find_all_not_sum_of_two_abundant_number(max_in=28123)

if __name__ == '__main__':
    exec_main()
