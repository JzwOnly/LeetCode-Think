#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/2 下午3:57
# @Author  : JiangZiWei
# @Email   : 836579250@qq.com
# @File    : Problem_2.py
# @Software: PyCharm

"""
问题描述
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

(   用两个非空链表来表示两个非负整数。
    数字以相反的顺序存储，每个节点包含一个数字。
    添加这两个数字并将其作为链接列表返回。
    您可以假定这两个数字不包含任何前导零，除了数字0本身。
)

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

"""
这题没什么特殊的，可能需要考虑的就是 1 进位
                                2 两个数字的位数
                                3 结果的位数
重新复习了一下单链表
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        m_str = str(self.val)
        m = self
        while m.next:
            m = m.next
            m_str = m_str + '=>' + str(m.val)
        return m_str


class LinkList:
    def __init__(self, length=0, head=None):
        self.length = length
        self.head = head

    def init_by_list(self, arr):
        for value in arr:
            self.append(value)

    def append(self, data_or_node):
        item = None
        if isinstance(data_or_node, ListNode):
            item = data_or_node
        else:
            item = ListNode(data_or_node)
        if self.head is None:
            self.head = item
            self.length += 1
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = item
            self.length += 1

    def is_empty(self):
        return self.length == 0


class Solution:
    @staticmethod
    def add_two_numbers(l1, l2):
        """
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        """
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next


if __name__ == '__main__':
    list_one = [3, 5, 2]
    list_two = [1, 7, 7]
    link_list_one = LinkList()
    link_list_one.init_by_list(list_one)
    link_list_two = LinkList()
    link_list_two.init_by_list(list_two)
    s = Solution()
    result = s.add_two_numbers(link_list_one.head, link_list_two.head)
    print(link_list_one.head, '+', link_list_two.head, '=', result)
