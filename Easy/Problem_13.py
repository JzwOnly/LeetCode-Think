#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 下午1:49
# @Author  : JiangZiWei
# @Email   : 836579250@qq.com
# @File    : Problem_13.py
# @Software: PyCharm
"""
Title: Roman to Integer

问题描述：
给定罗马数字，将其转换为整数。 输入保证在1到3999的范围内。
(Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.)


罗马数字有七个不同的字符表示： I、V、X、L、C、D、M
I  --  1
V  --  5
X  --  10
L  --  50
C  --  100
D  --  500
M  --  1000
罗马数字从左到右从大到小，特殊情况
IV  --  4
IX  --  9
XL  --  40
XC  --  90
CD  -- 400
CM  -- 900
...


Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :param s:
        :rtype: int
        """
        # 添加匹配规则  注意特殊情况一定要放在前面，以免被后面的规则提前匹配掉
        rules = [{'name': 'CM', 'value': '900'}, {'name': 'CD', 'value': '400'}, {'name': 'XC', 'value': '90'},
                 {'name': 'XL', 'value': '40'}, {'name': 'IX', 'value': '9'}, {'name': 'IV', 'value': '4'},
                 {'name': 'M', 'value': '1000'}, {'name': 'D', 'value': '500'}, {'name': 'C', 'value': '100'},
                 {'name': 'L', 'value': '50'}, {'name': 'X', 'value': '10'}, {'name': 'V', 'value': '5'},
                 {'name': 'I', 'value': '1'}]
        values = []
        while s != '':
            for rule in rules:
                if rule['name'] in s:
                    match_index = s.index(rule['name'], 0)
                    s = s[0:match_index] + s[match_index+len(rule['name']):]
                    values.append(rule['value'])
        result = 0
        # 累加最后所有匹配的值
        for value in values:
            result += int(value)
        return result


if __name__ == '__main__':
    solution = Solution()
    result = solution.romanToInt('MCMXCIV')
    print('整数', result)