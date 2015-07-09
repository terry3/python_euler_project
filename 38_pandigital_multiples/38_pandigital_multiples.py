#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

d_list = range(0, 11)


def is_all_digit_1_to_9(d_str):
    for var in range(0, 11):
        d_list[var] = 0
    for var in d_str:
        tmp = int(var)
        if tmp == 0:
            return False
        d_list[tmp] += 1
        if d_list[tmp] > 1:
            return False
    return True

def generate_concatenating_string(n):
    num = 1
    d_str = ""
    while True:
        d_str += str(n * num)
        if len(d_str) > 9:
            return [False, ""]
        elif len(d_str) == 9:
            return [is_all_digit_1_to_9(d_str), d_str]
        else:
            num += 1

def find_max_creep_number():
    n = 3
    t_max = 0
    while n < 10000:            # less than xxxxx 
        # print n
        ret, d_str = generate_concatenating_string(n)
        if ret:
            if int(d_str) > t_max:
                t_max = int(d_str)
                print d_str
        n += 1
    return t_max

print find_max_creep_number()
