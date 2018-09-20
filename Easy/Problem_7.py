#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 下午2:12
# @Author  : JiangZiWei
# @Email   : 836579250@qq.com
# @File    : Problem_7.py
# @Software: PyCharm
"""
问题描述
Given a 32-bit signed integer, reverse digits of an integer.
（给定一个32位的有符号整数，求这个整数的反向数字）
注意：因为32位有符号整数的取值范围是[−2^31,  2^31 − 1], 所以当这个整数的反向数字溢出，可以返回0

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

"""
####
# 个人算法版本
####

import math
import operator


def reverse_integer_32(num):
    sign = True if num >= 0 else False
    str_num = str(int(math.fabs(num)))
    reverse_str = ''
    for i in range(0, len(str_num)):
        v = int(math.fabs(num)) // (10**i) % 10
        reverse_str = '{0}{1}'.format(reverse_str, v)
    reverse_integer = int(reverse_str)
    if -2**31 <= reverse_integer <= 2**31-1:
        return reverse_integer if sign else 0-reverse_integer
    else:
        return 0

####
# 网上版本
####


def reverse(x):
    s = operator.gt(x, 0)
    r = int(str(s*x)[::-1])
    return s*r * (r < 2**31)


if __name__ == '__main__':
    a_num = 4396
    a_out_of_num = 7463847412
    reverse_num = reverse_integer_32(a_num)
    reverse_num1 = reverse(a_out_of_num)
    print(reverse_num, reverse_num1)

