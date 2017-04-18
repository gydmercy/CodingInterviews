# -*- coding:utf-8 -*-

"""
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
"""


class Solution:
    def NumberOf1(self, n):
        count = 0

        # 因为负数的符号位为1，但是符号位不参与运算，所以直接将其变为0，同时计数增加1，以正数的形式来统计
        # 否则下面的循环会进入死循环
        if n < 0:
            n = n & 0x7fffffff
            count += 1

        while n:
            count += 1
            n = n & (n - 1)

        return count
