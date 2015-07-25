#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
just check if palindromic.
"""

def is_palindromic(t_str):      # just input type string
    str_len = len(t_str)

    for t_index in range(0, str_len/2):
        if t_str[t_index] != t_str[-t_index - 1]:
            return False
    return True

def reverse_int(t_input):
    t_str = str(t_input)
    t_str = t_str[::-1]
    return int(t_str)
