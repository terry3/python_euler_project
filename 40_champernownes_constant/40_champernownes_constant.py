#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""
global d_str

def init():
    d_list = []
    t_base = 2
    t_t = 10
    t_sum = 9
    while t_sum < 1000000:
        t_sum += t_base * t_t
        t_base += 1
        t_t *= 10
    for var in range(1, t_t / 2):
        d_list.append(str(var))
    global d_str
    d_str = ''.join(d_list)
    return t_t

def find_n_th_value(n):
    global d_str
    print d_str[n-1]
    return int(d_str[n-1])

init()

print find_n_th_value(1) * find_n_th_value(10) * find_n_th_value(100) * find_n_th_value(1000) * find_n_th_value(10000) * find_n_th_value(100000) * find_n_th_value(1000000)
