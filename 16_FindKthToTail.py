# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
输入一个链表，输出该链表中倒数第k个结点。
"""


class Solution:
    def FindKthToTail(self, head, k):

        # 用来记录离 head 指针 k - 1 个节点距离的指针
        another = head

        # 如果求第 0 个节点，直接返回 None
        if k == 0:
            return None

        # 如果空链表，直接返回 None
        if head is None:
            return None

        # head 指针先往前走 k - 1 步
        for i in range(1, k):
            head = head.next
            # 如果链表数量少于 k 个，则返回 None
            if head is None:
                return None

        # 两个指针一起走，head 到达尾部的时候，another 指向的就是倒数第 k 个节点
        while head.next is not None:
            head = head.next
            another = another.next

        return another
