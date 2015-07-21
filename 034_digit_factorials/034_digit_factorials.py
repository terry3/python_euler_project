#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
import sys
sys.path.append("..")
from t_base import exec_time

df_list =[]

def factorial_ret(n):
    ret = 1
    if n == 0:
        return 1                # oh, it's really important!
    while n != 1:
        ret *= n
        n -= 1
    return ret

def factorial_init(n):
    for var in range(0, n):
        df_list.append(factorial_ret(var))

@exec_time
def find_another_courious_num():
    n = 10
    str_n = ""
    sum = 0
    ret_sum = 0
    factorial_init(10)
    while n < 2550000:
        sum = 0
        # print n
        str_n = str(n)
        for var in str_n:
            sum += df_list[int(var)]
            if sum > n:
                break
        if sum == n:
            print sum
            ret_sum += sum
        n += 1
    return ret_sum

# print factorial_ret(9)
print find_another_courious_num()
