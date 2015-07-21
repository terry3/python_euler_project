#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

class Fibonacci():
    def __init__(self):
        self.a = 1
        self.b = 1
        self.index = 2

    def next(self):
        tmp = self.a + self.b
        self.a = self.b
        self.b = tmp
        self.index += 1
        return tmp

def find_1000_digit_fib_index():
    fib = Fibonacci()
    while len(str(fib.next())) < 1000:
        pass
    return fib.index


def exec_main():
    print find_1000_digit_fib_index()

if __name__ == '__main__':
    exec_main()


