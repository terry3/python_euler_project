#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Consider all integer combinations of ab for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

    22=4, 23=8, 24=16, 25=32
    32=9, 33=27, 34=81, 35=243
    42=16, 43=64, 44=256, 45=1024
    52=25, 53=125, 54=625, 55=3125

If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?

"""

def calc_distinct_powers(a=5, b=5):
    d_list = []
    for x in range(2, a+1):
        for y in range(2, b+1):
            d_list.append(x ** y)

    d_set = set(d_list)
    return len(d_set)


def exec_main():
    print calc_distinct_powers(a=100, b=100)

if __name__ == '__main__':
    exec_main()
