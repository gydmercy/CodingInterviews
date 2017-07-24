# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
输入一个链表，反转链表后，输出链表的所有元素。
"""


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):

        # 如果输入为空，则直接返回
        if pHead is None:
            return pHead

        p = pHead  # p 始终指向最初的头结点

        # 循环将最初头结点后面的节点移到最前面
        while p.next is not None:
            q = p.next
            p.next = q.next
            q.next = pHead
            pHead = q

        return pHead
