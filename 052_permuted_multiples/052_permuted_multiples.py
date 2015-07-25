#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

# import pdb

# bad algo
def is_have_all_same_digit(t_a, t_hash_a, t_b):
    t_hash_b = {}
    t_a_str = str(t_a)
    t_b_str = str(t_b)
    # create hash to match string
    for var in t_b_str:
        if t_hash_b.has_key(var):
            t_hash_b[var] += 1
        else:
            t_hash_b[var] = 1
    # pdb.set_trace()

    for var in t_b_str:
        if not t_hash_a.has_key(var):
            return False
        if t_hash_a[var] != t_hash_b[var]:
            return False
    for var in t_a_str:
        if not t_hash_b.has_key(var):
            return False
        if t_hash_a[var] != t_hash_b[var]:
            return False
    return True

def find_smallest_wired_number():
    t_member = 10
    t_flag   = True
    # from 10 - 14
    #     100 - 140
    #    1000 - 1400
    while True:
        var = t_member
        var_1_4 = int(1.7 * t_member);
        while var < var_1_4:
            # print var
            t_flag = True
            t_hash_a = {}
            for t_char in str(var):
                if t_hash_a.has_key(t_char):
                    t_hash_a[t_char] += 1
                else:
                    t_hash_a[t_char] = 1
            for t_base in range(2, 7):
                if not is_have_all_same_digit(var, t_hash_a, t_base * var):
                    t_flag = False
                    break
            if t_flag:
                print var
                return var
            var += 1
        # print t_member
        t_member *= 10

def exec_main():
    find_smallest_wired_number()

if __name__ == '__main__':
    exec_main()
