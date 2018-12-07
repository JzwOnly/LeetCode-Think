#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/7 上午10:25
# @Author  : JiangZiWei
# @Email   : 836579250@qq.com
# @File    : Problem_14.py
# @Software: PyCharm
"""
Title:  Longest Common Prefix

问题描述: 编写一个函数来查找字符串数组中最长的公共前缀字符串。如果没有公共前缀，则返回空字符串“”。
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".


Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        max_prefix = ''
        len_list = [len(item_str) for item_str in strs]
        if len(len_list) > 0:
            minlen = min([len(item_str) for item_str in strs])
            for index in range(0, minlen):
                prefix_list = [item_str[index] for item_str in strs]
                if len(set(prefix_list)) == 1:
                    max_prefix = strs[0][0:index + 1]
                else:
                    break
        return max_prefix


# 另一种解题方式 （学会一种用法zip(*)）
# zip(*) 可以理解为解压，返回一个二维矩阵   zip(*) 是zip()的一个逆过程

class Solution1:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        max_prefix = ''
        i = 0
        for compare_list in zip(*strs):
            if len(set(compare_list)) == 1:
                max_prefix = strs[0][:i+1]
                i += 1
            else:
                break
        return max_prefix


if __name__ == '__main__':
    solution = Solution()
    result = solution.longestCommonPrefix(["dog", "racecar", "car"])
    print(result)

    solution1 = Solution1()
    result1 = solution1.longestCommonPrefix(["flower","flow","flight"])
    print(result1)

