# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):

        tmpHead = ListNode(0)  # 创建一个临时表头节点
        current = tmpHead

        p = pHead1
        q = pHead2
        while p is not None and q is not None:
            if p.val <= q.val:
                current.next = p
                p = p.next
            else:
                current.next = q
                q = q.next
            current = current.next

        if p is not None:
            current.next = p

        if q is not None:
            current.next = q

        # 返回临时表头节点的下一个节点之后的链表（剔除临时表头节点）
        if tmpHead.next is None:
            return None
        else:
            return tmpHead.next
