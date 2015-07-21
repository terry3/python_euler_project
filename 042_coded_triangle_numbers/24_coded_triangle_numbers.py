#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

d_list = [1]

def calc_triangle_number(n):
    return (n * (n + 1)) / 2

def is_triangle_number(n):
    while d_list[len(d_list) - 1] < n:
        d_list.append(calc_triangle_number(len(d_list) + 1))
    if n in d_list:
        return True
    return False

def calc_string_number(d_str):
    sum = 0
    for var in d_str:
        sum += (ord(var) - 64)
    return sum

def calc_triangle_string():
    words_file = open("p042_words.txt", "r")
    text = words_file.read().split(',')
    words_file.close()
    sum = 0
    for var in text:
        word_number = calc_string_number(var[1:len(var) - 1])
        if is_triangle_number(word_number):
            sum += 1
    return sum
print calc_triangle_string()

