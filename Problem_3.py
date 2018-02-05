#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/5 上午11:55
# @Author  : JiangZiWei
# @Email   : 836579250@qq.com
# @File    : Problem_3.py
# @Software: PyCharm

"""
问题描述:
Given a string, find the length of the longest substring without repeating characters.
(给定一个字符串，找到最长且内容不重复的子字符串)
Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring,
"pwke" is a subsequence and not a substring.
"""


"""
个人思考：解题思路就是脑子里想的最佳方式，只不过是把脑子里抽象的方法代码化。

"""

"""
思路：1 首先定义一个记录从某个小标开始的有效子字符串的起始位置，
     2 通过一个dict 判断当前字符是否出现过。a 出现过这起始下标往后一位
                                       b 未出现，则存入字典中 以 'char:index' 的形式 
"""


class Solution:
    @staticmethod
    def length_of_longest_substring(s):
        """
        :type s: str
        :rtype: int
        """
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)
            used[c] = i
        return max_length
