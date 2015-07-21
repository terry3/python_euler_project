#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty

"""

digit_list =["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

digit_ten_list = ["twenty", "thirty", "forty", "fifty", "sixty","seventy", "eighty", "ninety"]

hundred_name = "hundred"
dash_name = "and"

def calc_digit_char_count():
    t_sum = 0
    t_index = 1
    t_tens = 2
    t_unit = 0
    t_handred = 0
    for var in digit_list:      # add 1-19
        t_sum += len(var)
    t_index = len(digit_list)
    for var in range(t_index, 1000):
        if t_unit > 9:
            t_unit = 0
            t_tens += 1
        if t_tens > 9:
            t_tens = 0
            t_handred += 1
        if t_handred > 9:
            t_handred = 0
        # reset t_*
        if t_unit > 0:
            t_sum += len(digit_list[t_unit - 1])
        if t_tens > 0:
            t_sum += len(digit_ten_list[t_tens - 2])
        if t_handred > 0:
            t_sum += len(digit_list[t_handred - 1]) + len(hundred_name) + len(dash_name)
        t_unit += 1
    return t_sum + len("one thousand")


def exec_main():
    print "wrong answer."
    print calc_digit_char_count()

if __name__ == '__main__':
    exec_main()

