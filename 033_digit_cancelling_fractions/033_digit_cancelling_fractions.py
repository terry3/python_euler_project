#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

def is_curious_fraction(x, y, m, n):
    xy = float(10 * x + y)
    mn = float(10 * m + n)
    ret_xymn = xy / mn
    if ret_xymn >= 1.0:
        return 1.0
    if x == m:
        return ret_xymn - (float(y) / float(n))
    elif x == n:
        return ret_xymn - (float(y) / float(m))
    elif y == n:
        return ret_xymn - (float(x) / float(m))
    elif y == m:
        return ret_xymn - (float(x) / float(n))
    else:
        return 1.0

def find_courious_fraction():
    ret = 0.0
    d_x = 1
    d_y = 1
    for x in range(1, 10):
        for y in range(1, 10):
            for m in range(1, 10):
                for n in range(1, 10):
                    ret = is_curious_fraction(x, y, m, n)
                    if ret == 0.0:
                        print x, y, m, n
                        d_x *= (10 * x + y)
                        d_y *= (10 * m + n)

    return [d_x, d_y]

def calc_product_of_couious_fraction(x, y):
    n = 2
    # print x, y
    while True:
        if x % n == 0 and y % n == 0:
            x /= n
            y /= n
            n -= 1
        n += 1
        if n > max(x, y):
            return [x, y]
            break


def exec_main():
    x, y = find_courious_fraction()
    print calc_product_of_couious_fraction(x, y)

if __name__ == '__main__':
    exec_main()
