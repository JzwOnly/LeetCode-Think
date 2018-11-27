#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/30 下午3:31
# @Author  : JiangZiWei
# @Email   : 836579250@qq.com
# @File    : Problem_9.py
# @Software: PyCharm
"""
Title: Palindrome Number

问题描述
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
（确定一个整数是否是回文数。当这个整数从前往后和从后往前相同，就是一个回文数）

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

难度提升： 你可以解决它而不将整数转换为字符串吗？
"""


class Solution:
    def is_palindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if not isinstance(x, int):
            return False
        if x < 0:
            return False
        # 获取整数的最高位
        integer_range = 1
        while x/integer_range >= 10:
            integer_range *= 10
        # 通过比较整数的首位和末位判断是否是回文数，这里可采用循环的方式，比较完首位和末位之后取出首位和末位。直到x=0
        while x:
            left = int(x / integer_range)
            right = x % 10
            if left != right:
                return False
            x = int((x % integer_range) / 10)
            integer_range /= 100
        # 跳出循环说明完全匹配
        return True


if __name__ == '__main__':
    solution = Solution()
    result = solution.is_palindrome(1221)
    print('回文数' if result else '非回文数')
