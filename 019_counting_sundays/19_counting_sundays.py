#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 一三五七八十腊


def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False

def calc_sundays_on_the_first_of_month(begin_y=1901, end_y=2000):
    t_base = 365 + 1                # 1900 is not leap year
                                    # plus 1 means the first day of month
    t_ret  = 0                      # to return(the sundays)
    for var in range(begin_y, end_y+1):
        for l_index in range(1, 13):
            if is_leap_year(var) and l_index == 2:
                t_base += 1     # add the leap year
            t_base += month_days[l_index]
            if t_base % 7 == 0:
                t_ret += 1
    return t_ret

print calc_sundays_on_the_first_of_month()
