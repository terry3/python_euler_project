#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
"""

def is_that_number(n):
    t_src = "1_2_3_4_5_6_7_8_9_0"
    t_str = str(n)
    if len(t_str) != 19:
        return False
    for var in range(0, 20, 2):
        if t_src[var] != t_str[var]:
            return False
    return True

def find_that_number():
    t_square = 0
    t_index = 1000000000
    while t_index < 10000000000:
        t_square = t_index ** 2
        if is_that_number(t_square):
            return t_index
        t_index += 10
        if t_index % 1000000 == 0:
            print t_index, t_square
    return 0

def exec_main():
    print "quite slowly, but worked."
    print find_that_number()
    # is_ended_with_89()

if __name__ == '__main__':
    exec_main()


