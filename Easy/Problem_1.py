#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/2 下午3:19
# @Author  : JiangZiWei
# @Email   : 836579250@qq.com
# @File    : Problem_1.py
# @Software: PyCharm

"""
Title：Two Sum

问题描述：
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
（给定一个整数数组，和一个特定的值，当数组中的两个元素相加等于这个特定值，返回这两个元素的索引，不能使用相同元素两次）

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


"""
思路：1 遍历nums数组
     2 目标值-数组元素的差值作为key 索引为value 加入字典中，每次遍历先判断数组元素是否在字典的key中
     （把差值作为key，在之后的循环中找到另一个值）时间复杂度O(n)
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
