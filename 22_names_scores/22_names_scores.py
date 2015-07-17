#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

def calc_names_scores():
    t_index = 0
    t_ret = 0
    name_file = open("p022_names.txt")
    name_list = name_file.read().split(',')
    name_file.close()
    name_list.sort()            # sort the list
    for var in name_list:
        t_sum = 0
        t_index += 1
        for t_char in var[1:-1]:
            t_sum += ord(t_char) - 64
        t_sum *= t_index
        t_ret += t_sum
    return t_ret

print calc_names_scores()
