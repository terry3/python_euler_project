#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""


def exec_main():
    print reduce(lambda x,y:int(x) + int(y), str(2**1000))

if __name__ == '__main__':
    exec_main()
