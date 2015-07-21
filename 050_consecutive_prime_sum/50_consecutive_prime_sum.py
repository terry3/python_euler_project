#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""
import sys
sys.path.append("..")
from t_base import exec_time

chk_prime = Prime_Num()

def calc_and_chk_len_sum(prime, offset_len, n):
    t_len = len(prime.q)
    t_index = 0
    t_first_index = 0
    t_sum = 0
    while t_first_index < t_len:
        t_index = 0
        t_sum = 0
        if t_first_index + offset_len > t_len:
            continue
        while t_index < offset_len :
            t_tmp = t_sum + prime.q[t_index + t_first_index]
            if t_tmp > n:
                break
            t_sum = t_tmp
            t_index += 1
        # print t_first_index
        if chk_prime.is_prime_o(t_sum):
            return t_sum
        t_first_index += 1
    return 0

def find_longest_prime_seq(n):
    prime_num = Prime_Num()
    while True:
        tmp = prime_num.next()
        if tmp > n / 2:
            break
            # 此时已经获得了小于n的prime串 prime_num.q
    t_sum = 0
    t_index = 0
    while True:
        t_sum += prime_num.q[t_index]
        if t_sum > n:
            break
        t_index += 1
        # 找到可能的最大的串长度，从2一直加到大于1m
    t_max_len_maybe = t_index + 1
    t_count = t_max_len_maybe
    # 从最大长度开始一直减，找到一个就停止
    # 这个程序纯属于瞎猫碰到了死耗子，刚到蒙对了
    # 不过Prime_Num这个class还是有精彩之处的，计算Prime相对较快
    while t_count > 0:
        ret = calc_and_chk_len_sum(prime_num, t_count, n)
        if ret:
            print ret
            return
        t_count -= 1

find_longest_prime_seq(n=1000000)
