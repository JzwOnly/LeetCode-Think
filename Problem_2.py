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
官方分析
算法

就像你如何在一张纸上总结两个数字一样，我们首先总结最低有效位，这是l1和l2的头。
由于每个数字在0 ... 9的范围内，所以总计两个数字可能会“溢出”。
例如5 + 7 = 12。在这种情况下，我们将当前数字设置为2，并将carry = 1carry = 1带到下一次迭代。
携带数必须是0或1，因为两位数字（包括进位）的最大可能和为9 + 9 + 1 = 19。

伪代码如下：

将当前节点初始化为返回列表的虚拟头部。
初始化进位到0。
初始化p和q分别到l1和l2的头部。
遍历列表l1和l2，直到达到两端。
将x设置为节点p的值。如果p已经到达l1的末尾，则设置为0。
将y设置为节点q的值。如果q已经达到l2的结尾，则设置为0。
设置sum = x + y +进位。
更新carry = sum / 10。
创建一个数字值为（summod10）的新节点，并将其设置为当前节点的下一个节点，然后将当前节点前进到下一个节点。
提前p和q。
检查是否携带= 1，如果是这样，将一个新的节点与数字1添加到返回列表。
返回虚拟头的下一个节点。
请注意，我们使用虚拟头来简化代码。没有虚拟头，你将不得不编写额外的条件语句来初始化头的值。

请特别注意以下情况：

测试用例解释
L1 = [0,1]
l2 = [0,1,2]当一个列表比另一个长时。
L1 = []
l2 = [0,1]当一个列表是空的，这意味着一个空的列表。
L1 = [9,9]
l2 = [1]最后可以有一个额外的进位，这很容易忘记。
复杂性分析

时间复杂度：O（max（m，n））。假设mm和nn分别表示l1和l2的长度，上面的算法最多迭代max（m，n）次。

空间复杂度：O（max（m，n））。新列表的长度最多为max（m，n）+1。

跟进

如果链表中的数字以非反转顺序存储，该怎么办？例如：

 （3→4→2）+（4→6→5）= 8→0→7
"""


"""
个人思考:
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
