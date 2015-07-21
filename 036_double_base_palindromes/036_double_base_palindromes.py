#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def is_palindromic_string(d_str):
    d_len = len(d_str)
    n = 0
    while n < d_len / 2:
        if d_str[n] != d_str[d_len - n - 1]:
            return False
        n += 1
    return True

def find_all_palindromic_number_in_2_10(n=1000):
    sum = 0
    for var in range(0, n):
        if is_palindromic_string(str(var)) and is_palindromic_string(bin(var)[2:]):
            # print var
            sum += var
    return sum


def exec_main():
    print find_all_palindromic_number_in_2_10(n=1000000)

if __name__ == '__main__':
    exec_main()
