#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

def calc_power_and_digit_len(n, power):
    return len(str(n ** power))


def find_n_digit_nth_power():
    t_sum = 0
    t_index = 2                 # not begin with 1, result must be add 1!
    t_power = 1
    t_pl = 0
    for var in range(2, 11):
        t_power = 1
        while True:
            t_pl = calc_power_and_digit_len(var, t_power)
            if t_pl == t_power:
                t_sum += 1
                print var, t_power
            else:
                break;
            t_power += 1
    return t_sum

def exec_main():
    print "63"
    print find_n_digit_nth_power() + 1 # remember to add 1!

if __name__ == '__main__':
    exec_main()
