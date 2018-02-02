#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/2 下午3:19
# @Author  : JiangZiWei
# @Email   : 836579250@qq.com
# @File    : Problem_1.py
# @Software: PyCharm

"""
问题描述：
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
（给定一个整数数组，返回两个数字的索引，使它们加起来成为一个特定的目标。每个输入都只有一个结果，而且不会使用相同的元素两次。）

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

"""
个人思考:
开始时想到的最笨的方法是两个for循环嵌套，找出相加等于目标值的两个下标，但是进行测试时，由于时间复杂度O(n^2)
之后也想过两个时间for循环分开的方式，但是时间复杂度也不理想。
网上提供的这种方式的时间复杂度O(n), 通过定义一个缓存区，用空间换时间
"""


class Solution:
    @staticmethod
    def two_sum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        buff_map = {}
        for i in range(len(nums)):
            if nums[i] not in buff_map:
                buff_map[target - nums[i]] = i
            else:
                return buff_map[nums[i]], i

        return -1, -1


if __name__ == '__main__':
    nums_param = [1, 2, 5, 8]
    target_param = 7
    s = Solution()
    result = s.two_sum(nums_param, target_param)
    print(result)
