# -*- coding:utf-8 -*-

"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""

"""
分析：
f(1) = 1
f(2) = 2
对于 n >= 3:
    f(n) = f(n-1) + f(n-2) + ... + f(0)
    f(n-1) = f(n-2) + f(n-3) + ... + f(0)
上式 - 下式得 f(n) - f(n-1) = f(n-1)
则 f(n) = 2 * f(n-1)
"""


class Solution:
    def jumpFloorII(self, number):

        if number <= 2:
            return number

        ele = 2

        return self.tail_recursion(number, ele)

    def tail_recursion(self, n, ele):
        if n <= 2:
            return ele
        return self.tail_recursion(n - 1, 2 * ele)
